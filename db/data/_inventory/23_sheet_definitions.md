# 시트별 한국어 정의 명세 (Phase 1.1 §3.1 background-search 14개 단위)

본 문서는 `db/CHECKLIST.md` §3.1의 14개 항목을 강의 자료(`background/BoP.pptx` 슬라이드 4·5·6·7·9·10·11·12·14·21·22·23·24·25·26 + `background/note/02·05·06·07·08·14·19·20·21·22·23`)에서 1차 발췌·정리한 것이다. Phase 3.4 명세서 CSV의 `STAT_NAME / 정의 / 구성 항목 / 계산식 / 부호 해석 / 다른 변수와의 관계` 컬럼을 채우는 1차 근거로 사용된다.

각 단위마다 다음 6 블록을 일관 구조로 적는다.
1. 시트 / 영문 라벨 / 한국어 STAT_NAME (20회차 매핑)
2. 한국어 정의 (강의 슬라이드 인용)
3. 구성 항목 / 계산식 (강의 항등식 인용)
4. 부호 해석 (19회차 NAFA·NIL 표현 + Notes Table_A note 1 인용)
5. 다른 변수와의 관계 (19·22회차 항등식 + Table_J·K 양면 회계)
6. 1차 근거 (슬라이드·노트 출처)

본문 항목 수: 14건 / 강의 자료 미수록 표기 4건(Table_BX 도입 배경의 일부, Table_R 시리즈 개정 정책 세부, FATS 등) — 사유는 본 문서 말미에서 따로 명시.

---

