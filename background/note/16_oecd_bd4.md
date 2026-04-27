# OECD BD4 SPE·FATS 보강 (web-search 16회차)

본 문서는 `db/CHECKLIST.md` §0.2 신규 中 1번 항목(OECD Benchmark Definition of FDI 4판의 SPE·FATS 보강)의 산출물이다. 10회차에서 OECD 공식 PDF 직접 접근이 차단되어 미확보된 BD4 고유 기준을 ONS·OECD·ECB·Eurostat·IMF 출처로 보강한다.

## 요약

1. **BD4 ↔ BPM6**: 10% 의결권 임계는 동일하지만 BD4는 **FDIR(Framework for Direct Investment Relationships)**, **UCP(Ultimate Controlling Parent)**, **UIC(Ultimate Investing Country)** 기준을 추가해 fellow enterprise까지 식별하고 round-tripping을 드러낸다.
2. **SPE**: 비거주자 모기업이 통제하고 자산·부채 90% 이상이 해외인 형식뿐인 법인. BD4는 SPE를 통한 FDI를 **별도 분리 표기**하도록 권고하며, 거시지표가 부풀려지지 않도록 "passing-through capital"로 인식한다.
3. **FATS**: BoP/FDI(분기 거래·잔액)와 달리 **연간 stock + 활동지표**(매출·고용·부가가치·R&D)를 측정. Inward FATS(자국 내 외국계 기업), Outward FATS(자국 기업의 해외 자회사)로 구분.
4. **ONS 적용**: ONS FDI는 **BD4를 완전 준수**(2011~12년부터 적용), **SPE 포함/제외 두 버전**을 발표하며, **IFATS와 OFATS도 별도 산출**한다(OFATS는 2020년부터 Outward FDI 조사에 통합).
5. **2025년 BD5 발표**: OECD는 2025년 3월 5판(BD5)을 공개했으며 회원국에 2029~2030년까지 이행을 요청 — 영국은 향후 BD5 전환 예정.

## 항목별 발췌 표

