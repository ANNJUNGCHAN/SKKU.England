# 18. ONS IIP 변동 3분해(가격·환율·기타) 시계열 공개 여부 점검

> §0.2 배경지식 사전 정리 18회차 (中 우선순위)
> 목적: 강의 슬라이드 26 BoP↔IIP 매트릭스의 **비거래요인(가격·환율·기타)** 영향을 영국 데이터로 정량 검증할 수 있는지 확인하고, Phase 3 명세서 활용 가이드를 정리.
> 작성: web-search 서브에이전트 위임 결과 정리.

---

## 핵심 결론 (3줄)

1. **부분 공개 확인** — ONS Pink Book annual statistical bulletin이 **Figure 12(자산)·Figure 13(부채)**에서 IIP 변동을 **Flows / Currency Changes / Price Changes / Other Changes**의 4열로 분해해 **2008–2024년(2025판) 시계열**로 CSV·XLS 직접 공개. 17회차에서 인용한 "ONS does not currently publish a full reconciliation…"은 **부문별 완전 분해**에는 여전히 유효하지만, **총량 4분해는 매년 갱신**되고 있음.
2. **분기 BoP statistical bulletin tables(`balanceofpayments2025q4.xlsx`)에는 분해 시트 없음** — 12회차 inventory에서 확인된 4개 IIP 시트(D1_3·D4_6·D7_9·Table_K)는 모두 stock 잔액. 분해는 **annual Pink Book bulletin** 부속 CSV 또는 **Dataset 08(chapter8.xlsx, 13시트)**에서만.
3. **권고: 부분 추가** — Figure 12·13 CSV 두 개(~3KB)는 슬라이드 26 매트릭스 총량 검증에 충분. chapter8.xlsx 추가는 시트 inventory 후 결정. ONS 2020 NIIP article은 sector × 4분해(Q1 2000–Q4 2019)로 historical 검증용 참고문헌.

---

## A. 직접 1차 분해 공개 여부

### A-1. Pink Book 2025 bulletin 본문 (가장 핵심)

**본문 인용 (자산측, 2024년)**:
> "Total flows increased by £364.4 billion. Price changes further boosted asset values by £299.5 billion … appreciation of the British pound … reduced the value of assets … by £134.7 billion."

**본문 인용 (부채측, 2024년)**:
> "Overall, total flows increased by £418.9 billion, while price changes added a further £160.8 billion. Currency revaluations … decreasing the value of liabilities by £29.9 billion and £310.7 billion respectively."

**차트**:
- **Figure 12** — "Total annual change in UK IIP **assets**, broken down into impacts" (2008–2024)
- **Figure 13** — "Total annual change in UK IIP **liabilities**, broken down into impacts" (2008–2024)

**CSV 컬럼 구조** (Figure 12 직접 fetch 결과, 자산측 2024 bulletin):

| 컬럼 | 단위 | 의미 |
|---|---|---|
| (Year) | — | 2008–2023 (2024판) / 2008–2024 (2025판 추정) |
| Flows | £ billion | BoP 금융계정 거래 |
| Currency Changes | £ billion | 환율 재평가 |
| Price Changes | £ billion | 시장가격 재평가 |
| Other Changes | £ billion | 기타 (재분류·상각·잔차) |
| Total change | £ billion | 4열 합 |

**예시(2023년 자산측)**: Flows +280.0 / Currency −469.0 / Price +458.0 / Other −245.9 / Total +23.1 (£bn). 본 4분해는 IMF BPM6 Chapter 9 *"Other Changes in Financial Assets and Liabilities Account"* 표준과 동일 구조.

**출처**:
- Pink Book 2025 bulletin: <https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025>
- Pink Book 2024 bulletin: <https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2024>
- Figure 12 CSV 직링크 (2024판): `https://www.ons.gov.uk/generator?uri=/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2024/efce8bb1&format=csv`
- Figure 13 CSV 직링크 (2024판): `https://www.ons.gov.uk/generator?uri=/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2024/6a074849&format=csv`

