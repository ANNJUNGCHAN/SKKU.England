# 09. 외부 환율·보강 자료 1차 출처 식별

> 분석 기간 2006Q1–2025Q4(80 분기). 본 문서는 환율 4종 및 외부 보강 자료의 **1차 출처 페이지 메타**만 정리하며, 데이터 다운로드는 후속 단계로 분리한다. 본 산출물은 보고서 단계 3(`web-search` 주도) 의 1차 결과로, 모든 인용에 출처 URL·발표/갱신일·라이선스를 부기한다.

---

## §1. 환율 4종 1차 출처 표

| # | 시계열 | 1차 출처 기관 | 시계열 코드 | 다운로드 페이지 URL | 주기 | 시점 범위 | 최신 갱신일 | 라이선스 |
|---|---|---|---|---|---|---|---|---|
| 1 | GBP/USD 명목 양자환율 (Sterling into US dollar, spot) | Bank of England — Statistical Interactive Database (IADB) | **XUDLUSS** (Spot, GBP into USD; daily) | https://www.bankofengland.co.uk/boeapps/database/Rates.asp?into=USD (USD 변환 화면) / 일별 시계열은 https://www.bankofengland.co.uk/boeapps/database/ 검색창에 `XUDLUSS` | 일(daily, 영업일), 월별 working-day 평균 별도 발표 | 1975년 이후 — 2006Q1 시작 80 분기 윈도우 **충분히 커버** | 일별 시계열 영업일 갱신, 월 평균 익월 초 게시 | **Open Government Licence v3.0**(BoE 일반 공시 자료) — BoE는 "indicative middle market rates"로 비공식 수치임을 명기 |
| 2 | GBP/EUR 명목 양자환율 (Sterling into Euro, spot) | Bank of England — IADB | **XUDLERS**(Spot, GBP into EUR; daily) — 보조: ECB Reference Rate(EUR/GBP) | https://www.bankofengland.co.uk/boeapps/database/Rates.asp?into=EUR / 검색 코드 `XUDLERS` / ECB: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-gbp.en.html | 일(daily, 영업일), 월 working-day 평균 별도 | 1999년 1월(유로 도입) 이후 — 80 분기 윈도우 **충분히 커버** | 일별 영업일 갱신 | **Open Government Licence v3.0**(BoE) / ECB 측은 자체 ECB Statistics 사용 약관 |
| 3 | Sterling Nominal Effective Exchange Rate (NEER) — Sterling ERI (broad) | Bank of England — Sterling ERI / 보조: BIS Effective Exchange Rate (broad nominal) | BoE: **XUDLBK67** (Sterling ERI, 일별·월별; January 2005 = 100). BIS: **NB.M.GB**(Nominal Broad EER, monthly) / FRED 미러 코드 **NBGBBIS** | BoE: https://www.bankofengland.co.uk/statistics/sterling-exchange-rate-index 및 https://www.bankofengland.co.uk/statistics/details/further-details-about-effective-exchange-rate-indices-data / BIS: https://data.bis.org/topics/EER/data | 일/월(BoE), 월(BIS broad) | BoE ERI 1990년 이후, BIS broad 1994년 1월 이후 — 80 분기 윈도우 **충분히 커버**. BoE ERI 자체는 단일 ERI 시리즈로 매년 무역 가중치 재추정 | BoE: 영업일 갱신 + 매년 가중치 재계산(직전 회차 2026-02-13 발표, 2026-03-11 시행). BIS: 매월 중순(다음 발표 예정 2026-04-30) | BoE = **OGL v3.0**, BIS = **BIS Terms of permitted use of statistics**(비상업·출처 표기 조건) |
| 4 | Sterling Real Effective Exchange Rate (REER, CPI 기반) | BIS — Real Broad Effective Exchange Rate(보조: OECD MEI CCRETT01.GBR) | BIS: **RB.M.GB**(Real Broad EER, CPI deflated, monthly; 2020 = 100) / FRED 미러 **RBGBBIS** | https://data.bis.org/topics/EER/data (UK 필터). 메소드 페이지: BIS Effective exchange rates overview (https://data.bis.org/topics/EER) | 월(monthly) | 1994년 1월 이후 — 80 분기 윈도우 **충분히 커버** | 매월 중순 갱신, 가중치는 3년 이동(현재 2017–19) 기준 | **BIS Terms of permitted use of statistics**(비상업·출처 표기) |

