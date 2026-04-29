# 29회차 — Phase 3.3 도메인 맥락 정리(단위 혼재 + BoP 항등식 거시경제학적 의의)

본 노트는 `db/CHECKLIST.md` Phase 3.3 §1(단위 혼재 강의 표현)·§4(BoP 항등식의 거시경제학적 의의 — 명세서 도입부 인용용)의 산출물. Phase 3.3 §3(결측 표기 분류 근거)·§5(금융계정 음수 부호 해석)는 §3에 cross-reference로 처리. 강의 슬라이드(`background/BoP.pptx`)와 기존 노트(02·03·04·05·07·08·12·14·15·19·20·22·23 등)를 1차 근거로 사용 — 노트 24~28(Phase 3.2 §4 web-search 보강)과 중복 회피.

---

## §1 단위 혼재(£ million·£ billion·% of GDP)의 강의 자료 표현 방식

### §1.1 강의 자료의 "단위" 자체에 대한 직접 언급 위치

강의 자료(`background/BoP.pptx`)는 BoP 통계 단위(currency·억/백만)를 별도 슬라이드에서 표 형태로 명시하지 않으며, **단위 개념은 다음 두 슬라이드에서 stock/flow 구분과 화폐 단위 표기를 통해 간접적으로 노출**된다.

| 위치 | 강의 자료 원문(발췌·요약) | 단위 관련 함의 |
|---|---|---|
| **슬라이드 4** ("국제수지표의 정의 및 특징") | "플로우(flow) 개념: stock means **gross (amount of purchase itself)**, while flow means **net (purchase minus sale)**. … Examples of stocks: **assets, debts, reserves**; Examples of flows: **export, import, account balances, changes in stocks**." | 단위 자체는 표기되지 않으나, **stock = 잔액(특정 시점)**, **flow = 일정 기간 거래 합**이라는 시간 차원의 차이가 단위 해석의 출발점. xlsx의 IIP 시트(K, D1.3 등)는 stock, BoP 본표(A·B·BX·E~J)는 flow에 해당. |
| **슬라이드 9** ("우리나라의 국제수지표 (2017년)") | 표 머리말 "**단위: 백만 달러**" — 한국은행 자료 인용 표기. 신·구매뉴얼 두 표 모두 "백만 달러" 사용. | BoP 표가 일반적으로 **백만 단위 통화**로 표기됨을 보여주는 강의 사례(영국 ONS의 GBP million과 같은 단위 체계). |
| **슬라이드 15** ("Korea CA/GDP, FA/GDP") | 그래프 세로축 "**−1.00% ~ 8.00%**" (GDP 대비 비율). 막대 라벨 CA/GDP·FA/GDP. | 단위가 통화액(£·$)에서 **% of GDP로 정규화**되는 분석 그래프 사용 사례. |
| **슬라이드 25** ("B.O.P vs IIP") | "**국제수지표(B.O.P)는 flow 통계이고 국제투자대조표(IIP)는 stock 통계**에 해당" | flow/stock 구분에 따라 "기간 합산값"과 "특정 시점 잔액"의 단위 의미가 갈린다는 거시 통계 원칙. |

요점: 강의 자료는 **"GBP million vs GBP billion"의 단위 격차를 직접 다루지 않는다**. 통화 단위 자체보다는 (a) flow/stock 차원, (b) 절대값/% of GDP 정규화 차원에 집중.

### §1.2 GDP 대비 비율(% of GDP) 표기 사용 위치

GDP 대비 비율은 강의 자료에서 단 한 곳, **슬라이드 15(한국 CA/GDP·FA/GDP, 2000~2025)** 에서만 정식 그래프 축으로 사용(노트 08 §슬라이드 15 참조).

