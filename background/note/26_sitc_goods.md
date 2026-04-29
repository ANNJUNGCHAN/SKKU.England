# 26회차 — ONS 상품무역(Trade in goods) · SITC Rev.4 · BPM6 Goods · CIF/FOB · 비통화용 금 보정

본 노트는 `db/CHECKLIST.md` Phase 3.2 §4 web-search 보강 **3차 라운드 — 상품무역 SITC·BPM6·비통화용 금** 산출물이다. `Table_E`(상품무역, 21)·`Table_BX`(귀금속 제외, 27)·`Table_B`(경상수지 본표 일부, 23) 합계 약 50 unmapped CDID에 적용. 강의 슬라이드 5의 1줄 정의 "상품수지: 재화의 수출입, net trade in merchandise goods"를 SITC Rev.4 + BPM6 §10 Goods + ONS UK Trade Glossary + HMRC OTS methodology + ONS NMG 보정 절차로 보강.

기존 노트(06회차 FA 분류 / 10회차 SITC 부분 인용 / 12회차 시트 인벤토리 / 24회차 EBOPS 12분류 / 25회차 FA 5분류)와 중복 회피.

---

## §1 SITC Rev.4 — 10개 1-digit 섹션과 ONS Pink Book "5분류" 표기

### §1.1 UN SITC Rev.4 (2006) 10개 섹션 원문

| 코드 | 영문 명칭 | 한국어 표기/일반 번역 |
|---|---|---|
| 0 | Food and live animals | 식료품 및 산동물 |
| 1 | Beverages and tobacco | 음료 및 담배 |
| 2 | Crude materials, inedible, except fuels | 비식용 원재료(연료 제외) |
| 3 | Mineral fuels, lubricants and related materials | 광물성 연료·윤활유 |
| 4 | Animal and vegetable oils, fats and waxes | 동·식물성 유지 |
| 5 | Chemicals and related products, n.e.s. | 화학 및 관련 제품 |
| 6 | Manufactured goods classified chiefly by material | 원재료별 제조품 |
| 7 | Machinery and transport equipment | 기계 및 운송기기 |
| 8 | Miscellaneous manufactured articles | 기타 제조품 |
| 9 | Commodities and transactions not classified elsewhere | SITC 미분류(비통화용 금 등) |

> "SITC, Rev. 4 was accepted by the United Nations Statistical Commission at its thirty-seventh session (March 2006) … same number of one-digit sections, two-digit divisions, and three-digit groups." — UNSD.

### §1.2 ONS Pink Book이 실제로 사용하는 묶음 (시리즈명 기준 6묶음)

강의·일반 표기 "5분류"는 단순화 표기이며, ONS time series 라벨은 다음 6묶음으로 표시.

| ONS 묶음 (SITC 코드) | 시리즈명 라벨 | 대표 시리즈 ID |
|---|---|---|
| **0+1** | Food, beverages and tobacco | BQPP (수출 volume index) |
| **2+4** | Basic materials | BQAS (수입), BOPM (수출), ELBF (Balance) |
| **3** | Fuels | (별도 시리즈 — 원유·정제유·천연가스·전력) |
| **5+6** | Semi-manufactures | BOPO (수출 SA £M) |
| **7+8** | Finished manufactures | BOPP (수출 SA £M), BQMY (수입 NSA) |
| **9** | Unspecified goods | (비통화용 금이 다수 비중) |

> "BOP:EX:volume index:NSA:**Food, beverages and tobacco: SITC 0+1**" — ONS time series BQPP.
> "Trade in Goods: **Basic materials (2and4)**: WW: Imports: BOP: CP: SA" — ONS time series BQAS.
> "BOP:Balance:NSA:**Material manufactures less erratics: SITC 6 less PS**" — ONS time series BQMJ (PS = Precious Stones·non-monetary gold 등 변동성 큰 항목 제외).

### §1.3 ONS UK Trade Glossary 2015 묶음 정의

> "basic materials (0+1), fuels (3), chemicals and semi-manufactures (5), material manufactures (6), finished manufactured goods (7), miscellaneous manufactures (8), and unspecified goods (9)" — ONS UK Trade Glossary 2015.
>
> *주의*: 2015 Glossary 표기는 0+1을 "basic materials"로 분류한 구판 표기. 현행 ONS time series 라벨은 0+1을 "Food, beverages and tobacco"로 표시(§1.2). 실데이터 보강 시 시리즈명을 우선 인용.