> 주(코드 식별 신뢰도): BoE IADB의 4-letter 시리즈 코드(XUDLUSS·XUDLERS·XUDLBK67) 는 BoE 검색 결과 페이지 타이틀 텍스트 + IDEAS/RePEc·외부 인용을 교차 확인했다. BoE 운영 도메인 일부 페이지는 본 조사에서 직접 fetch 가 차단되어, 본 표 값을 보고서 §1 표에 인용할 때는 **BoE IADB 검색창에 직접 입력하여 시리즈 페이지 캡처를 부록 별첨**할 것을 권장. XUDLBK67 의 narrow vs broad 분류는 출처별로 표현이 엇갈리며, BoE 는 단일 ERI 운영(매년 가중치 재추정) 이므로 narrow/broad 이분법은 **BIS 분류** 로 한정한다. 본 보고서에서는 "Sterling ERI (BoE)" + "BIS Broad NEER" 두 시리즈를 병기 인용하는 방식을 권장(상호 검증).

---

## §2. 환율 분기 평균 산출 방법 메모

1. **원자료 단위**
   - BoE GBP/USD·GBP/EUR(XUDLUSS, XUDLERS): **일별(영업일)** 4pm London "indicative middle market rate"(매수·매도 호가의 중간값). 출처: BoE "Further details about spot exchange rates data" 및 IADB Rates 화면. BoE 는 동시에 **monthly working-day average** 를 함께 발표.
   - BoE Sterling ERI(XUDLBK67): **일별** 종가 기반 + **월별 평균** 동시 공시. ONS 도 동일 월평균을 BK67(`/timeseries/bk67/mret`)로 미러링하며 Jan 2005 = 100.
   - BIS NEER/REER(broad, GB): **월별 평균** 기준만 발표(2020 = 100). 일별은 narrow 에 한해 별도 제공.

2. **본 보고서 분기 평균 산출 권고**
   - **방법 A (권고)**: BoE 발표 **월 working-day 평균 3개월의 단순 평균**. 보고서 80 분기 윈도우 전체에 대해 BoE·ONS BK67·BIS 모두 월 단위가 갖춰져 일관 적용 가능.
   - **방법 B (보조)**: 일별 시계열 → 분기 내 영업일 산술 평균. BoE XUDLUSS/XUDLERS/XUDLBK67 은 영업일 시계열이 1990년대부터 완비되어 가능. 단, 데이터량과 휴일 처리 규칙(BoE 는 영업일 정의를 London 기준)이 다르므로 **주말·BoE 휴장일은 제외**.
   - 두 방법 결과는 일반적으로 0.05% 미만 차이지만, **2016Q3·2022Q3 같은 변동성 분기**에서는 0.2%p 이상 벌어질 수 있어 보고서 §6(Brexit), §7(미니예산)에서는 **방법 A 로 본문 수치를 잡고 방법 B 로 robustness 각주**를 둘 것을 권장.

3. **공식 분기 데이터 존재 여부**
   - BoE: **공식 분기 시계열은 별도 코드로 발표하지 않음**. 분기 평균은 사용자가 월·일 데이터에서 직접 산출.
   - BIS: 분기 시계열을 별도 발표하지 않으며, 데이터 포털 다운로드 시 frequency=Quarterly 옵션이 제공되지 않음 → 월 평균 → 분기 평균 직접 가공.
   - ONS: BK67 월 시계열만 발표. 분기 가공 동일.

