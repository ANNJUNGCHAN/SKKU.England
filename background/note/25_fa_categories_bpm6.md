# 25회차 — 금융계정 5분류 BPM6/BD5 한국어 정의 (FA web-search 2차 보강 라운드)

본 노트는 `db/CHECKLIST.md` Phase 3.2 §4 web-search 보강 작업의 **2차 라운드 — 금융계정 FA 5분류**(직접투자·증권투자·금융파생상품·기타투자·준비자산) 보강 산출물이다. `Table_J`(금융계정 NSA, 15)·`Table_D1_3`(IIP+FA+투자소득, 5)·`D4_6`(4)·`D7_9`(5)·`Table_K`(IIP, 12) 합계 41 unmapped CDID에 적용. 강의 슬라이드 6의 1줄 정의를 BPM6 §6~§9·OECD BD5(2025-03 발간 BD4 후속판)·IMF CDIS·CPIS·BoE/HMT 자료로 보강.

1차 자료 우선 — IMF BPM6 / OECD BD5 / Bank of England / HM Treasury / ONS / 한국은행.

---

## §1 직접투자 (Direct Investment, BPM6 §6.8~§6.45)

### 1) 정의 · 의결권 10% 임계
- **한국어 명칭**: 직접투자 (한국은행 BPM6 표기)
- **한국어 정의**: 한 경제권 거주자가 다른 경제권 거주 기업의 경영에 대해 **지배(control) 또는 유의미한 영향력(significant degree of influence)** 을 행사하는 것과 결부된 국경 간 투자 범주.
- **영문 인용 (BPM6 §6.8)**: "Direct investment is a category of cross-border investment associated with a resident in one economy having control or a significant degree of influence on the management of an enterprise that is resident in another economy."
- **10% 임계 (BPM6 §6.12~§6.13)**: "Ownership of 10 percent or more of the voting power … is evidence of a direct investment relationship." — 50% 초과는 지배(control), 10~50%는 영향력(influence). §6.13: "These definitions should be used in all cases … for international consistency and to avoid subjective judgments."

### 2) Fellow enterprises · Reverse investment
- **Fellow enterprises (BPM6 §6.17)**: 동일한 직접투자자(direct investor)를 공유하지만 서로는 10% 미만의 지분만 보유한 자매 기업 간 거래. **재투자수익(Reinvestment of earnings)은 fellow enterprises 사이에는 적용되지 않음** — 모회사–자회사 관계에만 적용.
- **Reverse investment**: 직접투자 기업이 자신의 직접투자자에 대해 지분 또는 채무를 보유하는 경우. BPM6는 BPM5의 directional principle을 폐기하고 BoP/IIP 본표는 자산·부채 **gross(총액)** 기준으로 표시 (§6.42).

### 3) Directional principle vs Asset/liability principle (BPM6 §6.42~§6.45)
- **Asset/liability principle (BPM6 표준)**: BoP·IIP의 기본 표시 원칙. 모든 자산은 자산 측, 부채는 부채 측에 총액으로 계상.
- **Directional principle (보조 표시)**: 모회사→자회사(outward)와 자회사→모회사(inward, reverse)를 차감해 순방향 흐름만 남기는 방식. **OECD BD5가 FDI 통계의 보충 표시(memo)** 로 권고.

### 4) SPE 처리 · OECD BD5 (BD4 후속, 2025-03 발간)
- **SPE 정의 (BD4/BD5)**: 비거주자 모회사가 100% 또는 사실상 지배하며 자산·부채 90% 이상이 해외인 법인.
- **BD4 권고**: SPE 포함 / SPE 제외 두 시리즈 병행 보고.
- **BD5(2025-03)**: BD4 후속판으로 SPE 가이드 강화 + pass-through capital 추적 + UCP(Ultimate Controlling Parent) 명료화.

### 5) 하위 분해 (BPM6 §6.25~§6.30)
- **Equity capital (지분자본)** — 보통주·우선주·자본 출자.
- **Reinvestment of earnings (재투자수익)** — 분배되지 않은 영업이익 중 직접투자자 지분.
- **Debt instruments (부채성 상품)** — 기업 간 대출, 무역신용, 부채증권 (단, 금융 중개기관 간 일부 차입은 제외).

### 6) 영국 ONS 적용
- **자료원**: Annual Foreign Direct Investment Survey (AFDI) — Inward(AIFDI) + Outward(AOFDI) + 분기 FDI 조사 + BoE 은행권 자료.
- **BD4 준수**: ONS는 BD4 권고를 채택, FDI 표시는 BPM6 자산·부채 원칙으로 본표 작성 후 directional 보조표 병기. SPE 포함·제외 두 시리즈 모두 발표(`background/note/16_oecd_bd4.md` UK SPE 비중 7.1%(2021)).

