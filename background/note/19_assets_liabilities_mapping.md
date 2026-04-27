# 금융계정 5분류 NAFA·NIL 양면 컬럼 매핑 (background-search 19회차)

본 문서는 `db/source/balanceofpayments2025q4.xlsx`의 금융계정(Financial Account, FA) 5분류에 대해 **자산(NAFA, Net Acquisition of Financial Assets) ↔ 부채(NIL, Net Incurrence of Liabilities) ↔ 순(Net = NAFA−NIL)** 3면 컬럼이 어느 시트·부표·열에 저장되어 있는지 정리한 매핑표이다. 1차 근거는 13회차 `13_cdid_dictionary.csv`이며, 6회차 §빠진 부분 2번에서 식별한 "자산·부채 양면 분류 매핑 필요성"을 해소한다.

## 요약

- **유량(Transactions)** 양면 컬럼: Direct/Portfolio/Other 3분류 각각 자산 1·부채 1·순 1 컬럼(시트당 3개), Financial derivatives는 순액만(자산·부채 분리 없음), Reserve assets는 자산 1개만(부채 부재). 시트 Table_J, Table_D1_3, Table_D4_6, Table_D7_9에 동일 트리플이 중복 게재됨.
- **저량(IIP)** 양면 컬럼: Direct/Portfolio/Derivatives/Other 4분류는 자산 stock·부채 stock·순 stock 3개씩, Reserve assets는 자산 stock 1개. Table_D1_3(자산), Table_D4_6(부채), Table_D7_9(순), Table_K(통합 IIP)에서 일관 게재.
- **sign_prefix 패턴**: Table_J 부표1(자산 측)·부표3(순)과 모든 D1_3·D7_9 유량 컬럼은 sign_prefix=true (CSV에 공백+마이너스 prefix 부착, 부호 반전 필요). Table_J 부표2(부채 측)와 모든 D4_6, 모든 IIP 저량(stock), Table_K는 sign_prefix=false (그대로 사용).
- **ONS 양면 분류 정합성**: D1_3 = NAFA(asset), D4_6 = NIL(liability), D7_9 = Net(asset−liability), Table_K = IIP 종합(자산·부채·순 전부) — Table_J 부표 1/2/3과 1:1 대응. 단 Financial derivatives 유량은 모든 시트에서 순액만 제공(자산·부채 분리 부재), Reserve assets는 부채 항목 자체가 BPM6 정의상 존재하지 않음.
- **CSV 산출**: `19_assets_liabilities_mapping.csv` 54행 (cls=DI:12, PI:12, FD:10, OI:12, RA:8 / side=asset:10, liability:6, net:10, asset_stock:12, liability_stock:8, net_stock:8).

## 5분류별 매핑 표 요지

### 1) Direct investment (직접투자)

| side | sheet | sub | col | label | cdid | sign |
|---|---|---|---|---|---|---|
| asset (flow) | Table_J | 1 | 5 | Direct investment abroad, Total | **N2SV** | true |
| liability (flow) | Table_J | 2 | 5 | Direct investment in the UK, Total | **N2SA** | false |
| net (flow) | Table_J | 3 | 5 | Net direct investment, Total | **MU7M** | true |
| asset (flow) | Table_D1_3 | 2 | 2 | FA transactions, Direct investment | N2SV | true |
| liability (flow) | Table_D4_6 | 2 | 2 | FA transactions, Direct investment | N2SA | false |
| net (flow) | Table_D7_9 | 2 | 2 | FA transactions, Direct investment | MU7M | true |
| asset stock | Table_D1_3 / Table_K(1,4) | 1 | 2 | IIP Direct investment | **N2V3** | false |
| liability stock | Table_D4_6 / Table_K(2,4) | 1 | 2 | IIP Direct investment | **N2UG** | false |
| net stock | Table_D7_9 / Table_K(3,4) | 1 | 2 | IIP Direct investment | **MU7O** | false |

추가 하위(Equity capital / Reinvestment of earnings / Debt instruments) 3개 컬럼이 Table_J 부표1·2·3의 col 2~4에 별도 존재 — Table_K도 Equity·Debt 2분할.

### 2) Portfolio investment (증권투자)

| side | sheet | sub | col | label | cdid | sign |
|---|---|---|---|---|---|---|
| asset (flow) | Table_J | 1 | 8 | Portfolio investment abroad, Total | **HHZC** | true |
| liability (flow) | Table_J | 2 | 8 | Portfolio investment in the UK, Total | **HHZF** | false |
| net (flow) | Table_J | 3 | 8 | Net portfolio investment, Total | **HHZD** | true |
| asset stock | Table_D1_3 / Table_K(1,7) | 1 | 3 | IIP Portfolio | **HHZZ** | false |
| liability stock | Table_D4_6 / Table_K(2,7) | 1 | 3 | IIP Portfolio | **HLXW** | false |
| net stock | Table_D7_9 / Table_K(3,7) | 1 | 3 | IIP Portfolio | **CGNH** | false |