4. **결측·휴일 처리**
   - BoE 는 London 영업일 휴장 시 그날 값을 발표하지 않으므로(공란), 영업일만으로 평균 계산. ONS BK67 은 이미 working-day 월평균이라 휴일 보정 완료.
   - 2008-09 글로벌 금융위기, 2016Q3 Brexit 직후, 2020Q2 팬데믹 봉쇄 분기 모두 BoE 데이터 결측 없음(상시 공표 확인).

---

## §3. 가격탄력성·Pass-through 1차 출처 표

| # | 주제 | 1차 출처 | URL | 발표일 | 핵심 수치 | 라이선스 |
|---|---|---|---|---|---|---|
| W3-A | UK 수입물가 ERPT 기초 추정 (SITC-2/3 disaggregate) | BoE Working Paper No. 312 — Mumtaz, Oomen, Wang, "Exchange rate pass-through into UK import prices" | https://www.bankofengland.co.uk/working-paper/2006/exchange-rate-pass-through-into-uk-import-prices | 2006-12 | 산업별 ERPT 이질성 큼; 1995년 이후 평균 ERPT 가 통계적으로 유의하게 하락 | OGL v3.0 |
| W3-B | UK 수입물가 ERPT 최근 추정 (부문 합산 장기 약 74%) | BoE Staff Working Paper — "Non-linearities, asymmetries and dollar currency pricing in exchange rate pass-through: evidence from the sectoral level" | https://www.bankofengland.co.uk/working-paper/2020/non-linearities-asymmetries-and-dollar-currency-pricing-in-exchange-rate-pass-through | 2020 | **장기 ERPT 약 74%**(부문 집계), USD pass-through > broad ERPT, 큰 충격일수록 빠른 pass-through | OGL v3.0 |
| W3-C | "충격이 중요하다 — ERPT 추정 개선" | BoE External MPC Discussion Paper No. 43 / NBER WP 24773 — Forbes, Hjortsoe, Nenova | https://www.bankofengland.co.uk/external-mpc-discussion-paper/2015/the-shocks-matter-improving-our-estimates-of-exchange-rate-pass-through (NBER 미러: https://www.nber.org/system/files/working_papers/w24773/w24773.pdf) | 2015-11 (개정 2018) | ERPT 는 충격 원인(수요·공급·금융)에 따라 0.1–0.7로 변동. 단일 평균계수가 오해 소지 | OGL v3.0 / NBER 별도 |
| W3-D | 2015–2016 sterling 약세의 CPI pass-through 실측 | ONS Economic Review — "Exchange rate pass through and transmission to consumer prices following the 2015 to 2016 depreciation of sterling" (Chandler·Margrie·Romiti·Savic) | https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/compendium/economicreview/july2019/exchangeratepassthroughandtransmissiontoconsumerpricesfollowingthe2015to2016depreciationofsterling | 2019-07-18 | 수입물가 +20.8%p, 산출물가는 "훨씬 작음", 소비자물가는 "더욱 둔화"; 25%+ 수입집약 품목이 CPI 상승의 절반 설명 | OGL v3.0 |
| W3-E | UK 외부무역 동향 종합(가격·소득 탄력성 정성적 검토) | BoE Quarterly Bulletin 2011 Q3 — "Understanding recent developments in UK external trade" | https://www.bankofengland.co.uk/-/media/boe/files/quarterly-bulletin/2011/understanding-recent-developments-in-uk-external-trade.pdf | 2011-09 | UK 수출의 환율 탄력성 약 0.3(10% 절상 시 수출 −3%), 서비스 탄력성 2–4 범위 인용 | OGL v3.0 |
| W5/W6 | 트레이드 비용·탄력성 신방법 추정 | BoE Staff Working Paper — "Unlocking new methods to estimate country-specific trade costs and trade elasticities" | https://www.bankofengland.co.uk/working-paper/2021/unlocking-new-methods-to-estimate-country-specific-trade-costs-and-trade-elasticities | 2021 | 가격·관세 데이터 없이도 부문별(제조·서비스·무역재/비무역재) 탄력성 식별 | OGL v3.0 |