## 1. 전체 잔액 요약 시트 (Table_A)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_A` / "Summary of Balance of Payments, Balances (net transactions)" / **「국제수지 잔액 요약」**(20회차 한국어 statname).
- **한국어 정의** — 강의 자료 슬라이드 13(복식부기 사후 항등성)·슬라이드 14(`CA = FA(narrow) + Reserve = FA(broad)`)의 잔액 단면을 한 시트에 모아 보여주는 **요약(summary)** 시트. 슬라이드 13 인용: "국제수지표상 대변(credit)의 총합과 차변(debit)의 총합은 사후적으로 항상 일치 … 이는 국제수지표상의 모든 계정(경상계정, 금융계정, 자본계정)을 합한 경우에 해당. 각각의 계정 혹은 일부 계정만 합하면 대변과 차변의 크기가 달라질 수 있음 — 예: 경상수지 불균형(흑자 혹은 적자)" (`background/note/03_sign_conventions.md` §발췌표). 즉 Table_A는 사후 항등성을 보여주기 전에 **부분합(경상·자본·금융·E&O·Reserve)** 의 흑·적자를 한눈에 보이는 표이다.
- **구성 항목 / 계산식** — Table_A는 **net transactions**(잔액)만 게재. 4개 잔액 컬럼 군: ① Current account balance, ② Capital account balance, ③ Financial account balance, ④ Net errors and omissions (`background/note/12_xlsx_sheet_inventory.md` 시트 인벤토리). 강의 항등식: `CA + KA + FA + E&O ≡ 0` (슬라이드 13 + 14 + 6 결합, 04회차 §발췌표 #2). 단순화 가정 시 슬라이드 14: `CA = FA(narrow) + Reserve = FA(broad)`.
- **부호 해석** — 슬라이드 10: "흑자(surplus)는 생산량이 일부 남아 외국에 잉여생산량을 수출한 것 / 적자(deficit)는 생산능력 이상으로 지출하기 때문에 모자라는 부분을 외국에서 수입해 지출했음을 의미." 즉 Table_A의 잔액 컬럼은 **+ = 자국 측 흑자(자금 유입 우위), − = 적자(자금 유출 우위)** 로 읽는다. 단 Table_A 자체는 19회차 표에서 "net transactions"로 게재되며 sign_prefix(공백+마이너스 prefix)는 없음(`background/note/12_xlsx_sheet_inventory.md`).
- **다른 변수와의 관계** — Table_A 4개 잔액은 다음 본표에서 양변(credit/debit)으로 분해됨: CA → Table_B(전체)·BX(귀금속 제외)·C(EU/non-EU), KA → Table_I, FA → Table_J(NSA), E&O → Table_A 자체. 슬라이드 25 IIP 분해(`ΔIIP = (FA + Reserve) + 비거래요인`)에서 Table_A의 FA 잔액이 Table_K 잔액 변화의 거래요인분과 직결.
- **1차 근거** — `background/BoP.pptx` 슬라이드 13·14·10·6 + `background/note/03_sign_conventions.md` §발췌표 + `background/note/04_identities.md` §발췌표 #1·#3 + `background/note/12_xlsx_sheet_inventory.md` Table_A 행.

---

## 2. 경상수지 본표 (Table_B)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_B` / "Current account, seasonally adjusted (4 sub-tables: Credits / Debits / Balances / Balances %GDP)" / **「경상수지 본표(SA)」**.
- **한국어 정의** — 슬라이드 5: "경상수지(Current account)는 상품·서비스의 수출입과 본원·이전소득의 합계." 슬라이드 14의 항등식 정의: `Current account = trade balance + balance on services + net primary income + net secondary income` (02회차 §발췌표). 분기 계절조정(SA) 기준의 4개 부표(Credits / Debits / Balances / %GDP)를 한 시트에 적층(`background/note/12_xlsx_sheet_inventory.md`: 600행 × 12열, 4 sub-tables).
- **구성 항목 / 계산식** — 4개 하위(슬라이드 5):
  1. **상품수지(Balance of goods)** — 재화 수출입(Goods, net trade in merchandise goods) — Table_E와 동일 정의·시계열.
  2. **서비스수지(Balance on services)** — 운수·여행·로열티 등 — Table_F와 동일.
  3. **1차소득(Primary income)** — 임금송금·배당·이자 — Table_G와 동일.
  4. **2차소득(Secondary income)** — 무상이전(원조·국제기구출연금) — Table_H와 동일.
  - 항등식(슬라이드 14): **CA = G + S + PI + SI** = (Goods balance) + (Services balance) + (Primary income balance) + (Secondary income balance) (`background/note/02_bop_components.md` §발췌표 마지막 행). 단순화 흑자조건(슬라이드 22): `Y − A = EX − IM = CA`.
- **부호 해석** — 슬라이드 13: "대변(credit)은 외국에서 자국으로 자금이 유입되는 거래(+) / 차변(debit)은 자국에서 외국으로 자금이 유출되는 거래(−)" (`background/note/03_sign_conventions.md`). Balances 부표 = Credits − Debits (Table_B 부표1 − 부표2). %GDP 부표는 Balances ÷ 분기 명목 GDP × 100. CA Balance + = 흑자(자국 생산>지출), − = 적자(`background/note/02_bop_components.md` §발췌표 5번).
- **다른 변수와의 관계** — Table_B는 (a) Table_E·F·G·H 4개 세부 시트의 합산 결과, (b) Table_BX는 동일 정의에서 비통화용 금(non-monetary gold)만 차감, (c) Table_C는 동일 합계를 EU/non-EU로 지리분해, (d) Table_R2는 Table_B의 시계열을 직전 발표 대비 개정. 슬라이드 14 항등식 `CA = FA(broad)`로 Table_J 합계와 사후 일치(영국 실측은 NEO 항을 포함, `background/note/20_neo_volatility.md`).
- **1차 근거** — `background/BoP.pptx` 슬라이드 5·9·14·22 + `background/note/02_bop_components.md` §발췌표 + `background/note/04_identities.md` §발췌표 #5a + `background/note/12_xlsx_sheet_inventory.md` Table_B 행.

---

## 3. 경상수지 귀금속 제외 보조표 (Table_BX)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_BX` / "Current account excluding precious metals, seasonally adjusted" / **「경상수지(귀금속 제외)」**.
- **한국어 정의** — Table_B와 동일 구조이나 **비통화용 귀금속(non-monetary gold) 거래분을 차감**한 보조표. 강의 자료 자체는 "귀금속 보정"을 별도로 다루지 않으며, 07회차 `background/note/07_glossary.md` §메타 표에 "귀금속 보정(Non-monetary Gold Adjustment) — 강의 자료 미수록, ONS 표준" 으로 표기.
- **구성 항목 / 계산식** — 4개 부표(Credits / Debits / Balances / %GDP) 구성은 Table_B와 동일. 강의 항등식 적용도 동일: `CA(excl. precious metals) = G' + S + PI + SI` (G' = Goods − Non-monetary gold). 정확한 ONS 보정 절차(어느 EBOPS·SITC 항목을 차감하는지)는 강의 자료에 없음 — `background/note/10_ons_web_research.md`의 ONS UK Trade Glossary("non-monetary gold" 정의 인용)로 보강.
- **부호 해석** — Table_B와 동일. + = credit 우위(흑자), − = debit 우위(적자). 비통화용 금 거래는 통상 큰 일회성 변동을 만들기 때문에 Table_BX는 **추세선 해석용**.
- **다른 변수와의 관계** — Table_B와 (Table_BX) 차이 = 비통화용 금 거래의 순규모. 강의 자료 슬라이드 21(상품수지 vs 무역수지) 차트의 예외적 변동을 해소하기 위한 ONS 운영 관행으로 추정(08회차 `background/note/08_multimodal_slide_analysis.md` §슬라이드 21 분석). Table_E의 상품 세부분해와 함께 보면 어느 분기에 어떤 SITC가 일회성 변동을 일으켰는지 추적 가능.
- **1차 근거** — `background/BoP.pptx` 슬라이드 5·14 (Table_B 정의 동일) + `background/note/12_xlsx_sheet_inventory.md` Table_BX 행. **도입 배경은 강의 자료 미수록(별도 web-search 위임)** — `background/note/10_ons_web_research.md` ONS UK Trade Glossary 인용으로 부분 보강.

---

## 4. EU/non-EU 분해 표 (Table_C)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_C` / "Current account, EU and non-EU (6 sub-tables)" / **「경상수지 (EU/non-EU)」**.
- **한국어 정의** — Table_B의 경상수지 4개 하위 + 합계를 **거래 상대방 국가군**(EU vs non-EU)으로 분해한 분기표. 강의 자료에는 지리분해 자체에 대한 정의가 없어 `background/note/23_geographic_breakdown.md` §1·2·5에서 보강: "Pink Book Ch.9가 Geographical breakdown of CA를 다루며, Table_C 6 부표는 분기 단위 EU vs non-EU 분해."
- **분해 기준** — `background/note/23_geographic_breakdown.md` §2: "2020-02-01 Brexit 이후 EU 정의가 EU27(영국 제외)로 전환. ONS는 시계열 일관성을 위해 과거 구간도 EU27 기준으로 재계산." 슬라이드 자체에는 EU 정의 변경에 대한 언급 없음.
- **구성 항목 / 계산식** — 6 sub-tables(추정 매핑, 23회차 §4): ① Trade in goods, ② Trade in services, ③ Primary income, ④ Secondary income, ⑤ Current account total, ⑥ Memo aggregates(EU27/non-EU/world). 각 부표는 Credits/Debits/Balance × {EU, non-EU} 매트릭스. 분기 단위 GBP million(`background/note/12_xlsx_sheet_inventory.md`).
- **부호 해석** — Table_B와 동일 (Credit + / Debit −). 단 **상대방 국가군별 합계**이므로 EU 흑자가 non-EU 적자로 상쇄될 때 전체 합계가 0에 가까워 보일 수 있음 — 해석 시 EU·non-EU 두 축을 분리해서 보고, 합계는 Table_B와 일치하는지 교차 검증 필요.
- **해석상 유의점** — `background/note/23_geographic_breakdown.md` §5: "Brexit 후 EU 정의 변경(EU28 → EU27)으로 시계열 단절 가능성. ONS는 과거를 재계산해 단절을 없앴으나, 외부 자료(Pink Book 2020 이전판) 비교 시 EU 집계 정의가 다를 수 있음." 또한 OECD/G7/BRICS 같은 다른 그룹은 Table_C에 포함되지 않음(개별국 단위 분해는 Pink Book Ch.9 연간 Dataset 9에서만 제공).
- **다른 변수와의 관계** — Table_C 부표5(CA total) = Table_B Balances 합계와 일치해야 함. 부표1·2·3·4 합계 = Table_E·F·G·H 합계와 정합. Table_K(IIP)의 지리분해는 **Table_C가 다루지 않으며**, Pink Book Ch.10 Dataset 10에서 별도 제공(`background/note/23_geographic_breakdown.md` §1).
- **1차 근거** — `background/BoP.pptx` 슬라이드 5·14 (CA 정의는 Table_B와 동일) + `background/note/23_geographic_breakdown.md` §1~5 + `background/note/12_xlsx_sheet_inventory.md` Table_C 행. **EU/non-EU 분류 자체는 강의 자료 미수록(별도 web-search 위임 → 23회차에서 보강 완료).**

---

## 5. 상품무역 시트 (Table_E)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_E` / "Trade in goods (3 sub-tables)" / **「상품무역」**.
- **한국어 정의** — 슬라이드 5: "상품수지: 재화의 수출입, **net trade in merchandise goods**". 02회차 §발췌표: "flow 개념. 복식부기, 대변(credit)=유입(+)·차변(debit)=유출(−). 통화액(예: 백만달러). 경상계정의 첫 하위항목."
- **구성 항목 / 계산식** — 3 sub-tables(`background/note/12_xlsx_sheet_inventory.md`: Exports / Imports / Balance, 451행 × 9열). 강의 자료에는 SITC 5분류·EBOPS 같은 세부 분류가 없으나 12회차 §매핑표는 "SITC 5 categories"로 표기. 슬라이드 21(`background/note/08_multimodal_slide_analysis.md`): "Balance of goods"와 "Balance of Trade" 두 시리즈가 한국 BoP에서는 거의 동일하게 그려지나, 영국 ONS는 "Trade in goods"(상품)와 "Trade balance"(상품+서비스)를 분리(`background/note/10_ons_web_research.md` §발췌표 #5).
- **세부 항목** — ONS UK Trade Glossary(10회차 §발췌표 #5): "general merchandise, goods for processing, repairs on goods, goods procured in port and non-monetary gold." 비통화용 금(non-monetary gold)은 Table_BX에서 분리 처리.
- **측정 단위** — GBP million, 1997~2025 분기·연간 적층(`background/note/12_xlsx_sheet_inventory.md`).
- **부호 해석** — `background/note/12_xlsx_sheet_inventory.md` 부호 컬럼: "Exports (+) / Imports (-)". 즉 부표1(Exports) 양(+) · 부표2(Imports) 양(+, 절대값으로 게재) · 부표3(Balance = Exports − Imports). 영국은 만성 상품수지 적자 → 부표3 통상 (−).
- **다른 변수와의 관계** — Table_E Balance = Table_B 부표3의 "Balance of goods" 행 = Table_BX(귀금속 제외) + Non-monetary gold 거래. 슬라이드 21·08회차 분석: "한국 BoP에서는 상품수지 ≈ 무역수지지만 영국은 분리. 영국 적용 시 두 개념을 혼용 금지."
- **1차 근거** — `background/BoP.pptx` 슬라이드 5·9·21 + `background/note/02_bop_components.md` §발췌표 1행 + `background/note/08_multimodal_slide_analysis.md` §슬라이드 21 + `background/note/10_ons_web_research.md` §발췌표 #5 + `background/note/12_xlsx_sheet_inventory.md` Table_E.

---

## 6. 서비스무역 시트 (Table_F)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_F` / "Trade in services (EBOPS 2010 12 categories)" / **「서비스무역」**.
- **한국어 정의** — 슬라이드 5: "서비스수지: 서비스의 수출입. 운수, 여행, 로열티 등 포함." 02회차 §발췌표 2행: "flow, 복식부기, 통화액. 상품수지와 합쳐서 광의의 무역수지(net exports, EX–IM)로 묶이며 슬라이드 22의 개방경제 항등식 Y=C+I+G+(EX–IM)에서 EX–IM에 해당."
- **세부 항목 (EBOPS 2010 12분류)** — 강의 자료에는 12분류 명세가 없음(02회차 §빠진 부분: "ONS 고유 용어, 강의 자료 미수록"). 10회차 §발췌표 #8(UN MSITS 2010)에서 보강:
  1. Manufacturing services on physical inputs owned by others (가공 서비스)
  2. Maintenance & repair n.i.e. (유지·보수)
  3. Transport (운송)
  4. Travel (여행)
  5. Construction (건설)
  6. Insurance & pension (보험·연금)
  7. Financial (금융)
  8. Charges for use of intellectual property n.i.e. (IP 사용료)
  9. Telecommunications, computer & information (통신·컴퓨터·정보)
  10. Other business (기타 비즈니스)
  11. Personal, cultural & recreational (개인·문화·여가)
  12. Government goods & services n.i.e. (정부)
- **측정 단위** — GBP million, 1997~2025 분기·연간(`background/note/12_xlsx_sheet_inventory.md`: 451행 × 13열). 12분류 + 합계 → 13열로 일치.
- **부호 해석** — Exports (+) / Imports (−). Balance = Exports − Imports. 영국은 만성 **서비스수지 흑자**(특히 Financial·Other business·Travel) → 부표3 통상 (+). `background/note/22_bop_data_sources.md` §자료원 카탈로그: "ITIS는 서비스 무역의 50% 이상을 차지하는 단일 최대 자료원."
- **다른 변수와의 관계** — Table_F Balance = Table_B 부표3의 "Balance on services" 행. 강의 슬라이드 21에서 "Balance of Trade = Balance of goods + Balance on services"로 종합 무역수지 정의(영국 ONS 정의, 10회차 §발췌표 #5). EBOPS 4번 Travel은 IPS(International Passenger Survey) 1차 자료 사용(`background/note/22_bop_data_sources.md`).
- **1차 근거** — `background/BoP.pptx` 슬라이드 5·22 + `background/note/02_bop_components.md` §발췌표 + `background/note/10_ons_web_research.md` §발췌표 #8 (12분류는 강의 자료 미수록, MSITS 2010 외부 출처) + `background/note/22_bop_data_sources.md` 자료원 카탈로그 + `background/note/12_xlsx_sheet_inventory.md` Table_F.

---

## 7. 1차소득 시트 (Table_G)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_G` / "Primary income" / **「1차소득(본원소득)」**.
- **한국어 정의** — 슬라이드 5: "본원소득수지(=1차소득수지): 임금송금, 배당 및 이자 등. ex) income receipts from Korea-owned assets abroad (including all factors of production) – income payment on foreign owned assets in Korea." 02회차 §발췌표 3행: "**대가성 소득(노동·자본 제공의 대가)** 의 순액. 이전소득과 구분되는 기준은 '대가의 유무'. IIP에 기록된 대외자산·부채(stock)에서 발생하는 수익 흐름(flow)이라는 점에서 슬라이드 25의 BoP(flow) vs IIP(stock) 구분과 연결."
- **세부 항목** — 강의 자료(슬라이드 5) 표현 기준:
  1. **근로자 보수(Compensation of employees)** — 노동 제공의 대가(임금송금).
  2. **투자소득(Investment income)** — 자본 제공의 대가, 다음 3분해(02회차 §빠진 부분 + `background/note/13_cdid_dictionary.md`):
     - 직접투자수익(DI income) — Table_D1_3·D4_6·D7_9의 sub3(Investment income earnings) 컬럼.
     - 증권투자수익(PI income) — 동일.
     - 기타투자수익(OI income) — 대출·예금 이자 등.
  - 강의 자료 슬라이드 6에는 직접투자/증권투자/기타투자 분류 정의는 있으나 "투자수익"이라는 별도 항목 정의는 없음 — Table_D 시리즈 sub3에서 양면 회계로 게재됨(`background/note/19_assets_liabilities_mapping.md`).
- **측정 단위** — GBP million, 1997~2025 분기·연간(`background/note/12_xlsx_sheet_inventory.md`: 451행 × 11열).
- **부호 해석** — Credit (+) / Debit (−). Balance = Credit − Debit. 영국은 만성 **1차소득 흑자**가 표준이었으나 최근 분기(2025 Q4) 적자 전환(`db/REPORT.md` 참조). 슬라이드 11 부호 정의(`background/note/03_sign_conventions.md` §발췌표 7행): "+ = 자국 자산이 외국으로부터 받은 수익 우위, − = 자국 부채에 대한 외국에 지불한 비용 우위."
- **다른 변수와의 관계** — Table_G Balance = Table_B 부표3의 "Balance on primary income" 행. 슬라이드 25 연결: "1차소득의 투자수익 부분은 IIP(Table_K)의 자산·부채 잔액에서 발생하는 flow." 따라서 Table_G의 투자소득 ↔ Table_D1_3/D4_6/D7_9 sub3의 투자수익 ↔ Table_K의 IIP 잔액의 3축이 정합. 영국이 만성 순채무국임에도 1차소득이 양(+)이었던 이유는 자산 측 수익률 > 부채 측 수익률(`background/note/18_iip_revaluation.md` §재평가 사례).
- **1차 근거** — `background/BoP.pptx` 슬라이드 5·6·9·25·11 + `background/note/02_bop_components.md` §발췌표 + `background/note/12_xlsx_sheet_inventory.md` Table_G + `background/note/19_assets_liabilities_mapping.md` (투자수익 양면 매핑).

---

## 8. 2차소득 시트 (Table_H)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_H` / "Secondary income" / **「2차소득(이전소득)」**.
- **한국어 정의** — 슬라이드 5: "이전소득수지(=2차소득수지): **아무런 대가 없이 제공되는 것으로** 원조, 국제기구출연금 등 포함." 02회차 §발췌표 4행: "flow, 통화액. **무상(unilateral) 이전**. 본원소득과 대칭(대가 無 vs 대가 有)."
- **세부 항목** — 강의 자료에 "원조, 국제기구출연금" 외 세부 분류는 없음. `background/note/12_xlsx_sheet_inventory.md` Table_H 14열 구조에서 ONS 표준 분해(추정): General government 부문 / Other sectors 부문, 각각 Credit·Debit·Balance 매트릭스. ONS Pink Book Ch.6의 표준 항목(personal transfers·workers' remittances·technical assistance grants·EU contributions 등)은 강의 자료 미수록.
- **측정 단위** — GBP million, 1997~2025 분기·연간(451행 × 14열).
- **부호 해석** — Credit (+) / Debit (−). Balance = Credit − Debit. 영국은 EU 분담금·해외 원조 지급으로 만성 **2차소득 적자**(부호 −)가 구조화. `background/note/02_bop_components.md` §발췌표 4행: "1차소득과 대칭(대가 無 vs 대가 有). 경상계정 4개 하위항목의 합계가 경상수지: 슬라이드 14의 항등식."
- **다른 변수와의 관계** — Table_H Balance = Table_B 부표3의 "Balance on secondary income" 행. CA 항등식: `CA = Goods + Services + Primary + Secondary` (슬라이드 14). 영국에서는 통상 |Goods 적자| + |Secondary 적자| > |Services 흑자| + |Primary 흑자| → CA 적자 구조.
- **1차 근거** — `background/BoP.pptx` 슬라이드 5·14 + `background/note/02_bop_components.md` §발췌표 4행 + `background/note/12_xlsx_sheet_inventory.md` Table_H. **세부 항목 분류는 강의 자료 미수록(BPM6 §12 외부 표준)** — Pink Book Ch.6 보강 권고.

---

## 9. 자본계정 시트 (Table_I)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_I` / "Capital account" / **「자본수지」**.
- **한국어 정의** — 슬라이드 5: "자본수지: 그 외 자산 및 부채의 금융거래 기록, transactions of fixed or nonfinancial assets (very small)." 슬라이드 7: "국가 간 부의 이전을 초래하는 그 외의 다른 거래들이 포함됨 / 시장거래와 상관없는 자본이전으로 발생하거나 비생산자산·비금융자산 또는 무형자산의 취득 및 처분을 나타내는 거래가 대부분." 02회차 §발췌표 5행: "예: 이민, 투자보조금, 채무면제, 토지(외국대사관)·지하자원 거래."
- **자본이전(Capital transfers)의 의미** — 슬라이드 7: "시장거래와 상관없는 자본 이전" — 정상적 매매가 아닌 일방적·구조적 이전(예: 채무면제, 자본 보조금). 거주자 변경(이민)에 따른 자산이동도 포함.
- **비생산비금융자산(Non-produced non-financial assets) 거래 의미** — 슬라이드 7: "비생산자산·비금융자산 또는 무형자산의 취득 및 처분" — 토지(외국대사관 부지)·지하자원·특허·상표 등이 대표 사례. 생산되지 않고 금융자산도 아닌 자산을 거주자·비거주자 간 거래할 때 자본수지에 기록.
- **측정 단위** — GBP million, 1997~2025 분기·연간(451행 × 14열).
- **부호 해석** — Credit (+) / Debit (−). Balance = Credit − Debit. 슬라이드 5: "**(very small)**. 규모는 매우 작음." 강의 항등식(슬라이드 14)에서는 "Assuming statistical discrepancy = capital account = 0" 단순화 — 즉 KA의 영향이 작아 무시 가능한 가정 하에 `CA = FA(broad)`로 다뤄짐.
- **다른 변수와의 관계** — `background/note/04_identities.md` §발췌표 #2·#3: "표적 항등식 `CA + KA + FA + E&O ≡ 0`" — KA는 단순화 가정에서 0이지만 실측에서 영국은 분기별 작은 양·음 변동. 슬라이드 26 매트릭스(`background/note/08_multimodal_slide_analysis.md`)에서 자본수지 행이 별도로 표시되며 "기타자본수지·자본이전·비금융자산취득" 3열로 분해됨.
- **1차 근거** — `background/BoP.pptx` 슬라이드 5·7·14 + `background/note/02_bop_components.md` §발췌표 5행 + `background/note/04_identities.md` §발췌표 #2·#3 + `background/note/08_multimodal_slide_analysis.md` §슬라이드 26 + `background/note/12_xlsx_sheet_inventory.md` Table_I.

---

## 10. 금융계정 시트 (Table_J)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_J` / "Financial account, NSA" / **「금융계정(NSA)」**.
- **한국어 정의** — 슬라이드 6: "금융계정(Financial account): 자산 및 부채의 소유권 변동과 관련된 거래." 슬라이드 14: `Financial account = Net acquisition of foreign financial assets − Net incurrence of liabilities + Net financial derivatives` (`background/note/04_identities.md` §발췌표 #3). 02회차 §발췌표: "광의 금융계정 = 비준비 FA + 준비자산."
- **자산/부채 부호 해석** — 슬라이드 8: "**새로운 매뉴얼에서는 금융계정 부호표기 방식을 '자산·부채의 증감 기준'으로 변경** … 이에 따라 금융계정 부채 항목의 부호는 종전과 동일하나 자산 항목의 부호는 반대 방향으로 바뀜." `background/note/03_sign_conventions.md` §발췌표 4행: "현행(BPM6): 부호 = '자산·부채 증감'. 자산 증가(자국의 대외자산 취득) = +, 부채 증가(외국의 자국 부채 취득) = +." 슬라이드 11: "금융수지(준비자산 제외)의 흑자(surplus)는 대외순자산(net external assets)이 증가했음을 의미. 적자(deficit)는 순차입이 증가했음을 의미."
- **음수 = 영국으로의 순자본 유입 해석** — 영국은 만성 CA 적자국이므로 항등식 `CA = FA(broad)`에서 FA 합계가 (−) → 즉 **자산 순취득 < 부채 순발행** = 부채 순증 = **외국으로부터의 순자본 유입**. 영국 BoP의 음수 FA 합계는 적자가 아니라 자본 유입을 뜻한다는 점이 핵심(`background/note/03_sign_conventions.md` §영국 적용 주의점 3번: "영국은 만성적 경상수지 적자 + 금융계정 부호 구조이므로, CA(−) ⇒ FA(−) ⇒ 부채 순증(net inflow)으로 읽어야 한다.")
- **Table_J 특이점 — sign_prefix prefix 부착** — `background/note/12_xlsx_sheet_inventory.md` Table_J 행: "CDID space+minus prefix means reverse sign". `background/note/19_assets_liabilities_mapping.md` §sign_prefix 패턴: "Table_J 부표1(자산 측)·부표3(순)과 모든 D1_3·D7_9 유량 컬럼은 sign_prefix=true (CSV에 공백+마이너스 prefix 부착, 부호 반전 필요). Table_J 부표2(부채 측)는 sign_prefix=false."
- **측정 단위** — GBP million, 1997~2025 NSA(계절미조정), 451행 × 14열.
- **다른 변수와의 관계** — Table_J 부표 1/2/3은 자산(NAFA) / 부채(NIL) / 순(Net = NAFA − NIL) 3축으로 19회차 매핑표와 일치. Table_D1_3(IIP+FA 자산), D4_6(IIP+FA 부채), D7_9(IIP+FA 순)와 1:1 대응(같은 CDID 공유). Table_K는 IIP 저량 종합. 슬라이드 14 항등식: `CA = FA(broad) = nonreserve FA + Reserve`. 영국에서는 NEO 잔차로 인해 사후 항등성 미달(`background/note/20_neo_volatility.md`: 2020Q1~2025Q4 |NEO|/GDP 평균 약 0.92%).
- **1차 근거** — `background/BoP.pptx` 슬라이드 6·8·9·11·14 + `background/note/03_sign_conventions.md` §발췌표 4·6·8행 + `background/note/06_financial_account_categories.md` §분류별 발췌표 + `background/note/19_assets_liabilities_mapping.md` 5분류별 매핑 + `background/note/12_xlsx_sheet_inventory.md` Table_J.

---

## 11. 직접투자·증권투자·금융파생상품·기타투자·준비자산 (FA 5분류 정밀)

본 단위는 Table_J 안의 5개 분류이자 Table_D1_3/D4_6/D7_9·Table_K에서 양면 회계로 게재되는 **FA 5분류**의 한국어 정의·BoP 매뉴얼상 분류 기준을 정리한다. 1차 근거는 슬라이드 6과 `background/note/06_financial_account_categories.md` §분류별 발췌표. 19회차 NAFA·NIL 매핑과 결합해 자산/부채 양면 컬럼 배치를 함께 표시한다.

### 11-1. 직접투자(Direct Investment, DI)

- **한국어 정의** — 슬라이드 6: "외국기업에 자금을 투입하여 **경영에 참가하기 위해** 행하는 투자." `background/note/06_financial_account_categories.md` §분류별 발췌표 1행: "해외 기업의 경영의사결정에 영향을 미칠 목적의 자본투입. 단순 수익 추구가 아닌 지배·관여 동기."
- **BoP 매뉴얼상 분류 기준** — 강의 자료(슬라이드 6)는 "경영참가" 동기만 제시하며 의결권 임계는 없음. `background/note/10_ons_web_research.md` §발췌표 #2(IMF DITT D.10): "BPM6 §6.12 — immediate direct investment relationships arise when a direct investor directly owns equity that entitles it to **10 percent or more of the voting power**." 10~50% = associate, 50% 초과 = subsidiary. ONS는 `background/note/16_oecd_bd4.md`에 따라 BD4(OECD Benchmark Definition of FDI 4판)를 완전 준수하며 SPE 포함·제외 두 시리즈 모두 발표.
- **양면 컬럼(19회차 §1)** — 자산 N2SV (Direct investment abroad) / 부채 N2SA (Direct investment in the UK) / 순 MU7M / IIP 자산 N2V3 / IIP 부채 N2UG / IIP 순 MU7O. 하위 3분해: Equity capital / Reinvestment of earnings / Debt instruments(Table_J 부표 col 2~4).

### 11-2. 증권투자(Portfolio Investment, PI)

- **한국어 정의** — 슬라이드 6: "투자자본의 **가치증가를 목적으로** 한 투자로 **주식과 채권으로 구분**." 06회차 §분류별 발췌표 2행: "경영관여 없이 시세차익·이자·배당 등 금융수익을 노린 투자."
- **BoP 매뉴얼상 분류 기준** — 가치증가(수익) 목적, 의결권 10% 미만 + 부채증권. 강의 자료에는 임계 명시 없음(BPM6 외부 표준). 하위: 지분증권(Equity & investment fund shares) + 부채증권(Debt securities), 만기·발행자별(은행/일반정부/기타) 추가 분해는 강의 자료 미수록.
- **양면 컬럼(19회차 §2)** — 자산 HHZC / 부채 HHZF / 순 HHZD / IIP 자산 HHZZ / IIP 부채 HLXW / IIP 순 CGNH. 하위 Equity·Debt 2분할.

### 11-3. 금융파생상품(Financial Derivatives, FD)

- **한국어 정의** — 슬라이드 6: "파생금융상품거래를 기록." 06회차 §분류별 발췌표 3행: "옵션·선물·스왑 등 기초자산 가치에 연동된 계약의 거래·청산을 별도 항목으로 분리." 슬라이드 14: `+ Net financial derivatives` (순액 표기).
- **BoP 매뉴얼상 분류 기준** — 상품 형식(파생계약) 기준. 슬라이드 6에는 옵션·선물·스왑 등 구체 상품 열거 없음. ESO(Employee Stock Options)는 BPM6 표준에 포함되나 강의 자료 미수록.
- **양면 컬럼(19회차 §3)** — **유량은 자산/부채 분리 부재**. 순(net) ZPNN만 존재. IIP 저량은 자산 JX96 / 부채 JX97 / 순 JX98 양면 게재. ONS는 유량 단계에서 순액만 공시(슬라이드 14의 `Net financial derivatives` 표기와 일치).

### 11-4. 기타투자(Other Investment, OI)

- **한국어 정의** — 슬라이드 6: "**대출, 차입, 무역신용, 현금 및 예금** 등의 금융거래." 06회차 §분류별 발췌표 4행: "직접·증권·파생·준비자산에 속하지 않는 잔여(residual) 금융거래."
- **BoP 매뉴얼상 분류 기준** — 상품유형 잔여 분류. 자산-부채 구분(예: 대출=자산 측, 차입=부채 측)은 슬라이드에 묵시적. 보험·연금·SDR 배분·기타지분은 강의 자료 미수록(BPM6 §8 표준).
- **양면 컬럼(19회차 §4)** — 자산 XBMM / 부채 XBMN / 순 HHYR / IIP 자산 HLXV / IIP 부채 HLYD / IIP 순 CGNG. 자료원: BIS Locational Banking Statistics + BoE 은행권 자료 결합(`background/note/22_bop_data_sources.md`).

### 11-5. 준비자산증감(Reserve Assets / IR)

- **한국어 정의** — 슬라이드 6: "통화당국(중앙은행)이 일정시점에 있어서 국제유동성 수단으로 보유하고 있는 **대외지급준비자산(international reserves: IR)**의 증감." 하위: 화폐용 Gold, SDR, IMF reserve position, 외화자산. 슬라이드 6 추가 인용: "국제수지의 불균형을 직접 보전하거나 외환시장개입을 통해 간접적으로 불균형을 조정하기 위해 사용."
- **BoP 매뉴얼상 분류 기준** — 보유주체(통화당국) + 사용목적(국제수지 불균형 조정·외환개입). 영국은 HM Treasury가 법적 보유 주체이며 BoE가 운용 대행(EEA, Exchange Equalisation Account) — `background/note/17_uk_reserves.md`. 2025년 10월 말 영국 net reserves 약 USD 112.4 bn.
- **양면 컬럼(19회차 §5)** — **부채 측 부재**(BPM6 정의: 자산 한쪽). 자산 LTCV(유량) / 자산 LTEB(IIP 저량). Table_J 부표2와 Table_D4_6에는 Reserve 행 없음 → NIL = 결측이 정상.
- **부호 해석 (BoP vs IIP 비대칭)** — `background/note/08_multimodal_slide_analysis.md` §슬라이드 26 매트릭스 부호 주석: "**준비자산이 증가할 경우 국제수지표에서는 음(−)으로 표시하며, 국제투자대조표에서는 양(+)으로 표시**." 즉 BoP flow = "자국의 외화자산 취득 = 자본 유출"로 음(−), IIP stock = "자산 보유고 증가"로 양(+). 학생 혼동을 일으키는 핵심 비대칭.

### 1차 근거 (11번 단위 통합)

- `background/BoP.pptx` 슬라이드 6·8·9·11·14·26
- `background/note/06_financial_account_categories.md` §분류별 발췌표 + §BPM6 표준 비교
- `background/note/10_ons_web_research.md` §발췌표 #2 (FDI 10% 임계)
- `background/note/16_oecd_bd4.md` §항목별 발췌표 (BD4·SPE·FATS·UCP)
- `background/note/17_uk_reserves.md` (영국 EEA·BoE 보유 외환)
- `background/note/19_assets_liabilities_mapping.md` 5분류별 양면 매핑
- `background/note/08_multimodal_slide_analysis.md` §슬라이드 26 매트릭스 부호 주석

---

## 12. IIP 시트 (Table_K + Table_D 시리즈 보강)

- **시트 / 영문 라벨 / STAT_NAME**: `Table_K` / "International investment position end-of-period" / **「국제투자대조표(분기말)」**. 보강 시트: `Table_D1_3 / Table_D4_6 / Table_D7_9` ("IIP / financial account / investment income — Investment abroad / in the UK / Net").
- **한국어 정의** — 슬라이드 25: "**국제투자대조표(IIP): 특정 시점에서 한 국가의 대외투자 잔액과 외국인의 국내투자 잔액 및 그 변동내역을 나타낸 표**" (`background/note/05_iip_nfa.md` §발췌표 1행). 슬라이드 4: "stock means gross (amount of purchase itself) … Examples of stocks: assets, debts, reserves." 슬라이드 25 추가: "국제수지표(B.O.P)는 flow 통계이고 국제투자대조표(IIP)는 stock 통계에 해당."
- **자산 / 부채 / 순대외자산 개념** — 슬라이드 11: "금융수지(준비자산 제외)의 흑자(surplus)는 **대외순자산(net external assets)** 이 증가했음을 의미. 적자(deficit)는 순차입이 증가했음을 의미." 슬라이드 24: "(X − IM) = ΔNFA"(`background/note/05_iip_nfa.md` §발췌표 6·7행). 즉 **Net IIP = 총자산 − 총부채 = NFA**. 영국은 만성 순채무국(2025 Q4 말 −£199.8 bn, `background/note/17_uk_reserves.md` §항목별 발췌).
- **BoP 거래 흐름과의 관계** — 슬라이드 25: "**국제투자대조표(IIP)의 증감내역은 거래요인과 비거래요인으로 구분하여 기록 / 거래요인에 의한 증감액은 국제수지표의 투자수지 및 준비자산증감의 합계와 일치**." 슬라이드 26 매트릭스(8회차 분석)에서 시각적으로 도식화:

  ```
  ΔNet IIP(t) = [FA(t) + ΔReserve(t)]      ← 거래요인 (= BoP의 거래분)
              + [재평가, 환율, 기타조정](t)  ← 비거래요인
  ```

  영국에서 비거래요인(재평가)이 거래요인보다 큰 영향을 미치므로 BoP 금융수지만으로 ΔNet IIP 추정 시 큰 오차 발생(`background/note/05_iip_nfa.md` §영국 ONS 적용 주의점 2번). 분기 단위 재평가 3분해는 ONS xlsx에 포함되지 않음(`background/note/18_iip_revaluation.md` §1: "보유 분기 BoP Statistical Bulletin Tables xlsx에는 재평가 3분해가 포함되지 않는다." → Pink Book Dataset 8 별도 다운로드 필요).
- **부호 해석** — 슬라이드 8: BPM6 — 자산↑ = (+), 부채↑ = (+). Table_K sub1(자산)·sub2(부채)·sub3(순) 모두 양수로 게재(부호 반전 prefix 없음, `background/note/19_assets_liabilities_mapping.md` §sign_prefix 패턴). 단 슬라이드 26 주석: "준비자산이 증가할 경우 국제수지표에서는 음(−), 국제투자대조표에서는 양(+)으로 표시" — Reserve 항목의 BoP/IIP 부호 비대칭 주의.
- **측정 단위** — GBP **billion**(주의: Table_B/F/G/H 등 GBP million과 다름), 1997~2025 NSA, 451행 × 11열(`background/note/12_xlsx_sheet_inventory.md`).
- **다른 변수와의 관계** — Table_K = Table_D1_3 sub1 + Table_D4_6 sub1 + Table_D7_9 sub1의 통합본(stock만). Table_J(flow)의 누적분 + 비거래요인 = Table_K(stock). 슬라이드 24 식 `NFA + DC = H`로 영국의 통화부문(BoE 대차대조표)과 연결 가능하나, 영국의 변동환율·인플레이션 타게팅 체계에서는 ΔDC 자율조정이 커 강의 식의 직접 적용보다 해석적 도구로 활용해야 함(`background/note/04_identities.md` §영국 ONS 적용 시 주의점 4번).
- **1차 근거** — `background/BoP.pptx` 슬라이드 4·8·11·14·24·25·26 + `background/note/05_iip_nfa.md` 전체 + `background/note/17_uk_reserves.md` (Net IIP 정량값) + `background/note/18_iip_revaluation.md` (재평가 3분해 위치) + `background/note/19_assets_liabilities_mapping.md` (양면 매핑) + `background/note/12_xlsx_sheet_inventory.md` Table_K + Table_D1_3/D4_6/D7_9.

---

## 13. 직전 발표 대비 개정 시트들 (Table_R1·R2·R3)

- **시트 / 영문 라벨 / STAT_NAME**:
  - `Table_R1` / "Revisions summary - balances" / **「개정 요약(잔액)」**.
  - `Table_R2` / "Current account revisions (4 sub-tables incl. %GDP)" / **「경상수지 개정」**.
  - `Table_R3` / "International investment revisions (9 sub-tables)" / **「국제투자 개정」**.
- **한국어 정의** — 직전 발표(예: 2025 Q3 Statistical Bulletin) 대비 본 발표(2025 Q4)에서 변경된 시계열 값의 차이를 게재한 시트. **강의 자료에는 개정(revision) 개념에 대한 정의가 없음** — `background/note/07_glossary.md` §메타 표 미정의 항목: "개정(리비전): 강의 자료 미수록, ONS 표준."
- **개정 발생 원인** — `background/note/22_bop_data_sources.md` §자료원 카탈로그에서 보강:
  1. **다중 출처의 후행 도착**: HMRC OTS(월간) → ITIS·IPS(분기) → AIFDI/AOFDI(연간) → BIS(분기 t+4개월)의 시차로 인해 한 발표에 잠정치가 들어가고 다음 발표에서 확정치로 교체.
  2. **ONS National Accounts Revisions Policy** (2024-05·2025-06 갱신): 직전 분기 외 시계열은 두 번째 릴리스 시 일괄 갱신. Pink Book(연간 10~11월)에서 모든 자료원을 동시 reconcile.
  3. **2023~2025 처리 오류**: HMRC 수입·ITIS 처리 시스템 오류로 2021년 이후 전 기간 개정(`background/note/22_bop_data_sources.md`).
- **해석 시 유의점** — `background/note/03_sign_conventions.md` §영국 ONS BoP 적용 시 주의점 4번: "ONS는 통계불일치(net errors and omissions)가 분기별로 크게 변동하므로 항등식이 실측에서 정확히 성립하지 않으며, REPORT.md 작성 시 잔차를 별도 표시할 필요." 개정에 따라 NEO 시계열도 변동(`background/note/20_neo_volatility.md`: 2020Q1~2025Q4 |NEO| 평균 5,872 £m, 최대 14,457 £m).
- **세부 구조** — `background/note/12_xlsx_sheet_inventory.md`:
  - Table_R1(445행 × 13열): Ch.01~08 잔액 개정 요약.
  - Table_R2(592행 × 13열): 경상수지 4 sub-tables(Credits/Debits/Balances/%GDP) 개정.
  - Table_R3(1327행 × 7열): 국제투자 9 sub-tables 수직 적층(IIP 자산/부채/순 + FA 자산/부채/순 + 투자소득 자산/부채/순 추정).
- **부호 해석** — Revisions 컬럼 = (현재 발표값 − 직전 발표값). + = 상향 개정, − = 하향 개정. R3는 GBP billion 단위로 다른 R1·R2(GBP million)와 단위 다름.
- **다른 변수와의 관계** — R1 ↔ Table_A(잔액 요약), R2 ↔ Table_B/BX/C·E·F·G·H(경상수지), R3 ↔ Table_D1_3/D4_6/D7_9·J·K(IIP·FA). 개정 영향이 큰 분기는 NEO 시계열에도 반영됨. Pink Book(연간) 발표는 Bulletin(분기) 발표와 reconcile되어 R1·R2·R3에 반영.
- **1차 근거** — **강의 자료 미수록(별도 web-search 위임)** — `background/note/22_bop_data_sources.md` (개정 정책·자료원 시차) + `background/note/10_ons_web_research.md` §발췌표 #10 (ONS National Accounts Revisions Policy) + `background/note/20_neo_volatility.md` (NEO 변동성) + `background/note/12_xlsx_sheet_inventory.md` Table_R1·R2·R3 행으로 보강.

---

## 14. 메타·주석 시트 (Cover_sheet, Notes, Records)

- **시트 / 영문 라벨 / STAT_NAME**:
  - `Cover_sheet` / "Balance of Payments, Quarter 4 (Oct to Dec) 2025: Published 31 March 2026" / **「표지·목차」**.
  - `Notes` / "Notes for all tables (10 sub-tables)" / **「공통 주석」**.
  - `Records` / "Summary of statistics for Quarter 4 (Oct to Dec) 2025" / **「분기 신기록 요약」**.
- **한국어 정의** — 본표(Table_A~K, R1~R3 17개)와 별도로 작성된 메타 시트. **강의 자료에는 ONS 표지·주석·기록 시트에 대한 직접 언급 없음** — `background/note/07_glossary.md` §메타 표의 "단위(파운드 백만)·결측 표기·개정·귀금속 보정" 항목은 모두 "강의 자료 미수록, ONS 표준."
- **각 시트의 역할** — `background/note/12_xlsx_sheet_inventory.md` §시트별 인벤토리 + `background/note/10_ons_web_research.md` §발췌표 #9·#10 보강:
  1. **Cover_sheet** (30행 × 19열): 분기 발표 식별 정보(분기·발표일), 17개 본표 + 3개 메타 시트의 색인(table of contents). ONS Service Manual은 결측 표기를 표지에 명시하라고 권고하나 강의 자료에는 언급 없음.
  2. **Notes** (51행 × 8열): 10개 sub-tables 형태의 공통 주석. 핵심 주석(`background/note/12_xlsx_sheet_inventory.md` Notes 행): "**reverse the sign of series prefixed with a minus**" — Table_J·D1_3·D7_9의 sign_prefix 컬럼에 적용되는 부호 반전 규칙(19회차 §sign_prefix 패턴). 슬라이드 8의 BPM6 부호 규약 변경(자산·부채 증감 기준)을 ONS가 운영적으로 구현하는 방식.
  3. **Records** (35행 × 5열): 분기 단위 신기록(highest/lowest 관측치)을 GBP billion 단위로 요약. Pink Book Ch.01 Main points와 대응(`background/note/12_xlsx_sheet_inventory.md` §매핑).
- **다른 변수와의 관계** — Notes 시트의 sign_prefix 규칙은 Table_J 부표1·3, Table_D1_3 sub2, Table_D7_9 sub2의 자동 처리 시 핵심 메타데이터. 강의 자료 슬라이드 8의 BPM5↔BPM6 부호 변경 설명(`background/note/03_sign_conventions.md` §발췌표 4행)과 정합되며, 강의 자료에서 언급되지 않은 "ONS 운영적 구현 방식"의 위치가 Notes 시트임이 본 매핑으로 확정됨.
- **부호 해석** — 메타 시트 자체는 데이터 값 없음. Notes 시트의 부호 규칙은 강의 슬라이드 8 BPM6 + 슬라이드 11(자산/부채 증감 부호) 정의를 운영적으로 풀어낸 것.
- **1차 근거** — **강의 자료 미수록(별도 web-search 위임)** — `background/note/12_xlsx_sheet_inventory.md` §시트별 인벤토리 (Cover_sheet/Notes/Records 행) + `background/note/10_ons_web_research.md` §발췌표 #9 (ONS Service Manual 결측 표기) + `background/note/19_assets_liabilities_mapping.md` §sign_prefix 패턴 (Notes 시트의 운영적 효과) + 슬라이드 8 BPM6 부호 변경 설명.

---

## 강의 자료 미수록(별도 web-search 위임) 항목 정리

다음 4건은 강의 자료에 직접 정의·도식이 없어 외부 웹/매뉴얼 자료(이미 수집된 `background/note/10/16/17/18/22/23` 등)로 보강했다. Phase 3.4 명세서 작성 시 1차 근거 컬럼에 명확히 표기 필요.

| # | 단위 | 강의 자료 미수록 부분 | 보강 출처 |
|---|---|---|---|
| 3 | Table_BX 도입 배경 | 비통화용 금(non-monetary gold) 보정 절차 | `note/10` (ONS UK Trade Glossary) |
| 4 | Table_C EU 정의 변경 | EU28 → EU27(Brexit) 전환 시점·재계산 | `note/23` (Pink Book Ch.9, Wikipedia EU27) |
| 13 | Table_R1·R2·R3 | 개정 정책·자료원 시차·처리 오류 | `note/10`, `note/22` (ONS Revisions Policy, BIS, HMRC) |
| 14 | Cover_sheet/Notes/Records | ONS 표지·주석·기록 운영 규칙 | `note/10`, `note/12` (Service Manual, sheet inventory) |

추가로 **부분 미수록**(강의 자료가 일부만 다루고 외부 보강이 필요한) 항목:

- 6번(Table_F): EBOPS 2010 12분류 명세 — 슬라이드 5는 "운수·여행·로열티" 등 예시만, 12분류 표는 `note/10` (UN MSITS 2010) 보강.
- 8번(Table_H): 세부 항목(personal transfers·EU contributions 등) — 슬라이드 5는 "원조·국제기구출연금" 예시만, BPM6 §12 외부 표준 필요.
- 11-1번(직접투자): 의결권 10% 임계 — 슬라이드 6은 "경영참가" 동기만, `note/10`·`note/16` (BPM6 §6.12, OECD BD4) 보강.
- 11-3번(파생상품): 옵션·선물·스왑·ESO 세부 — 슬라이드 6·14에 순액 표기만, BPM6 §7 외부 표준 필요.
- 11-4번(기타투자): 보험·연금·SDR 배분 — 슬라이드 6은 "대출·차입·무역신용·예금"만, BPM6 §8 외부 표준 필요.

---

## 사용 가이드 (Phase 3.4 명세서 CSV 매핑)

본 14개 단위는 Phase 3.4 명세서 CSV의 다음 컬럼을 채우는 1차 근거이다.

| 명세서 CSV 컬럼 | 본 문서 매핑 |
|---|---|
| `STAT_NAME` (한국어 통계표명) | 각 단위 §1 "한국어 STAT_NAME" 헤더 |
| `정의` | 각 단위 §2 "한국어 정의" 본문 (슬라이드 인용) |
| `구성 항목` | 각 단위 §3 "구성 항목" 부분 |
| `계산식` | 각 단위 §3 "계산식" 부분 (강의 항등식 인용) |
| `부호 해석` | 각 단위 §4 "부호 해석" 부분 |
| `다른 변수와의 관계` | 각 단위 §5 "다른 변수와의 관계" 부분 |
| `1차 근거` | 각 단위 §6 "1차 근거" 인용 목록 |

각 셀에 출처를 표기할 때는 본 문서의 단위 번호(예: §1, §11-2)와 슬라이드 번호를 함께 적어 추적성을 확보한다. 강의 자료 미수록 항목은 위 표의 "보강 출처" 컬럼을 명시 — 정의 셀에 "(강의 자료 미수록, `background/note/<NN>` 보강)" 부기.

---

## 관련 절대경로

- 1차 근거 슬라이드: `C:\Projects\SKKU.England\background\BoP.pptx` (슬라이드 4·5·6·7·9·10·11·12·14·21·22·23·24·25·26)
- 1차 근거 노트: `C:\Projects\SKKU.England\background\note\02_bop_components.md` ~ `23_geographic_breakdown.md`
- 인벤토리 12회차: `C:\Projects\SKKU.England\background\note\12_xlsx_sheet_inventory.md` (시트별 메타·표 코드·Pink Book 챕터 매핑)
- STAT_NAME 매핑(20회차): `C:\Projects\SKKU.England\db\data\_inventory\20_korean_statname.md`
- Phase 2.2 long-form CSV: `C:\Projects\SKKU.England\db\data\balanceofpayments2025q4_long.csv` (74,006행, 17 시트)