- 메시지: BoP 항등식 `CA = FA(broad)`(슬라이드 14)의 **실측 검증**을 GDP-정규화로 시각화. 두 막대(CA/GDP·FA/GDP)가 거의 동일한 높이로 나타나 항등성을 직관적으로 보임.
- 강의 의도: 절대 통화액으로 표시하면 국가·시기 간 비교가 어려우므로 **GDP 대비 비율로 정규화**해 항등식의 거시적 일관성을 보임.
- 영국 ONS xlsx 적용: `Table_B`/`Table_BX`/`Table_R2`의 **부표 4 ("Balances as a percentage of GDP")** 가 정확히 이 표기 방식에 대응. ONS는 한 시트 내에서 부표 1~3(£million)과 부표 4(%GDP)를 함께 묶어 강의 슬라이드 15와 동일한 정규화 분석을 가능케 한다.

### §1.3 ONS xlsx의 단위 혼재 패턴 (노트 09·12·15에서 인용)

| 정규화 라벨 | scale_factor | 시트(부표) 수 | 대표 시트 |
|---|---:|---:|---|
| **GBP_million** | 1,000,000 | 35 | A, B, BX, C, E, F, G, H, I, J, R1, R2 (부표 1~3) |
| **GBP_billion** | 1,000,000,000 | 22 | D1.3, D4.6, D7.9, K, R3 (IIP·금융계정 누적치 시트) |
| **MIXED / unknown** | (없음) | 부표 4 (% of GDP) | Table_B/BX/R2 부표 4 |

핵심 패턴:
- **백만(£m) vs 십억(£bn) 분리 기준**: BoP flow(분기 거래액) = £million / IIP·금융계정 누적 잔액 = £billion. **stock 통계는 십억 단위**, flow는 **백만 단위**라는 ONS 관행이 슬라이드 4의 stock/flow 구분과 일치.
- **단일 시트 내 부표 단위 혼재 4종**: Table_B / Table_BX / Table_R2(각 부표 1~3 = £m, 부표 4 = %GDP), Table_R3(9개 부표 모두 £bn).
- **메타 시트 단위**: Cover_sheet·Notes는 단위 없음, Records는 "Current account (net) (£ billion)" 단일 표기.

### §1.4 Phase 3.3 §2 단위 정리 표 골격 (시트 → 단위 정규화 → 변환 규칙)

| sheet | sub_table | unit_raw | unit_normalized | scale_factor | 변환 규칙 |
|---|---|---|---|---:|---|
| Table_A | 1 | £ million | GBP_million | 1,000,000 | value × 1e6 → GBP |
| Table_B | 1 | £ million Credits | GBP_million | 1,000,000 | 동일 |
| Table_B | 2 | £ million Debits | GBP_million | 1,000,000 | 동일 |
| Table_B | 3 | £ million Balances | GBP_million | 1,000,000 | 동일 |
| Table_B | 4 | % of GDP Balances | PCT_GDP | 1 (비율) | 분기 GDP(£m) × value/100로 통화 환산 |
| Table_BX | 1~4 | (Table_B와 동일) | GBP_million / PCT_GDP | 동일 | 동일 |
| Table_C | 1~6 | £ million (EU·non-EU × Cr·Dr·Bal) | GBP_million | 1,000,000 | 동일. 1997~1998 EU 시계열 = "x"(비공개) |
| Table_D1_3 | 1~3 | £ billion | GBP_billion | 1,000,000,000 | value × 1e9 → GBP. ×1,000으로 £million 환산 |
| Table_D4_6 | 1~3 | £ billion | GBP_billion | 1,000,000,000 | 동일 |
| Table_D7_9 | 1~3 | £ billion | GBP_billion | 1,000,000,000 | 동일 |
| Table_E | 1~3 | £ million | GBP_million | 1,000,000 | 동일 |
| Table_F | 1 | £ million | GBP_million | 1,000,000 | 동일 |
| Table_G | 1 | £ million | GBP_million | 1,000,000 | 동일 |
| Table_H | 1 | £ million | GBP_million | 1,000,000 | 동일 |
| Table_I | 1 | £ million | GBP_million | 1,000,000 | 동일 |
| Table_J | 1 | £ million | GBP_million | 1,000,000 | 동일 (CDID 공백+마이너스 prefix 시 부호 반전) |
| Table_K | 1 | £ billion | GBP_billion | 1,000,000,000 | 동일 |
| Table_R1 | 1 | £ million | GBP_million | 1,000,000 | 개정 잔액 |
| Table_R2 | 1~3 | £ million | GBP_million | 1,000,000 | 개정값 |
| Table_R2 | 4 | % of GDP | PCT_GDP | 1 (비율) | 개정 비율 |
| Table_R3 | 1~9 | £ billion | GBP_billion | 1,000,000,000 | IIP·거래·소득 9 부표 |
| Records | (메타) | £ billion | GBP_billion | 1,000,000,000 | 분기 신기록 요약 |
| Cover_sheet / Notes | (메타) | n/a | NA | — | 목차·footnote |