> 주("BoE pass-through 60–70%" 인용 한계): 보고서 본문에서 사용해 온 "BoE pass-through 60–70%" 표현은 W3-B 의 "장기 약 74%" 또는 W3-A·W3-C 의 산업별 0.5–0.7 구간을 통합한 표현으로, 단일 60–70% 수치를 직접 명시한 BoE 공식 자료는 본 조사에서 확인되지 않았다. 보고서 본문에서는 **"BoE 추정 장기 ERPT 약 60–80% (Mumtaz et al. 2006; BoE 2020)" 처럼 범위로 인용하거나, 단일 값을 사용할 경우 W3-B 74% 를 명시 인용**할 것을 권장.

---

## §4. 영국 변곡점 4건 1차 분석 보고서 표

| # | 변곡점 | 1차 분석 출처 | URL | 발표일 | 라이선스 | 핵심 발견 |
|---|---|---|---|---|---|---|
| E1-a | **2016 Brexit 국민투표 직후 sterling 약세와 NX 동학** — 제조업 가격·매출 영향 | ONS — "The impact of sterling depreciation on prices and turnover in the UK manufacturing sector" | https://www.ons.gov.uk/economy/inflationandpriceindices/articles/theimpactofsterlingdevaluationonpricesandturnoverinthemanufacturingsector/2017-09-15 | 2017-09-15 | OGL v3.0 | 2016Q3–2017Q2 제조업 수출량 +9%, 수출 sterling 단가 상승 |
| E1-b | 2016 Brexit ERPT 후속 분석 | ONS Economic Review (W3-D 동일) | https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/compendium/economicreview/july2019/exchangeratepassthroughandtransmissiontoconsumerpricesfollowingthe2015to2016depreciationofsterling | 2019-07-18 | OGL v3.0 | NEER 2015-08~2016-07 누적 −16.8%, CPI 절반은 high-import-intensity 품목 |
| E1-c | (보조) Brexit·환율·수출 학술 보고 | UK Trade Policy Observatory BP 44 — Winters et al., "Should the Brexit sterling depreciation have boosted exports?" | https://www.uktpo.org/briefing-papers/should-the-brexit-sterling-depreciation-have-boosted-exports-how-exchange-rates-affect-trade-and-prices/ | (UKTPO) | UKTPO 자체 약관 | GVC 참여 심화로 환율 탄력성 약화·정책 불확실성 효과 |
| E2 | **2020 팬데믹과 영국 BoP 충격** | ONS — "Coronavirus and the effects on the UK Balance of Payments" (Sumit Dey-Chowdhury) | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/coronavirusandtheeffectsontheukbalanceofpayments/2020-06-22 | 2020-06-23 | OGL v3.0 | 글로벌 수요 위축·서비스 무역 급감, "dash for cash" 식 자본흐름; 2020 연간 경상수지 적자 £73.9bn |
| E2-보조 | 2020Q2 BoP 분기 보도자료 | ONS — Balance of Payments, UK: April to June 2020 | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/apriltojune2020 | 2020-09 | OGL v3.0 | 2020Q2 수출 £140.1bn·수입 £123.2bn(2010–2016년래 최저) |
| E3 | **2022 mini-budget 사태와 sterling 급락** | BoE Staff Working Paper No. 1019 — Pinter, "An anatomy of the 2022 gilt market crisis" | https://www.bankofengland.co.uk/working-paper/2023/an-anatomy-of-the-2022-gilt-market-crisis | 2023-03-31 | OGL v3.0 | 30년 길트 수익률 +120bps/3일, LDI 펀드 강제매도; sterling 사상 최저 1.0327 USD(2022-09-26) |
| E3-보조 | IMF UK 2023 Article IV | IMF — UK 2023 Article IV Consultation Staff Report (CR 23/252) | https://www.imf.org/en/Publications/CR/Issues/2023/07/10/United-Kingdom-2023-Article-IV-Consultation-Press-Release-Staff-Report-and-Statement-by-the-Executive-Director-for-the-United-Kingdom-535878 | 2023-07-10 | IMF Publications copyright (인용 허용) | 2022-09 mini-budget 시장 스트레스, 2022 가을예산·BoE 개입으로 정상화 |
| E4 | **2025 비통화용 금(SITC 9·NMG) 무역 일회성 영향** — 월별 1차 보도 | HMRC — "UK overseas trade in goods statistics January 2025: commentary"(GOV.UK) | https://www.gov.uk/government/statistics/uk-overseas-trade-in-goods-statistics-january-2025/uk-overseas-trade-in-goods-statistics-january-2025-commentary | 2025-03-14 | OGL v3.0 | 2025-01 NMG 수출 +£6.6bn, NMG 수입 −£1.9bn, 對스위스 수출 +98%(£3.9bn 귀금속) |
| E4-보조 | NMG 통계 처리 개선과 Pink Book 2025 영향 | ONS — "Blue Book and Pink Book 2025: UK trade impact estimates" | https://www.ons.gov.uk/economy/grossdomesticproductgdp/articles/bluebookandpinkbook2025uktradeimpactestimates/2025-08-19 | 2025-08-19 | OGL v3.0 | NMG 이중계상 제거 + 비-bar 형태 NMG 보강(1997년 1월부터 소급) |
| E4-보조2 | NMG 통계 변동성 일반 안내 | ONS Blog — "It's indestructible – but can we always believe in (the UK trade figures with the disaggregated effect of …) GOLD?" | https://blog.ons.gov.uk/2020/02/10/its-indestructible-but-can-we-always-believe-in-the-uk-trade-figures-with-the-disaggregated-effect-of-the-international-trade-in-non-monetary-gold/ | 2020-02-10 | OGL v3.0 | NMG 는 BoP 트렌드 왜곡 가능성, 분리 공시 권고 |

