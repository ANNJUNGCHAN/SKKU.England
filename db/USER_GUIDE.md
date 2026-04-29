# 영국 BoP ECOS 스타일 RDB 사용자 안내

본 문서는 `db/data/_db/ecos_uk_bop.sqlite` (Phase 4 ECOS 스타일 RDB)의 사용자 호출 안내. 한국은행 ECOS Open API의 4 주요 서비스(통계 자료 검색·통계표 목록·통계 항목 목록·계열 내보내기)에 대응하는 호출 예시·갱신 절차를 정리.

---

## 1. 개요

- **DB 파일**: `db/data/_db/ecos_uk_bop.sqlite` (sqlite3, 단일 파일)
- **테이블 5개**: `stat_table_meta` 63행 / `stat_item_meta` 512행 / `observation` 74,006행 / `missing_dict` 6행 / `term_dict` 30행
- **인덱스 3개**: `idx_item_code1` / `idx_obs_time` / `idx_item_meta_stat`
- **외래키 2개**: `stat_item_meta.STAT_CODE` → `stat_table_meta` / `observation.item_id` → `stat_item_meta`
- **유일성 제약 1개**: (`STAT_CODE`, `ITEM_CODE1~4`)

## 2. 갱신 절차 (재현 가능 멱등)

```bash
# 1) 가상환경 활성화 (저장소 루트 env/)
env\Scripts\activate

# 2) 빈 DB 스키마 생성 (기존 DB 자동 백업)
env\Scripts\python.exe db\code\source\init_ecos_db.py

# 3) 데이터 적재 + 무결성 점검
env\Scripts\python.exe db\code\source\build_ecos_db.py

# 4) 조회 예시 4종 실행
env\Scripts\python.exe db\code\source\query_examples.py
```

## 3. 호출 예시

### 3.1 통계항목 코드(CDID) 단일 조회 (ECOS 통계 자료 검색 대응)

```python
import sqlite3
conn = sqlite3.connect("db/data/_db/ecos_uk_bop.sqlite")
rows = conn.execute("""
    SELECT m.STAT_CODE, m.ITEM_NAME_KR, m.UNIT_NAME, m.CYCLE,
           o.TIME, o.RAW_CELL, o.DATA_VALUE
    FROM stat_item_meta m
    JOIN observation o ON m.item_id = o.item_id
    WHERE m.ITEM_CODE1 = 'HBOP'    -- 경상수지 합계
    ORDER BY o.TIME
""").fetchall()
```

### 3.2 분야·키워드 통계표 검색 (ECOS 통계표 목록 대응)

```python
keyword = "%경상수지%"
rows = conn.execute("""
    SELECT STAT_CODE, STAT_NAME, FIELD_SUB, CYCLE, START_TIME, END_TIME
    FROM stat_table_meta
    WHERE STAT_NAME LIKE ? OR FIELD_SUB LIKE ? OR KOREAN_DESCRIPTION LIKE ?
       OR STAT_NAME_EN LIKE ?
    ORDER BY STAT_CODE
""", (keyword, keyword, keyword, keyword)).fetchall()
```

### 3.3 통계표 단위 항목 트리 조회 (ECOS 통계 항목 목록 대응)

```python
rows = conn.execute("""
    SELECT ITEM_CODE1, ITEM_CODE2, ITEM_CODE3, ITEM_NAME_KR,
           LVL, P_ITEM_CODE, UNIT_NAME, SIGN_CONVENTION
    FROM stat_item_meta
    WHERE STAT_CODE = 'UK_BoP_Table_A_sub1'
    ORDER BY ITEM_CODE2, ITEM_CODE3, ITEM_CODE1
""").fetchall()
```

### 3.4 선택 계열 CSV 내보내기 (1 CSV = 1 평면 표)

```python
import csv
rows = conn.execute("""
    SELECT m.STAT_CODE, m.ITEM_CODE1, m.ITEM_NAME_KR, m.UNIT_NAME, m.CYCLE,
           o.TIME, o.RAW_CELL, o.DATA_VALUE
    FROM stat_item_meta m
    JOIN observation o ON m.item_id = o.item_id
    WHERE m.ITEM_CODE1 = 'HBOP'
    ORDER BY o.TIME
""").fetchall()
with open("db/data/_export/export_HBOP.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["STAT_CODE","ITEM_CODE1","ITEM_NAME_KR","UNIT_NAME","CYCLE","TIME","RAW_CELL","DATA_VALUE"])
    writer.writerows(rows)
```

## 4. 시범 CDID 추천 (학생 학습용)

| CDID | 한국어 명칭 | 강의 슬라이드 |
|---|---|---|
| HBOP | 경상수지 합계 | slide 14 항등식 좌변 |
| LQCT/BOKI | 상품무역 합계 | slide 5·21 |
| IKBD | 서비스무역 합계 | slide 5 |
| HBOJ | 1차소득 합계 | slide 5·9·25 |
| IKBP | 2차소득 합계 | slide 5·14 |
| FNVQ | 자본수지 합계 | slide 5·7 |
| HBNT | 금융계정 합계 | slide 6·14 |
| HHDH | 오차 및 누락(NEO) | slide 6·14 |
| LTEB | 준비자산 IIP stock | slide 6·26 |

상세는 `background/note/37_demo_cdids.md` 참조.

## 5. 결측·부호 규약

- **결측 코드**: `missing_dict` 테이블 6행. `x` 비공개·미가용 / `(empty)` 시계열 시작 이전 / `..`·`[c]`·`[z]`·`[low]` 외부 표준.
- **부호 규약**: 강의 슬라이드 8(BPM6 자산·부채 증감 기준)·11(NFA·순차입). 상세는 `background/note/03·19·30·32·33`.
- **sign_prefix prefix**: ONS Notes 시트 11번 운영 규칙. Table_J·D1_3·D7_9 일부 컬럼은 `_neg_<cdid>` 명명으로 부호 반전 보존(노트 13·19).

## 6. BoP 항등식 검증

강의 슬라이드 13(복식부기 항등성) + 14(`CA = FA(broad)` 단순화 항등식) → 표적 항등식 `CA + KA + FA + NEO ≡ 0`. 실측 시 영국 NEO(HHDH, 노트 20)는 분기 GDP 대비 평균 0.92%. 임계 권고는 `background/note/36`.

## 7. 무결성 점검

`build_ecos_db.py` 실행 결과:

| 지표 | 값 |
|---|---:|
| n_table | 63 |
| n_item | 512 |
| n_obs | 74,006 |
| 결측 비율 | 0.4864% |
| 시점 일관성 불일치 | 0건 |

## 8. 출처·메타 cross-reference

| 노트 | 영역 |
|---|---|
| 02·05·06·07 | 강의 자료 BoP·IIP 정의 발췌 |
| 03·19 | 부호 규약·NAFA·NIL 양면 매핑 |
| 04·20 | BoP 항등식·NEO 변동성 |
| 12·13·15 | xlsx 시트 인벤토리·CDID 사전·결측 카탈로그 |
| 24~28 | EBOPS·FA 5분류·SITC·1·2차소득·자본·개정 BPM6 보강 |
| 29~35 | 도메인 맥락·명세서 감수·분야 분류·메타데이터·항목 위계·결측 사전·용어 사전 |
| 36 | 무결성 점검 임계 권고 |
| 37 | 시범 CDID 추천 |