권고 — 단일 long-form CSV 적재 시 **value_raw**(원문 숫자), **unit_normalized**(GBP_million/GBP_billion/PCT_GDP), **scale_factor**, **value_gbp**(통화 단위로 환산한 절대값) 4개 컬럼을 분리해 보관. 부표 4의 PCT_GDP는 분기 명목 GDP(YBHA) 시계열과 join한 후에야 통화액과 비교 가능.

---

## §2 BoP 항등식의 거시경제학적 의의 — 명세서 도입부 인용용 한국어 문장

### §2.1 강의 슬라이드의 BoP 항등식 표현 (노트 04 cross-reference)

강의 자료는 표적 항등식 `CA + KA + FA + E&O ≡ 0`을 **명시적 식 형태로는 적지 않고**, 다음 세 슬라이드의 결합으로 도출.

| 인용 위치 | 강의 자료 원문(발췌) | 한국어 풀이 |
|---|---|---|
| **슬라이드 6** ("국제수지의 구성") | "오차 및 누락계정은 실제로 국제수지표를 작성하는 데 있어서 통계상의 불일치를 조정해 주기 위해서 사후적으로 기장해주는 항목임" | E&O는 통계 불일치를 사후 조정하는 보정 항목 — 항등식 잔차로 작용. |
| **슬라이드 13** ("국제수지 균형의 의미") | "국제수지표상 대변(credit)의 총합과 차변(debit)의 총합은 사후적으로 항상 일치 … 복식부기원리(Double-entry bookkeeping)에 따라 모든 거래는 대변과 차변에 동시에 한 번씩 기재되기 때문 … 이는 국제수지표상의 모든 계정(경상계정, 금융계정, 자본계정)을 합한 경우에 해당" | 복식부기에 따라 **전 계정 합 ≡ 0**이 사후 성립. 단일 계정만 보면 흑/적자 가능. |
| **슬라이드 14** ("주요계정의 관계") | "Identity: Assuming statistical discrepancy = capital account = 0, **Current account = Financial account (narrow concept) + Reserve account = Financial account (broad concept)**" / "Financial account in a broad sense = nonreserve FA + reserve account" / "Official Settlements balance = Reserve account" | **단순화 가정**: E&O = 0, KA = 0이면 **CA = FA(broad)** = 비준비 FA + 준비자산. |

### §2.2 경상수지 적자의 자금조달 측면 해석 (슬라이드 9·11·22·24)

| 인용 위치 | 강의 자료 원문(발췌) | 자금조달 해석 |
|---|---|---|
| **슬라이드 9** ("우리나라의 국제수지표 2017년") | 한국 신매뉴얼 표: 경상수지 +78,460 ↔ 금융수지 +87,110(자산·부채 증감 기준) — 절대값이 거의 일치 | 경상수지 흑자분이 **금융계정의 대외순자산 증가**로 흡수됨을 한국 사례로 시각화. |
| **슬라이드 10** ("경상수지 개념") | "흑자(surplus)는 생산량이 일부 남아 외국에 잉여생산량을 수출한 것 / 적자(deficit)는 생산능력 이상으로 지출하기 때문에 모자라는 부분을 외국에서 수입해 지출했음을 의미" | 적자 = "외국에서 수입해 지출" → **모자라는 자금을 외국으로부터 조달**. |
| **슬라이드 11** | "금융수지(준비자산 제외)의 흑자(surplus)는 대외순자산(net external assets)이 증가했음을 의미. 적자(deficit)는 **순차입이 증가**했음을 의미" | 비준비 FA 적자 = 순차입(net borrowing) 증가 — 자금조달 메커니즘 직접 명시. |
| **슬라이드 22** ("국제수지와 타 사회계정의 관계") | "Y = C+I+G+(EX−IM) … Y−A = EX−IM (혹은 CA) … 국민소득이 총지출을 초과하면 경상수지 흑자, 반대이면 경상수지 적자" | CA = Y − A(absorption). **적자 = 국내 지출이 국내 소득 초과** → 외국 자금 동원 필요. |
| **슬라이드 24** ("국제수지와 통화부문의 관계") | "(X−IM) = ΔNFA (3-4)" / "경상수지 흑자는 외국에 더 많은 물건을 팔아 외화를 취득했음을 의미하기 때문에 순외화자산(NFA)이 증가하고, 반대로 적자의 경우에는 순외화자산이 감소" | CA = ΔNFA. 경상수지 적자 = **순대외자산 감소(=외국으로부터 순차입)**. |

