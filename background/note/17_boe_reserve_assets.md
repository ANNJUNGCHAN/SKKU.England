# 17. 영국 보유 준비자산(International Reserves) 출처·정의 정리

> §0.2 배경지식 사전 정리 17회차 (中 우선순위)
> 목적: 강의 슬라이드 24의 **NFA(중앙은행)** 개념과 ONS Pink Book의 **Net IIP(국가 전체)** 개념을 정량적으로 분리하기 위한 1차 출처·정의 카탈로그.
> 작성: web-search 서브에이전트 위임 결과 정리.

---

## 핵심 결론 (한 줄 요약)

영국의 외환보유고(IR)는 **법적으로 HM Treasury 소유(EEA)**이며 BoE는 관리 대행에 불과하다. 따라서 강의 슬라이드 24의 "중앙은행 NFA" 개념을 영국에 그대로 적용하면 안 되고, **EEA 보유분(IR)**과 **순수 BoE 대차대조표 NFA**를 분리해야 한다. ONS Pink Book의 "Reserve assets" 라인은 *central government sector*에 귀속되며, 2025년 10월말 IR 잔액은 **약 $112bn (£85.5bn)**, 같은 시점 영국 Net IIP는 **약 −£200bn** — 부호도 규모도 달라 학생용 학습 사례로 적합.

---

## 1. 발표 체계와 1차 출처

### 1.1 HM Treasury / Bank of England — 월간 *UK Official Holdings of International Reserves*

- **HMT 컬렉션(보도자료 게시판)**: <https://www.gov.uk/government/collections/statistical-release-uk-official-holdings-of-international-reserves>
- **BoE 호스팅(히스토리 데이터 + 월간 페이지)**: <https://www.bankofengland.co.uk/statistics/uk-international-reserves>
- **BoE 메타데이터**: <https://www.bankofengland.co.uk/statistics/details/further-details-about-uk-international-reserves-data>
- **IMF SDDS Plus 영국 페이지(IRFCL 템플릿)**: <https://www.imf.org/external/np/sta/ir/IRProcessWeb/data/gbr/eng/curgbr.pdf>
- **IMF DSBB 영국(ILV00 분류)**: <https://dsbb.imf.org/sdds/dqaf-base/country/GBR/category/ILV00>

발표 주체는 **HMT(보도자료)**, 데이터 호스팅·관리 대행은 **BoE**. 매월 **세 번째 영업일** 발표(IMF SDDS Plus 양식 준수). 1999년 7월말부터의 시계열 보유.

### 1.2 BoE Bankstats — Reserve assets 시리즈

- **인터랙티브 DB 진입**: <https://www.bankofengland.co.uk/boeapps/database/>
- **Bankstats tables 메뉴**: <https://www.bankofengland.co.uk/statistics/tables>
- **"Reserve assets – total" 시리즈 ID**: `ACLRA`, `ATOTRA` (CategId=6)
  - URL: <https://www.bankofengland.co.uk/boeapps/database/FromShowColumns.asp?Travel=NIxAZxI3x&FromCategoryList=Yes&NewMeaningId=ACLRA,ATOTRA&CategId=6&HighlightCatValueDisplay=Reserve+assets+-+total>

> 본 조사 시점 BoE 도메인 일부가 HTTP 403 차단 → 정확한 표 코드(A·B·C 시리즈)와 단위·주기는 **사용자 환경에서 직접 DB 접속 후 확인 필요**. URL 파라미터로는 두 식별자(ACLRA, ATOTRA) 확인됨.

### 1.3 ONS Pink Book — Reserve assets 행

- **Pink Book 2025 게시판**: <https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025>
- **Dataset 08 (IIP)**: <https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/8internationalinvestmentpositionthepinkbook2016>
  - 설명 발췌: "reserve assets for **central government** and financial derivatives". 최신 갱신 2025-10-31.
- **CDID 예시**:
  - `CGDF` — IMF IIP: Reserve Assets Currency & Deposits with banks (£m, 월·분기·연)
  - `CGDG` — BoP: IIP: Reserve assets: Other assets: Total securities: NSA £m

