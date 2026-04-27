# ONS Errors and Omissions(NEO) 분기 시계열 변동성 (web-search 20회차)

본 문서는 `db/CHECKLIST.md` §0.2 신규 中 5번 항목(ONS Errors and omissions 분기 시계열 변동성 직접 확인. 영국 NEO의 절대값·표준편차 수치 확보)의 산출물이다. 강의 슬라이드 13(사후 항등성)·슬라이드 14(통계 불일치=0 가정)와 영국 실측의 차이를 검증한다.

## 요약

- **CDID = HHDH** (BoP net errors and omissions, NSA, £million, UKEA 데이터셋, 최신 갱신 2025-07-08).
- 2020Q1~2025Q4 24개 분기 NEO 평균 −1,503 £m, 표본 표준편차 약 6,840 £m, **절대값 평균 약 5,872 £m** — 분기 명목 GDP의 평균 약 0.9% 수준.
- 단일 분기 최댓값 +14,457 £m(2024Q1)·최솟값 −11,752 £m(2020Q4)으로 부호도 잦게 바뀜(양 11회·음 13회) → 강의 슬라이드의 "통계 불일치=0" 가정과 정면으로 어긋남.
- ONS 본문(분기 BoP 게시물·Pink Book 2025)은 NEO를 별도 절로 다루지 않고 부속 통계표·UKEA 시계열(HHDH)에서만 공개 — 잔차 항목으로 취급.
- IMF BPM6/BOPCOM 19/14는 선진국 NEO가 1990년대 이후 부호 전환은 잦으나 절대 규모는 축소 추세라 평가; 다만 G7 국가별 분기 NEO 비교 수치는 본 조사에서 확정하지 못함.

## 분기 시계열 (HHDH, NSA, £million)

| 분기 | NEO | 분기 GDP(YBHA) | NEO/GDP |
|---|---:|---:|---:|
| 2020Q1 | −8,045 | 559,365 | −1.44% |
| 2020Q2 | 8,600 | 481,227 | +1.79% |
| 2020Q3 | 1,817 | 540,319 | +0.34% |
| 2020Q4 | −11,752 | 543,809 | −2.16% |
| 2021Q1 | −4,344 | 545,116 | −0.80% |
| 2021Q2 | −5,512 | 576,525 | −0.96% |
| 2021Q3 | 1,444 | 592,707 | +0.24% |
| 2021Q4 | −5,838 | 608,304 | −0.96% |
| 2022Q1 | 3,031 | 623,014 | +0.49% |
| 2022Q2 | −5,962 | 639,293 | −0.93% |
| 2022Q3 | −7,140 | 650,233 | −1.10% |
| 2022Q4 | 2,712 | 668,409 | +0.41% |
| 2023Q1 | −1,396 | 679,194 | −0.21% |
| 2023Q2 | 11,755 | 689,618 | +1.70% |
| 2023Q3 | 9,433 | 692,982 | +1.36% |
| 2023Q4 | −1,731 | 690,370 | −0.25% |
| 2024Q1 | 14,457 | 705,573 | +2.05% |
| 2024Q2 | −2,582 | 717,865 | −0.36% |
| 2024Q3 | −7,936 | 729,877 | −1.09% |
| 2024Q4 | −7,775 | 738,129 | −1.05% |
| 2025Q1 | −2,879 | 748,000 | −0.38% |
| 2025Q2 | 1,437 | 757,927 | +0.19% |
| 2025Q3 | −9,851 | 764,673 | −1.29% |
| 2025Q4 | 3,467 | 769,261 | +0.45% |

(GDP는 ONS YBHA 분기 명목 GDP, 시즌 조정·current prices)

## 변동성 통계 (2020Q1–2025Q4, n=24, £million)

| 지표 | 값 |
|---|---:|
| 평균(mean) | −1,503 |
| 표본 표준편차(SD) | 약 6,840 |
| 절대값 평균 Mean(\|NEO\|) | 약 5,872 |
| 최댓값 | +14,457 (2024Q1) |
| 최솟값 | −11,752 (2020Q4) |
| 양수 분기 수 | 11 |
| 음수 분기 수 | 13 |
| \|NEO\|/GDP 평균 | 약 0.92% |
| \|NEO\|/GDP 최대 | 2.16% (2020Q4) |

(평균/SD/절대값 평균은 위 시계열로 산술 계산. 소수 둘째 자리 반올림.)

