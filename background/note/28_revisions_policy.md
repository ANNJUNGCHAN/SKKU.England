# 28회차 — ONS BoP 통계 개정(Revisions) 정책 · Table_R1·R2·R3 보강 정의

본 노트는 영국 ONS *Balance of Payments Statistical Bulletin Tables* 2025 Q4의 개정 시트 3종(Table_R1·R2·R3, 합계 52 unmapped CDID)에 한국어 정의를 부여하기 위한 1차 출처 정리. 강의 자료(`background/BoP.pptx`)에는 통계 개정 개념이 부재하므로 ONS·UNECE·IMF 공식 문서 기반. 부호 규약은 `background/note/03`, 시트 인벤토리는 `background/note/12`, NEO 변동성은 `background/note/20`, 자료원 카탈로그는 `background/note/22`, 지리분해는 `background/note/23`을 cross-reference.

---

## §1 ONS 개정 정책 일반론

### §1.1 ONS *National Accounts Revisions Policy* 핵심 원칙

ONS는 *National Accounts Revisions Policy*(현행본 **2025-06 갱신**, 직전 주요본 2017-12; URL slug에 "December2017" 유지)를 통해 GDP·BoP 등 국민계정 통계의 개정 일정과 절차를 공개. 핵심 원칙 세 가지:

1. **사전 공지(advance notice) 원칙** — 정기 개정 일정 외의 계획된 개정(planned revision)은 ONS 웹사이트 articles 형태로 사전 공지.
2. **개정 사유 3분류** — (i) 자료 갱신(*data updates*: 응답자 정정·후행 도착 자료), (ii) 방법론 변경(*methodology changes*: 개념·정의·분류 변경), (iii) 오류 보정(*corrections*: identification of an error). 오류 보정은 정기 개정과 명시적으로 구분 표기.
3. **revision triangle 공개** — 사용자가 과거 개정 패턴을 직접 분석할 수 있도록 *revision triangle* 데이터셋을 ONS 웹사이트에 공개.

### §1.2 BoP 분기 발표 일정 (t+1 / t+2 / t+annual)

| 단계 | 시점 | 개정 범위 |
|---|---|---|
| **1차(t+1)** *first estimate* | 분기 종료 후 약 12~13주(약 90일) | 최근 분기 잠정치 신규 게시, 직전 분기 일부 갱신 |
| **2차(t+2)** *second release / full accounts* | 1차 발표 후 다시 약 12~13주(약 90일) | 최근 분기 + 그 이전 분기 component 단위 전반 개정 |
| **연간(t+annual)** *Pink Book reconciliation* | 매년 10~11월 (Pink Book 공표) | 모든 자료원·전 시계열 동시 reconcile |

> ONS 명시 표현: *"At the second release of each quarter it is possible to provide a complete set of accounts for the quarter and to take account of revisions to the component items for earlier quarters."* (NA Revisions Policy, 2025-06)

2025 Q4 BoP Statistical Bulletin은 2026-03-31 발표, 차회(2026-06-30)가 동일 분기의 2차 release.

### §1.3 Pink Book 연간 reconciliation 시점

- *UK Balance of Payments, The Pink Book*은 매년 가을(통상 10월 말)에 *Blue Book*과 동시 발간. **2025년판 2025-10-31** 발표.
- Pink Book은 분기 발표보다 포괄적인 연간 자료원(Annual Financial Services Survey, ITIS 연간 reconcile, AIFDI/AOFDI, 그리고 supply-and-use framework 통합)을 흡수.
- ONS BoP QMI 명시: *"In the UK, the National Accounts and balance of payments are fully integrated and coherent and therefore a parallel process is followed for balance of payments"*.

---

## §2 개정 발생 원인 4분류

| 분류 | 정의 | 영국 BoP 대표 사례 | cross-reference |
|---|---|---|---|
| **(1) 다중 자료원 후행 도착** | 자료원별 보고 주기 차이로 후행 자료가 들어올 때마다 시계열 갱신 | HMRC OTS(월) → ITIS·IPS(분기) → AIFDI/AOFDI(연) → BIS Locational Banking(분기 t+4개월) | `background/note/22` |
| **(2) 잠정치 → 확정치 교체** | provisional → final. Pink Book 시점 동시 reconcile | Annual Financial Services Survey 흡수 시 분기 시계열 일괄 개정 | BoP QMI |
| **(3) 방법론 개선** | 개념·정의·분류·추계법 변경. *exceptional / benchmark revision* | BPM5→BPM6, SPE 분리, 교육서비스 추계, FDI stratification, supply-and-use 적용 | ONS *Detailed assessment of changes to BoP annual estimates 1997~2021* |
| **(4) 처리 시스템 오류 보정** | unplanned correction. 별도 명시 표기 | 2025 Q4 발표의 HMRC OTS 광물연료·기름 수출 오류(2024-03 이후), ITIS 처리 시스템 오류(2023~2024), 귀금속 bar 이중계상 보정(2024 Q1 이후) | 2025 Q4 BoP Bulletin |