하위 Equity & investment fund shares / Debt securities는 Table_J col 6·7, Table_K col 5·6에 별도 분할.

### 3) Financial derivatives (파생금융상품)

| side | sheet | sub | col | label | cdid | sign |
|---|---|---|---|---|---|---|
| net (flow only) | Table_J | 1, 3 | 9 | Financial derivatives and ESO | **ZPNN** | true |
| net (flow) | Table_D1_3 | 2 | 4 | FA transactions, FD (net) | ZPNN | true |
| net (flow) | Table_D7_9 | 2 | 4 | FA transactions, FD | ZPNN | true |
| asset stock | Table_D1_3 / Table_K(1,8) | 1 | 4 | IIP FD | **JX96** | false |
| liability stock | Table_D4_6 / Table_K(2,8) | 1 | 4 | IIP FD | **JX97** | false |
| net stock | Table_D7_9 / Table_K(3,8) | 1 | 4 | IIP FD | **JX98** | false |

**유량은 자산/부채 분리 부재**. Table_J 부표2(부채측)에는 derivatives 행이 빠져 있음(col 9가 Other investment in the UK로 직행). Table_D4_6 sub2(부채 유량)에도 derivatives 항목 없음. 즉 ONS는 유량 단계에서 순액만 공시, IIP에서만 양면 분리.

### 4) Other investment (기타투자)

| side | sheet | sub | col | label | cdid | sign |
|---|---|---|---|---|---|---|
| asset (flow) | Table_J | 1 | 10 | Other investment abroad | **XBMM** | true |
| liability (flow) | Table_J | 2 | 9 | Other investment in the UK | **XBMN** | false |
| net (flow) | Table_J | 3 | 10 | Other net investment | **HHYR** | true |
| asset (flow) | Table_D1_3 | 2 | 5 | FA transactions, Other | XBMM | true |
| liability (flow) | Table_D4_6 | 2 | 4 | FA transactions, Other | XBMN | false |
| net (flow) | Table_D7_9 | 2 | 5 | FA transactions, Other | HHYR | true |
| asset stock | Table_D1_3 / Table_K(1,9) | 1 | 5 | IIP Other | **HLXV** | false |
| liability stock | Table_D4_6 / Table_K(2,9) | 1 | 5 | IIP Other | **HLYD** | false |
| net stock | Table_D7_9 / Table_K(3,9) | 1 | 5 | IIP Other | **CGNG** | false |

Table_J 부표2의 col 9 위치 차이(부표1·3은 col 10) — 부표2가 derivatives 행을 건너뛰기 때문.

### 5) Reserve assets (준비자산)

| side | sheet | sub | col | label | cdid | sign |
|---|---|---|---|---|---|---|
| asset (flow) | Table_J | 1, 3 | 11 | Reserve assets | **LTCV** | true |
| asset (flow) | Table_D1_3 | 2 | 6 | FA transactions, Reserve | LTCV | true |
| asset (flow) | Table_D7_9 | 2 | 6 | FA transactions, Reserve | LTCV | true |
| asset stock | Table_D1_3 / Table_K(1,10) | 1 | 6 | IIP Reserve | **LTEB** | false |
| asset stock | Table_D7_9 / Table_K(3,10) | 1 | 6 | IIP Reserve | LTEB | false |

**부채 측 부재**(BPM6 정의: 통화당국이 보유하는 외화·금·SDR·IMF 포지션은 자산 한쪽). Table_J 부표2와 Table_D4_6 어디에도 Reserve 컬럼 없음, 매핑상 NIL = 결측이 정상.

## ONS 양면 분류 일관성 비교

| 표 코드 | 자산(NAFA) | 부채(NIL) | 순(Net) | Reserve 포함 | Derivatives 양면 |
|---|---|---|---|---|---|
| Table_J | 부표1 (col 5/8/10/11) | 부표2 (col 5/8/9) | 부표3 (col 5/8/9/10/11) | yes (asset만) | net만 |
| Table_D1_3 | sub2 | — | — | yes | net만 |
| Table_D4_6 | — | sub2 | — | no | 부재 |
| Table_D7_9 | — | — | sub2 | yes | net만 |
| Table_K | sub1 (stock) | sub2 (stock) | sub3 (stock) | yes (sub1·sub3) | sub1/2/3 양면 |

