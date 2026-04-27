# ONS Pink Book Ch.9 IIP 재평가 3분해 시계열 위치 (background-search 18회차)

본 문서는 `db/CHECKLIST.md` §0.2 신규 中 3번 항목(ONS Pink Book Chapter 9 IIP에서 영국의 재평가 가격·환율·기타 3분해 시계열 추출 → 슬라이드 26 매트릭스 비거래요인 정량 검증)의 산출물이다.

## 1. 보유 분기 xlsx 직접 점검 결과

`env/Scripts/python.exe`로 본 저장소의 `db/source/balanceofpayments2025q4.xlsx` 4개 IIP 시트(`Table_D1_3`, `Table_D4_6`, `Table_D7_9`, `Table_K`)의 메타·라벨·컬럼명을 키워드 검색한 결과, 다음 키워드 모두 0건 매칭:

- `revaluation`
- `exchange rate change`
- `price change`
- `non-transaction`
- `other change`
- `valuation`
- `reclassification`

`Table_D1_3` 메타 영역(1~5행)도 다음과 같이 **잔액(stock)·거래(transactions)·투자소득(investment income)** 만 다루며, 재평가 분해는 포함되어 있지 않다:

> Table D: Summary of international investment position (IIP), financial account transactions, and investment income, not seasonally adjusted

**결론**: 보유 **분기 BoP Statistical Bulletin Tables xlsx에는 재평가 3분해가 포함되지 않는다**. 별도 자료가 필요.

## 2. 외부 보강 — ONS Pink Book Dataset 8 위치

ONS Pink Book의 IIP 재평가(가격·환율·기타) 3분해 시계열은 **연간 발표** 자료에서만 공식 제공되며, 본 저장소가 보유한 분기 BoP Statistical Bulletin Tables에는 포함되지 않는다. 데이터 위치는 Pink Book **Dataset 8 (International Investment Position, The Pink Book)** — 연 1회(매년 10월말) 갱신, 2025년판은 2025-10-31 발표.

| 자료 | URL | 주기 | 비고 |
|---|---|---|---|
| Pink Book Dataset 8 — IIP | [ONS Dataset 8](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/8internationalinvestmentpositionthepinkbook2016) | 연간(10월) | 직접투자·포트폴리오·기타투자 잔액, 부문분석 |
| Pink Book 시계열(전체) | [pinkbook/current](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/pinkbook/current) | 연간 | CDID 단위 시계열 묶음 |
| Pink Book 2025 Bulletin | [Pink Book 2025](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025) | 연간 | Figure 12·13에 자산·부채 변동 4분해(거래·가격·환율·기타) 게재 |
| 분석 문서: NIIP 이해 | [NIIP analysis 2020-04-27](https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/articles/understandingtheuksnetinternationalinvestmentposition/2020-04-27) | 일회성 | 분해 방법론·환율·주가지수 가중치 설명 |

**구체적 표 식별 (확인된 범위)**: Pink Book 2025 본문은 분해를 **Figure 12 (자산 변동 분해)**·**Figure 13 (부채 변동 분해)** 형태로 제시. CDID 단위 시계열은 Dataset 8의 xlsx 파일 또는 `pinkbook/current` 데이터셋에서 추출해야 하며, 표지 페이지에는 CDID가 노출되지 않는다(직접 다운로드 후 열별 헤더 확인 필요).

## 3. 분기 vs 연간 차이

- **분기 BoP Statistical Bulletin Tables (저장소 보유 xlsx)**: IIP의 잔액(stock)과 그 분기말 수준만 제공(Table K 계열). 변동분에 대한 거래·재평가·기타 3분해는 미수록. "revaluation"·"price change"·"exchange rate change" 키워드가 분기 표에 없는 이유.
- **연간 Pink Book Dataset 8 + Bulletin**: 연간 단위로 자산·부채 변동을 (1) 순거래(net financial transactions), (2) 가격 재평가(price/equity), (3) 환율 재평가(exchange rate), (4) 기타조정(other changes/residual)로 분해.
- 이유: 환율·가격 재평가 추정에는 분기말 환율·주가/채권 지수와 부문별 통화구성 가정이 필요하며, ONS는 이를 **모형 기반(modelled)** 으로 산출해 연간 Pink Book에 반영한다(분기 단위 모형 산출은 공표되지 않음).

## 4. 영국 재평가 효과 정량 사례