## ONS·국제기구 공식 설명 발췌

- ONS HHDH 시리즈 정의: "BoP net errors and omissions NSA £m" — 잔차 항목으로 공시되며, 별도 해석 문단 없이 시계열만 제공. 최근 정정 공지: "low level quarterly data within this output were incorrect for the period 1997-2019 for current price (CP) data" (2025-07-08 갱신).
- IMF BOPCOM 19/14 "Analysis of Net Errors and Omissions" (2019): "Net errors and omissions are final results from the balance of payments compilation and not a targeted number, because all accounts can contribute to NEO… it is important to analyze NEOs over time for bias in terms of persistent positive or negative NEOs, which can offer clues about the relative strength and weaknesses across the accounts." 선진국(EU·G7) NEO는 부호 전환이 잦고, 최근에는 비대칭(asymmetry) 해소 노력으로 규모가 축소되는 추세.
- IMF BPM6 Ch.2: "Although the balance of payments accounts are, in principle, balanced, in practice imbalances between the current, capital and financial accounts arise from imperfections in source data and compilation. This imbalance… is labelled net errors and omissions."

## 슬라이드 13·14 가정과의 대조

- 강의 슬라이드 13의 사후 항등성(CA + KA + FA = 0)은 **정의식**이지만, 실측에서는 NEO 항을 두어 강제로 0이 되게 한다.
- 슬라이드 14의 "통계 불일치 = 0" 가정과 달리, 영국은 분기당 평균 절대 약 5.9 십억 파운드, 즉 분기 GDP 대비 약 0.9%(최대 2.2%)의 NEO를 기록 → 단순 항등식으로 CA·FA를 동일시할 때 이 잔차만큼의 측정 오차가 잠재.

## 국제 비교

- IMF BOPCOM 19/14는 EU·G7 NEO가 "노이즈는 있으나 평균 규모는 축소" 패턴이라 평가하나, 국가별 분기 NEO/GDP 수치는 본 조사 단계에서 확정하지 못함.
- FRED 시리즈 G7B6EOTT01CXCUQ에 G7 합계 NEO(분기) 데이터가 존재(1999Q1–2024Q4, OECD 출처)하지만 본 호출에서 페이지 본문 확보 실패(403). 참조 URL: https://fred.stlouisfed.org/series/G7B6EOTT01CXCUQ.

## 빠진/확인 못한 부분

1. **국가별 G7 NEO/GDP 정량 비교** — 본 호출에서는 IMF BOPCOM 정성 평가만 확보. 미국·독일·일본 등 개별국 분기 NEO 절대값 평균을 공식 데이터로 비교하려면 IMF BOP database(BPM6) 또는 OECD QNA 추가 다운로드 필요.
2. **ONS Pink Book 2025 본문의 NEO 설명** — 요약 페이지에는 NEO 별도 해석이 없음. PDF 본문(부속 챕터·QMI)을 직접 다운로드해 확인할 필요 있음.
3. **계절조정(SA) 계열** — HHDH는 NSA만 공개. SA 시리즈 존재 여부 미확정.
4. **NEO 정정 폭(revision history)** — 2025-07-08 정정 공지가 있으나 그 영향 크기는 미확인.

## 출처

- [ONS HHDH: BoP net errors and omissions NSA £m (UKEA time series)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/hhdh/ukea)
- [ONS YBHA: GDP at current market prices, quarterly](https://www.ons.gov.uk/economy/grossdomesticproductgdp/timeseries/ybha/qna)
- [ONS Balance of payments, UK: October to December 2025](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/balanceofpayments/octobertodecember2025)
- [ONS UK Balance of Payments, Pink Book 2025](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025)
- [IMF BOPCOM 19/14 — Analysis of Net Errors and Omissions](https://www.imf.org/external/pubs/ft/bop/2019/pdf/19-14.pdf)
- [IMF BPM6 Chapter 2 — Overview of the Framework](https://www.elibrary.imf.org/view/IMF069/09838-9781589068124/09838-9781589068124/ch02.xml)
- [FRED — G7 BoP Net Errors and Omissions (G7B6EOTT01CXCUQ)](https://fred.stlouisfed.org/series/G7B6EOTT01CXCUQ)
- [UNESCWA glossary — Balance of payments, net errors and omissions](https://www.unescwa.org/sd-glossary/balance-payments-net-errors-and-omissions)
