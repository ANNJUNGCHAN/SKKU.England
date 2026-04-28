# Phase 1.1 — 결측 표기 인벤토리

본 문서는 `db/CHECKLIST.md` §1.1 열두 번째 항목("사용된 결측 표기(`x`, 빈 셀, `..` 등)의 종류와 등장 위치 기록")의 산출물이다. ONS BoP 2025 Q4 xlsx의 데이터 영역(CDID 행이 존재하는 컬럼 + CDID 행 아래 데이터 행)만 정밀 스캔한 결과를 정리한다.

## 핵심 발견

- xlsx 데이터 영역에 등장한 결측 표기는 **`x` 단 한 종**(360건). 모두 **Table_C**(EU/non-EU 분해)의 6개 부표에 분산.
- ONS Service Manual / Government Analysis Function이 권장하는 `[c]`/`[x]`/`[z]`/`[low]` 기호는 **본 xlsx에 등장하지 않는다** — legacy `x` 표기 유지.
- `..`(legacy 미가용), `-`(legacy 진정한 0), `n/a`/`NA` 등 모호 표기 **0건** — 권장 부합.
- 빈 셀(`(empty)`)은 데이터 컬럼(CDID가 표기된 컬럼) **안쪽에서는 등장하지 않는다**. 본 추출 이전 단계(15회차 background)의 `(empty)` 약 35,000건은 모두 (a) 시트 우측 trailing padding 컬럼, (b) 부표 머리글·빈 행, (c) 시트 하단 padding 행에 한정됨을 본 인벤토리가 정량 확정.

## 결측 표기 종류·의미

| 마커 | 카운트 | 의미(ONS Service Manual / GAF 권고와 대조) |
|---|---:|---|
| `x` | 360 | ONS 미가용(not available): xlsx Notes B23 메타 정의 "Cells containing x represent unavailable data". GAF 권고 기호 `[x]`에 해당. 13회차 검증으로 보정(이전 "비공개"·`[c]` 라벨은 추정이었음) |
| `(empty)` | 0 | 데이터 컬럼 안쪽 등장 0건 → 시리즈 시작 이전·이후 또는 비해당 의미는 본 데이터셋에 미적용 |
| `..` | 0 | ONS legacy 미가용 — 본 xlsx 미등장 |
| `-` | 0 | ONS legacy 진정한 0 / nil — 본 xlsx 미등장 |
| `[c]` / `[x]` / `[z]` / `[low]` | 0 | GAF 권고 기호 — 본 xlsx 미사용(legacy 형식 유지) |
| `n/a` / `NA` | 0 | Service Manual 비권장 모호 표기 — 본 xlsx 미등장 |

### 결측 표기 → ECOS 매핑 (Phase 4 결측 사전 시드)

| 마커 | ECOS 결측 사전 한국어 의미 |
|---|---|
| `x` | 미가용(not available, GAF `[x]`) — 본 BoP Bulletin에서 1997~1998 분기 EU/non-EU 분해 시계열이 작성되지 않은 셀(xlsx Notes B23의 1차 메타 정의 인용). "비공개(`[c]`)"·"적용 불가(`[z]`)"와 의미가 다르므로 단일 라벨로 통합하지 않음 |
| `(empty)` | 데이터 영역 외(부표 padding) — 결측이 아니므로 ECOS 적재 대상 외 |

## `x` 마커 등장 위치 (Table_C 6 부표)

| 부표 | 시트 영역 | 첫 등장 | 마지막 등장 | 셀 수 |
|---|---|---|---:|---:|
| 1 | EU Credits | B9 | G45 | 60 |
| 2 | EU Debits | B158 | G194 | 60 |
| 3 | EU Balances | B307 | G343 | 60 |
| 4 | non-EU Credits | B456 | G492 | 60 |
| 5 | non-EU Debits | B605 | G641 | 60 |
| 6 | non-EU Balances | B754 | G790 | 60 |

각 부표 60건 = 1997 Q1 ~ 1998 Q4(8 분기 × 6~8 계열) + 1997·1998 연간. 두 해의 EU/非EU 분해 시계열이 ONS에 의해 공표 보류되었음을 의미.

## 추출 절차 (재현 가능)

1. `env/Scripts/python.exe db/code/source/extract_missing_markers.py` 실행.
2. 메타 시트(Cover_sheet, Notes, Records)는 통계 본표가 아니므로 결측 인벤토리 대상 외.
3. 본표 17개에 대해 (a) CDID 행 인덱스 모두 식별(부호 prefix 행 포함, 13회차 사전과 동일 규칙), (b) CDID 행에 코드가 등장한 컬럼만 데이터 컬럼으로 한정, (c) 부표별 데이터 영역의 마지막 데이터 행을 하단 padding 제거 위해 동적 산출.
4. 데이터 영역의 비숫자 셀을 마커로 분류해 (시트, 부표, 마커) 단위로 카운트·첫·마지막 위치 기록.

## Phase 2.1 적재 시 처리 규약

- **`x` → 원문 보존**: `value_raw="x"`, `value_numeric=NULL`, `missing_reason="not_available"` 3-컬럼 패턴(13회차 검증으로 사유 라벨을 `confidential`에서 `not_available`로 보정). 0이나 NaN으로 임의 치환 금지(db/CLAUDE.md "값 불변" 원칙).
- **trailing padding `(empty)` → 적재 대상 외**: 데이터 영역(CDID 컬럼 × 첫 분기 이후 행) 외부 빈 셀은 ECOS 관측치 테이블에 행으로 적재하지 않음.
- **Table_C 1997·1998 사용 주의**: 사용자 인터페이스 안내 문구에 EU 시계열은 1999 Q1부터 사용 가능함을 명시. 동 구간 미가용 사유는 (a) ITIS 분기 조사 표본 안정화 전 + (b) Brexit 후 EU 정의 변경(EU15→EU27)으로 인한 소급 재계산 불가가 결합된 결과로 추정(13회차 §3 강의용 해석 참조).

## 산출 파일

- 기계 판독: `db/data/_inventory/12_missing_markers.csv` (헤더 + 6행, 7 컬럼).
- 사람 검토: 본 문서.
- 추출 스크립트: `db/code/source/extract_missing_markers.py` (env/Scripts/python.exe로 재현).

## 15회차 background 결과와의 차이

15회차(`background/note/15_missing.csv`)는 시트 전체(메타 시트 헤더 텍스트 + 우측 trailing 컬럼 + 하단 padding 행 포함)를 결측 후보로 잡아 546행이었다. 본 인벤토리는 다음 3개 필터를 추가해 데이터 영역 결측만 추출:

1. 메타 시트(Cover_sheet, Notes, Records) 제외.
2. CDID 행에 코드가 등장한 컬럼만 데이터 컬럼으로 한정 — Table_G/Table_K 부표 2의 col K, Table_R3 부표 3~6의 col F-G 등 trailing padding 모두 제외.
3. 각 부표의 데이터 영역 끝을 마지막 데이터 행(숫자 또는 결측 마커 등장 행)까지로 동적 한정 — 부표 머리글·빈 행 제외.

이로써 ECOS 적재용 결측 사전 시드는 본 인벤토리(6행)를 사용하고, 15회차 결과는 광역 검사용 보조 자료로 보관.