---

## §2 증권투자 (Portfolio Investment, BPM6 §6.54~§6.79)

### 1) 정의
- **한국어 명칭**: 증권투자 (한국은행 BPM6 표기)
- **한국어 정의**: 직접투자 또는 준비자산에 포함되지 않는 **지분증권 또는 부채증권**과 관련된 국경 간 거래·포지션.
- **영문 인용 (BPM6 §6.54)**: "Portfolio investment is defined as cross-border transactions and positions involving debt or equity securities, other than those included in direct investment or reserve assets."
- **핵심 특성**: 증권의 **양도가능성(negotiability)** — 인도·배서로 소유권이 쉽게 이전되며 조직된 거래소 또는 OTC 시장에서 거래.

### 2) 분해
- **상품별**: 지분증권·투자펀드 지분(Equity and investment fund shares) ↔ 부채증권(Debt securities)
- **만기별 (BPM6 §5.103, §6.65)**: Long-term ≥ 1년 (원만기) ↔ Short-term < 1년
- **발행자 부문별 (institutional sector)**: 중앙은행 / 예금취급기관 / 일반정부 / 기타 금융기관 / 비금융법인·가계
- **10% 미만 지분**: 의결권 10% 미만 지분 + 투자펀드 지분 모두 PI에 분류

### 3) 영국 ONS 적용
- **자료원**: Bank of England 통계조사 + ONS 증권투자 조사. 영국은 만성적인 PI 부채 순증가국(외국인의 영국 채권·주식 보유 증가).

---

## §3 금융파생상품 및 종업원 스톡옵션 (Financial Derivatives and ESOs, BPM6 §6.58~§6.62, §7.78~§7.92)

### 1) 정의
- **한국어 명칭**: 금융파생상품 (한국은행 BPM6 표기)
- **한국어 정의**: 특정 금융위험을 분리·이전하기 위해 거래되는 금융계약. 원금 자체가 거래되지 않고 위험만 거래된다는 점에서 다른 기능 범주와 구별됨.
- **영문 인용 (BPM6 §6.58)**: "A financial derivative contract is a financial instrument that is linked to another specific financial instrument or indicator or commodity, through which specific financial risks … can be traded in their own right in financial markets."

### 2) 분류
- **Forward-type contracts**: 양 당사자가 향후 합의된 조건으로 결제. **Futures, Forwards, Swaps**(통화·금리·crosscurrency) 모두 forward 계열.
- **Option-type contracts**: 매수자는 프리미엄을 지급하고 권리를 보유, 매도자는 조건 충족 시 결제 의무.
- **Employee Stock Options (ESOs)** (BPM6 §6.62): 종업원 보상 일부로 부여되는 옵션 — 별도로 식별.

### 3) 순액(net) 표기 사유
- **유량(자산·부채 분리 부재)**: 파생상품 거래는 정산금(settlement payments)이 자산↔부채로 빈번히 전환되므로 자산·부채 분리가 실무상 어려움. BPM6 §8.34는 ISDA Master Agreement payment netting 등 **gross 보고가 비현실적인 경우 net 보고를 허용**.
- **저량(IIP)**: 시장가치 기준으로 **자산(positive market value)·부채(negative market value)를 양면(gross) 게재** — 파생상품 가치는 시장 변동에 따라 부호가 바뀜.

### 4) 영국 ONS 적용
- **자료원**: BoE 외환·금리 파생상품 조사, ICMA 자료 보완. ONS Table_J 부표는 **net ZPNN 단일 컬럼**(`background/note/19_assets_liabilities_mapping.md` 양면 매핑표 참조).

---

## §4 기타투자 (Other Investment, BPM6 §6.63~§6.79, §7.93~§7.123)

### 1) 정의 · 잔여 분류 정당화
- **한국어 명칭**: 기타투자 (한국은행 BPM6 표기)
- **한국어 정의**: 직접투자·증권투자·금융파생상품·준비자산 어디에도 속하지 않는 모든 금융 거래·포지션. **잔여(residual) 범주**.
- **영문 인용 (BPM6 §6.63)**: "Other investment is a residual category that includes positions and transactions other than those included in direct investment, portfolio investment, financial derivatives and employee stock options, and reserve assets."