### §1.4 BPM6 §10 Goods chapter와의 위계

- IMF BPM6 Chapter 10(Goods)은 SITC가 아닌 **기능적 분류**(general merchandise / net export under merchanting / non-monetary gold)를 본문 분류로 사용.
- ONS는 BPM6 본표(경상수지 — 상품) 작성 후, 분석용으로 SITC 묶음 부표를 제공.
- 한국은행 국제수지 매뉴얼(BPM6)도 동일하게 "상품(Goods)" 본표는 일반상품·중계무역·비통화용 금 3 분류, SITC는 부표/통계청 무역통계 차원에서 사용.

---

## §2 General merchandise · Goods for processing · Repairs · Goods procured in port · Non-monetary gold (BPM6 Chapter 10)

### §2.1 General merchandise (BPM6 §10.17~§10.20)

- **정의**: 거주자–비거주자 간 소유권이 이전되는 모든 동산 중 비통화용 금·중계무역 순수출·운송수단 항만 조달분을 제외한 거래.
- **한국어 표기**: 일반상품.
- BPM6 본표에서 가장 큰 비중.

### §2.2 Goods for processing (가공용 재화) — BPM5 → BPM6 핵심 변경점

- **BPM5**: 가공 후 반환되는 재화의 총액(Gross)을 양변(수출·수입)에 모두 계상.
- **BPM6**: 소유권 이전이 없으면 **상품**이 아닌 **서비스(Manufacturing services on physical inputs owned by others)** 로 재분류 — 가공 수수료(net)만 서비스 항목에 계상 (§10.41~§10.42).
- ONS도 BPM6 시행 후 `Manufacturing services on physical inputs` 항목으로 이전.
- 한국어: 가공용 재화 → 위탁가공서비스(BPM6).

### §2.3 Repairs on goods — BPM6 서비스 분류

- BPM6: "Maintenance and repair services n.i.e."로 서비스에 계상(상품에서 제외).
- 한국어: 유지·수리 서비스. ONS Pink Book도 동일.

### §2.4 Goods procured in port by carriers (BPM6 §10.31)

- **정의**: 운송수단(선박·항공기)이 외국 항만/공항에서 조달하는 연료·식량·소모품 등.
- **한국어**: 운송수단 항만 조달 재화.
- 일반상품과 별도 항목으로 BoP에 계상되며, ONS Pink Book Ch.2도 별도 부표.

### §2.5 Non-monetary gold (비통화용 금) — BPM6 §10.13~§10.16

- **정의**: 통화당국(중앙은행·재무부)이 준비자산으로 보유하지 않는 모든 금·귀금속.
  > "Nonmonetary gold covers all gold other than monetary gold … not held as reserve assets (monetary gold) by the authorities. Non-monetary gold can be subdivided into gold held as a store of value and other (industrial) gold." — IMF BPM6 Chapter 10/11.
- **하위 분류**: (a) 가치저장용 금 bullion·동전, (b) 산업용/보석용 금.
- **분류 위치**: SITC 9 "Unspecified goods"의 대부분.
  > "Non-monetary gold forms the majority of the commodity group 'unspecified goods' and is the technical term for gold bullion not owned by central banks. Silver, platinum and palladium bullion form part of the 'material manufactures' commodity group." — ONS BoP Bulletin 2020 Q3.
- **GDP 중립**: ONS는 NMG 거래를 GDP 중립적으로 처리(수출은 valuables 음(-)의 투자로 상쇄).
  > "Imports and exports of gold are GDP-neutral; most exports add to GDP, but not gold, because the sale of gold is counted as negative investment, and vice versa for imports." — ONS, A brief explanation of non-monetary gold.
- **자료원**: 2013-04부터 Bank of England가 영국 주요 귀금속 청산기관(precious metals clearers) 월간 서베이. troy ounce를 LBMA·LPPM 월말 가격(파운드화)으로 환산.
- **한계**: 총수출·총수입 분리 자료 없음 — 순수출(net)만 추정.

---

## §3 CIF/FOB 조정 (BPM6 §10.34, ONS UK Trade Glossary)