### A-2. Pink Book Dataset 08 (chapter8.xlsx)

- 페이지: <https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/8internationalinvestmentpositionthepinkbook2016>
- 최신본: 2025-10-31, **chapter8.xlsx (172KB, 13시트)**.
- 페이지 설명: "detailed annual statistics on the international investment position including direct, portfolio and other investment balance sheets and **sector analysis**, reserve assets for central government and financial derivatives."
- **chapter8.xlsx 시트 구조 미확정** — sharedStrings 압축 상태로 헤더 확인 실패. 12회차 inventory 절차(`inspect_bop.py`) 재사용 필요.
- 다운로드 직링크: `https://www.ons.gov.uk/file?uri=/economy/nationalaccounts/balanceofpayments/datasets/8internationalinvestmentpositionthepinkbook2016/thepinkbook2025/chapter8.xlsx`

### A-3. 분기 BoP statistical bulletin tables

**확인 완료** — 본 프로젝트 원본 `db/source/balanceofpayments2025q4.xlsx`에는 IIP 분해 시트 **없음**. 12회차 inventory(`background/note/12_xlsx_sheet_inventory.md`)에서 확정:
- IIP 시트: D1_3·D4_6·D7_9·Table_K (4개)
- 모두 end-period stock 잔액
- "revaluation"·"flows"·"currency"·"reconciliation" 시트 없음

→ **분기 발표는 IIP 분해 미제공**. 연간 Pink Book bulletin이 유일한 정기 1차 출처.

---

## B. 우회 출처 / 부분 공개

### B-1. ONS 2020 NIIP article (가장 정밀한 historical 분해)

- 페이지: <https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/articles/understandingtheuksnetinternationalinvestmentposition/2020-04-27>
- 분해: **Net transactions / Exchange rate revaluations / Market price revaluations / Other changes in volume**
- 기간: **Q1 2000 – Q4 2019** (분기)
- 세분: **Direct / Portfolio equity / Portfolio debt / Other Investment** 투자유형별
- **명시적 한계 인용**: *"it is not currently possible to estimate the other flows (revaluation and other changes in volumes) directly"* — 모델링·judgement 의존. 정기 시리즈 아님.
- 후속 갱신 부재 — 2020Q1 이후 데이터는 본 article에 없음.

### B-2. ONS sector accounts (S2 rest-of-world)

분해 4열 단독 시계열 정기 dataset 없음. ONS BoP QMI(<https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpaymentsqmi>)도 IIP 분해 방법론 별도 챕터 없음.

### B-3. IMF BOP/IIP database

- 카탈로그: <https://data.imf.org/en/datasets/IMF.STA:BOP>
- BPM6 표준은 *"Other changes in financial assets and liabilities account"* (Chapter 9) 정의:
  - (i) Exchange rate changes
  - (ii) Other price changes
  - (iii) Other changes in volume
- IMF Reconciliation Guidance B.4: *"out of 52 countries, the compilation systems of only around 10 economies would support the production of a complete set of integrated international accounts with the full reconciliation"*
- **영국이 10개국에 포함되는지 본 조사로 미확정**. SDMX query로 GBR `_OF_*` (Other Flows) 가용성 직접 확인 필요(별도 회차 후보).
- 출처: <https://www.imf.org/-/media/Files/Data/Statistics/BPM6/approved-guidance-notes/b4-reconciliation-between-flows-and-stocks.ashx>

### B-4. Eurostat

- 메타데이터: <https://ec.europa.eu/eurostat/cache/metadata/en/tipsii_esms.htm>
- BPM6 표준 인용: *"Stocks at the end of a period should equal the sum of stocks at the beginning of the period, value of transactions during the period, and value of changes in positions other than transactions"*
- 데이터셋 후보: `bop_iip6_q`, `bop_iip6_a`, `tipsii*`
- **UK가 분해 변수와 함께 제공되는지 미확정** — Brexit 이후 UK는 "neighbour" country group이지만 모든 변수 갱신은 아님. SDMX 직접 query 권장.