### 2) 6 + 1 sub-functional categories (BPM6 §6.64)
1. **Other equity** (직접투자·증권투자·준비자산 외 지분)
2. **Currency and deposits** (현금·예금)
3. **Loans** (대출)
4. **Insurance, pension, and standardized guarantee schemes** (보험·연금·표준화 보증)
5. **Trade credit and advances** (무역신용·선급금)
6. **Other accounts receivable/payable** (기타 미수·미지급)
7. **SDR allocations** (부채 측에만; 자산 측 SDR 보유는 준비자산)

### 3) SDR 배분 처리 (2009·2021)
- **BPM6 변경점**: BPM5에서는 SDR 배분이 부채로 인식되지 않았으나, **BPM6는 SDR 배분을 통화당국의 장기 부채로 인식** (Other investment 부채 측, "SDR allocations" 항목).
- **2009-08·09 일반 + 특별 배분** ($250bn 상당), **2021-08 일반 배분** ($650bn 상당) 모두 자산 측은 준비자산(SDRs)에, 부채 측은 기타투자(SDR allocations)에 동시 계상.

### 4) 영국 ONS 적용
- **자료원**: BIS Locational Banking Statistics(은행 부문 국가 간 대출·예금) + Bank of England 통계 + 무역신용 조사.

---

## §5 준비자산 (Reserve Assets, BPM6 §6.64~§6.81, §7.124~§7.143)

### 1) 정의 · 가용성 기준
- **한국어 명칭**: 준비자산 (한국은행 BPM6 표기)
- **한국어 정의**: 통화당국이 BoP 자금조달, 외환시장 개입, 환율 영향 등을 위해 **언제든 사용 가능하고 통제하는 외화표시 대외자산**.
- **영문 인용 (BPM6 §6.64)**: "Reserve assets are those external assets that are readily available to and controlled by monetary authorities for meeting balance of payments financing needs, for intervention in exchange markets to affect the currency exchange rate, and for other related purposes."
- **"Readily available" 기준**: 즉시 처분 가능, 외화표시(태환 가능 통화), 비거주자 청구권. **담보·질권 설정·동결된 자산은 제외**, 거주자 청구권 제외, 비태환 통화 자산 제외.

### 2) 4구성
1. **Monetary gold (통화금)** (BPM6 §6.78~§6.79) — 통화당국이 보유한 금. **Gold bullion(금괴)** + **unallocated gold accounts**(할당되지 않은 금 계정).
2. **SDRs** (Special Drawing Rights) — IMF 회원국에 배분된 국제 준비자산. *자산 측은 보유분, 부채 측 배분은 기타투자*.
3. **Reserve position in the IMF** — 회원국의 IMF 일반자원계정(GRA) 내 잔여 청구권.
4. **Other reserve assets** — Currency and deposits + Securities + Financial derivatives(net) + Other claims.

### 3) 영국 ONS 적용
- **법적 보유 구조**: UK reserves는 **HM Treasury 명의의 Exchange Equalisation Account (EEA)** 에 보유. **Bank of England는 Treasury의 대리인(agent)** 으로 일상 운용 담당.
- **EEA 구성**: 외화 준비자산 + 금 + SDR + IMF 준비포지션 + 기타.
- **2025-10 정량**: Net reserves = **$112,358m** (£85,518m), 9월말 $111,022m 대비 +$1,335m 증가.
- **2024~2025 EEA 회계연도 보고서**: HMT가 의회 제출 (gov.uk 공개).

### 4) BoP/IIP 부호 비대칭 (슬라이드 26 핵심 인용)
- **BoP(유량)**: 준비자산은 **자산 측만** 기록 — 부채 측 부재. BoP에서 준비자산 증가는 자금 유출(부호 음 → 자산 NAFA 증가).
- **IIP(저량)**: 준비자산은 **자산 측 잔액만**. 부채 측 부재.
- **슬라이드 26 비대칭 해석**: BoP에서 준비자산 변동(flow)이 음(-)으로 보이더라도 이는 자산 증가이며, IIP 잔액(stock)은 양(+) 자산으로 표시 — 부호 차이는 회계 표시 관점 차이.

---

## 영국 ONS 적용 함의 종합 표 (자료원 분담 · 자산/부채 측 회계)

