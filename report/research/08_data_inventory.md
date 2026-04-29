# 보고서 단계 2 §1 — RDB·정형 사전 인벤토리 1회 점검

본 메모는 `report/PLAN.md` 단계 2(`data-scientist` 주도) 의 첫 항목으로, 영국 BoP·환율 분석 보고서가 사용할 데이터 자산을 1회 점검한 결과이다. 점검은 읽기 전용(SELECT) 으로만 수행했으며, 데이터 값·구조에 손을 대지 않았다.

- 점검 일시 기준: 2026-04-29
- 점검 스크립트: `db/code/source/inventory_check_report_step2.py` (env/Scripts/python.exe 로 실행)
- 점검 대상 DB: `db/data/_db/ecos_uk_bop.sqlite`
- 점검 대상 정형 사전 디렉터리: `db/data/_spec/`
- 분석 윈도우: 2006Q1~2025Q4 80 분기

---

## (1) RDB 5 테이블 행 수·인덱스·외래키 점검

### 1.1 테이블 행 수

| 테이블 | 행 수 | USER_GUIDE.md 등재값 | 일치 |
|---|---:|---:|:---:|
| `stat_table_meta` | 63 | 63 | OK |
| `stat_item_meta` | 512 | 512 | OK |
| `observation` | 74,006 | 74,006 | OK |
| `missing_dict` | 6 | 6 | OK |
| `term_dict` | 30 | 30 | OK |

5 테이블 모두 USER_GUIDE.md §1·§7 의 등재값과 일치한다. Phase 4 종료 시점의 RDB 무결성이 그대로 보존돼 있다.

### 1.2 인덱스 (3개)

| 인덱스 | 대상 테이블 |
|---|---|
| `idx_item_code1` | `stat_item_meta` |
| `idx_item_meta_stat` | `stat_item_meta` |
| `idx_obs_time` | `observation` |

USER_GUIDE.md §1 의 인덱스 3개와 일치.

### 1.3 외래키 (2개)

| 자식 컬럼 | 부모 |
|---|---|
| `stat_item_meta.STAT_CODE` | `stat_table_meta.STAT_CODE` |
| `observation.item_id` | `stat_item_meta.item_id` |

USER_GUIDE.md §1 의 외래키 2개와 일치. 본 보고서는 `observation -> stat_item_meta -> stat_table_meta` 의 3계층 조인을 모든 조회의 기본 패턴으로 사용한다.

---

## (2) 정형 사전 CSV 행 수·컬럼 수 점검

| 파일 | 행 수 | 컬럼 수 | 역할 |
|---|---:|---:|---|
| `specification.csv` | 512 | 16 | CDID 단위 명세서(STAT_CODE·정의·부호 규약·시점 범위 1차 사전) |
| `statcatalog.csv` | 63 | 15 | 통계표 카탈로그(시트·부표 단위 메타·자료원) |
| `cdid_definitions.csv` | 512 | 16 | CDID 사전(한국어 명칭·정의) |
| `missing_dict_seed.csv` | 6 | 4 | 결측 코드 시드(`x`·(empty)·`..`·`[c]`·`[z]`·`[low]`) |
| `term_dict_seed.csv` | 30 | 5 | BoP 용어 사전 시드(BoP·IIP·CA·FA·NFA·CDID·BPM6 등) |

`specification.csv` 와 `cdid_definitions.csv` 는 각각 RDB `stat_item_meta` 의 512행과 1:1 대응한다(컬럼 16개 동일). `statcatalog.csv` 는 `stat_table_meta` 의 63행과 대응한다. `missing_dict` 는 RDB 6행, `term_dict` 는 RDB 30행이며 시드 CSV 와 행 수가 같다.

**참고**: `db/data/_spec/cdid_definitions_unmapped.csv` 도 존재하지만 사용자 요청 5종에 포함되지 않아 별도 점검하지 않았다(필요 시 후속 단위에서 점검).

---

## (3) 핵심 13 변수 RDB 등재·시점 범위

> **사전 메모(부호 규약)**: 사용자 요청에서 FA 5 세부항목 + 합계는 `-MU7M / -HHZD / -ZPNN / -HHYR / -LTCV / -HBNT` 로 표기된다. 이는 ONS Notes 시트 11번의 `sign_prefix` 운영 규칙(노트 13·19) 에 따라 RDB 가 부호 반전을 보존하기 위해 ITEM_CODE1 에 `-` prefix 를 붙여 등재한 결과다. RDB 의 실제 ITEM_CODE1 은 `-MU7M` 등이며, 이는 사용자 요청과 정확히 일치한다.

### 3.1 표 — 13 변수(+ 보조 2변수) 등재·시점 범위