종합 해석: **"경상수지 적자 ⇒ 외국으로부터 순차입(net borrowing) ⇒ FA(broad) 부채 순증"** 의 등식은 슬라이드 11·14·24의 결합으로 표현된다. 영국처럼 만성적 CA 적자국에서는 이 해석이 직접 적용되어 **CA(−) ⇒ FA(broad)(−) ⇒ 비거주자에 대한 부채 순증**으로 읽힌다.

### §2.3 BoP는 flow, IIP는 stock — flow의 거래요인이 stock의 일부 변동분만 설명 (슬라이드 25)

> "국제수지표(B.O.P)는 일정 기간 동안 일어난 모든 국제거래를 종합적으로 정리한 통계 / 국제투자대조표(IIP): 특정 시점에서 한 국가의 대외투자 잔액과 외국인의 국내투자 잔액 및 그 변동내역을 나타낸 표 … 국제수지표(B.O.P)는 **flow 통계**이고 국제투자대조표(IIP)는 **stock 통계**에 해당 / 국제투자대조표(IIP)의 증감내역은 **거래요인과 비거래요인**으로 구분하여 기록 / 거래요인에 의한 증감액은 국제수지표의 **투자수지 및 준비자산증감의 합계**와 일치"

- **거래요인 (transactions)**: BoP의 금융계정 + 준비자산증감 — 실제 자금 흐름.
- **비거래요인 (non-transactions)**: 가격 변동·환율 변동·기타 조정(슬라이드 26 매트릭스 표에서 3분해, 노트 08).
- **ΔIIP = (BoP FA + 준비자산) + 재평가**. BoP flow는 IIP stock 변동의 일부분만 설명 — 만성적 채무국(영국)은 자국 통화 절상·자산가격 상승으로 인한 비거래 재평가가 거래요인보다 클 수 있어, BoP만 보면 IIP stock 동학을 정확히 추적할 수 없다(노트 05·18 인용).

### §2.4 명세서 도입부에 인용할 한국어 단락 (3~5문장)