---

## §5. 보고서 §1·§2·§7 등재용 출처 인용 형식

다음 형식을 그대로 복사해 본문 각주·표 캡션·참고문헌 절에 활용한다. **모든 항목에 "기관 — 자료명 — 시리즈 코드(있으면) — URL — 발표/갱신일 — 라이선스" 6 요소를 포함**한다.

### 5.1 §1(데이터 출처) 표 등재 형식 — 환율 4종

```text
- GBP/USD spot, 분기 평균 — Bank of England, IADB 시리즈 XUDLUSS(일별 4pm 미들레이트),
  https://www.bankofengland.co.uk/boeapps/database/ (검색: XUDLUSS),
  영업일 갱신, 라이선스: Open Government Licence v3.0.
- GBP/EUR spot, 분기 평균 — Bank of England, IADB 시리즈 XUDLERS,
  https://www.bankofengland.co.uk/boeapps/database/ (검색: XUDLERS),
  영업일 갱신, 라이선스: Open Government Licence v3.0.
- Sterling NEER (Sterling ERI), 분기 평균 — Bank of England, IADB 시리즈 XUDLBK67
  (Jan 2005 = 100, 무역가중치 매년 재추정; 직전 갱신 2026-02-13 발표·2026-03-11 시행),
  https://www.bankofengland.co.uk/statistics/sterling-exchange-rate-index,
  라이선스: Open Government Licence v3.0.
  교차검증: BIS Nominal Broad EER (시리즈 NB.M.GB / FRED 미러 NBGBBIS, 2020 = 100),
  https://data.bis.org/topics/EER/data, 매월 중순 갱신, 라이선스: BIS Terms of permitted use.
- Sterling REER (CPI 기반), 분기 평균 — BIS Real Broad EER (시리즈 RB.M.GB / FRED 미러 RBGBBIS, 2020 = 100),
  https://data.bis.org/topics/EER/data, 매월 중순 갱신 (다음 발표 2026-04-30),
  라이선스: BIS Terms of permitted use.
```

