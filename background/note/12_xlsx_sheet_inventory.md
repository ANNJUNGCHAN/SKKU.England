# xlsx 시트 인벤토리 + Pink Book 챕터 매핑 (12회차)

본 문서는 db/source/balanceofpayments2025q4.xlsx 원본을 read-only로 검사해 시트별 메타·표 코드·Pink Book 챕터 매핑을 정리한 결과이다.

## 요약

- 시트 수 20개 (db/REPORT.md 1.1절과 동일).
- 7분류 분포: 메타·주석 3 / 잔액 요약 1 / 경상수지 본표 3 / 경상수지 세부 4 / 자본·금융 2 / IIP 4 / 개정 3 = 20.
- 표 코드 매핑 충족율 17/20(본표). Cover_sheet/Notes/Records 3개를 제외한 모든 시트가 ONS BoP Statistical Bulletin Tables 코드 A/B/BX/C/D1.3/D4.6/D7.9/E/F/G/H/I/J/K/R1/R2/R3 와 1:1 대응.
- Pink Book 챕터 매핑 충족율: 본표 17개 모두 챕터 1~11 중 하나와 매핑 가능.
- 이상점: (1) Table_J CDID에 공백+마이너스 prefix 부착 (Notes Table A note 1과 정합). (2) 단위가 시트마다 GBP million / GBP billion / %GDP 혼재. (3) Table_R3은 9개 부표를 단일 시트에 수직 적층(1327행).

## 시트별 인벤토리 표

| sheet_name | rows | cols | classification | table_code | title_en | title_ko | unit_text | period_text | sign_convention_text | cdid_row |
|---|---:|---:|---|---|---|---|---|---|---|---:|
| Cover_sheet | 30 | 19 | meta | (none) | Balance of Payments, Quarter 4 (Oct to Dec) 2025: Published 31 March 2026 | 표지/목차 | n/a | Q4 2025 | n/a | n/a |
| Notes | 51 | 8 | meta | (none) | Notes for all tables (10 sub-tables) | 주석 모음 | n/a | n/a | reverse the sign of series prefixed with a minus | n/a |
| Records | 35 | 5 | meta | (none) | Summary of statistics for Quarter 4 (Oct to Dec) 2025 | 분기 신기록 요약 | GBP billion | Q1=Jan-Mar to Q4=Oct-Dec | n/a | n/a |
| Table_A | 451 | 19 | summary | A | Summary of Balance of Payments, Balances (net transactions) | BoP 잔액 요약 | GBP million | 1997~2025 quarterly+annual | net transactions | 8 |
| Table_B | 600 | 12 | CA-main | B | Current account, seasonally adjusted (4 sub-tables) | 경상수지 (전체) | GBP million (1-3) / % of GDP (4) | 1997~2025 | Credit (+) / Debit (-) | 8 |
| Table_BX | 600 | 12 | CA-main | BX | Current account excluding precious metals, seasonally adjusted | 경상수지 (귀금속 제외) | GBP million / % of GDP | 1997~2025 | Credit (+) / Debit (-) | 8 |
| Table_C | 898 | 20 | CA-main | C | Current account, EU and non-EU (6 sub-tables) | 경상수지 (EU/non-EU) | GBP million | 1997~2025 | Credit (+) / Debit (-) | 8 |
| Table_D1_3 | 451 | 13 | IIP | D1.3 | IIP / financial account / investment income - Investment abroad | IIP/FA/투자소득 (해외투자) | GBP billion | 1997~2025 quarter-end | assets positive | 8 |
| Table_D4_6 | 451 | 11 | IIP | D4.6 | Same - Investment in the UK | IIP/FA/투자소득 (대내투자) | GBP billion | 1997~2025 | liabilities positive | 8 |
| Table_D7_9 | 451 | 13 | IIP | D7.9 | Same - Net investment | IIP/FA/투자소득 (순) | GBP billion | 1997~2025 | net | 8 |
| Table_E | 451 | 9 | CA-detail | E | Trade in goods (3 sub-tables) | 상품무역 | GBP million | 1997~2025 | Exports (+) / Imports (-) | 8 |
| Table_F | 451 | 13 | CA-detail | F | Trade in services (EBOPS 2010 12 cat.) | 서비스무역 | GBP million | 1997~2025 | Exports (+) / Imports (-) | 8 |
| Table_G | 451 | 11 | CA-detail | G | Primary income | 1차소득 | GBP million | 1997~2025 | Credit (+) / Debit (-) | 8 |
| Table_H | 451 | 14 | CA-detail | H | Secondary income | 2차소득 | GBP million | 1997~2025 | Credit (+) / Debit (-) | 8 |
| Table_I | 451 | 14 | KA-FA | I | Capital account | 자본수지 | GBP million | 1997~2025 | Credit (+) / Debit (-) | 8 |
| Table_J | 451 | 14 | KA-FA | J | Financial account, NSA | 금융계정 | GBP million | 1997~2025 NSA | CDID space+minus prefix means reverse sign | 8 |
| Table_K | 451 | 11 | IIP | K | International investment position end-of-period | 국제투자대조표 | GBP billion | 1997~2025 NSA | assets-liab = net IIP | 8 |
| Table_R1 | 445 | 13 | revision | R1 | Revisions summary - balances | 개정 요약 (잔액) | GBP million | 1997~2025 | revision | 8 |
| Table_R2 | 592 | 13 | revision | R2 | Current account revisions (4 sub-tables incl. %GDP) | 경상수지 개정 | GBP million / % of GDP | 1997~2025 | revision | 8 |
| Table_R3 | 1327 | 7 | revision | R3 | International investment revisions (9 sub-tables) | 국제투자 개정 | GBP billion | 1997~2025 NSA | revision | 8 |