### §3.1 원자료 vs BoP 기준

| 구분 | 수출 | 수입 |
|---|---|---|
| **HMRC OTS 원자료**(IMTS 기준) | FOB | CIF |
| **ONS BoP 기준** | FOB | **FOB** |
| 차액 | — | 국제운임·보험료(CIF − FOB) |

- IMTS(국제상품무역통계) 권고는 수입 CIF, BPM6는 양변 FOB.
- ONS는 HMRC OTS의 CIF 수입에서 국제운임·보험료를 차감하여 FOB 수입으로 환산.
- 차감된 운임·보험료는 **서비스(Transport·Insurance services)** 로 별도 계상.
- 결과적으로 경상수지 합계는 동일하되, 상품-서비스 분해 시 경계가 이동.

### §3.2 ONS UK Trade Glossary 인용

> "Exports are valued on a free on board (FOB) basis (the cost of goods to the purchaser abroad), while imports are valued on a cost, insurance and freight (CIF) basis. … To conform to the IMF Balance of Payments definition, the value of imports required is the value of goods at the point of export … so the freight and insurance costs of transporting goods to the UK needs to be deducted from the values recorded by HMRC." — ONS UK Trade Glossary 2015.

### §3.3 BoP adjustment 일반론

> "Balance of Payments requires that imports and exports are valued at the customs frontier of the economy from which the goods are first exported (FOB), while IMTS recommends CIF-type valuation for imports, so BOP applies FOB-type valuation for imports of goods." — IMF C.11 CIF to FOB Compilation Guide.

---

## §4 Table_BX (귀금속 제외 보조표) 도입 사유 및 정의

### §4.1 도입 배경

- 비통화용 금·은·백금·팔라듐 거래는 일회성 변동이 매우 커서 추세 해석을 왜곡.
- ONS는 분석 편의를 위해 BoP 본표(Table B) 외에 "귀금속 제외" 시리즈(Table BX)를 별도 제공.

### §4.2 ONS 공식 정의

> "In recent periods the trade in precious metals, notably non-monetary gold, has been more volatile than usual. In this release the ONS introduced estimates that exclude trade in precious metals (Table BX) so the underlying trends in the current account balance are clearer." — ONS Balance of payments, UK: July to September 2020.
>
> "Precious metals include non-monetary gold, silver bullion, platinum bullion and palladium bullion."

### §4.3 차감 대상 SITC 항목

- **SITC 9 Unspecified goods** 전체(대부분 비통화용 금) — 차감.
- **SITC 6 Material manufactures** 중 silver/platinum/palladium bullion 부분만 차감 (이를 위해 ONS는 "SITC 6 less PS" 시리즈[BQMJ 등] 별도 발간; PS = Precious Stones·non-monetary metals).
- 결과: **Table_B − Table_BX = 비통화용 금 + 기타 귀금속 bullion 순거래액**.

### §4.4 신설 시리즈 (Table BX 대표 식별자)

> "Table BX presents new trade in goods and current account aggregates and includes the following new series: **FUS7**: Exports of goods and services excluding precious metals, **FUS8**: Total trade exports excluding precious metals, and **FUS9**: Current account excluding precious metals credits." — ONS BoP Bulletin 2020 Q3.

---

## §5 영국 ONS 적용 함의

### §5.1 자료 흐름

1. **HMRC Overseas Trade Statistics (OTS)** — 월간. CHIEF/CDS 시스템(2020-08부터 CDS로 점진 전환). GB→EU는 customs export declaration, 북아일랜드–EU는 Windsor Framework 하 Intrastat 잔존.
2. **HS 8-digit 분류**로 수집 → SITC Rev.4로 매핑. 저액 거래 £873 이하는 SITC group 931에 일괄 합산.
   > "Imports and exports of an individual value of £873 or less are aggregated under SITC group 931" — GOV.UK.
3. **ONS BoP adjustment** — change of ownership 원칙 적용, CIF→FOB 조정, 비통화용 금 BoE 서베이 통합, 30여 자료원 보강(ITIS·BoE 등).
4. **분기 BoP 통합** → Pink Book Ch.2(Trade in goods).

### §5.2 영국의 만성 상품수지 적자 + 서비스수지 흑자