| 분류 | CDID(RDB ITEM_CODE1) | STAT_CODE | ITEM_NAME_KR | START_TIME | END_TIME | 총 관측 행 | DATA_VALUE NULL |
|:---|:---|:---|:---|:---:|:---:|---:|---:|
| CA  | `BOKI`  | UK_BoP_Table_A_sub1 | 상품무역 | 1997 | 2025Q4 | 145 | 0 |
| CA  | `IKBD`  | UK_BoP_Table_A_sub1 | 서비스무역 | 1997 | 2025Q4 | 145 | 0 |
| CA  | `HBOJ`  | UK_BoP_Table_A_sub1 | 1차소득 합계 | 1997 | 2025Q4 | 145 | 0 |
| CA  | `IKBP`  | UK_BoP_Table_A_sub1 | 2차소득 합계 | 1997 | 2025Q4 | 145 | 0 |
| CA  | `HBOP`  | UK_BoP_Table_A_sub1 | 경상수지 합계 | 1997 | 2025Q4 | 145 | 0 |
| FA  | `-MU7M` | UK_BoP_Table_A_sub3 | 직접투자 | 1997 | 2025Q4 | 145 | 0 |
| FA  | `-HHZD` | UK_BoP_Table_A_sub3 | 증권투자 | 1997 | 2025Q4 | 145 | 0 |
| FA  | `-ZPNN` | UK_BoP_Table_A_sub3 | 파생금융상품(순) | 1997 | 2025Q4 | 145 | 0 |
| FA  | `-HHYR` | UK_BoP_Table_A_sub3 | 기타투자 | 1997 | 2025Q4 | 145 | 0 |
| FA  | `-LTCV` | UK_BoP_Table_A_sub3 | 준비자산 | 1997 | 2025Q4 | 145 | 0 |
| FA  | `-HBNT` | UK_BoP_Table_A_sub3 | 국제수지 요약(FA 합계) | 1997 | 2025Q4 | 145 | 0 |
| AUX | `FNVQ`  | UK_BoP_Table_A_sub1 | 자본수지 합계(KA) | 1997 | 2025Q4 | 145 | 0 |
| AUX | `HHDH`  | UK_BoP_Table_A_sub3 | 국제수지 요약(NEO) | 1997 | 2025Q4 | 145 | 0 |
| AUX | `AA6H`  | UK_BoP_Table_B_sub4 | 경상수지 합계(% of GDP) | 1997 | 2025Q4 | 145 | 0 |
| AUX | `HBQC`  | UK_BoP_Table_K_sub3 | 국제투자대조표(NIIP, stock) | 1997 | 2025Q4 | 145 | 0 |

### 3.2 145행 구성

15 변수 모두 동일하게 145행이며 내역은 다음과 같다(예: HBOP 표본 검증 결과).

- 연간(YYYY) 29행: 1997 ~ 2025
- 분기(YYYYQn) 116행: 1997Q1 ~ 2025Q4

`145 = 29 + 116` 의 등식이 정확히 성립한다. RDB 는 `observation.TIME` 컬럼에 연간·분기 시점을 함께 보관하며, 본 보고서는 분기 시점만 추출해 사용한다(연간은 횡단 비교·연환산 검증 보조용).

### 3.3 등재 일관성 점검

- 13 핵심 변수 중 RDB 등재 누락은 없다(15/15 OK).
- START_TIME·END_TIME 이 모두 `1997 ~ 2025Q4` 로 시점 일관성을 만족한다(USER_GUIDE.md §7 의 "시점 일관성 불일치 0건"과 정합).
- DATA_VALUE NULL 0건 = 변수 단위로 결측 0건. 단, 이는 전체 145행 기준이며 80 분기 윈도우 한정 결측은 §(4) 에서 별도 점검한다.
- AUX 4종은 사용자 요청 명세("FNVQ / HHDH / AA6H / HBQC") 에 정확히 등재돼 있어 항등식 검증·GDP 정규화·NIIP 짝개념 분석에 즉시 활용 가능하다.

---

## (4) 80 분기(2006Q1~2025Q4) 윈도우 결측 점검

### 4.1 표 — 13 변수(+ 보조 2변수) 윈도우 결측

| 분류 | CDID | 윈도우 내 행 수 | 윈도우 결측 행 수 | 결측 시점 |
|:---|:---|---:|---:|:---|
| CA  | `BOKI`  | 80 | 0 | (없음) |
| CA  | `IKBD`  | 80 | 0 | (없음) |
| CA  | `HBOJ`  | 80 | 0 | (없음) |
| CA  | `IKBP`  | 80 | 0 | (없음) |
| CA  | `HBOP`  | 80 | 0 | (없음) |
| FA  | `-MU7M` | 80 | 0 | (없음) |
| FA  | `-HHZD` | 80 | 0 | (없음) |
| FA  | `-ZPNN` | 80 | 0 | (없음) |
| FA  | `-HHYR` | 80 | 0 | (없음) |
| FA  | `-LTCV` | 80 | 0 | (없음) |
| FA  | `-HBNT` | 80 | 0 | (없음) |
| AUX | `FNVQ`  | 80 | 0 | (없음) |
| AUX | `HHDH`  | 80 | 0 | (없음) |
| AUX | `AA6H`  | 80 | 0 | (없음) |
| AUX | `HBQC`  | 80 | 0 | (없음) |