| 분류 | BoP 유량 | IIP 저량 | 영국 자료원 | 회계 측면 |
|---|---|---|---|---|
| 직접투자 | 자산(NAFA) + 부채(NIL) 양면 | 자산 + 부채 양면 | ONS AIFDI/AOFDI 연차 + 분기 + BoE | BD5 준수 · SPE 포함/제외 두 시리즈 · directional 보조 |
| 증권투자 | 자산 + 부채 양면 | 자산 + 부채 양면 | BoE 통계 + ONS 증권투자조사 | 만기·발행자부문별 · 영국은 만성 PI 부채 순증 |
| 금융파생상품 | **순액(net)** 단일 | 자산 + 부채 양면 (시장가치) | BoE 외환·금리 파생조사 + ICMA | 정산금 회전 → BoP 유량은 net 표기 |
| 기타투자 | 자산 + 부채 양면 | 자산 + 부채 양면 | BIS Locational Banking + BoE | SDR 배분(부채), 무역신용·예금·대출 |
| 준비자산 | **자산 측만** | **자산 측만** | EEA(HMT 보유, BoE 운용대행) | 부채 측 부재 정상 — 슬라이드 26 부호 비대칭 |

---

## Phase 3.2 §4 활용 가이드 — 41 unmapped CDID 시트별 보강 방법

### 시트별 보강 원칙

- **Table_J (Financial Account NSA, 15건)** — BoP **유량(transactions)**.
  - 직접투자 CDID: §1 정의 + Equity/Reinvested earnings/Debt instruments 분해. **자산·부채 양면**.
  - 증권투자 CDID: §2 정의 + 만기(LT/ST) + 발행자부문 + 자산·부채 양면.
  - 금융파생 CDID: §3 + **net 단일 표기** (자산·부채 분리 없음 명시).
  - 기타투자 CDID: §4 + 6+1 sub-categories 중 해당 항목.
  - 준비자산 CDID: §5 + **자산 측만**.

- **Table_D1_3 / D4_6 / D7_9 (IIP + FA + 투자소득, 14건)** — IIP **저량** + FA 유량 + 투자소득 cross-link.
  - 직접투자 IIP: §1 정의 + IIP는 시장가치 기준 잔액. directional 보조표 병기.
  - 증권투자 IIP: §2 정의 + 발행자부문·만기 분해. 투자소득 cross-link은 BPM6 §11(1차소득) 참조.
  - 금융파생 IIP: §3 + **양면(자산·부채) 시장가치** 게재.
  - 기타투자 IIP: §4 + SDR 배분 부채 측 표기 명기.

- **Table_K (IIP, 12건)** — 순수 저량 잔액.
  - 5분류별 §1~§5 정의 적용.
  - 준비자산 항목은 §5의 4구성 분해 명기.
  - **자산 측만 게재되는 준비자산**은 부호 비대칭 주석 추가.

### 정의 텍스트 표준 형식 (8필드)

각 unmapped CDID 행에 다음 8 필드를 채워 정합성 유지:
1. 영문 라벨(원문)
2. 한국어 명칭(한국은행 표기)
3. BPM6 §x.xx 정의 인용(영문 1줄)
4. 한국어 정의(2~3줄)
5. 분해(LT/ST · 부문 · sub-category 등 해당 시)
6. BoP/IIP 자산·부채 측 표기 규칙
7. 영국 ONS 자료원
8. 슬라이드 6 1줄 정의 대비 보강 포인트 (10% 임계 / SPE / equity vs debt / option vs forward / SDR 배분 등)

---

## 출처 카탈로그 (1차 출처 우선)

### IMF (BPM6)
- IMF BPM6 — full manual PDF: https://www.imf.org/external/pubs/ft/bop/2007/pdf/bpm6.pdf
- IMF BPM6 — Chapter 6 Functional Categories: https://www.imf.org/external/pubs/ft/bop/2007/pdf/chap6.pdf
- IMF BPM6 — Chapter 10 Financial Account: https://www.imf.org/external/pubs/ft/bop/2014/pdf/BPM6_10F.pdf
- IMF BPM6 — Appendix 4 FDI: https://www.imf.org/external/pubs/ft/bop/2014/pdf/BPM6_A4F.pdf
- IMF BPM6 — Compilation Guide 2014: https://www.imf.org/external/pubs/ft/bop/2014/pdf/guide.pdf
- IMF BPM6 — Sixth Edition landing: https://www.imf.org/external/pubs/ft/bop/2007/bopman6.htm
- IMF BPM6 — Defining the boundaries of direct investment (DITT): https://www.imf.org/-/media/files/data/statistics/bpm6/ditt/d10-defining-the-boundaries-of-direct-investment.pdf
- IMF BPM6 — F.4 Financial Derivatives by Type (FITT): https://www.imf.org/-/media/files/data/statistics/bpm6/approved-guidance-notes/f4-financial-derivatives-by-type.pdf
- IMF BPM6 — Standardized Definition of Net International Reserves: https://www.imf.org/-/media/files/data/statistics/bpm6/approved-guidance-notes/b2-standardized-definition-of-net-international-reserves.pdf
- IMF — Coordinated Direct Investment Survey Guide 2015: https://www.imf.org/external/np/sta/pdf/cdisguide.pdf
- IMF — CDIS dataset: https://data.imf.org/?sk=40313609-F037-48C1-84B1-E1F1CE54D6D5
- IMF — CPIS Guide Third Edition: https://data.imf.org/-/media/iData/External-Storage/Documents/390C683A8FA24B58B7EBBBB33B82AD3B/en/CPIS-Guide-Third-Edition.pdf
- IMF — What is the CPIS? (DATA Help): http://datahelp.imf.org/knowledgebase/articles/505725-what-is-the-coordinated-portfolio-investment-surve

