# 영국 공식 외환보유액(UK Official Reserves) 시계열 (web-search 17회차)

본 문서는 `db/CHECKLIST.md` §0.2 신규 中 2번 항목(BoE Bankstats 또는 BoE Statistical Release에서 영국 보유 준비자산(IR) 시계열 확보. 슬라이드 24 NFA(중앙은행)와 슬라이드 11 Net IIP(국가 전체) 정량 분리)의 산출물이다.

## 요약

1. 영국 공식 외환보유액은 HM Treasury(HMT)와 Bank of England(BoE)가 공동 운영하는 **Exchange Equalisation Account(EEA, 환평형계정)** 에 보유되며, **금(Gold)·외화자산(Foreign Currency Assets)·SDR·IMF Reserve Position** 4가지로 구성된다.
2. **2025년 10월 말 기준 영국 순(net) 공식 보유 외환은 약 1,123억 달러**(USD 112.4 bn / GBP 85.5 bn), 9월 말은 1,110억 달러로 비교적 작은 규모.
3. 발표 주체는 HMT(법적 책임자)이며 BoE가 일상 운용을 대행. **매월 초** Statistical Release(보도자료) 형태로 발표(IMF SDDS 양식 준수).
4. 영국의 **Net IIP(국가 전체 순대외자산)** 는 2025Q4 말 기준 **−£199.8 bn**(약 −2,500억 달러)로 만성 순채무국이며, 중앙은행 보유 외환(IR)은 약 +1,123억 달러로 부호도 다르고 **Net IIP의 절반 이하** 규모.
5. 즉 슬라이드 24의 ΔNFA(중앙은행 NFA, 외환보유액 증감)와 슬라이드 11의 Net IIP(국가 전체 대외순자산)는 **부호·규모·주체가 모두 다른 별개 개념**이다.

## 항목별 발췌