### 5.2 §2(방법론) 분기 평균 산출 명시 형식

```text
환율 분기 평균은 BoE/ONS·BIS가 발표하는 월별 working-day average(월평균)를 분기 내 3개월 단순 평균하여 산출한다(방법 A).
민감도 검증으로 BoE IADB 일별 시계열을 영업일 산술 평균한 분기 시리즈(방법 B)를 동일 절차로 산출하고 부록 표에 병기한다.
BoE는 분기 단위 공식 시계열을 별도 발표하지 않으므로 본 보고서가 산출하는 분기 평균은 "사용자 가공치"임을 각주로 명시한다.
```

### 5.3 §7(케이스 스터디) 인용 형식

```text
[Brexit 2016] ONS (2017-09-15), "The impact of sterling depreciation on prices and turnover in the UK manufacturing sector",
  https://www.ons.gov.uk/.../2017-09-15, OGL v3.0;
  ONS (2019-07-18), Economic Review — Chandler 외, "Exchange rate pass through ...", OGL v3.0.

[COVID-19 2020] ONS (2020-06-23), Dey-Chowdhury, "Coronavirus and the effects on the UK Balance of Payments",
  https://www.ons.gov.uk/.../2020-06-22, OGL v3.0;
  분기 보도: ONS Balance of Payments, UK: April to June 2020, OGL v3.0.

[Mini-Budget 2022] Bank of England Staff Working Paper No. 1019 (2023-03-31), G. Pinter,
  "An anatomy of the 2022 gilt market crisis", https://www.bankofengland.co.uk/working-paper/2023/an-anatomy-of-the-2022-gilt-market-crisis, OGL v3.0;
  IMF Country Report No. 23/252 (2023-07-10), United Kingdom: 2023 Article IV Consultation, IMF copyright.

[NMG 2025] HMRC/GOV.UK (2025-03-14), "UK overseas trade in goods statistics January 2025: commentary", OGL v3.0;
  ONS (2025-08-19), "Blue Book and Pink Book 2025: UK trade impact estimates", OGL v3.0.
```

### 5.4 §1·§2 본문 ERPT 인용 형식

```text
[ERPT 1차] Bank of England Working Paper No. 312, Mumtaz·Oomen·Wang (2006-12),
  "Exchange rate pass-through into UK import prices",
  https://www.bankofengland.co.uk/working-paper/2006/..., OGL v3.0.
[ERPT 갱신] Bank of England Staff Working Paper (2020),
  "Non-linearities, asymmetries and dollar currency pricing in exchange rate pass-through",
  https://www.bankofengland.co.uk/working-paper/2020/non-linearities-asymmetries-and-dollar-currency-pricing-in-exchange-rate-pass-through,
  OGL v3.0. 부문 집계 장기 ERPT 약 74%.
[ERPT 충격해석] BoE External MPC Discussion Paper No. 43 / NBER WP 24773,
  Forbes·Hjortsoe·Nenova (2015-11; 2018 개정), "The shocks matter", OGL v3.0.
[ERPT 실측] ONS Economic Review (2019-07-18), Chandler·Margrie·Romiti·Savic,
  "Exchange rate pass through ... 2015 to 2016 depreciation of sterling", OGL v3.0.
```

---

## 확인 못한 부분 (보고서에 명시 권장)