> ESS QAF 용어로는 (1)·(2)는 *routine revisions*, (3)·(4)는 *exceptional / benchmark revisions*에 해당.

---

## §3 Table_R1·R2·R3 시트 구조

### §3.1 Table_R1 — Revisions summary (balances)

- 경상수지·자본수지·금융수지의 **잔액(balance) 항목 요약 개정표**.
- 8개 chapter(소표) 구조로 BoP 본 표(Table_A 잔액 요약)와 행 단위 대응.
- 단위: **GBP million**.

### §3.2 Table_R2 — Current account revisions

4개 sub-table:

| Sub-table | 내용 |
|---|---|
| Credits | 경상수지 수입(credit) 항목별 개정액 |
| Debits | 경상수지 지급(debit) 항목별 개정액 |
| Balances | 잔액 개정액 |
| % of GDP | GDP 대비 비율 단위 개정 |

- 단위: **GBP million** (단, % of GDP sub-table은 백분율).

### §3.3 Table_R3 — International investment revisions

9개 sub-table 매트릭스(IIP·Financial Account·Investment Income × Asset/Liability/Net):

| 차원 | 항목 |
|---|---|
| 행(블록) | IIP(잔액 stock) / FA(거래 transaction) / Income(소득 flow) |
| 열(부호) | Assets / Liabilities / Net |

- 단위: **GBP billion** (R1·R2와 단위가 다름 — 자릿수 변환 시 1,000배 차이 주의).

### §3.4 단위 차이 요약

| 시트 | 단위 |
|---|---|
| Table_R1 | GBP million |
| Table_R2 (Credits/Debits/Balances) | GBP million |
| Table_R2 (% of GDP) | percentage point of GDP |
| Table_R3 (IIP·FA·Income) | **GBP billion** |

---

## §4 부호 해석

- **개정액(Revisions) = 현재 발표값 − 직전 발표값**.
- **양수(+)** → 현재 발표가 직전 발표보다 **상향**(upward revision).
- **음수(−)** → 현재 발표가 직전 발표보다 **하향**(downward revision).
- 잔액(Balance) 항목은 부호가 두 번 작용하므로(원 잔액의 부호 + 개정 방향), 해석 시 *원 시계열의 부호 규약*(`background/note/03` 참조)과 분리해 읽어야 함.

---

## §5 영국 적용 함의

### §5.1 NEO(Net Errors and Omissions) 동시 변동

`background/note/20`에 따르면 2020 Q1~2025 Q4 |NEO| 평균 5,872 £m, 최대 14,457 £m로 변동성 매우 큼. BoP 항등식 *Current + Capital = Financial + NEO*의 미해소 잔여이며, 자료원별 후행 도착·방법론 개선·오류 보정이 누적 반영되는 시점에 **R1·R2·R3 개정과 NEO가 동시에 흔들리는** 구조적 특징. R 시트 분석 시 NEO 변동을 별도 시계열로 동반 점검 권장.

### §5.2 Revision triangle 공개 여부

- ONS *Balance of payments – revision triangles* 데이터셋 별도 공개(롤링 5년 윈도우).
- 최신 갱신 **2025-09-30**, 다음 갱신 시점 미공지(2026-04 기준).
- 본 저장소가 다루는 2025 Q4 발표분 자체의 revision triangle은 아직 미공개 → R1·R2·R3 시트가 **현재 시점에서 가장 빠른 개정 정보 공시**.

---

## §6 다른 변수와의 관계

| 개정 시트 | 대응 본표(Table) | 비고 |
|---|---|---|
| **Table_R1** | Table_A (Summary balances) | 잔액 8개 chapter 행 단위 대응 |
| **Table_R2** | Table_B / Table_BX / Table_C / Table_E / Table_F / Table_G / Table_H | 경상수지 component 전반 — 무역(goods/services), Primary income, Secondary income |
| **Table_R3** | Table_D1_3 / Table_D4_6 / Table_D7_9 / Table_J / Table_K | IIP(stock) 및 Financial Account(transaction) — Direct·Portfolio·Other Investment |

R 시트의 행 라벨(CDID 포함)은 본표와 동일 코드를 사용하므로 매핑은 CDID join으로 1:1 결합 가능(예외: %GDP sub-table 일부는 본표에 직접 대응 코드가 없을 수 있음 — §9 참조).