| 항목 | 정의·수치 | 출처 URL | 07_glossary 매핑 |
|---|---|---|---|
| **EEA 정의** | 1932년 설립, "to check undue fluctuations in the exchange value of sterling". 1979년 EEA Act로 정비. **Gold·외화·SDR·IMF Reserve Position** 보유. HMT 소유, BoE가 대행 운용 | [Wikipedia EEA](https://en.wikipedia.org/wiki/Exchange_Equalisation_Account); [HMT Management of the Official Reserves 2020](https://assets.publishing.service.gov.uk/media/5e667304d3bf7f1084169646/EEA_final.pdf) | Reserve Assets / Official Reserves |
| **월간 발표** | HMT Statistical Release "UK Official Holdings of International Reserves" — 매월 초 발표(IMF SDDS 템플릿) | [HMT Collection](https://www.gov.uk/government/collections/statistical-release-uk-official-holdings-of-international-reserves) | — |
| **2025년 10월 말 잔액** | **순보유: USD 112,358 mn (GBP 85,518 mn)**. 9월: USD 111,022 mn. 월중 변동 +USD 1,335 mn | [HMT Oct 2025 PDF](https://assets.publishing.service.gov.uk/media/690a272714b040dfe82922be/Statistical_Release_UK_official_holdings_of_international_reserves_-_October_2025.pdf); [HMT Sep 2025 PDF](https://assets.publishing.service.gov.uk/media/68de9cccdadf7616351e4da1/Statistical_Release_UK_official_holdings_of_international_reserves_-_September_2025.pdf) | Reserve Assets (Official) |
| **총(gross) 외환** | TradingEconomics/CEIC 보조집계: 2025년 6월 약 USD 249.6 bn (gross, 외화부채 차감 전) | [CEIC UK FX Reserves](https://www.ceicdata.com/en/indicator/united-kingdom/foreign-exchange-reserves); [TradingEconomics UK](https://tradingeconomics.com/united-kingdom/foreign-exchange-reserves) | gross vs net 구분 |
| **BoE 자체 외화준비** | EEA와 별개로 BoE 자체 대차대조표상 외화준비도 보유(BoE Foreign Currency Reserves 페이지에서 별도 발표). 2025년 9·10월 Market Notice 발행 | [BoE Foreign Currency Reserves](https://www.bankofengland.co.uk/markets/foreign-currency-reserves); [BoE Market Notice 7 Oct 2025](https://www.bankofengland.co.uk/markets/market-notices/2025/october/foreign-currency-reserves-7-october-2025) | NFA(중앙은행) |
| **ONS BoP Reserve Assets와 매핑** | ONS BoP Pink Book의 Financial Account "Reserve Assets" 항목은 HMT 발표 net reserves 변동분과 개념적으로 동일(BPM6 기준). 표 K에서 분기별 flow 보고 | [ONS BoP 2025Q3](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/julytoseptember2025) | Financial Account → Reserve Assets |
| **Net IIP (국가 전체)** | **2025Q4 말 −£199.8 bn**(잠정), 2025Q3 −£151.8 bn(개정), 2025Q2 −£243.4 bn(개정). 자산 £14,778.8 bn vs 부채 £14,978.6 bn | [ONS BoP Oct–Dec 2025](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/octobertodecember2025); [CEIC UK Net IIP](https://www.ceicdata.com/en/indicator/united-kingdom/net-international-investment-position) | Net IIP(슬라이드 11) |

## 다른 주요국 IR 비교 (2025 후반 기준, USD bn)

| 국가 | 외환보유액(공식) | 발표 시점 | 출처 |
|---|---|---|---|
| 중국 | ≈ 3,449–3,570 | 2025 후반 | Statista/Wiki |
| 일본 | ≈ 1,230 | 2025 초 | Statista |
| 스위스 | 세계 3위 | 2025 | 동상 |
| 한국 | **428.1** | 2025-12 말 | [BOK](https://www.bok.or.kr/eng/main/contents.do?menuNo=400196); [Korea Herald](https://www.koreaherald.com/article/10649508) |
| **영국** | **≈ 112(net) / 250(gross)** | 2025-10 / 2025-06 | HMT, CEIC |
| 미국 | ≈ 240(공식 reserves, 금 제외 시) | — | (확인 못함) |

영국은 기축통화국이자 변동환율제이므로 IR 규모가 GDP 대비 작은 편(GDP의 4–8% 수준). 한국·일본·중국은 GDP 대비 20–40% 이상.

## 강의 슬라이드 11·24 적용 함의 (NFA 두 정의의 정량 분리)

- **슬라이드 24의 ΔNFA = X − IM**: 여기서 NFA는 **중앙은행 보유 외환(공식 준비자산)** 즉 EEA 잔액. 영국에서는 **약 +USD 112 bn(2025-10)** 수준이며, 변동 폭이 매월 수십억 달러로 작음. 경상수지 흑자/적자에 1:1로 반영되지 않음(영국은 변동환율제로 IR 변동이 BoP 조정 변수가 아님).
- **슬라이드 11의 Net IIP**: **국가 전체(정부+민간+중앙은행) 대외 순자산**. 영국은 **−£200 bn(약 −USD 250 bn)** 로 만성 순채무국. 민간(은행·기업·가계)의 대규모 대외부채가 주된 구성.
- **정량 분리 결론**: 영국 Net IIP(−$250 bn)에서 중앙은행 IR(+$112 bn) 비중은 약 −45%(절댓값 대비). 즉 영국의 음(−)의 대외순자산은 **민간·정부 부문의 순부채**가 압도적이며, 중앙은행 외환보유액으로 상쇄되는 부분은 일부에 불과. 두 NFA 개념을 동일시하면 안 됨을 보여주는 좋은 실증 사례.

## 빠진/확인 못한 부분

- **HMT PDF 본문 직접 파싱 실패**: 10월 PDF 바이너리가 비정상 디코딩되어 **자산 유형별(금/외화/SDR/IMF Reserve Position) 세부 분해 수치는 미확인**. 공식 PDF 직접 열람 필요.
- **BoE 자체(EEA 외) 보유 외환 규모**: BoE Foreign Currency Reserves 페이지가 403 차단 — Market Notice 본문 미확인.
- **미국 공식 reserves 2025 최신치**: 정확한 월말 수치 미확인(US Treasury TIC/IMF SDDS 직접 조회 필요).
- **ONS Table K(Reserve Assets) 분기별 flow 수치**: 본 회차에서 직접 발췌하지 못함 — `db/source/balanceofpayments2025q4.xlsx` 내부 Table K 직접 확인 권장.

## 출처

- [HMT Statistical Release Collection — UK Official Holdings of International Reserves](https://www.gov.uk/government/collections/statistical-release-uk-official-holdings-of-international-reserves)
- [HMT October 2025 Statistical Release (PDF)](https://assets.publishing.service.gov.uk/media/690a272714b040dfe82922be/Statistical_Release_UK_official_holdings_of_international_reserves_-_October_2025.pdf)
- [HMT September 2025 Statistical Release (PDF)](https://assets.publishing.service.gov.uk/media/68de9cccdadf7616351e4da1/Statistical_Release_UK_official_holdings_of_international_reserves_-_September_2025.pdf)
- [HMT Management of the Official Reserves (March 2020 PDF)](https://assets.publishing.service.gov.uk/media/5e667304d3bf7f1084169646/EEA_final.pdf)
- [HMT Exchange Equalisation Accounts collection](https://www.gov.uk/government/collections/hmt-exchange-equalisation-accounts)
- [EEA Report and Accounts 2024–2025](https://www.gov.uk/government/publications/exchange-equalisation-account-report-and-accounts-2024-to-2025)
- [Wikipedia — Exchange Equalisation Account](https://en.wikipedia.org/wiki/Exchange_Equalisation_Account)
- [BoE Foreign Currency Reserves landing page](https://www.bankofengland.co.uk/markets/foreign-currency-reserves)
- [BoE Market Notice — Foreign Currency Reserves 7 October 2025](https://www.bankofengland.co.uk/markets/market-notices/2025/october/foreign-currency-reserves-7-october-2025)
- [BoE — UK International Reserves September 2025](https://www.bankofengland.co.uk/statistics/uk-international-reserves/2025/september-2025)
- [ONS BoP July to September 2025](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/julytoseptember2025)
- [ONS BoP October to December 2025](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/octobertodecember2025)
- [ONS — Understanding the UK's Net International Investment Position](https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/articles/understandingtheuksnetinternationalinvestmentposition/2020-04-27)
- [CEIC — UK Net International Investment Position](https://www.ceicdata.com/en/indicator/united-kingdom/net-international-investment-position)
- [CEIC — UK Foreign Exchange Reserves](https://www.ceicdata.com/en/indicator/united-kingdom/foreign-exchange-reserves)
- [TradingEconomics — UK Foreign Exchange Reserves](https://tradingeconomics.com/united-kingdom/foreign-exchange-reserves)
- [Bank of Korea — International Reserves](https://www.bok.or.kr/eng/main/contents.do?menuNo=400196)
- [Korea Herald — Korea reserves Dec 2025](https://www.koreaherald.com/article/10649508)
- [IMF Data Home](https://data.imf.org/en)
- [Wikipedia — List of countries by foreign exchange reserves](https://en.wikipedia.org/wiki/List_of_countries_by_foreign_exchange_reserves)
- [World Bank — Total reserves (includes gold)](https://data.worldbank.org/indicator/FI.RES.TOTL.CD)