- Pink Book 2023: **상품수지 적자 GDP 대비 약 8.8% (2022년) / 서비스수지 흑자 약 6.0%**.
- 강의 슬라이드 21의 "한국 BoP는 상품수지≈무역수지지만 영국은 분리"의 의미:
  - 한국은행 BoP "상품수지" ≈ "무역수지".
  - 영국 ONS는 **Trade in goods**(상품) ↔ **Trade balance**(상품+서비스)를 명확히 구분, "Trade balance ≠ Goods balance".

### §5.3 데이터 검사 시 주의점

- HMRC OTS(월) ↔ ONS BoP(분기) **격차 존재** → "compiled to different sets of rules"(GOV.UK methodology). 분기 합산이 OTS 월합과 일치하지 않을 수 있음.
- 비통화용 금 변동 → Table_E·B 해석 시 반드시 Table_BX와 비교.
- SITC 9의 대부분이 비통화용 금이지만, **모두 금은 아님** — 저액 거래(£873↓) SITC 931이 섞여 있음.

---

## §6 출처 카탈로그 (1차 출처 우선)

| 영역 | 기관 | 자료 | URL |
|---|---|---|---|
| SITC Rev.4 | UN Statistics Division | Standard International Trade Classification, Revision 4 | https://unstats.un.org/unsd/trade/sitcrev4.htm |
| BPM6 Goods | IMF | BPM6 Chapter 10 (Goods Account) | https://www.imf.org/external/pubs/ft/bop/2007/pdf/bpm6.pdf |
| BPM7 Outline | IMF | BPM7 Chapter 10 Annotated Outline | https://www.imf.org/-/media/files/data/statistics/bmp7/chapters/ao-bpm-ch-10.pdf |
| CIF/FOB | IMF | C.11 CIF to FOB Compilation Guide | https://www.imf.org/external/pubs/ft/bop/2020/pdf/20-06.pdf |
| ONS Glossary | ONS | UK Trade Glossary of terms 2015 | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/uktradeglossaryofterms2015 |
| ONS NMG | ONS | A brief explanation of non-monetary gold | https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/articles/nationalaccountsarticles/abriefexplanationofnonmonetarygoldinnationalaccounts |
| ONS BoP QMI | ONS | Balance of payments QMI | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpaymentsqmi |
| ONS Methodological Notes | ONS | BoP methodological notes (BPM6 basis) | https://www.ons.gov.uk/file?uri=%2Feconomy%2Fnationalaccounts%2Fbalanceofpayments%2Fmethodologies%2Fbalanceofpayments%2Fbalanceofpaymentsmethodologicalnotes.pdf |
| ONS Pink Book 2023 | ONS | UK Pink Book 2023 bulletin | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2023 |
| Table BX 도입 | ONS | BoP UK: Q3 2020 (Table BX 신설 release) | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/julytosept2020/pdf |
| HMRC OTS | GOV.UK | OTS methodology and quality report | https://www.gov.uk/government/statistics/overseas-trade-statistics-methodologies/overseas-trade-in-goods-statistics-methodology-and-quality-report--3 |
| HMRC OTS 월간 | GOV.UK | UK overseas trade in goods statistics February 2026: methodology notes | https://www.gov.uk/government/statistics/uk-overseas-trade-in-goods-statistics-february-2026/uk-overseas-trade-in-goods-statistics-february-2026-methodology-notes |
| HMRC RTS | GOV.UK | Regional trade in goods statistics methodology | https://www.gov.uk/government/statistics/overseas-trade-statistics-methodologies/regional-trade-in-goods-statistics-methodology |
| ONS NMG 옵션페이퍼 | UK Statistics Authority | Treatment of Non-Monetary Gold in the UK National Accounts (NSCASE 2023/28) | https://uksa.statisticsauthority.gov.uk/wp-content/uploads/2023/11/NSCASE2328_Treatment_of_Non_Monetary_Gold_in_the_UK_National_Accounts.pdf |
| ONS BQPP | ONS | time series BQPP (Food, beverages and tobacco SITC 0+1) | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/bqpp/pb |
| ONS BQAS | ONS | time series BQAS (Basic materials 2and4) | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/bqas/pnbp |
| ONS BOPP | ONS | time series BOPP (Finished manufactures SITC 7+8) | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/bopp |
| ONS BQMJ | ONS | time series BQMJ (Material manufactures less erratics SITC 6 less PS) | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/bqmj/pb |