### 1.4 Exchange Equalisation Account (EEA) — 법적 보유 주체

- **컬렉션**: <https://www.gov.uk/government/collections/hmt-exchange-equalisation-accounts>
- **EEA 2024–25 연차보고**: <https://www.gov.uk/government/publications/exchange-equalisation-account-report-and-accounts-2024-to-2025>
- **법적 근거**: Exchange Equalisation Account Act 1979 — <https://www.legislation.gov.uk/ukpga/1979/30>

---

## 2. 시리즈 정의·범위

### 2.1 구성요소 (IRFCL Section I 기준)

| 분류 | 세부 |
|---|---|
| 외환자산(Foreign currency assets) | 현금·예금(통화당국·은행), 증권(주식·채권·MMF·MM), 기타 청구권. 통화: USD·EUR·JPY·CAD·RMB |
| 금(Gold) | 시장가 평가 |
| IMF 자산 | SDR holdings + IMF reserve position |
| 기타 준비자산 | 외환 forward, swap position, reverse repo claims |

> 인용(BoE *Further details*): "Foreign currency reserves comprise currency and deposits (held with monetary authorities and banks), securities (equities, bonds, notes and money market instruments) and other claims. ... Other reserve assets comprise of foreign currency forwards, swap positions and reverse repo claims on counterparties."

### 2.2 헤지 / 언헤지 분리 (EEA 관리 구조)

- **헤지(hedged)**: USD·EUR·JPY·CAD·RMB 표시 적격자산 + SDR
- **언헤지(unhedged)**: USD·EUR 표시 채권, **금**, IMF 대출(NLF 일부), 통상 yen forward 통한 yen exposure

### 2.3 발표·평가 규약

- **빈도**: 월간(매월 3rd working day)
- **단위**: USD millions 기본, GBP millions 병기
- **시점**: 월말(end-month) 잔액
- **가치평가**: **시가평가(marked-to-market)**
- **표준**: IMF SDDS Plus → IRFCL 템플릿(Section I~IV)

> 인용(BoE): "The data released follows the IMF's Dissemination Standard (SDDS) and measures the value of the UK's foreign currency and gold assets, liabilities and derivatives on a marked-to-market basis."

### 2.4 최신 발표 수치 (2025년 10월말, 2025-11-05 발표)

| 항목 | 값 |
|---|---:|
| 총 준비자산 (USD) | **$112,358m** |
| 총 준비자산 (GBP) | **£85,518m** |
| 직전월(2025-09말) | $111,022m / £82,471m |

출처 PDF: <https://assets.publishing.service.gov.uk/media/690a272714b040dfe82922be/Statistical_Release_UK_official_holdings_of_international_reserves_-_October_2025.pdf>

> 사용자 메모의 "약 $1,800억" 수치는 SDDS Section I의 *official reserve assets*(현재 약 $112bn)와 다름. *gross foreign currency assets*(다른 정의) 또는 EEA 자산총계(부채 포함)일 가능성 → 메모 출처 재확인 권장.

---

## 3. BoP·IIP와의 매핑

### 3.1 ONS Pink Book Reserve assets ↔ HMT/BoE IR

| 구분 | Pink Book IIP | HMT/BoE IR |
|---|---|---|
| 통화 | GBP (£m) | USD 우선, GBP 병기 |
| 시점 | 연말(12-31) 또는 분기말 | 월말 |
| 빈도 | 연 1회(매년 10월 대규모) + 분기 BoP | 월간 |
| 개정 | 매년 10월 대규모 개정 | 매월 잠정치 → 차후 개정 |
| 부문 분류 | central government 라인 별도 | 동일 모집단(EEA + BoE 자체 외환자산) |
| 평가 기준 | BPM6 시가평가 | IRFCL 시가평가 |

> ONS는 IIP 변동의 **가격·환율·기타 요인 분해**를 전면 공개하지 않음 — 18회차(Pink Book Ch.9 재평가 분해) 작업 시 이 한계가 핵심 제약.

### 3.2 BoP 금융계정 거래흐름과의 연결

