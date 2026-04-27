# xlsx 단위 표기 + 결측 표기 카탈로그 (15회차)

본 문서는 db/source/balanceofpayments2025q4.xlsx를 read-only로 스캔해 시트/부표별 (1) 단위 표기, (2) 결측 표기 등장 위치/빈도를 정리한 결과이다. 12회차(시트 인벤토리), 13회차(CDID 사전)와 (sheet, sub_table) 키로 join 가능하다.

## 요약

- 단위 표기 종류: 정규화 라벨 기준 **3종** (GBP_million, GBP_billion, unknown). 본문 인용 단위 진술 행은 82건 — 17개 본표 × 평균 3 부표 + 메타 시트.
- 결측 표기 의미 카테고리: **5개** (1) x = 비공개·미산출, (2) (empty) = padding 또는 시리즈 외, (3) 컬럼 헤더 텍스트 잔류, (4) ../- = 미등장, (5) [c]/[x]/[z]/[low] = 미등장. 진짜 데이터-결측은 x 유형 360건.
- 부표별 단위가 혼재되어 있어 *세분화가 필요한 시트 4개*: Table_B, Table_BX, Table_R2 (각 부표 1~3 = £million, 부표 4 = %GDP), Table_R3 (9 부표 모두 £billion).
- 가장 많이 등장한 결측 표기: (empty) 약 35,000건 (시트 padding 포함), 진짜 데이터-결측 x 360건 (Table_C 6 부표 × 60건).
- 산출물: background/note/15_units.csv (82행), background/note/15_missing.csv (546행), db/code/source/extract_units_missing.py.

## 단위 표기 카탈로그 요지

### 시트/부표별 단위 정규화 분포

| 정규화 라벨 | scale_factor | 시트(부표) 수 | 비고 |
|---|---:|---:|---|
| GBP_million | 1,000,000 | 35 | A/B/BX/C/E/F/G/H/I/J/R1/R2 본표 부표 다수 |
| GBP_billion | 1,000,000,000 | 22 | D1.3/D4.6/D7.9/K/R3 (IIP·금융계정) + Records |
| unknown | (없음) | 25 | 시트 머리글(예: "Table B: ...") 단독 잡힘 — 다음 부표 행에 단위 진술 확인됨 |

### 부표 단위가 혼재된 시트 (db/data/ 분리 권고)

| 시트 | 부표 1 | 부표 2 | 부표 3 | 부표 4 | 비고 |
|---|---|---|---|---|---|
| Table_B | £m Credits | £m Debits | £m Balances | %GDP Balances | 4부표는 본 추출에서 별도 sub-CDID 그룹으로 잡히지 않음 — 추가 sweep 필요 |
| Table_BX | £m | £m | £m | %GDP | 동일 |
| Table_R2 | £m | £m | £m | %GDP | 동일 |
| Table_R3 | £bn ×9 부표 | — | — | — | 단위 동일하나 IIP/transactions/income 9개 부표 적층 |

### 메타 시트 단위

| 시트 | 단위 진술 |
|---|---|
| Cover_sheet | 없음 (목차) |
| Notes | 없음 (시리즈별 footnote 본문) |
| Records | "Current account (net) (£ billion)" → GBP_billion |

## 결측 표기 카탈로그 요지

### 의미 카테고리별 분포

| 마커 | sheet/sub_table | 누적 셀 수 | 의미 |
|---|---:|---:|---|
| x | 6 (Table_C) | 360 | ONS confidential / suppressed - EU 1997-1998 비공개 |
| (empty) | 모든 시트 | ~35,000 | 셀 padding 또는 시리즈 외 |
| .. | 0 | 0 | 본 xlsx 미등장 |
| - | 0 | 0 | 본 xlsx 미등장 |
| [c]/[x]/[z]/[low] | 0 | 0 | GAF 기호 미사용 |
| 비숫자 텍스트 | 다수 | 다수 | 부표 헤더 잔류 — 결측 아님 |

### x 마커 위치 (Table_C)