---

## C. 강의 슬라이드 26 정량 검증 가능성

**판정: 총량 수준에서 검증 가능, 부문별 세분 검증은 부분 가능.**

### 가능 (총량 검증)
Pink Book 2025 Figure 12 + Figure 13 결합으로 영국 NIIP 변동의 4분해 직접 산출:
```
Δ NIIP = (Asset Total) − (Liability Total)
       = (Flow_a − Flow_l)
       + (Currency_a − Currency_l)
       + (Price_a − Price_l)
       + (Other_a − Other_l)
```
이를 분기 BoP 금융계정 flow와 cross-check → 슬라이드 26의 핵심 메시지(파운드 평가절하 → 자산 currency gain ↑ → NIIP 개선) 정량 검증.

### 부분 가능 (부문·통화별)
- ONS 2020 article로 **2000Q1–2019Q4** 기간 한정 부문별 4분해.
- 2020년 이후는 article 갱신 부재 → "역사적 패턴은 article, 최근 5년은 Pink Book 총량" 분담.

### 불가능 (부문 × 4분해 × 최근 시점)
- 2020년 이후 부문별 분해 정기 시리즈 없음.
- ONS QMI·2020 article 정성 기술 + IMF BPM6 표준으로 대체.

---

## D. Phase 3 명세서 활용 가이드

### D-1. 새 STAT_CODE 등록 권고 (분기점 — 사용자 결정 대기)

- `IIP_DECOMP_ASSETS_PB2025` — Figure 12 부속 CSV (자산측 4분해, 2008–2024)
- `IIP_DECOMP_LIAB_PB2025` — Figure 13 부속 CSV (부채측 4분해, 2008–2024)
- 두 파일 합산 ~3KB.
- 명명 후보: `iip_decomp_assets_pinkbook2025.csv`, `iip_decomp_liabilities_pinkbook2025.csv`
- README 데이터 출처 항목에 발간일·source URL 명시 필수.

### D-2. 참고 문헌 인용 (다운로드 불필요)
- ONS 2020 NIIP article (sector × 4분해, Q1 2000–Q4 2019)
- chapter8.xlsx (13시트) — inventory 후 reval 분해 시트 발견되면 STAT_CODE 추가
- IMF BPM6 Chapter 9 (개념·표준)

### D-3. 학습자료 한계 명시
- 분기 BoP는 IIP 분해 미제공.
- "Other Changes" 열은 잔차 → ONS 2020 article *"not currently possible to estimate other flows directly"* caveat 명세서·REPORT.md 기록.

---

## E. 후속 작업 제안 (사용자 분기점 질문 대상)

다음 중 어느 옵션으로 진행할지 사용자 결정 필요:

### 옵션 A — 부분 추가 (권고)
1. Figure 12·13 CSV 2개를 `db/source/`에 다운로드 (~3KB).
2. chapter8.xlsx (172KB)도 받아 12회차 inventory 절차로 13시트 헤더·CDID 확인.
3. 새 명명 규칙 `iip_decomp_<assets|liabilities>_pinkbook<yyyy>.csv` 도입 (CLAUDE.md `<항목><yyyy><기간>` 패턴 확장 케이스).
4. README "데이터 출처" 항목 갱신.

### 옵션 B — 노트만 유지
1. 본 18회차 노트만으로 출처 카탈로그 정리 종결.
2. 새 데이터셋 추가는 Phase 1 진입 후 별도 회차로 분리.
3. Phase 3 명세서 작성 시점에 재검토.

### 옵션 C — 별도 IMF SDMX 회차로 확장
1. IMF SDMX API로 GBR `Other Flows` 가용성 점검 (B-3 후속).
2. Eurostat NIIP quarterly UK 분해 변수 가용성 점검 (B-4 후속).
3. 결과에 따라 옵션 A 또는 B로 회귀.

