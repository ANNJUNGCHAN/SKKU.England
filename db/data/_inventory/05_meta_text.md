# Phase 1.1 — 시트 상단 메타 영역 원문 텍스트

본 문서는 PLAN.md Phase 1.1 다섯 번째 항목("상단 메타 영역(헤더 4~5행)의 원문 텍스트 추출 — 부호 규약·단위·발표 기간 진술 포함")의 산출물이다. 시트 20개 각각의 1~6행 텍스트를 추출해 부호 규약·단위·발표 기간이 어디 위치하는지 인벤토리화한다.

## 산출 파일

- 기계 판독: `db/data/_inventory/05_meta_text.csv` (헤더 + 120행 = 20시트 × 6행, 3 컬럼: sheet, row, text)
- JSON: `db/data/_inventory/05_meta_text.json` (시트별 6행 list)
- 사람 검토: 본 문서

## 주요 진술 위치 (관찰)

ONS BoP 분기 통계 불러틴은 시트별로 다음의 일관된 메타 행 구조를 사용한다.

| 행 | 내용 | 예시 (Table_A) |
|---|---|---|
| 1 | 표 제목 (Table N: Title) | "Table A: Summary of Balance of Payments, Balances (net transactions)" |
| 2 | 부표 갯수·구조 진술 | "This worksheet contains three tables presented underneath each other vertically with one blank row between each table." |
| 3 | 단위 진술 (또는 분기 정의) | "The tables in this worksheet refer to, Q1 = Jan to Mar, …" 또는 "All tables in this worksheet are in £ million." |
| 4 | 단위 진술 (또는 분기 정의) | "All tables in this worksheet are in £ million." 또는 분기 정의 |
| 5 | CDID 안내 | "These tables refer to CDID's which stands for Central Database Identifier, …" |
| 6 | 첫 부표 제목 (Table N.1) + 단위 부기 | "Table A.1, Current Account, seasonally adjusted (£ million)" |

부호 규약(`[note 1]`, `[note 2]` 마커)은 시트 1행 표 제목에 부착된다(Table_J 사례). Notes 시트(r1~r51)에 note 본문이 별도 정의되어 있다.

## 주요 시트 메타 발췌

### Cover_sheet
- r1: Balance of Payments, Quarter 4 (Oct to Dec) 2025: Published 31 March 2026
- r2: This worksheet contains two tables presented underneath each other vertically with one blank row between.
- r3: Contents
- r4: Notes | Notes for all tables
- r5: Records | Summary of Statistics
- r6: Table A | Summary of Balance of Payments

### Table_A
- r1: Table A: Summary of Balance of Payments, Balances (net transactions)
- r2: This worksheet contains three tables presented underneath each other vertically with one blank row between each table.
- r3: The tables in this worksheet refer to, Q1 = Jan to Mar, Q2 = Apr to June, Q3 = July to Sept, Q4 = Oct to Dec.
- r4: All tables in this worksheet are in £ million.
- r5: These tables refer to CDID's which stands for Central Database Identifier, the codes used to identify specific datasets.
- r6: Table A.1, Current Account, seasonally adjusted (£ million)

### Table_B (단위 혼재)
- r1: Table B: Current account, seasonally adjusted
- r2: This worksheet contains four tables presented underneath each other vertically with one blank row between each table.
- r3: The first three tables are in pounds million, the fourth table displays percentages of GDP.
- r4: The tables in this worksheet refer to, Q1 = Jan to Mar, …
- r5: These tables refer to CDID's …
- r6: Table B.1, Current Account Credits (£ million)

### Table_J (부호 규약 마커)
- r1: Table J: Financial account `[note 1]` `[note 2]`, not seasonally adjusted
- r3: All tables in this worksheet are in pounds million.
- r6: Table J.1, UK Investment Abroad (net acquisition of financial assets) (£ million)

### Table_R3 (단위 £ billion + 9 부표)
- r1: Table R3: Revisions to international investment since last Balance of Payments Statistical Bulletin, not seasonally adjusted
- r2: This worksheet contains nine tables presented underneath each other vertically with one blank row between each table.
- r3: All tables in this worksheet are in pounds billion.

## 12·15회차와의 정합성

- 12회차 `12_xlsx_sheet_inventory.csv`의 `title_en`·`unit_text`·`period_text`·`sign_convention_text` 컬럼이 본 메타 영역에서 추출된 것임을 본 산출물로 확정.
- 15회차 `15_units.csv` 단위 정규화는 r3·r4의 단위 진술(예: "All tables in this worksheet are in £ million") 또는 r3의 혼재 진술(Table_B "first three tables are in pounds million, the fourth table displays percentages of GDP")에서 직접 도출됨.

## Phase 2.1 활용

- Phase 2.1 가공 시 r1~r5(또는 r6 이전까지) 메타 영역을 별도 메모로 분리해 보존.
- r1의 표 제목·`[note N]` 마커는 부호 규약 진술 위치 식별 키.
- r3·r4의 단위·분기 진술은 Phase 2.2 통합 CSV의 `UNIT_NAME`·`CYCLE` 컬럼 채움 근거.