| sub_table | 첫 등장 |
|---:|---|
| 1 EU Credits | B9 |
| 2 EU Debits | B158 |
| 3 EU Balances | B307 |
| 4 non-EU Credits | B456 |
| 5 non-EU Debits | B605 |
| 6 non-EU Balances | B754 |

각 60건 = 1997 Q1 ~ 1998 Q4 (8 분기) × 7~8 컬럼. Notes 11번에 명시.

## ONS Service Manual 권고와 실제 표기 차이

10회차 §발췌 #9의 ONS Service Manual 권장 (Government Analysis Function 표기) 비교.

| 의미 | GAF 권장 | 본 xlsx 실제 | 평가 |
|---|---|---|---|
| 비공개 | [c] | x | legacy 형식 유지 |
| 미산출 | [x] | 사용 사례 없음 | x로 통합 사용 |
| 진정한 0 | [z] | 0 그대로 | 회피 OK |
| 반올림 0 | [low] | 0 또는 작은 값 | OK |
| 모호 | NA/n/a 회피 | 미사용 | OK |
| legacy 미가용 | .. 비권장 | 미사용 | 권장과 일치 |
| legacy nil | - 비권장 | 미사용 | 권장과 일치 |

**평가**: BoP Bulletin은 GAF 권장 [c] 미전환 상태이나, 단일 x 마커만 사용해 모호성은 낮음. legacy ../- 미사용은 ONS 권장 부합.

## 12회차/13회차와 join 일관성

15회차 산출물의 sub_table은 13회차와 동일 규칙(1부터, 메타는 0). 다음 join 가능:

- 15_units LEFT JOIN 13_cdid_dictionary ON (sheet, sub_table) → 부표 단위 + CDID 매트릭스
- 15_missing LEFT JOIN 12_xlsx_sheet_inventory ON (sheet) → 시트 분류 + 결측 위치

## 후속 작업 권고 (Phase 2.2 통합 CSV 적재)

1. **unit 컬럼 자동 채움**: 통합 long-form CSV(db/data/balanceofpayments2025q4_tidy.csv)에 unit 컬럼을 추가할 때 15_units.csv의 (sheet, sub_table) → unit_normalized lookup. scale_factor는 별도 컬럼으로 보존하되 실제 환산은 분석 단계에서 결정.
2. **value_raw vs value_numeric 분리**: ONS는 x를 비공개로 명시했으므로 적재 시 value_raw="x" + value_numeric=NULL + missing_reason="confidential" 3-컬럼 패턴 권장. 결측을 0/NA로 치환하지 않음(db/CLAUDE.md §3 결측 보존 원칙).
3. **부표 단위 혼재 시트 분리**: Table_B/BX/R2의 부표 4(% of GDP)는 sub_table 식별이 본 추출에서 누락 — db/data/ 가공 단계에서 cdid_row 외에 머리글 텍스트("Balances as a percentage of GDP")로 4부표 경계 식별 권고.
4. **Table_C x 마커 처리 정책**: 적재 후 EU 시계열은 1999 Q1부터 사용 가능하다는 메타 정보(coverage_start)를 컬럼 사전에 추가. 강의용 분석에서 1997-1998 EU 시계열 제외가 표 코드 C 사용 시 필수.
5. **GAF 기호 도입 검토**: db/data/ 가공본에서 ONS Service Manual 권장 [c]/[x]/[z]/[low] 표기로 전환 가능. 단 db/CLAUDE.md §3에 따라 원본 표기 보존 우선이므로 별도 컬럼(gaf_code)으로 병행 표기 권장.

## 출처

- 원본: db/source/balanceofpayments2025q4.xlsx (read-only, openpyxl 3.1.5, env/)
- 추출 절차: openpyxl.load_workbook(read_only=True, data_only=True), 시트별 cdid_row 식별 → 부표 경계 분할 → 메타 7행 단위 진술 + 데이터 영역 결측 표기 카운트.
- 교차 검증: background/note/12_xlsx_sheet_inventory.csv (시트 분류), background/note/13_cdid_dictionary.csv (CDID·sign_prefix), background/note/10_ons_web_research.md §발췌 #9 (ONS Service Manual 결측 권장).
- 재현: env/Scripts/python.exe db/code/source/extract_units_missing.py