BoP 금융계정의 **Reserve assets transactions(거래)** ↔ HMT/BoE IR 월간 발표의 *flow* 항목(외환 매매·SDR 배분 등).

**잔액·거래 항등식**:
```
Δ Reserve assets (stock) = transactions (BoP flow)
                         + revaluations (가격·환율)
                         + other changes in volume
```

### 3.3 BPM6 부문 분류상 영국의 특수 처리

> 인용: "The UK follows the definitions of institutional sectors as set out in the BPM6. Where possible, sector data are made available with the exception of the **Central Bank which is included in MFIs**."

영국은 Central Bank를 **MFIs(Monetary Financial Institutions)에 통합**해 보고하지만, **Reserve assets 라인 자체는 별도 분리**(Pink Book Dataset 08의 "central government" 귀속 라인).

---

## 4. NFA(중앙은행) vs Net IIP(국가) 분리 — 학습 포인트

### 4.1 EEA는 BoE 대차대조표에 포함되지 않음 (영국 제도의 특수성)

> 인용(BoE *Further details about central bank's balance sheet*): "The Exchange Equalisation Account, the government account which holds the government's official reserves of gold, convertible currencies and special drawing rights, **does not form part of the Central Bank's balance sheet**."

**제도적 함의**: 강의 슬라이드 24가 묵시적으로 가정하는 "외환보유고 = 중앙은행 자산"이 영국에는 그대로 적용되지 않는다. 영국의 IR은 **HMT(EEA)** 소유·**BoE** 운영. EEA Act 1979 + 연간 service-level agreement에 근거.

### 4.2 BoE 자체 NFA 시리즈

- BoE Bank Return(주간)에 외화자산 항목이 **자체 보유분**(USD facility 운영, 외환 swap 라인 사용분 등)에 한해 표시.
- EEA 보유분과 **분리**되어 있어 규모는 매우 작음.
- 정확한 mnemonic은 본 조사 시점 미확정(BoE 도메인 403 차단으로 DB 직접 접속 필요).

### 4.3 Net IIP 대비 Reserve assets 비중

| 시점 | 항목 | 값 |
|---|---|---:|
| 2024년말 | Net IIP | −£145.6bn (GDP의 5.0% 부채) |
| 2023년말 | Net IIP | −£267.3bn |
| 2025년말 | Net IIP (REPORT.md 인용) | −£199.8bn |
| 2025-10말 | Reserve assets | +£85.5bn ($112bn) |

**학습 포인트**: Reserve assets는 부호(+), Net IIP는 부호(−). 규모도 차원이 다름(자산측 1조 파운드 단위 portfolio·direct·other investment 대비 reserve assets는 매우 작음). 강의 자료의 "NFA(중앙은행) vs Net IIP(국가)" 격차를 보여주는 직관적 사례.

---

## 5. 출처 카탈로그 (CSV는 동일 폴더 `17_boe_reserve_assets.csv`)

| 기관 | 제목 | URL | 갱신주기 | 단위 |
|---|---|---|---|---|
| HMT | UK official holdings of IR (컬렉션) | https://www.gov.uk/government/collections/statistical-release-uk-official-holdings-of-international-reserves | 월간 | USD m / GBP m |
| HMT | Statistical Release Oct 2025 (PDF) | https://assets.publishing.service.gov.uk/media/690a272714b040dfe82922be/Statistical_Release_UK_official_holdings_of_international_reserves_-_October_2025.pdf | 월간 | USD m / GBP m |
| BoE | UK International Reserves (허브) | https://www.bankofengland.co.uk/statistics/uk-international-reserves | 월간 | USD m / GBP m |
| BoE | Further details about UK IR data | https://www.bankofengland.co.uk/statistics/details/further-details-about-uk-international-reserves-data | — | — |
| BoE | Bankstats interactive DB | https://www.bankofengland.co.uk/boeapps/database/ | 월간 | 다양 |
| BoE | Reserve assets – total (ACLRA, ATOTRA) | https://www.bankofengland.co.uk/boeapps/database/FromShowColumns.asp?Travel=NIxAZxI3x&FromCategoryList=Yes&NewMeaningId=ACLRA,ATOTRA&CategId=6 | 월간 | (UI 확인 필요) |
| BoE | Foreign currency reserves (Markets) | https://www.bankofengland.co.uk/markets/foreign-currency-reserves | — | — |
| BoE | Bank Return data — Further details | https://www.bankofengland.co.uk/statistics/details/further-details-about-central-banks-balance-sheet-bank-of-england-bank-return-data | 주간/월간 | GBP m |
| HMT | EEA: report and accounts 2024–25 | https://www.gov.uk/government/publications/exchange-equalisation-account-report-and-accounts-2024-to-2025 | 연간 | GBP m |
| Parliament | Exchange Equalisation Account Act 1979 | https://www.legislation.gov.uk/ukpga/1979/30 | — | — |
| ONS | Pink Book 2025 (게시판) | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025 | 연간 | GBP m |
| ONS | Pink Book 2025 PDF | https://backup.ons.gov.uk/wp-content/uploads/sites/3/2025/10/UK-Balance-of-Payments-The-Pink-Book-2025.pdf | 연간 | GBP m |
| ONS | Dataset 08 — IIP (xlsx) | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/8internationalinvestmentpositionthepinkbook2016 | 연간 | GBP m |
| ONS | CGDF 시계열 | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/cgdf/pb | 월·분기·연 | GBP m |
| ONS | CGDG 시계열 | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/cgdg/pb | 월·분기·연 | GBP m |
| ONS | Understanding the UK's net IIP (해설) | https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/articles/understandingtheuksnetinternationalinvestmentposition/2020-04-27 | 1회성 | — |
| IMF | SDDS UK ILV00 | https://dsbb.imf.org/sdds/dqaf-base/country/GBR/category/ILV00 | 월간 | USD m |
| IMF | UK IRFCL 템플릿 PDF | https://www.imf.org/external/np/sta/ir/IRProcessWeb/data/gbr/eng/curgbr.pdf | 월간 | USD m |
| IMF | IRFCL Guidelines 2013 | https://www.imf.org/external/np/sta/ir/irprocessweb/pdf/guide2013.pdf | — | — |
| IMF | BPM6 Manual | https://www.imf.org/external/pubs/ft/bop/2007/bopman6.htm | — | — |

---

## 6. 미해결·후속 조사 항목

1. **BoE Bankstats 정확한 표 코드(A·B·C 시리즈)** — 사용자 환경에서 BoE DB 직접 접속해 ACLRA·ATOTRA의 단위·주기·전체 시리즈 목록 확정 필요(본 조사 시 403 차단).
2. **2025-10말 IR 구성요소별 분해**(외환·금·SDR·IMF position) — HMT PDF 직접 열람 권장.
3. **사용자 메모의 "$180bn"** — 다른 정의 가능성 농후. 메모 원문 출처 재확인.
4. **순수 BoE 대차대조표 NFA 분기 시계열** — Bank Return의 외환자산·외환부채 라인 mnemonic 확정 필요.

---

## 7. Phase 3 명세서 활용 가이드

- **STAT_NAME 한국어**: "영국 공식 보유 준비자산(월간)" / "영국 IIP 준비자산(분기·연)"
- **부호 규약 메모**: Reserve assets 자산측 (+), 거래(transactions) 부호는 BoP 일반 규약(BPM6) 따름.
- **결측·통화 통일 주의**: ONS Pink Book과 HMT/BoE IR은 단위·주기·시점이 모두 다름 → 통합 CSV에서 별도 STAT_CODE 부여 필수.
- **학습 사례**: 11회차 final_review에서 식별된 "NFA(중앙은행) vs Net IIP(국가)" 격차 학습용 자료로 본 노트 인용.

---

## 8. 인용·저작권

본 노트의 모든 정의·인용은 1차 출처(HMT, BoE, ONS, IMF) 공식 페이지에서 발췌. 한국어 정리 및 해석은 프로젝트 노트 목적으로 작성됨.