---

## §7 52 unmapped CDID 시트별 보강 8필드 형식

| 필드 | 설명 | 예시 |
|---|---|---|
| `cdid` | ONS 4자 영문 코드 | `HBOP` |
| `sheet` | 소속 개정 시트 | `Table_R2` |
| `sub_table` | sub-table 구분 | `Credits` / `Debits` / `Balances` / `% of GDP` (R2) 또는 `IIP_Asset` … (R3) |
| `series_kr` | 한국어 항목명 | "경상수지 — 서비스 수입 개정액" |
| `series_en` | 영문 원 라벨 | "Current account — Services credits revision" |
| `unit` | 단위 | `GBP million` / `GBP billion` / `% of GDP` |
| `revision_basis` | 개정 산식 | "현재 발표값(2025 Q4 release) − 직전 발표값(2025 Q3 release)" |
| `source_table_xref` | 본표 cross-ref | `Table_B` / `Table_D4_6` 등 |

---

## §8 출처 카탈로그

1. **ONS, *National Accounts Revisions Policy*** (현행본 2025-06 갱신; URL slug "December2017" 유지)
   https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/revisions/revisionspoliciesforeconomicstatistics/nationalaccountsrevisionspolicyupdateddecember2017
2. **ONS, *Balance of Payments QMI*** (Quality and Methodology Information)
   https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpaymentsqmi
3. **ONS, *Balance of payments, UK: October to December 2025*** (2026-03-31 발표 — 본 저장소 대상 발표분)
   https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/octobertodecember2025
4. **ONS, *Balance of payments – revision triangles* dataset** (최신 2025-09-30)
   https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsrevisiontriangles
5. **ONS, *Detailed assessment of changes to balance of payments annual estimates 1997 to 2021*** (방법론 개선 사례 — BPM6·교육서비스·SUT)
   https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/detailedassessmentofchangestobalanceofpaymentsannualestimates1997to2020/1997to2021
6. **ONS, *UK Balance of Payments, The Pink Book: 2025*** (연간 reconciliation, 2025-10-31)
   https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025
7. **Eurostat, *Quality Assurance Framework of the European Statistical System (ESS QAF)*** (v2.0, 2019; routine vs benchmark revision 정의)
   https://ec.europa.eu/eurostat/documents/64157/4392716/ESS-QAF-V1-2final.pdf/bbf5970c-1adf-46c8-afc3-58ce177a0646
8. **IMF, *Dissemination Standards Bulletin Board (DSBB)* — UK SDDS Plus, BoP category**
   https://dsbb.imf.org/sdds/dqaf-base/country/GBR/category/BOP00
9. **IMF, *Revision Policy for Official Statistics*** (DSBB 가이드 PDF, 2003)
   https://dsbb.imf.org/content/pdfs/RevPolicyStat.pdf

---

## §9 확인 못한 부분 정직 명시

1. **"2024-05 갱신" 직접 검증 실패** — 사용자 요청 본문은 "2024-05·2025-06 갱신"을 언급했으나, 웹검색으로는 **2025-06 갱신본**과 **2017-12 원본**만 확인. 2024-05 중간 갱신 여부는 본 조사로 확정하지 못함(ONS revisions policy 페이지가 단일 URL slug에서 누적 갱신되는 구조라 중간 이력은 페이지 푸터의 "Last revised" 메타데이터로만 식별 가능).
2. **IMF DSBB UK BoP 메타데이터 본문 직접 추출 실패** — DSBB는 동적 네비게이션 페이지로 WebFetch가 본문을 잡지 못함. 인용은 IMF SDDS Plus 일반 원칙 수준.
3. **Statistical discrepancy 처리 절차의 공식 문서화** — ONS QMI는 NEO 존재만 언급하고 *처리(treatment)* 절차(NEO 흡수 algorithm, balancing item 분배 규칙)는 별도 문서화하지 않은 것으로 보임. 명시적 처리 알고리즘을 1차 출처에서 미확보.
4. **Table_R2 "% of GDP" sub-table의 본표 직접 cross-reference** — Table_A·B 등 본표는 절대값 기준 시계열이고 GDP 대비 비율은 별도 파생 항목이라, R2 %GDP sub-table의 모든 행이 본표 단일 CDID에 매핑되지 않을 가능성 있음. CDID 단위 join 시 일부 행은 GDP 시계열(예: ABMI)과 결합 필요.
5. **Table_R3 "GBP billion" 단위 표기의 행별 일관성** — R3 전체가 billion인지, IIP만 billion이고 Income은 million인지 등 sub-table별 단위 미세 차이는 시트 메타데이터 직접 확인 필요(자료 검사 단계 작업).