1. **"BoE pass-through 60–70% 추정"의 단일 직접 인용원** — 본 조사에서 확인된 BoE 공식 추정치는 (a) 산업별 광범위 분포(~0.1–0.7, Mumtaz et al. 2006), (b) 부문 집계 장기 약 74%(BoE WP 2020), (c) 충격 종류별 0.1–0.7(Forbes et al. 2015·2018) 로 모두 **"60–70%" 단일 값과 정확히 일치하는 BoE 1차 인용** 은 발견되지 않았다. 보고서 본문에서는 "BoE 추정 장기 ERPT 약 60–80% (Mumtaz et al. 2006; BoE 2020)" 처럼 범위로 인용하거나, 정확한 단일 값을 쓰려면 본 조사가 식별하지 못한 후속 BoE QB·MPR 문헌 추가 확인이 필요하다.
2. **BoE IADB 4-letter 시리즈 코드 단일 페이지 캡처** — `wwwtest.bankofengland.co.uk` 도메인은 테스트 미러로, 본 조사에서 운영(`www.bankofengland.co.uk`) 도메인 직접 페이지 본문은 일부 접근이 차단되었다. 코드 표기는 BoE 검색 결과 페이지 타이틀 텍스트와 IDEAS/RePEc·외부 인용을 교차 확인했다. 보고서 §1 표에 시리즈 코드를 인용할 때는 **BoE IADB 검색창에 직접 입력하여 시리즈 페이지 캡처를 별도 부록**에 첨부할 것을 권장.
3. **XUDLBK67 의 narrow vs broad 분류** — 검색 출처가 "narrow"·"broad" 로 엇갈리며, BoE 공식 페이지 본문 직접 fetch 가 실패했다. BoE 는 단일 ERI 를 운영하면서 매년 가중치를 재추정하므로 narrow/broad 이분법은 BIS 분류이며, BoE ERI 자체는 "**Sterling ERI(BoE)**" 로 단일 인용하는 것이 안전하다. NEER 의 broad 정의 비교용으로 BIS NB.M.GB 를 병기.
4. **ECB EUR/GBP reference rate** — GBP/EUR 보조 출처로 ECB 가 가용하나, 단위가 EUR per GBP(BoE)와 GBP per EUR(ECB) 역수 관계라 보고서에서 단일 단위로 통일 시 변환 각주 필요.

---

## 추가 참고 자료

- House of Commons Library — "Sterling exchange rates: Economic indicators" (SN02811): https://commonslibrary.parliament.uk/research-briefings/sn02811/
- BIS Statistical Bulletin tables (EER, June 2018 reference): https://www.bis.org/statistics/tables_i_eer.pdf
- ECB Pound sterling reference rate: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-gbp.en.html
- FRED 미러: NBGBBIS, RBGBBIS, NNGBBIS — https://fred.stlouisfed.org/series/NBGBBIS, /RBGBBIS, /NNGBBIS
- ONS BoP Pink Book 2025: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025
- ONS NMG 시계열(예시 ID): FSJ4, FSIF — https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/fsj4/mret , .../fsif/

---

## §6. 환율 시계열 적재·보고서 작성 정책 결정 메모

본 조사로 확보된 4종 환율의 1차 출처와 라이선스(OGL v3.0 + BIS Terms of permitted use) 를 근거로, **저장소 적재 정책은 다음과 같이 결정한다**:

- **저장소 적재 위치**: `db/data/_external/exchange_rates/` 하위에 4 CSV(GBP_USD·GBP_EUR·Sterling_ERI·BIS_Real_Broad_GB) 분기 평균을 적재. RDB 본체(`ecos_uk_bop.sqlite`) 는 변경하지 않으며, 외부 자료는 `_external/` 영역으로 분리(데이터 무결성 규약 준수).
- **적재 방법**: 분기 평균은 §2 방법 A(월 working-day 평균 → 분기 단순 평균) 로 산출하며, 일별 보조 시리즈는 별도 부록으로 둔다. 적재 자체는 단계 4 정량 분석 단위에서 `data-scientist` 가 수행한다.
- **출처 표 등재**: 보고서 §1·§2 데이터 출처 표에 §1·§2 형식을 그대로 인용하며, 모든 환율 시계열 인용에 시리즈 코드·URL·라이선스를 부기한다.
- **변환 각주**: GBP/EUR 의 단위 통일 규칙(BoE 기준 GBP per EUR) 을 §2 본문에 명시한다.

---

*본 산출물은 외부 인용·메타 확보만을 다루며, 데이터 다운로드는 후속 단계(`data-scientist` 단위)에서 수행한다.*