> 영국 국제수지(Balance of Payments, BoP)는 일정 기간(분기·연간)에 거주자와 비거주자 사이에 발생한 모든 경제적 거래를 복식부기(double-entry bookkeeping) 원칙에 따라 기록한 **flow 통계**이며, 강의 자료(`background/BoP.pptx`) 슬라이드 13에 따르면 모든 계정(경상·자본·금융계정 + 오차 및 누락)을 합한 합계는 사후적으로 항상 0이 되어야 한다. 슬라이드 14는 통계 불일치 = 자본수지 = 0이라는 단순화 가정 하에 **`경상수지(Current Account) = 금융계정(좁은 의미, narrow Financial Account) + 준비자산(Reserve Assets) = 광의 금융계정(Financial Account, broad)`** 의 항등식을 제시하며, 이는 곧 경상수지 흑자(적자)가 비거주자에 대한 순대외자산 증가(부채 순증)로 정확히 흡수됨을 의미한다(슬라이드 11·24의 NFA·순차입 해석과 정합). 따라서 영국과 같은 만성적 경상수지 적자국에서는 본 항등식이 "경상수지 적자 ⇒ 외국으로부터의 순차입 ⇒ 광의 금융계정의 부채 순증"이라는 자금조달 측면 해석으로 읽히며(슬라이드 22의 `Y − A = CA`, 슬라이드 24의 `(X−IM) = ΔNFA`로 동치 표현 가능), 거시경제 분석에서 저축-투자 격차·국민소득 항등식과 직접 연결된다. 또한 슬라이드 25는 BoP가 flow 통계인 반면 국제투자대조표(IIP)는 stock 통계임을 명시하여, BoP의 거래요인이 IIP 잔액 변동의 일부(거래분)만 설명하고 나머지(가격 변동·환율 재평가)는 비거래요인으로 별도 기록됨을 분명히 한다. 본 명세서의 검증 절차는 이 강의 항등식을 영국 ONS BoP 분기 실측치(2025 Q4 등)에 적용하되, ONS는 자본수지(KA)가 0이 아니고 오차 및 누락(E&O, CDID = HHDH)이 분기 GDP의 약 0.9% 수준 변동성을 가지므로(노트 20), 표적 항등식 `CA + KA + FA + E&O ≡ 0`(부호 약속: FA는 자산취득 − 부채증가 = 순대출/순차입)으로 잔차를 명시 보존해 적용한다.

---

## §3 (cross-reference) 결측 표기·금융계정 음수 부호 해석

Phase 3.3 §3·§5는 **추가 발췌 없이 기존 노트로 충족**. 본 §3에는 cross-reference 위치만 정리.

### §3.1 결측 표기 의미 (Phase 3.3 §3)

- 1차 위치: **노트 15 §결측 표기 카탈로그**(`background/note/15_units_and_missing.md` 40~64행).
  - x 마커 360건(Table_C 1997~1998 EU 시계열, ONS 비공개·suppressed) — Notes 11번에 명시.
  - (empty) 약 35,000건(셀 padding 또는 시리즈 외).
  - GAF 권장 [c]/[x]/[z]/[low] 미사용, legacy `..`/`-` 미사용.
- 보완 위치: 노트 12 §이상점·노트 13 CDID별 결측 위치.
- 추가 적재 정책: 노트 15 §후속 작업 권고 — `value_raw="x" + value_numeric=NULL + missing_reason="confidential"` 3-컬럼 패턴 권장.

### §3.2 금융계정 음수 부호 해석 (Phase 3.3 §5)

- 1차 위치: **노트 03 §항목별 발췌 표** 4·5·6·7행.
  - 슬라이드 8: "새로운 매뉴얼에서는 금융계정 부호표기 방식을 '자산·부채의 증감 기준'으로 변경 … 자산 항목의 부호는 반대 방향으로 바뀜" — BPM6 부호 약속.
  - 슬라이드 9 한국 2017년 표: 신매뉴얼에서 금융수지 = −87,110으로 표시(흑자임에도 부호 음). **부호의 음(−)은 자본의 순유출이 아니라 부호 정의 변경에 따른 표현 변화**.
  - 슬라이드 11: "금융수지(준비자산 제외)의 흑자 = 대외순자산 증가, 적자 = 순차입 증가."
- 보완 위치: 노트 12 §시트별 인벤토리 표 sign_convention_text 컬럼(Table_J `_neg_<cdid>` prefix 운영 규칙) + 노트 19 양면 매핑.

### §3.3 BoP↔IIP 부호 비대칭

- 1차 위치: **노트 08 §슬라이드 26 매트릭스 표 분석**.
  - 슬라이드 26 도식 주석: "준비자산이 증가할 경우 국제수지표에서는 음(−)으로 표시하며, 국제투자대조표에서는 양(+)으로 표시."
- 보완 위치: 노트 05 §IIP 변화 분해 — ΔIIP = 거래요인 + 비거래요인.

---

## §4 출처 카탈로그

### §4.1 BoP.pptx 슬라이드 번호별 인용 위치