→ Table_J 부표 1/2/3 ↔ Table_D1_3/D4_6/D7_9 ↔ Table_K 부표 1/2/3 의 3축 구조가 일관됨. **CDID도 동일**(예: Direct asset N2SV는 Table_J 1.5 = Table_D1_3 2.2). IIP 저량은 추가로 Table_K가 종합 게재.

## 빠진 부분·이상점

1. **Financial derivatives 유량의 자산/부채 분리 부재** — Table_J·D1_3·D7_9 모두 net만 제공. 강의 자료 슬라이드 14의 `Net financial derivatives` 표기와 일치. ONS Pink Book에서도 양면 분리는 IIP 저량(JX96/JX97)에서만 공식 수치. → Phase 2.2 통합 CSV에서 Derivatives의 ITEM_CODE2(asset/liability)는 flow=net only로 표시 필요.
2. **Reserve assets 부채측 부재** — 정의상 정상이나 자동화 코드에서 NIL = NaN을 결측이 아닌 "0 by definition"으로 처리해야 BoP 항등식 검증 시 혼동이 없음.
3. **Table_J 부표2 컬럼 위치 점프** — 부표1·3과 달리 derivatives 행이 빠져 col 인덱스가 한 칸씩 당겨짐(Other investment가 col 9). 자동 매핑 시 column_position 직접 매칭 금지, **column_label 또는 CDID로 매칭 권장**.
4. **Direct investment 하위 분류**: Equity capital / Reinvestment of earnings / Debt instruments 3개 부분 합계가 Total과 일치하는지 검증 필요(부호 반전 후 Σ = Total CDID). 본 19회차 매핑은 Total만 다룸; 하위는 13회차 dictionary에서 col 2~4로 별도 추출 가능.
5. **Portfolio investment 하위**: Equity & investment fund shares / Debt securities. Table_J col 6·7, Table_D 부표 등에 분리.
6. **D7_9 sub1 col 6 = Reserve assets** — IIP 종합표에서 reserve를 "asset only"임에도 **net 시트 안에 그대로 반영**(부채가 0이므로 net = asset). 일관성 관점에서 ONS는 Reserve를 net 측에 자산 그대로 게재.

## Phase 2.2 통합 CSV의 ITEM_CODE2(자산/부채 차원) 매핑 가능성 평가

- **가능**: 본 매핑표의 side 컬럼(asset/liability/net + _stock 변형)은 그대로 ITEM_CODE2 카테고리 차원으로 활용 가능. 분류(ITEM_CODE1) × 자산/부채(ITEM_CODE2) × 유량/저량(ITEM_CODE3) × 시트(ITEM_CODE4) 4축 키로 정규화 권장.
- **권장 코드 체계 예시**:
  - ITEM_CODE1: DI / PI / FD / OI / RA
  - ITEM_CODE2: A (asset) / L (liability) / N (net)
  - ITEM_CODE3: T (transaction/flow) / P (position/stock) / Y (income) — 13회차 dictionary의 income(Investment income earnings, sub_table 3) 컬럼도 동일 키로 통합 가능
  - 예: DI-A-T = N2SV, DI-L-T = N2SA, DI-N-T = MU7M, DI-A-P = N2V3
- **제약**: ① Derivatives는 FD-A-T/FD-L-T 결측, FD-N-T만 존재. ② Reserve는 RA-L-* 정의상 결측. ③ sign_prefix를 별도 메타 컬럼으로 두어 부호 반전 자동화 필요(true → multiply by −1, 또는 raw 그대로 저장하고 분석 단계에서 처리).
- **권장 방향**: Phase 2.2에서 long-form CSV 변환 시 본 매핑표를 키 테이블로 사용해 join, ITEM_CODE2 차원이 자연스럽게 부여됨. CDID가 unique key 역할(예: ZPNN은 모든 derivative net 행이 같은 코드로 식별).

## 관련 절대경로

- 산출물: C:\Projects\SKKU.England\background\note\19_assets_liabilities_mapping.md (본 문서), C:\Projects\SKKU.England\background\note\19_assets_liabilities_mapping.csv
- 1차 근거: C:\Projects\SKKU.England\background\note\13_cdid_dictionary.csv (Table_J/D1_3/D4_6/D7_9/K 행)
- 인접 산출물: C:\Projects\SKKU.England\background\note\06_financial_account_categories.md §빠진 부분 2번; C:\Projects\SKKU.England\background\note\12_xlsx_sheet_inventory.csv (시트 메타)
- 원본: C:\Projects\SKKU.England\db\source\balanceofpayments2025q4.xlsx