## ONS 표 코드 - Pink Book 챕터 매핑

10회차에서 확인한 Pink Book 공식 챕터 구조(01 Main points, 02 Economic commentary, 03 Trade in goods, 04 Trade in services, 05 Primary income, 06 Secondary income, 07 Capital account, 08 Financial account, 09 IIP, 10 Geographical breakdown of CA, 11 Geographical breakdown of IIP)와 매핑한다. 본 xlsx는 Pink Book(연간)이 아닌 분기 Statistical Bulletin Tables이지만 항목 구조는 동일하므로 챕터 단위 매핑이 가능하다.

| 시트 | ONS 표 코드 | Pink Book 챕터 (추정) | 매핑 근거 |
|---|---|---|---|
| Cover_sheet | (none) | (n/a) | table of contents |
| Notes | (none) | (n/a) | notes for all tables |
| Records | (none) | Ch.01 Main points 대응 | quarterly headline records |
| Table_A | A | Bulletin 고유 Ch.01-02 요약 | consolidated CA+KA+FA balances |
| Table_B | B | Ch.03+04+05+06 (CA total) | Credits/Debits/Balances + %GDP |
| Table_BX | BX | Ch.03 (precious metals supplement) | non-monetary gold adjustment |
| Table_C | C | Ch.10 Geographical breakdown of CA | EU vs non-EU |
| Table_D1_3 | D1.3 | Ch.08 + Ch.09 (Investment abroad) | assets side |
| Table_D4_6 | D4.6 | Ch.08 + Ch.09 (Investment in UK) | liabilities side |
| Table_D7_9 | D7.9 | Ch.08 + Ch.09 (Net investment) | net position |
| Table_E | E | Ch.03 Trade in goods | SITC 5 categories |
| Table_F | F | Ch.04 Trade in services | EBOPS 2010 12 categories |
| Table_G | G | Ch.05 Primary income | compensation + investment income |
| Table_H | H | Ch.06 Secondary income | govt + other sectors |
| Table_I | I | Ch.07 Capital account | capital transfers |
| Table_J | J | Ch.08 Financial account | DI/PI/FD/OI/Reserve, NSA |
| Table_K | K | Ch.09 IIP (partly Ch.11) | quarter-end balance |
| Table_R1 | R1 | Bulletin revision annex | Ch.01-08 revisions |
| Table_R2 | R2 | Bulletin-only | Ch.03-06 revisions |
| Table_R3 | R3 | Bulletin-only | Ch.08-09 revisions |