---

## F. 출처 카탈로그 (CSV는 동일 폴더 `18_iip_revaluation_decomp.csv`)

| 기관 | 제목 | URL | 갱신주기 | 단위 |
|---|---|---|---|---|
| ONS | Pink Book 2025 bulletin | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025 | 연간(매년 10월) | £bn / £m |
| ONS | Pink Book 2024 bulletin | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2024 | 연간 | £bn / £m |
| ONS | Figure 12 CSV (2024 assets, 4분해) | https://www.ons.gov.uk/generator?uri=/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2024/efce8bb1&format=csv | 연간 | £bn |
| ONS | Figure 13 CSV (2024 liab, 4분해) | https://www.ons.gov.uk/generator?uri=/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2024/6a074849&format=csv | 연간 | £bn |
| ONS | Dataset 08 chapter8.xlsx (172KB, 13시트) | https://www.ons.gov.uk/file?uri=/economy/nationalaccounts/balanceofpayments/datasets/8internationalinvestmentpositionthepinkbook2016/thepinkbook2025/chapter8.xlsx | 연간 | £m |
| ONS | Dataset 08 페이지 | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/8internationalinvestmentpositionthepinkbook2016 | 연간 | £m |
| ONS | Pink Book 시계열 데이터셋 | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/pinkbook | 연간 | 다양 |
| ONS | Understanding the UK's net IIP (2020 article) | https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/articles/understandingtheuksnetinternationalinvestmentposition/2020-04-27 | 1회성 | — |
| ONS | BoP QMI | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpaymentsqmi | — | — |
| ONS | UK Economic Accounts BoP-IIP (단종 2022-04) | https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/datasets/unitedkingdomeconomicaccountsbalanceofpaymentsinternationalinvestment | — | — |
| ONS | BoP October–December 2025 bulletin | https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/octobertodecember2025 | 분기 | £m |
| IMF | BPM6 Reconciliation Guidance B.4 | https://www.imf.org/-/media/Files/Data/Statistics/BPM6/approved-guidance-notes/b4-reconciliation-between-flows-and-stocks.ashx | — | — |
| IMF | BPM6 Chapter 9 PDF | https://www.imf.org/external/pubs/ft/bop/2007/pdf/chap9.pdf | — | — |
| IMF | BOP / IIP dataset 카탈로그 | https://data.imf.org/en/datasets/IMF.STA:BOP | 분기·연 | USD m |
| Eurostat | BoP & IIP (BPM6) Statistics Explained | https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Balance_of_payments_and_international_investment_position_manual_(BPM6) | — | — |
| Eurostat | tipsii 메타데이터 | https://ec.europa.eu/eurostat/cache/metadata/en/tipsii_esms.htm | — | — |
| Eurostat | NIIP quarterly (tipsii40) | https://ec.europa.eu/eurostat/databrowser/view/tipsii40/default/table?lang=en | 분기 | EUR m |

---

## G. 미해결·후속 조사 항목

1. **chapter8.xlsx 13시트 inventory** — sharedStrings 압축 해제 후 시트별 헤더·CDID 확인. 12회차 절차 재사용.
2. **IMF SDMX GBR `Other Flows` 가용성** — `data.imf.org` API 직접 query.
3. **Eurostat tipsii UK 분해 변수 가용성** — Brexit 이후 갱신 여부 확인.
4. **Pink Book Figure 12·13 CSV 2025판** — 2024판 직링크 확인됨, 2025판은 동일 패턴 URL 재구성 필요.

---

## H. 인용·저작권

본 노트의 모든 정의·인용은 1차 출처(ONS, IMF, Eurostat) 공식 페이지에서 발췌. 한국어 정리 및 해석은 프로젝트 노트 목적으로 작성.