| 항목 | 정의 (영문 발췌 + 한국어 풀이) | 출처 URL | 07_glossary 매핑 |
|---|---|---|---|
| **BD4 vs BPM6** | "FDI statistics compiled by the ONS are fully compatible... adhering to the fourth edition of the OECD Benchmark Definition of FDI (BD4)... reflecting international best-practice set out in BPM6 and BD4." → BD4는 BPM6과 호환되면서 FDI 전용 추가 가이드 제공. | [ONS FDI methods comparison](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/foreigndirectinvestmentamethodscomparisonofonsandexternallyproducedestimates/2020-04-14) | `BD4`, `BPM6` 신규 |
| **FDIR** | "Framework of Direct Investment Relationships (FDIR)... aims to identify all enterprises over which the investor has significant influence following the 10% voting power criterion for FDI." → 10% 임계를 모회사·자회사·동료회사(fellow enterprises)까지 확장 적용하는 식별 체계. | [OECD International Standards for FDI](https://www.oecd.org/en/topics/sub-issues/measuring-foreign-direct-investment/international-standards-for-fdi-statistics.html) | `FDIR` 신규 |
| **UCP / UIC** | "UCP is defined as the controlling entity above which there is no other controlling entity according to FDIR... BD4 recommended that countries compile inward investment positions according to the Ultimate Investing Country (UIC)." → 최상위 모회사(UCP)와 그 거주국(UIC) 기준으로 inward FDI를 재집계. | [OECD International Standards for FDI](https://www.oecd.org/en/topics/sub-issues/measuring-foreign-direct-investment/international-standards-for-fdi-statistics.html); [ONS UK FDI by ultimate controlling economy](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/ukforeigndirectinvestmenttrendsandanalysis/july2022) | `UCP`, `UIC` 신규 |
| **Round-tripping** | "FDI data based on the Ultimately Investing Economy (UIE)... can also reveal round-tripping, where resident investors channels funds abroad only for these to return as foreign direct investment." → 자국 자금이 해외를 거쳐 FDI로 위장 회귀하는 현상을 UIC 분석으로 식별. | [OECD International Standards](https://www.oecd.org/en/topics/sub-issues/measuring-foreign-direct-investment/international-standards-for-fdi-statistics.html) | `Round-tripping` 신규 |
| **SPE 정의** | "A special purpose entity (SPE) is a legal unit within a multinational enterprise established in a different economy to that of its parent company yet has a very low presence in that host economy. Examples... are financing subsidiaries, conduits, holding companies, shell companies, shelf companies and brass-plate companies." | [ONS Classifying SPEs in UK FDI (2019)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/classifyingspecialpurposeentitiesinukforeigndirectinvestmentstatisticsexperimentalanalysis/2019-06-03) | `SPE` 신규 |
| **SPE 식별 6단계 (ONS)** | "An entity must satisfy all six stages to be identified as an SPE... must be directly or indirectly controlled by at least one non-resident company... majority control must be with non-UK enterprises and transact almost exclusively with non-residents." | [ONS Classifying SPEs (2019)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/classifyingspecialpurposeentitiesinukforeigndirectinvestmentstatisticsexperimentalanalysis/2019-06-03) | `SPE 식별기준` |
| **SPE 권고: 분리 표기** | "ESA 2010, OECD BD4, and IMF BPM6 all include definitions on SPEs and recommend national statistical institutes separately identify FDI transactions and positions undertaken by resident SPEs in their statistics." → 통계 왜곡 방지를 위한 분리 공시 권고. | [ONS Classifying SPEs (2019)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/classifyingspecialpurposeentitiesinukforeigndirectinvestmentstatisticsexperimentalanalysis/2019-06-03) | `SPE 분리표기` |
| **Pass-through capital** | "Transit FDI through SPEs results in a pass-through of capital, which tends to inflate gross flows and generate a very high degree of co-movement between asset and liability flows." → SPE 통과 자금은 양 방향 잔액을 동시에 부풀림. | [ECB Economic Bulletin – SPEs (2019)](https://www.ecb.europa.eu/press/economic-bulletin/focus/2019/html/ecb.ebbox201905_03~9ea9063965.en.html) | `Pass-through capital` |
| **SPE 비중 (룩셈/네덜란드)** | "SPEs were responsible for almost 60% of FDI assets and liabilities in Luxembourg and almost 30% in the Netherlands." → 영국(7.1%)보다 훨씬 큰 SPE 비중. | [ECB Economic Bulletin (2019)](https://www.ecb.europa.eu/press/economic-bulletin/focus/2019/html/ecb.ebbox201905_03~9ea9063965.en.html) | 보충 사례 |
| **SPE 비중 (UK)** | "UK-resident SPEs accounted for £156.4 billion or 7.1% of total FDI assets in 2021." → 영국 FDI 자산의 7% 수준. | [ONS UK-resident SPEs (Jan 2023)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/ukforeigndirectinvestmenttrendsandanalysis/january2023) | `SPE_UK 비중` |
| **FATS 정의** | "Foreign Affiliates Statistics (FATS) describe the activities of foreign affiliates: enterprises resident in a country... controlled or owned by (multinational) enterprises which are resident outside that country." | [Eurostat FATS Glossary](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Foreign_affiliates_statistics_(FATS)) | `FATS` 신규 |
| **Inward FATS** | "Inward FATS describe the overall activity of foreign affiliates resident in the compiling economy... how many jobs, how much turnover, etc. are generated by foreign investors in a given host economy." | [Eurostat FATS Glossary](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Foreign_affiliates_statistics_(FATS)) | `IFATS` |
| **Outward FATS** | "Outward FATS describe the activity of foreign affiliates abroad controlled by the compiling country... how many employees work for affiliates abroad." | [Eurostat FATS Glossary](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Foreign_affiliates_statistics_(FATS)) | `OFATS` |
| **BoP ↔ FATS 차이** | BoP/FDI: 분기 단위 **거래(flow)·잔액(stock)** 금융지표 / FATS: 연간 단위 **활동지표(매출·고용·부가가치·R&D)** — 다국적기업의 실물 영향 측정. | [OECD AMNE dataset](https://www.oecd.org/en/data/datasets/activity-of-multinational-enterprises.html) | `FATS vs BoP` |
| **ONS IFATS** | "Inward foreign affiliates (IFATS) statistics include information on the characteristics of UK businesses that are foreign owned, covering the number of enterprises, turnover, employment and value added." | [ONS Inward FATS UK 2018-2022](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/adhocs/1805inwardforeignaffiliatesstatisticsuk2018to2021) | `IFATS_UK` |
| **ONS OFATS** | "From the 2020 annual reference period onwards, the collection of OFATS data has been embedded into the annual Outward Foreign Direct Investment (FDI) Survey." | [ONS UK OFATS 2019](https://www.ons.gov.uk/businessindustryandtrade/internationaltrade/bulletins/ukoutwardforeignaffiliatestatisticsofats/2019) | `OFATS_UK` |
| **ONS FDI = BD4 준수** | "2011 to 2012 — work began to ensure that the surveys became compliant with... Benchmark definition of Foreign Direct Investment (4th edition)." + "producing estimates both including and excluding special purpose entities (SPEs)." | [ONS FDI QMI](https://www.ons.gov.uk/businessindustryandtrade/business/businessinnovation/methodologies/foreigndirectinvestmentfdiqmi) | `ONS_BD4 적용` |

## 영국 ONS 적용 시 함의

- **BD4 완전 준수**: ONS는 2011~12년 FDI 서베이 개편 이후 BD4 기준에 맞춰 발표하므로, `db/source/balanceofpayments2025q4.xlsx`의 직접투자(Direct Investment) 항목은 BPM6+BD4 이중 준수 데이터로 해석하면 된다.
- **SPE 이중 발표**: ONS는 SPE **포함·제외 두 시리즈**를 모두 산출. 보고서에서 영국 FDI 흐름의 변동성을 분석할 때는 어느 버전인지 명시해야 하며, 2021년 기준 UK SPE 비중은 FDI 자산의 7.1%(£156.4bn)로 룩셈부르크(60%)·네덜란드(30%)와 비교하면 상대적으로 작지만 **여전히 의미 있는 규모**.
- **FATS는 별도 산출물**: ONS의 IFATS·OFATS는 BoP 분기보고서에는 포함되지 않고 **연 1회 별도 발표**(OFATS는 2020년 reference period부터 Outward FDI 서베이에 통합). BoP/FDI 분석을 보강하려면 별도 데이터셋을 수집해야 한다.
- **UCP/UIC 분석**: ONS는 "FDI by ultimate controlling economy" 시리즈로 round-tripping과 실질 모회사 국가를 식별 — 영국의 inward FDI에서 룩셈부르크·네덜란드 경유분이 미국·일본 등으로 재배분되는 효과를 확인할 수 있음.
- **BD5 전환 일정 주시**: 2025년 3월 OECD가 BD5를 발표했고 2029~2030년 이행 권고. 향후 ONS 발표 변경 가능성 모니터링 필요.

## 빠진(확인 못한) 부분

- **ONS의 BD5(5판) 이행 일정**: 영국의 구체적 전환 로드맵 미확인 — OECD 권고는 2029~2030년이지만 ONS 공식 일정 부재.
- **BD4 4판 PDF 본문 직접 인용**: OECD iLibrary HTML(BD4)도 403/유료 벽으로 직접 fetch 실패. 본 회차도 BD5 본문(2025) 및 BD4를 인용한 IMF/ONS/Eurostat 2차 출처에 의존.
- **UK 2022·2023 SPE 비중**: ONS가 2023년 1월에 2021년 데이터까지 발표한 것은 확인했으나, 2022~2023년 UK SPE 비중 최신치 미확인.
- **OFATS의 BoP 일관성**: OFATS가 2020년부터 Outward FDI 서베이에 통합된 후 BoP 직접투자 잔액과의 정합성·차이 설명 미확인.

## 출처 목록

- [OECD International Standards for FDI Statistics](https://www.oecd.org/en/topics/sub-issues/measuring-foreign-direct-investment/international-standards-for-fdi-statistics.html)
- [OECD Benchmark Definition of FDI – Fifth Edition (2025)](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/03/oecd-benchmark-definition-of-foreign-direct-investment-fifth-edition_38a25baf/7f05c0a3-en.pdf)
- [OECD Measuring FDI](https://www.oecd.org/en/topics/foreign-direct-investment-fdi.html)
- [OECD Activity of Multinational Enterprises (AMNE)](https://www.oecd.org/en/data/datasets/activity-of-multinational-enterprises.html)
- [IMF BOPCOM 24-17 – Update of OECD BD4](https://www.imf.org/external/Pubs/FT/BOP/2024/pdf/44/BOPCOM%2024-17-Update%20of%20the%20OECD%20Benchmark%20Definition%20of%20FDI-fourth%20edition-BD4.pdf)
- [IMF – Effects of Including SPEs on BoP and FDI Statistics (2013)](https://www.imf.org/external/pubs/ft/bop/2013/13-15.pdf)
- [IMF – Special Purpose Entities: Guidelines for a Data Template (2020)](https://www.imf.org/external/pubs/ft/bop/2020/pdf/20-26.pdf)
- [ECB Economic Bulletin – Euro area FDI: role of SPEs (2019)](https://www.ecb.europa.eu/press/economic-bulletin/focus/2019/html/ecb.ebbox201905_03~9ea9063965.en.html)
- [Eurostat – FATS Glossary](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Foreign_affiliates_statistics_(FATS))
- [Eurostat – Implementing new international FDI standards](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Implementing_the_new_international_standards_for_foreign_direct_investment_(FDI)_statistics)
- [ONS – FDI QMI (methodology)](https://www.ons.gov.uk/businessindustryandtrade/business/businessinnovation/methodologies/foreigndirectinvestmentfdiqmi)
- [ONS – FDI methods comparison (2020)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/foreigndirectinvestmentamethodscomparisonofonsandexternallyproducedestimates/2020-04-14)
- [ONS – Classifying UK SPEs in FDI (2019)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/classifyingspecialpurposeentitiesinukforeigndirectinvestmentstatisticsexperimentalanalysis/2019-06-03)
- [ONS – UK-resident SPEs January 2023](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/ukforeigndirectinvestmenttrendsandanalysis/january2023)
- [ONS – UK FDI by ultimate controlling economy (July 2022)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/ukforeigndirectinvestmenttrendsandanalysis/july2022)
- [ONS – Inward FATS UK 2018-2022](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/adhocs/1805inwardforeignaffiliatesstatisticsuk2018to2021)
- [ONS – UK Outward FATS (OFATS) 2019](https://www.ons.gov.uk/businessindustryandtrade/internationaltrade/bulletins/ukoutwardforeignaffiliatestatisticsofats/2019)
- [House of Commons Library – FDI Statistics CBP-8534](https://commonslibrary.parliament.uk/research-briefings/cbp-8534/)