### 4.2 결론

- 본 보고서가 사용할 15개 시계열 모두 2006Q1~2025Q4 80 분기 윈도우에서 **결측 0건**.
- 따라서 본 보고서 본문에서는 결측 보간·결측 한계 부기가 필요하지 않다.
- `missing_dict` 매핑 부기는 본 윈도우 한정 미적용. 단, 보고서가 추후 다른 시트(예: Table_C 1997~1998 EU 비공개 360건 `x`) 를 추가로 인용한다면 다음 매핑을 그대로 활용한다.

| 결측 코드 | KR 의미 | EN 의미 | 출처 |
|:---|:---|:---|:---|
| `x` | 비공개·미가용 (ONS 비밀유지 또는 미산출) | unavailable, suppressed (confidential or not produced) | ONS Notes 시트 11번; background/note/15 |
| (empty) | 시리즈 시작 이전 또는 자료 없음 (데이터 영역 한정) | not available / not yet observed | background/note/15; ONS Methodology |
| `..` | 해당 없음(개념상 정의 불가) | not applicable | ONS Service Manual; background/note/10 |
| `[c]` | 비밀유지 (GAF 권장 표기) | confidential | Government Analysis Function table symbols |
| `[z]` | 의미상 0 (정확히 0인 진정한 영) | true zero | GAF table symbols |
| `[low]` | 정확도 낮음 (반올림 결과 0에 근접) | low precision (rounded to near zero) | GAF table symbols |

(15 변수가 본 윈도우에서 결측 0건이므로 위 6개 코드 매핑은 참고 사전으로만 등재.)

---

## (5) 환율 시계열 RDB 등재 여부

### 5.1 검색 절차

다음 두 경로로 환율 관련 데이터의 RDB 등재 여부를 점검했다.

1. **통계표 메타 검색**: `stat_table_meta` 의 `STAT_NAME / STAT_NAME_EN / FIELD_SUB / KOREAN_DESCRIPTION` 4개 컬럼에 대해 9개 키워드(`Exchange / exchange / EXCHANGE / Sterling / sterling / 환율 / FX / effective rate / Effective`) LIKE 검색.
2. **통계 항목 메타 검색**: `stat_item_meta` 의 `ITEM_NAME_KR / ITEM_NAME1 / ITEM_NAME2 / ITEM_NAME3 / ITEM_NAME4` 5개 컬럼에 대해 같은 키워드(영문 부분 일치는 어미 일치로 변형) 검색.

### 5.2 결과

| 검색 경로 | HIT 건수 |
|---|---:|
| `stat_table_meta` 4컬럼 × 9키워드 | **0건** |
| `stat_item_meta` 5컬럼 × 환율 어휘 | **0건** |

### 5.3 결론 및 권고

- **RDB 에 환율 시계열은 등재돼 있지 않다(0/0 HIT).**
- 따라서 본 보고서 §7(환율–경상수지 검증) 에 필요한 GBP 명목·실효환율 시계열은 외부 1차 출처에서 신규 확보해야 한다.

> **단계 3 (`web-search`) 트리거 권고**
>
> - 1차 출처 후보: 영란은행(BoE) Statistical Interactive Database, BIS Effective Exchange Rate Indices, OECD Main Economic Indicators.
> - 확보 대상 시계열(분기 평균):
>   - GBP 명목 양자환율: GBP/USD, GBP/EUR
>   - 명목 실효환율 지수(Sterling NEER)
>   - 실질 실효환율 지수(Sterling REER, CPI 디플레이터 기준)
> - 시점: 2006Q1~2025Q4 80 분기 일치 보장.
> - 라이선스·출처 URL·발표일·갱신 주기 메타 동시 확보(PLAN.md §3.2 강제 사항).
> - 본 단계에서는 데이터를 저장소에 적재하지 않는다. 적재는 사용자 협의 후 메인 에이전트 또는 `data-scientist` 가 수행(PLAN.md §3.2·§4 단계 3).

---

## 부록 — 점검 산출 요약

| 항목 | 점검 결과 |
|---|---|
| RDB 5 테이블 행 수 | USER_GUIDE.md 등재값과 100% 일치 |
| RDB 인덱스·외래키 | 인덱스 3개·외래키 2개 모두 일치 |
| 정형 사전 5 CSV | 행 수·컬럼 수 모두 정상(512/63/512/6/30 행) |
| 13 변수 + 보조 2변수 RDB 등재 | 15/15 등재(FA 6종은 `-` sign_prefix 적용) |
| 80 분기 윈도우 결측 | 15/15 변수 모두 결측 0건 |
| 환율 시계열 RDB 등재 | 0건 — 단계 3 web-search 트리거 권고 |

본 메모로 단계 2 §1 의 인벤토리 점검은 종료. 다음 단위(§2 정량 분석) 에서 분기 시계열·통계량·항등식·그래프를 산출한다.