### OECD
- OECD Benchmark Definition of Foreign Direct Investment, Fifth Edition (2025) — landing: https://www.oecd.org/en/publications/oecd-benchmark-definition-of-foreign-direct-investment-fifth-edition_7f05c0a3-en.html
- OECD BD5 — full PDF: https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/03/oecd-benchmark-definition-of-foreign-direct-investment-fifth-edition_38a25baf/7f05c0a3-en.pdf
- OECD — International Standards for FDI Statistics: https://www.oecd.org/en/topics/sub-issues/measuring-foreign-direct-investment/international-standards-for-fdi-statistics.html
- BOPCOM 24-17 — BD4 Update note: https://www.imf.org/external/Pubs/FT/BOP/2024/pdf/44/BOPCOM%2024-17-Update%20of%20the%20OECD%20Benchmark%20Definition%20of%20FDI-fourth%20edition-BD4.pdf

### Bank of England · HM Treasury
- Bank of England — Foreign currency reserves: https://www.bankofengland.co.uk/markets/foreign-currency-reserves
- BoE — Further details about UK International reserves data: https://www.bankofengland.co.uk/statistics/details/further-details-about-uk-international-reserves-data
- BoE — Foreign Currency Reserves 2025 (Market Notice 6 Oct 2025): https://www.bankofengland.co.uk/markets/market-notices/2025/october/foreign-currency-reserves-6-october-2025
- HMT — UK official holdings of international reserves October 2025 PDF: https://assets.publishing.service.gov.uk/media/690a272714b040dfe82922be/Statistical_Release_UK_official_holdings_of_international_reserves_-_October_2025.pdf
- GOV.UK — Exchange Equalisation Account report and accounts 2024 to 2025: https://www.gov.uk/government/publications/exchange-equalisation-account-report-and-accounts-2024-to-2025

### ONS
- ONS — UK Balance of Payments, The Pink Book 2025: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025
- ONS — Balance of payments landing: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments
- ONS — Summary of the balance of payments methodology: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpayments
- ONS — Balance of payments UK October to December 2025 bulletin: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/octobertodecember2025
- ONS — An introduction to the UK BoP BPM6: https://www.ons.gov.uk/file?uri=%2Feconomy%2Fnationalaccounts%2Fbalanceofpayments%2Fmethodologies%2Fbalanceofpayments%2Fanintroductiontotheukbopbpm6tcm77279821.pdf
- ONS — Annual FDI Survey landing: https://www.ons.gov.uk/surveys/informationforbusinesses/businesssurveys/foreigndirectinvestmentfdi

### 추가 참고
- Eurostat — BPM6 Statistics Explained: https://ec.europa.eu/eurostat/statistics-explained/index.php/Balance_of_payments_and_international_investment_position_manual_(BPM6)
- BIS — IFC Bulletin 35 Treatment of financial derivatives in BPM6: https://www.bis.org/ifc/publ/ifcb35d.pdf
- OeNB — Reconciling asset/liability and directional principle: https://www.oenb.at/en/Statistics/Standardized-Tables/external-sector/foreign-direct-investment/concepts-and-components/reconciling-asset-liability--and-directional-principle.html

---

## 확인 못한 부분

- **BPM6 본문 §6.78~§6.79 monetary gold 원문 인용**: IMF PDF 직접 fetch가 403 차단. 단락 번호는 BPM6 manual landing + IMF guidance note 복수 인용으로 신뢰 가능.
- **ONS Pink Book 2025 SPE 정량 분석**: bulletin 페이지 fetch 일부 차단 → backup mirror 별도 다운로드 권고.
- **OECD BD5 SPE 식별 결정 트리 단계 수**: BD5 본문 PDF 직접 펼쳐 검증 권고. 본 노트는 핵심 기준(비거주자 모회사 100%·자산부채 90% 해외)만 확정.