매핑 충족율: 본표 17개 전부 Pink Book 챕터(또는 Bulletin 고유 요약/개정)와 1:1 대응 가능. 10회차에서 미확정으로 남았던 표 코드 D1.3/D4.6/D7.9/BX/K/A/B/C/R1/R2/R3가 모두 본 인벤토리에서 확정됐다.

## REPORT.md 1.1절과의 차이점

| 항목 | REPORT.md 1.1절 | 12회차 인벤토리 | 평가 |
|---|---|---|---|
| sheet count | 20 | 20 | 일치 |
| meta sheets | Cover_sheet/Notes/Records | 동일 | 일치 |
| summary | Table_A | 동일 | 일치 |
| CA | Table_B/BX/C | 동일 | 일치 |
| CA detail | Table_E~H | 동일 | 일치 |
| KA-FA | Table_I/J | 동일 | 일치 |
| IIP | Table_D1_3/D4_6/D7_9/K | 동일 | 일치 |
| revision | Table_R1/R2/R3 | 동일 | 일치 |
| Table_J 부호 prefix | 미언급 | 신규: CDID 공백+마이너스 prefix | REPORT.md 보강 권고 |
| Table_R3 9 부표 | 미언급 | 신규 (1327행) | 부표 분할 권고 |
| 단위 위치 | 일반 진술 | 시트별 명시 | 보강 |

분류표 자체는 100% 일치. 추가로 (a) Table_J CDID 부호 prefix, (b) Table_R3 부표 9개 구조, (c) 시트별 단위 명세는 REPORT.md 1.1/1.2절에 한 줄씩 보강할 가치가 있다.

## 후속 작업 권고 (13회차 자연 연결)

1. CDID 사전 추출 (13회차 후보): 각 시트의 8행 CDID 행을 전수 추출해 (sheet, sub-table, column_name, cdid, unit, sign_prefix) 형태의 마스터 사전 작성. 본 12회차에서 8행 위치가 모든 본표에서 일관됨을 확인했으므로 자동화 가능. 예상 CDID 수 약 200개.
2. 부호 prefix 일괄 식별: Table_J 외 Table_D 계열/Table_K에서 prefix 여부 점검. Notes Table A note 1을 본 인벤토리에 옮겨놓았으므로 13회차 추출 스크립트에서 자동 감지 가능.
3. 부표 분할 (db/data/ 작업): Table_R3(9 부표), Table_C(6 부표), Table_B/BX/R2(4 부표) 등 다부표 시트는 db/data/ 가공 시 부표 단위 분할 권고. 가공 원칙(값 불변, 구조만 조정) 부합.
4. REPORT.md 1.1/1.2절 보강: (a) Table_J 부호 prefix, (b) Table_R3 9 부표, (c) 단위 시트별 명세 한 단락 추가.
5. Pink Book 연간 - Bulletin 분기 대조: Pink Book xlsx 추가 시 본 매핑표 기준 1:1 검증 가능.

## 출처

- 원본: db/source/balanceofpayments2025q4.xlsx (read-only, openpyxl 3.1.5, env/)
- 추출 절차: openpyxl.load_workbook(read_only=True, data_only=True), wb.sheetnames + ws.iter_rows(max_row=10) 헤더 추출
- 교차 검증: background/note/10_ons_web_research.md (Pink Book 챕터 구조), db/REPORT.md 1.1절