---

## §7 ~50 unmapped CDID 시트별 보강 가이드 — 8필드 표준 형식

| 필드 | 내용 | 본 노트 §참조 |
|---|---|---|
| 1. cdid | 4자리 ONS 코드 (예: BQPP, BOPM, FUS7) | 원자료 |
| 2. ko_label | 한국어 항목명 (예: "상품수출 — 식료품·음료·담배(SITC 0+1) 수량지수") | §1.2 시리즈명 |
| 3. en_label | ONS 시리즈명 원문 | §1.2 |
| 4. sitc_section | SITC 묶음 ("0+1", "2+4", "3", "5+6", "7+8", "9", "전체") | §1 |
| 5. bpm6_category | BPM6 분류 ("General merchandise", "Non-monetary gold", "Goods procured in port") | §2 |
| 6. valuation | 평가 기준 ("FOB-수출/FOB-수입(BoP 조정)") | §3 |
| 7. table_origin | 원본 시트 (Table_E / Table_BX / Table_B) | 원자료 |
| 8. source_url | 1차 출처 URL | §6 카탈로그 |

### §7.1 시트별 보강 우선순위

- **Table_E (상품무역, 21건)**: Exports/Imports/Balance × SITC 6묶음 + 합계. §1.2 라벨 매핑 + §3 CIF/FOB 표시 필수.
- **Table_BX (귀금속 제외, 27건)**: §4 정의 일괄 적용. FUS7~FUS9 신설 식별자 우선 매핑.
- **Table_B (경상수지 본표 일부, 23건)**: §2 BPM6 기능 분류로 본표 분해. 슬라이드 21 한국–영국 차이 주석.

---

## §8 확인 못한 부분 (정직 명시)

1. **BPM6 PDF §10.13~§10.42 문단별 영문 원문 직접 인용 실패** — IMF 서버 PDF fetch 403. 인용은 IMF BPM7 Annotated Outline·Eurostat·ABS 2차 인용 기반. 메인 에이전트가 로컬 BPM6 PDF 보유 시 §10.31, §10.34, §10.41 paragraph 직접 대조 권장.
2. **ONS UK Trade Glossary 2015 PDF 직접 다운로드 실패**(403). Glossary 본문 인용은 ONS HTML landing + 검색 결과 기반. 0+1을 "Food/beverages/tobacco"로 부르는지 "basic materials"로 부르는지는 시점에 따라 다름 — **현행 ONS time series 라벨(§1.2) 우선**.
3. **Pink Book Chapter 2 데이터셋(2016/2023/2025)의 정확한 sub-table 구조** — Excel 다운로드만 제공. `db/source/balanceofpayments2025q4.xlsx` Table_E 헤더와 직접 대조 필요.
4. **한국은행 BPM6 한국어 매뉴얼 정확한 URL** 미확보. ECOS 통계검색·한국은행 발간 BPM6 PDF 별도 확인.
5. **Table_BX의 FUS7/FUS8/FUS9 외 추가 신설 시리즈 ID 전체 목록** — 2020 Q3 release만 확보. 이후 release 확장 가능성.
6. **저액 거래 임계값(£873)**의 시점별 변동 여부 — 2026-02 기준. 과거 시계열은 임계 다를 수 있음.
7. **SITC 6 less PS** 시리즈에서 PS의 정확한 정의 — ONS time series 페이지 약어만 확인. 메타데이터 직접 대조 필요.

---

## §9 본 노트 적용 체크리스트 (Phase 3.4 명세서 단계용)

- [ ] `db/data/_spec/cdid_definitions_unmapped.csv` 상품무역 ~50건에 §7 8필드 채워 보강 CSV 산출.
- [ ] `db/REPORT.md`에 §5(영국 만성 상품수지 적자) 서술 보강.
- [ ] `db/source/balanceofpayments2025q4.xlsx` Table_E·Table_BX·Table_B 헤더와 §1.2 ONS 라벨이 일치하는지 직접 대조.
- [ ] 06·10·12·24·25 회차와의 cross-reference 확인(중복 회피).