| 슬라이드 | 강의 자료 위치 | 본 문서 사용 |
|---|---|---|
| 슬라이드 4 | "국제수지표의 정의 및 특징" — stock vs flow | §1.1, §2.3 |
| 슬라이드 6 | "구성 — 금융계정·E&O" | §2.1 |
| 슬라이드 8 | "최근 매뉴얼 vs 이전 매뉴얼" — BPM6 부호 변경 | §3.2 cross-ref |
| 슬라이드 9 | "우리나라의 국제수지표 (2017년)" — "단위: 백만 달러" | §1.1, §2.2, §3.2 cross-ref |
| 슬라이드 10 | 경상수지 개념 — 흑자/적자 의미 | §2.2 |
| 슬라이드 11 | NFA·순차입 정의 | §2.2 |
| 슬라이드 13 | "복식부기 항등성" — 전 계정 합 ≡ 0 | §2.1, §2.4 |
| 슬라이드 14 | "Identity: CA = FA(narrow) + Reserve = FA(broad)" | §2.1, §2.4 |
| 슬라이드 15 | "Korea CA/GDP, FA/GDP" | §1.1, §1.2 |
| 슬라이드 22 | NIA — Y − A = CA | §2.2, §2.4 |
| 슬라이드 24 | (X−IM) = ΔNFA | §2.2, §2.4 |
| 슬라이드 25 | "B.O.P(flow) vs IIP(stock)" | §1.1, §2.3, §2.4 |
| 슬라이드 26 | BoP↔IIP 매트릭스 도식 | §3.3 cross-ref |

### §4.2 cross-reference 노트 위치

| 노트 파일 | 본 문서 사용처 |
|---|---|
| `background/note/02_bop_components.md` | §2 일반 배경 |
| `background/note/03_sign_conventions.md` | §3.2 — 슬라이드 8·9·11 발췌 |
| `background/note/04_identities.md` | §2.1·§2.4 — 6개 항등식 발췌표 |
| `background/note/05_iip_nfa.md` | §2.3 — 슬라이드 25 발췌 |
| `background/note/08_multimodal_slide_analysis.md` | §1.1·§1.2 슬라이드 15, §3.3 슬라이드 26 |
| `background/note/12_xlsx_sheet_inventory.md` | §1.3·§1.4 단위 인벤토리 |
| `background/note/15_units_and_missing.md` | §1.3·§1.4 단위 + §3.1 결측 |
| `background/note/19_assets_liabilities_mapping.md` | §3.2 양면 매핑 |
| `background/note/20_neo_volatility.md` | §2.4 HHDH 분기 변동성 |

---

## §5 확인 못한 부분

1. **ONS의 GBP million ↔ GBP billion 단위 분리 기준의 공식 이유**: 강의 자료는 단위 분리 기준 미제시. ONS BoP QMI에서 "왜 IIP·D 계열은 £bn, BoP flow는 £m을 쓰는가"의 명시 진술은 본 폴더에서 미확인.
2. **슬라이드 9 단위 표기 "백만 달러" — 영국 ONS 적용 시 통화 단위 차이**: 한국 사례 USD million, 영국 GBP million. 강의 자료는 통화 단위 변환·환율 적용 절차를 별도로 다루지 않음.
3. **% of GDP 표기에서 GDP의 정의 (명목 vs 실질, SA vs NSA)**: 슬라이드 15 그래프는 "GDP" 라벨만 있고 SA/NSA·분기 vs 연간 GDP 분모 정의 미상. ONS xlsx 부표 4 footnote에서 분모 GDP 정의 추가 점검 필요.
4. **표적 항등식 `CA + KA + FA + E&O ≡ 0`을 그 형태 그대로 적은 슬라이드는 없음**: 강의 자료는 슬라이드 13(복식부기) + 슬라이드 14(단순화 항등식) + 슬라이드 6(E&O 정의)의 결합으로만 도출 가능.
5. **만성적 CA 적자국(영국)의 자금조달 메커니즘에 대한 강의 자료 진술**: 슬라이드 11·24가 일반론으로만 다루며, 영국 특유 사례(예: 1차소득 흑자가 상품수지 적자를 부분 상쇄, 직접투자·증권투자 자본유입 비중 등)는 강의 자료에 없음 — `db/REPORT.md`·노트 22·23으로 보완.