- **2016 EU 국민투표(파운드 약세)**: NIIP 순부채 비율을 GDP의 6.8%까지 축소시키는 약 +27% GDP 규모의 양의 재평가 효과. (출처: Understanding the UK's NIIP, 2020-04-27)
- **2008 글로벌 금융위기**: 환율 변동이 양의 재평가 효과를 발생시켜 순부채 비율이 GDP의 1.1%까지 축소.
- **2024년**: 자산 +£365.2bn (가격 +£299.5bn, 환율 −£134.7bn[파운드 강세], 기타 −£164.0bn), 부채 +£239.0bn (가격 +£160.8bn, 환율 −£29.9bn). NIIP 순부채는 GDP의 9.7%(2023년말 £267.3bn) → 5.0%(2024년말 £145.6bn)로 축소. (Pink Book 2025)
- **2022년 파운드 약세**: 본 조사에서 Pink Book 2025 본문의 2022년 단년 수치는 명시 추출 실패 — Figure 12·13의 2022년 막대값을 xlsx로 직접 확인 필요.

## 5. 강의 슬라이드 26 매트릭스와의 정합성

슬라이드 26의 도식은 **거래요인 = BoP 투자수지 + 준비자산증감**, **비거래요인 = 가격변동 + 환율변동 + 기타조정**으로 정확히 분해한다. ONS Pink Book Dataset 8 / Bulletin Figure 12·13의 4분해(거래·가격·환율·기타)는 이 슬라이드 도식과 **개념적으로 1:1 일치**한다.

따라서 본 저장소는 (a) 분기 거래 흐름은 기존 보유 xlsx의 Table_D 시리즈로 확보, (b) 연간 재평가 3분해는 ONS Pink Book Dataset 8을 외부 보강으로 추가하면 슬라이드 26 매트릭스 전 항목을 정량 검증 가능.

## 6. 빠진 부분 / 후속 권고

- **CDID 코드**: Dataset 8 표지 페이지·검색 결과 모두 표·CDID 매핑을 노출하지 않음. 구체적 CDID는 `pinkbook/current` 시계열 데이터셋(또는 Dataset 8 xlsx)을 직접 열어 헤더에서 확인해야 함.
- **2022년 파운드 약세 영향 정량값**: Pink Book 2025 본문에 명시된 2022년 분해 수치는 추출 실패 — Figure 12·13 차트 데이터 직접 다운로드 필요.
- **분기 단위 재평가 분해**: ONS는 분기 단위로 공표하지 않음. 학술·BoE 분석에서는 자체 추정치 사용.

### 후속 권고

1. `db/source/`에 Pink Book Dataset 8(2025) xlsx 신규 다운로드(파일명 예: `pinkbookdataset8iip2025.xlsx`). 사용자 명시 승인 시 Phase 1 신규 자료로 등록.
2. 해당 xlsx 내부에서 IIP 변동 분해 표(거래·가격·환율·기타) 위치 및 CDID를 검사 절차(`db/code/source/extract_*.py`)로 식별.
3. 분기 BoP 자료(현재 보유)는 잔액/거래만 제공한다는 한계를 `db/REPORT.md`의 IIP 절에 명시.

## 추가 참고 자료

- IMF BPM6 Ch.9 "Other Changes in Financial Assets and Liabilities Account" — 국제표준 분해 정의: https://www.imf.org/external/pubs/ft/bop/2007/pdf/chap9.pdf
- ONS "Analysis of the UK's international investment position" (2016): https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/analysisoftheuksinternationalinvestmentposition/2016

## 출처

- [Pink Book Dataset 8: International Investment Position](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/8internationalinvestmentpositionthepinkbook2016)
- [UK Balance of Payments, The Pink Book: 2025 (Bulletin)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025)
- [Pink Book time series (current)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/pinkbook/current)
- [Understanding the UK's net international investment position (2020-04-27)](https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/articles/understandingtheuksnetinternationalinvestmentposition/2020-04-27)
- [Analysis of the UK's international investment position (2016)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/articles/analysisoftheuksinternationalinvestmentposition/2016)
- [Pink Book Dataset 10 — Geographical breakdown of IIP](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/10geographicalbreakdownoftheukinternationalinvestmentpositionthepinkbook2016)
- [IMF BPM6 Ch.9 Other Changes in Financial Assets and Liabilities](https://www.imf.org/external/pubs/ft/bop/2007/pdf/chap9.pdf)
