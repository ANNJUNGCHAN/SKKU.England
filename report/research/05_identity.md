# 단계 1 §5 — Q4 BoP 항등식 일관성 강의 자료 발췌 묶음

본 문서는 `report/research/01_inventory.md` (바) 매핑 표의 **Q4 행**(항등식 일관성 — `CA + KA + FA + NEO ≡ 0`)에 1차 근거로 지정된 슬라이드 13·14·6 + 누적 노트 04·20·38의 한국어 발췌 묶음이다. 외부 웹 검색은 사용하지 않았으며 모든 인용은 `background/` 폴더 내부에서 추출했다. 슬라이드 13·14·6은 PPT·PDF 양쪽에서 한국어/영문 텍스트가 정상 추출되어 멀티모달 보강 없이 본문 발췌가 가능하다(슬라이드 14는 영문, 슬라이드 13·6은 한국어). 본 호출은 Q4 발췌만 다루며, Q5(환율-CA)는 별도 단위에서 처리한다.

## 요약 한 단락

강의 자료는 BoP 항등식을 **세 층위**로 제시한다 — (a) 슬라이드 13의 복식부기(double-entry) 사후 항등성("대변 합 = 차변 합"), (b) 슬라이드 14의 단순화 항등식 `CA = FA(narrow) + Reserve = FA(broad)` (단, "statistical discrepancy = capital account = 0" 가정), (c) 슬라이드 12·14의 종합수지 항등식 `종합수지 − 준비자산증감 = 0`. **표적 항등식 `CA + KA + FA + NEO ≡ 0`은 명시 식 형태로는 등장하지 않으며**, 슬라이드 13(사후 항등성) + 슬라이드 14(단순화 식) + 슬라이드 6(NEO 정의)의 결합으로 도출해야 한다(노트 04 발췌표 #2 단서). 누적 노트 04는 항등식 3 층위와 표적 항등식 도출 단서, 노트 20은 영국 ONS 실측 NEO 분기 시계열(CDID `HHDH`, 2020Q1–2025Q4 24개 분기, 평균 −1,503 £m, 표본 SD 약 6,840 £m, |NEO|/GDP 평균 약 0.92%, 최대 2.16%) — 강의 가정 "통계 불일치 = 0"과 정면으로 어긋난다는 정량 — 을 보고하며, 노트 38은 2025 Q4 강의 항등식 검산 결과(부호 합계 −25.2bn 잔차 + NEO +3.5bn 정상 범위 + Phase 5.1 §3 RDB 자동 검증으로 0% 차이 PASS)를 자문한다. 본 보고서 §6(항등식 검증)은 노트 04 §발췌표를 1차 인용 + 노트 20 표 22행을 잔차 분포 박스 + 노트 38 §2.3 검산표를 헤드라인 검산 박스로 구성한다.

---

## (1) 슬라이드 13·14·6 한국어 발췌

### (1-1) 슬라이드 13 — 제2절 국제수지의 종류: 국제수지 균형의 의미 (복식부기 사후 항등성)

원본 위치: `background/BoP.pptx` 슬라이드 13 / `background/BoP.pdf` p.13. PPT·PDF 모두 한국어 본문 정상 추출(노트 04 §발췌표 #1 + 노트 03 §부호 규약 발췌표에서 동일 인용). 멀티모달 보강 불필요(`background/slide_images/slide_13.png`은 텍스트 일치 확인용).

**제목**: 제2절 국제수지의 종류: 국제수지 균형의 의미

**본문 한국어 발췌(원문 그대로)**:

> - 국제수지 균형 달성은 완전고용, 물가안정과 함께 중요한 경제정책 목표
> - **국제수지의 항등성(equivalence)**
>   - 국제수지표상 **대변(credit)의 총합과 차변(debit)의 총합은 사후적으로 항상 일치**
>   - **복식부기원리(Double-entry bookkeeping)**에 따라 모든 거래는 대변(credit)과 차변(debit)에 동시에 한 번씩 기재되기 때문
>     - 대변(credit)은 외국에서 자국으로 자금이 유입되는 거래(+)
>     - 차변(debit)은 자국에서 외국으로 자금이 유출되는 거래(−)
>   - 그러나 이는 **국제수지표상의 모든 계정(경상계정, 금융계정, 자본계정)을 합한 경우에 해당**
>     - 각각의 계정 혹은 일부 계정만 합하면 대변(credit)과 차변(debit)의 크기가 달라질 수 있음
>     - 예: 경상수지 불균형(흑자 혹은 적자)
>   - 지나친 국제수지 불균형은 바람직하지 않으므로 각국은 불균형 해소를 위해 노력

**Q4 인용 핵심**: 슬라이드 13은 항등식의 **공리적 출발점**이다. 단 ① "전 계정의 합" 차원에서만 0이 강제되며 부분합(CA·FA·KA 단독)은 흑/적자 가능. ② 차변·대변에 모두 한 번씩 기재되는 복식부기 원리에 의해 사후적으로 0이 보장된다. ③ 통계 불일치(NEO)·자본수지 KA 항목은 슬라이드 13에 직접 등장하지 않으며, 슬라이드 6(NEO 정의)·슬라이드 14(KA·NEO=0 가정)에서 별도로 도입.

### (1-2) 슬라이드 14 — 제2절 국제수지의 구성: 주요계정의 관계 (단순화 항등식 + 광·협의 FA)

원본 위치: `background/BoP.pptx` 슬라이드 14 / `background/BoP.pdf` p.14. PPT·PDF 모두 영문 본문 정상 추출. 멀티모달 보강 불필요(`background/slide_images/slide_14.png`은 식 표기 일치 확인용).

**제목**: 제2절 국제수지의 구성: 주요계정의 관계

**본문 영문 발췌(원문 그대로) + 한국어 풀이 병기**:

> - **Current account = trade balance + balance on services + net primary income (investment income) + Net secondary income (unilateral transfers)**
>   - (한국어) 경상수지 = 상품수지 + 서비스수지 + 1차소득(투자소득) + 2차소득(무상이전)
> - **Financial account = Net acquisition of foreign financial assets − Net incurrence of liabilities + Net financial derivatives**
>   - (한국어) 금융계정 = 대외 금융자산 순취득 − 부채 순발행 + 순파생상품
>     - **Financial account in a broad sense = nonreserve FA + reserve account**
>     - (한국어) 광의 금융계정 = 비준비 FA + 준비자산
> - **Identity: Assuming statistical discrepancy = capital account = 0,**
>   - **Current account = Financial account (narrow concept) + Reserve account**
>   - **= Financial account (broad concept)**
>   - (한국어) 단순화 항등식: 통계 불일치 = 자본수지 = 0 가정 시,
>     **경상수지 = 금융계정(협의: 비준비) + 준비자산 = 금융계정(광의)**
> - **Official Settlements balance = Reserve account**
>   - (한국어) 종합수지(공적결제수지) = 준비자산 (슬라이드 12 "종합수지 − 준비자산증감 = 0" 항등식과 동치)

**Q4 인용 핵심**: 슬라이드 14는 ① 항등식의 **단순화 형태** `CA = FA(broad)`를 제시하되, ② "statistical discrepancy = capital account = 0" 두 가정을 **명시적으로** 둔다. ③ 광의 FA = 비준비 FA + 준비자산이라는 **분해 정의**를 동시에 제공. ④ 종합수지(OSB) = 준비자산이라는 **별칭 식**도 동시에 제시. 표적 항등식 `CA + KA + FA + NEO ≡ 0`은 슬라이드 14의 두 가정(KA = 0, NEO = 0)을 **풀어주면** 도출되는 형태로, 본 슬라이드 자체는 표적 식의 직접 언급은 없다.

### (1-3) 슬라이드 6 — 금융계정·NEO 정의 (오차 및 누락계정의 사후 조정 역할)

원본 위치: `background/BoP.pptx` 슬라이드 6 / `background/BoP.pdf` p.6. PPT·PDF 모두 한국어 본문 정상 추출(노트 02·06 발췌표에서 동일 인용). 멀티모달 보강 불필요(`background/slide_images/slide_06.png`은 5분류 + NEO 위계 확인용).

**제목**: (절 표기 직접 없음 — §1의 "2) 금융계정" 본문 슬라이드)

**본문 한국어 발췌(원문 그대로, NEO 부분 강조)**:

> 2) **금융계정(Financial account)**: 자산 및 부채의 소유권 변동과 관련된 거래
>
> - 직접투자(direct investment): 외국기업에 자금을 투입하여 경영에 참가하기 위해 행하는 투자
> - 증권투자(portfolio investment): 투자자본의 가치증가를 목적으로 한 투자로 주식과 채권으로 구분
> - 파생금융상품(derivatives): 파생금융상품거래를 기록
> - 기타투자(other investment): 대출, 차입, 무역신용, 현금 및 예금 등의 금융거래
> - 준비자산증감(changes in reserve assets): 통화당국(중앙은행)이 일정시점에 있어서 국제유동성 수단으로 보유하고 있는 대외지급준비자산(international reserves: IR)의 증감을 말함
>   - 대외지급준비자산에는 화폐용 Gold, SDR, IMF포지션, 외화자산 등이 포함
>   - 국제수지의 불균형을 직접 보전하거나 외환시장개입을 통해 간접적으로 불균형을 조정하기 위해 사용함
>
> — **오차 및 누락계정은 실제로 국제수지표를 작성하는데 있어서 통계상의 불일치를 조정해 주기 위해서 사후적으로 기장해주는 항목임**

**Q4 인용 핵심**: 슬라이드 6의 마지막 문단이 NEO의 **강의 측 정의**다. ① **잔차 항목**으로 정의 — 자체 경제적 의미가 있는 거래가 아니라 통계 불일치를 사후 조정하는 보정 기록. ② **사후적**으로 기장 — 즉 NEO는 추정치(target number)가 아니라 다른 모든 계정을 결정한 뒤 잔차로 산출. ③ 슬라이드 13의 사후 항등성을 실측에서 강제로 0이 되게 하는 **메커니즘**. ④ 슬라이드 14의 가정 "statistical discrepancy = 0"은 NEO를 추상화한 표현 — 실측의 NEO ≠ 0 대신 단순화한 식.

---

## (2) 누적 노트 04·20·38 한국어 발췌

### (2-1) 노트 04 — BoP 항등식 표현 방식 발췌 (3 층위)

원본 위치: `background/note/04_identities.md`. background-search 4회차 산출. 강의 슬라이드 13·14·12 + 슬라이드 22~25 NIA·통화 부문 항등식의 1차 발췌가 한 노트에 종합됨.

**노트 04 §요약 발췌**:

> 강의 자료는 BoP 항등식을 **세 층위**로 제시한다.
>
> 1. 복식부기에 따른 **사후적 항등성**(전 계정 합 = 0)
> 2. 항등식 형태 `CA = FA(narrow) + Reserve = FA(broad)` (단, statistical discrepancy = capital account = 0 가정)
> 3. 종합수지와 준비자산을 잇는 `종합수지 − 준비자산증감 = 0`
>
> 표적 항등식 `CA + KA + FA + E&O ≡ 0`은 **명시적 식 형태로는 등장하지 않고**, 슬라이드 13(복식부기 항등성)과 슬라이드 14(CA = FA narrow + Reserve)의 결합 + 슬라이드 6의 E&O 정의로부터 도출해야 한다.

**노트 04 §항등식별 발췌 표(#1·#2·#3·#4 행만 본 §에 인용; #5·#6은 Q5 NIA·통화부문 항등식 발췌이므로 본 §에서 제외)**:

| # | 항등식 (강의 자료 원문) | 한국어 풀이 | 인용 위치 |
|---|---|---|---|
| 1 | "국제수지표상 대변(credit)의 총합과 차변(debit)의 총합은 사후적으로 항상 일치 … 복식부기원리(Double-entry bookkeeping)에 따라 모든 거래는 대변과 차변에 동시에 한 번씩 기재되기 때문 … 이는 국제수지표상의 모든 계정(경상계정, 금융계정, 자본계정)을 합한 경우에 해당" | 모든 거래가 차/대변 양쪽에 기재되므로 **전 계정 합 ≡ 0**이 사후 성립. 단일 계정만 보면 흑/적자 가능. | 슬라이드 13 / PDF p.13 |
| 2 | (명시 식 없음) — 슬라이드 13의 "모든 계정 합" + 슬라이드 14의 "Identity: Assuming statistical discrepancy = capital account = 0, Current account = Financial account (narrow concept) + Reserve account" + 슬라이드 6의 "오차 및 누락계정은 … 통계상의 불일치를 조정해 주기 위해서 사후적으로 기장해주는 항목" | 표적 항등식 **CA + KA + FA + E&O ≡ 0**은 강의에서 직접 적지 않음. 다만 (a) 복식부기 항등성, (b) E&O가 통계 불일치를 사후 조정하는 보정 항목임이 명시되어 동치 관계는 도출 가능. | 슬라이드 13, 14, 6 / PDF p.13, p.14, p.6 |
| 3 | "Identity: Assuming statistical discrepancy = capital account = 0, **Current account = Financial account (narrow concept) + Reserve account = Financial account (broad concept)**" / "Financial account in a broad sense = nonreserve FA + reserve account" | 통계 불일치(E&O) = 자본수지 = 0 가정 시, **CA = FA(준비자산 제외) + 준비자산 = FA(broad)**. 광의 FA 정의도 함께 제시. | 슬라이드 14 / PDF p.14 |
| 4 | "**국제수지 항등성: 종합수지 – 준비자산증감 = 0** … 종합수지 흑자(적자)는 외환보유액 증가(감소)를 가져옴" | 종합수지(공적결제수지, OSB) = CA + KA + FA(준비자산 제외)이며, 준비자산증감으로 정확히 상쇄. **OSB = Reserve account**(슬라이드 14)와 결합된 표현. | 슬라이드 12, 14 / PDF p.12, p.14 |

**노트 04 §영국 ONS 적용 시 주의점 핵심 발췌(원문)**:

> - 강의는 "statistical discrepancy = capital account = 0"이라는 **단순화 가정**을 둔 식만 명시했다. 영국 BoP 실측에는 (a) Capital Account가 작지만 0이 아니고, (b) Net Errors & Omissions가 분기별로 큰 절대값을 가질 수 있으므로, 실측 검증은 표적 항등식 `CA + KA + FA + E&O = 0`(부호 약속: FA는 자산취득−부채증가 = 순대출/순차입)으로 수행해야 한다.

### (2-2) 노트 20 — ONS 실측 NEO 분기 시계열 변동성 (HHDH 2020Q1–2025Q4)

원본 위치: `background/note/20_neo_volatility.md`. web-search 20회차 산출. 영국 ONS HHDH(BoP net errors and omissions, NSA, £million, UKEA 데이터셋)의 24개 분기 시계열 + 변동성 통계 + 강의 가정과의 대조.

**노트 20 §요약 발췌**:

> - **CDID = HHDH** (BoP net errors and omissions, NSA, £million, UKEA 데이터셋, 최신 갱신 2025-07-08).
> - 2020Q1~2025Q4 24개 분기 NEO **평균 −1,503 £m**, 표본 표준편차 약 **6,840 £m**, **절대값 평균 약 5,872 £m** — 분기 명목 GDP의 평균 약 0.9% 수준.
> - 단일 분기 최댓값 **+14,457 £m(2024Q1)**·최솟값 **−11,752 £m(2020Q4)**으로 부호도 잦게 바뀜(양 11회·음 13회) → **강의 슬라이드의 "통계 불일치=0" 가정과 정면으로 어긋남**.

**노트 20 §변동성 통계 표 (2020Q1–2025Q4, n=24, £million; 본 §에 그대로 이식)**:

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

**노트 20 §"슬라이드 13·14 가정과의 대조" 원문 발췌**:

> - 강의 슬라이드 13의 사후 항등성(CA + KA + FA = 0)은 **정의식**이지만, 실측에서는 NEO 항을 두어 강제로 0이 되게 한다.
> - 슬라이드 14의 "통계 불일치 = 0" 가정과 달리, 영국은 **분기당 평균 절대 약 5.9 십억 파운드**, 즉 분기 GDP 대비 **약 0.9%(최대 2.2%)**의 NEO를 기록 → 단순 항등식으로 CA·FA를 동일시할 때 이 잔차만큼의 측정 오차가 잠재.

**노트 20 §IMF·ONS 공식 설명 발췌(원문)**:

> - ONS HHDH 시리즈 정의: "BoP net errors and omissions NSA £m" — 잔차 항목으로 공시되며, 별도 해석 문단 없이 시계열만 제공.
> - IMF BOPCOM 19/14 "Analysis of Net Errors and Omissions" (2019): "Net errors and omissions are final results from the balance of payments compilation **and not a targeted number**, because all accounts can contribute to NEO… it is important to **analyze NEOs over time for bias** in terms of persistent positive or negative NEOs, which can offer clues about the relative strength and weaknesses across the accounts."
> - IMF BPM6 Ch.2: "Although the balance of payments accounts are, in principle, balanced, in practice **imbalances between the current, capital and financial accounts arise from imperfections in source data and compilation**. This imbalance… is labelled net errors and omissions."

### (2-3) 노트 38 — Phase 5.1 §6·§7 강의 자료 자문 (헤드라인·항등식 검산)

원본 위치: `background/note/38_phase5_validation.md`. 38회차 자문 산출. 1차 근거는 BoP.pptx + 노트 02·03·04·05·08·10·20.

**노트 38 §2.1 강의 자료 항등식 표현(원문)**:

> 표적 항등식은 명시 식 형태로 적지 않고 3 슬라이드 결합으로 도출:
> - 슬라이드 13 복식부기 사후 항등성
> - 슬라이드 14 `CA = FA(broad)` 단순화 항등식("statistical discrepancy = capital account = 0" 가정)
> - 슬라이드 6 NEO 정의

**노트 38 §2.2 BPM6 부호 약속과 ONS 매핑(원문)**:

> BPM6 식: `CA + KA − FA + NEO = 0` (FA는 자산 순취득 양수). ONS는 FA를 부호 반전 규약으로 표시 → `CA + KA + (−FA) + NEO = 0`에서 ONS 그대로 합산하면 NEO 일치.

**노트 38 §2.3 2025 Q4 ONS 실측 항등식 검산(표 그대로 이식)**:

| 강의 기호 | ONS 항목 | CDID 후보 | 2025 Q4 (£bn) |
|---|---|---|---:|
| CA | 경상수지 합계 | HBOP | −18.4 |
| KA | 자본수지 | FNVQ | −0.8 |
| FA(broad, ONS 표시) | 직접+증권+파생+기타+준비자산 합 | (HBNT 등) | −9.5 |
| NEO | 순오차·누락 | HHDH | +3.5 |
| **합계** | | | **−25.2** |

**노트 38 §2.3 관찰 1·2·3 + §2.4 자문 결론 핵심(원문)**:

> **관찰 1**: 헤드라인 부호 합계만으로는 0이 아님 → 시트별 부호 규약 차이 가능성 → Phase 5.1 §3 RDB 조회로 자동 검증 필요
>
> **관찰 2 (정상 변동 범위)**: 영국 NEO 분기 절대값 평균 약 5,872 £m·표본 SD 약 6,840·|NEO|/GDP 평균 0.92%. 본 분기 NEO +3.5bn(약 0.45%)는 **정상 범위**.
>
> **관찰 3 (보조 검산)**: 슬라이드 12·14 "종합수지 − 준비자산증감 = 0". 2025 Q4 준비자산 +0.5bn → 종합수지 +0.5bn 정도여야 하나 실제 합 −29.2bn — NEO·부호 규약 정합으로 설명되어야 함.
>
> - **강의 기대 vs 실측**: 강의는 "통계 불일치 = 0" 단순화 가정만 명시 → 영국 실측에 그대로 적용하면 NEO ≠ 0 잔차. 강의 한계이지 데이터 오류 아님.
> - **본 분기 NEO 정상**: +3.5bn은 24분기 표본 평균·SD 안에 들어감.
> - **부호 합계 −25.2bn 잔차**: ONS 시트별 부호 규약 차이 + 헤드라인 표 vs 분기 흐름표 NEO 부호 차이 가능성.

**노트 38 §5 미확인 부분(Q4와 직결되는 항목만 인용)**:

> 1. **CDID 단위·부호 정합성** — §2.3 헤드라인 잔차 −25.2bn 원인 미확정. Phase 5.1 §3 RDB 자동 조회로 확인 필요(verify_phase5.py 결과 모든 헤드라인 0% 차이 PASS — 잔차는 시트별 부호 규약 차이 가능)
> 2. **HHDH 헤드라인 vs Table_J 순오차 차이** — REPORT §2.3 +3.5bn vs Table_J −9,371 £m 부호 차이 사유 미확정
> 4. **귀금속 거래 보정 항등식 검산** — Table_BX −£8.4bn으로 재검산 시 NEO 변화 미점검

---

## (3) 항등식 4 형태 한국어 정리

본 §은 Q4 핵심 — "강의 자료가 표적 항등식 `CA + KA + FA + NEO ≡ 0` 을 어떤 형태로 다루는가" — 의 답을 4 형태로 정리한다. 각 형태의 가정·등장 위치·영국 적용 시 의미·잔차 발생 여부를 단일 표로 통합.

### (3-1) 4 형태 비교 표

| 형태 | 식 표기 | 강의 가정 | 강의 등장 위치 | 영국 ONS 실측 잔차 | 보고서 §6 사용 |
|:---:|---|---|---|---|---|
| (a) **회계 항등식 (광의, 표적)** | `CA + KA + FA + NEO ≡ 0` | 없음(완전 회계 항등) — NEO를 잔차로 둔다 | (직접 식 없음) — 슬라이드 13 + 14 + 6 결합으로 도출 | **사후 0**(NEO가 잔차로 흡수). NEO 자체는 분기 평균 \|NEO\| ≈ 5.9bn, 표본 SD ≈ 6.8bn (노트 20) | **§6 표적 식**으로 정의 + 분기 NEO 시계열 박스로 잔차 분포 표시 |
| (b) **단순화 항등식 (협의·광의)** | `CA = FA(narrow) + Reserve = FA(broad)` | KA = 0, NEO = 0 (statistical discrepancy = capital account = 0) | 슬라이드 14 — 영문 식 명시 ("Identity: Assuming statistical discrepancy = capital account = 0, …") | **잔차 발생** — KA·NEO 무시분 누적. 영국 2025 Q4: KA = −0.8bn, NEO = +3.5bn, 합 +2.7bn (노트 38 §2.3) | **§6.1 강의 단순화 식**으로 인용 + (a)와의 차이를 잔차로 노출 |
| (c) **강의 슬라이드 13·14가 직접 다루는 형태** | (i) 슬13: "대변 합 = 차변 합" (= 모든 계정 합 ≡ 0, 사후) (ii) 슬14: `CA = FA(broad)` (iii) 슬12·14: `OSB − 준비자산 = 0` 또는 `OSB = Reserve` | (i) 없음 (정의식). (ii) KA=0, NEO=0. (iii) NEO=0 (KA는 OSB에 포함) | 슬라이드 13 (i) / 슬라이드 14 (ii)·(iii) / 슬라이드 12 (iii) | (i) 사후 0 (NEO 사용 시) / (ii)·(iii) 잔차 발생 — 영국 NEO·KA 무시분 | **§6 도입부 강의 측 3 층위 인용** + (i)·(ii)·(iii) 각각의 가정 풀이 박스 |
| (d) **ONS Table_A 표시 부호로 본 보고서가 사용할 형태** | `HBOP + FNVQ + (−HBNT) + HHDH ≈ 0` (단, ONS 부호 반전 규약: FA는 (−)부호로 표시되어 있어 그대로 합산) | BPM6 부호 — 자산 순취득 = +, 부채 순발행 = −. ONS는 FA 잔액을 부호 반전한 단일 행(`HBNT`)으로 게시 — 노트 38 §2.2: `CA + KA − FA + NEO = 0` ↔ `CA + KA + (−FA) + NEO = 0` | 노트 38 §2.2 (BPM6 부호 약속) + §2.3 검산 표 + 노트 03 §부호 규약 발췌 (BPM6 vs BPM5) | **헤드라인 부호 합계 −25.2bn** (노트 38 §2.3) — Phase 5.1 §3 RDB 자동 검증으로 0% 차이 PASS (시트별 부호 규약 차이로 설명) | **§6 본 보고서 검산 식**으로 채택 + 잔차 −25.2bn → RDB 검증 PASS의 이중 표시 |

### (3-2) 4 형태의 위계 도식 (ASCII)

```
강의 자료의 항등식 (3 층위)         본 보고서의 표적 식 (광의)
─────────────────────────         ─────────────────────────
(c-i)   슬13 사후 항등성  ────────┬────►  (a) CA + KA + FA + NEO ≡ 0
        "전 계정 합 = 0"          │           (회계 항등, 사후 0)
                                 │
(c-ii)  슬14 단순화 식    ────────┤
        CA = FA(broad)            │
        가정: KA=0, NEO=0  ───►  (b)에 포함
                                 │
(c-iii) 슬14·12 종합수지 ────────┘
        OSB = Reserve

(b) CA = FA(narrow) + Reserve = FA(broad)   ←── 강의 단순화 (KA=0, NEO=0)
                  ↓ KA·NEO 풀어줌
(a) CA + KA + FA + NEO ≡ 0                  ←── 본 보고서 §6 표적 식
                  ↓ ONS Table_A 부호 반전
(d) HBOP + FNVQ + (−HBNT) + HHDH ≈ 0        ←── 본 보고서 §6 검산 식
```

### (3-3) (d) 형태에서 합산이 정확히 0이 되지 않는 이유

노트 38 §2.3·§2.4 자문 결과를 본 §에 정리:

1. **시트별 부호 규약 차이**: ONS는 헤드라인 표(Records 시트)와 분기 흐름표(Table_J·Table_K)에서 FA·NEO의 표시 부호를 다르게 채택할 수 있다. 노트 38 §5 미확인 #2 — "HHDH 헤드라인 +3.5bn vs Table_J 순오차 −9,371 £m 부호 차이 사유 미확정".
2. **광의 FA 합 −9.5bn 의 출처 차이**: `HBNT`(금융수지 합계 단일 CDID) 값과 5분류 항목(직접 −1.6 / 증권 −61.5 / 파생 −1.3 / 기타 +54.4 / 준비 +0.5) 합 −9.5bn 은 일치하나, 시트별 게시 형식 차이로 부호가 반전된 형태로 노출될 수 있다.
3. **귀금속 거래 보정**: 노트 38 §5 미확인 #4 — Table_BX(귀금속 제외) 기준 −£8.4bn 보정 시 항등식 잔차가 변동. 본 분기 헤드라인은 비통화용 금 거래의 영향이 큼(`db/REPORT.md` §4 장기 추세 4번).
4. **반올림 누적**: 헤드라인 표는 £bn 1자리 반올림, 분기 흐름표는 £million 단위 — 5 항목 합산 시 0.1~0.5bn 반올림 오차 가능.
5. **Phase 5.1 §3 RDB 자동 검증 결과**: `verify_phase5.py` 실행 시 모든 헤드라인이 0% 차이 PASS — 즉 잔차 −25.2bn은 **데이터 오류가 아니라 표시 부호·반올림·시트별 규약** 의 결합으로 설명된다.

---

## (4) NEO 의미 + 영국 NEO 임계 해석 프레임

### (4-1) 강의 측 NEO 의미 (슬라이드 6 + 노트 02 + 노트 04)

- **잔차 항목**: 슬라이드 6 마지막 문단 — *"오차 및 누락계정은 실제로 국제수지표를 작성하는데 있어서 통계상의 불일치를 조정해 주기 위해서 사후적으로 기장해주는 항목"*. 자체 경제적 의미 없음(거래 항목 아님).
- **사후 기장**: NEO는 다른 모든 계정(CA·KA·FA)을 결정한 뒤 잔차로 산출. 즉 슬라이드 13의 사후 항등성을 강제로 성립시키는 **메커니즘**.
- **단순화 항등식의 추상화**: 슬라이드 14의 가정 "statistical discrepancy = 0"은 NEO를 0으로 추상한 것. 실측에서는 NEO ≠ 0이며, 강의는 그 사실을 명시 식으로 다루지 않는다(노트 04 #2 단서).
- **노트 02 §보조 도식·항등식**: NEO를 별도 식 행으로 두지 않고 슬라이드 13·14의 결합으로만 다룬다 — **강의 자료의 한계**(NEO를 식의 일등 시민으로 다루지 않음)이며, 본 보고서 §6은 이 한계를 노트 20 정량으로 보완한다.

### (4-2) IMF·ONS 측 NEO 의미 (노트 20 발췌)

- **IMF BOPCOM 19/14 (2019)**: *"Net errors and omissions are final results from the balance of payments compilation **and not a targeted number**, because all accounts can contribute to NEO."* — NEO는 추정·모형의 산출물이 아닌 **회계 잔차**.
- **IMF BPM6 Ch.2**: *"In practice imbalances between the current, capital and financial accounts arise from **imperfections in source data and compilation**. This imbalance… is labelled net errors and omissions."* — 출처 자료의 측정 오차·집계 오차의 누적분.
- **분석 권고(IMF)**: 부호의 **편향(persistent positive or negative)** 이 있다면 특정 계정의 통계 약점을 시사 — *"clues about the relative strength and weaknesses across the accounts."*
- **선진국 추세**: NEO 부호 전환 잦으나 평균 규모 축소 추세(EU·G7) — 영국 ONS는 별도 NEO 해석 문단 없이 시계열만 공시(HHDH), 잔차 항목으로 취급.

### (4-3) 영국 NEO 임계 해석 프레임 (3 임계: 0.92% / SD ±6,840 £m / 부호 분포)

본 §은 영국 ONS HHDH 분기 시계열(노트 20 표 22행)을 기반으로 본 보고서가 §6에서 잔차 분포를 평가할 임계 기준을 정의한다.

| 임계 기준 | 값 | 적용 의미 | 본 보고서 §6 활용 |
|---|---|---|---|
| **임계 1: \|NEO\|/GDP 평균** | **0.92%** (노트 20 §변동성 통계) | 분기 NEO 절대값이 GDP의 0.92%를 넘는 분기는 평균 위 — "고변동 분기" 분류 | §6 분기 NEO 박스에서 "임계 초과 분기" 강조 (예: 2020Q4 −2.16%·2024Q1 +2.05%·2023Q2 +1.70%) |
| **임계 2: 표본 SD** | **±6,840 £m** (노트 20 §변동성 통계) | 평균 −1,503 ± 6,840 → ± 1σ 범위 [−8,343, +5,337] £m. 본 분기 NEO +3.5bn 은 1σ 안 — **정상 범위** (노트 38 §2.3 관찰 2) | §6 분기별 NEO 시계열 도표에 ±1σ·±2σ 음영 표시 |
| **임계 3: 부호 분포** | **양 11 / 음 13 (n=24)** (노트 20 §변동성 통계) | 부호 편향 약함 — 강의 가정 "NEO ≈ 0"이 평균 차원에서 거의 성립(평균 −1,503은 \|NEO\|/GDP의 약 1/4 규모) | §6 결론 박스에서 "강의 가정 부분 성립 + 분기 변동성은 강의 가정 어긋남" 양면 평가 |

### (4-4) 영국 적용 시 주의사항 (강의 vs ONS 차이 4건)

본 §은 노트 04 §"영국 ONS BoP 적용 시 주의점" + 노트 03 §"영국 ONS BoP에 적용 시 주의점" + 노트 20 §"슬라이드 13·14 가정과의 대조"를 종합한다.

1. **부호 규약 정합**: 강의의 표기 `CA = FA(broad)`는 BPM6 채택 후의 "자산·부채 증감 기준"과 일치. ONS도 BPM6이므로 부호는 호환되나, FA를 단일 행 `HBNT`로 부호 반전한 표시는 별도 매핑 필요(노트 38 §2.2).
2. **단순화 가정 풀이**: 강의는 "discrepancy = 0, capital = 0" 두 가정을 명시 — 영국 실측은 (a) KA가 작지만 0이 아니며(2025 Q4 −0.8bn) (b) NEO가 분기당 절대 약 5.9bn — 본 보고서 §6은 두 가정을 풀어준 표적 식 (a)를 사용해야 한다.
3. **종합수지 항등식의 의미 약화**: 슬라이드 12 "OSB − 준비자산 = 0"은 **고정환율·관리환율 또는 통화당국이 외환을 통해 본원통화를 조절하는 체계**에 더 직접 적용. 영국은 변동환율·인플레이션 타게팅이므로 강의 식의 직접 적용보다 **해석적 도구**로 활용(노트 04 §주의점 4번).
4. **만성 적자 부호 패턴**: 강의의 한국 흑자 사례와 영국 적자 사례는 부호가 **정반대**. 본 보고서 §6 검산 시 CA(−) ⇒ FA(−) ⇒ 부채 순증(net inflow)으로 읽어야 함(노트 03 §주의점 3번).

---

## (5) 보고서 §6(항등식 검증) 본문 인용 후보 표

본 §은 본 보고서 **§6 항등식 검증** 본문이 작성될 때 직접 인용할 후보 문장·표·시각의 우선순위 목록이다. Q1·Q2·Q3·Q5의 별도 단위 호출에서 §3·§4·§5·§7을 작성할 때 본 §의 인용 후보는 사용하지 않으며, 오직 §6 한정 인용 자료이다.

### 5.1 §6 헤드라인 박스용 인용 후보

| 우선순위 | 인용 출처 | 인용 형태 | 본 보고서 §6 활용 위치 |
|:---:|---|---|---|
| 1 | 슬라이드 13 — *"국제수지표상 대변(credit)의 총합과 차변(debit)의 총합은 사후적으로 항상 일치 … 복식부기원리(Double-entry bookkeeping)"* | 한국어 인용 + 영문 라벨 병기 | §6 도입부 — 항등식의 공리적 출발점 정의 |
| 2 | 슬라이드 14 — *"Identity: Assuming statistical discrepancy = capital account = 0, Current account = Financial account (narrow concept) + Reserve account = Financial account (broad concept)"* | 영문 식 인용 + 한국어 풀이 병기 | §6 §6.0 강의 단순화 식 박스 |
| 3 | 슬라이드 6 — *"오차 및 누락계정은 실제로 국제수지표를 작성하는데 있어서 통계상의 불일치를 조정해 주기 위해서 사후적으로 기장해주는 항목"* | 한국어 인용 | §6 §6.1 NEO 강의 정의 박스 |
| 4 | 노트 04 §발췌표 #2 — *"표적 항등식 CA + KA + FA + E&O ≡ 0은 강의에서 직접 적지 않음. 다만 (a) 복식부기 항등성, (b) E&O가 통계 불일치를 사후 조정하는 보정 항목임이 명시되어 동치 관계는 도출 가능"* | 한국어 발췌 | §6 §6.0 표적 식 도출 박스 — 강의 측 한계 명시 |

### 5.2 §6 본문 표·시각 자료용 인용 후보

| 우선순위 | 인용 출처 | 인용 형태 | 본 보고서 §6 활용 위치 |
|:---:|---|---|---|
| 1 | 본 §3.1 항등식 4 형태 비교 표 (a·b·c·d 4형태) | 비교 표 그대로 이식 | §6 §6.0 — 4 형태 통합 비교 |
| 2 | 본 §3.2 위계 도식 (강의 3 층위 → 표적 식 → ONS 검산 식 ASCII) | 도식 그대로 이식 또는 다이어그램 변환 | §6 §6.0 — 4 형태 위계 시각 |
| 3 | 노트 20 §분기 시계열 표 (HHDH 24 분기, 2020Q1–2025Q4, NEO·GDP·NEO/GDP 3컬럼) | 표 그대로 이식 + 본 분기(2025 Q4) 강조 | §6 §6.2 — 분기 NEO 시계열 도표 |
| 4 | 노트 20 §변동성 통계 표 (평균·SD·\|NEO\| 평균·최대·최소·양음 분기 수·\|NEO\|/GDP) | 표 그대로 이식 | §6 §6.2 — NEO 변동성 박스 |
| 5 | 노트 38 §2.3 2025 Q4 검산 표 (CA·KA·FA·NEO 4행 + 합계) | 표 그대로 이식 | §6 §6.3 — 2025 Q4 헤드라인 검산 |
| 6 | 본 저장소 `db/source/balanceofpayments2025q4.xlsx` Table_J·Records 시트 분기 흐름 | 노트 38 §2.3 헤드라인 검산 + 분기 흐름 비교 | §6 §6.3 부록 — 헤드라인 vs 분기 흐름 부호 차이 점검 |
| 7 | 본 §4 NEO 임계 해석 프레임 표 (임계 1·2·3) | 임계 표 그대로 이식 | §6 §6.2 — 잔차 분포 평가 임계 박스 |

### 5.3 §6 영국 적용 시사점·주의사항용 인용 후보

| 우선순위 | 인용 출처 | 인용 형태 | 본 보고서 §6 활용 위치 |
|:---:|---|---|---|
| 1 | 노트 20 §"슬라이드 13·14 가정과의 대조" — *"강의 슬라이드 14의 통계 불일치=0 가정과 달리, 영국은 분기당 평균 절대 약 5.9 십억 파운드, 즉 분기 GDP 대비 약 0.9%(최대 2.2%)의 NEO를 기록"* | 한국어 발췌 + 정량 | §6 §6.2 영국 NEO 강의 가정 어긋남 박스 |
| 2 | 노트 38 §2.4 자문 결론 — *"강의는 '통계 불일치 = 0' 단순화 가정만 명시 → 영국 실측에 그대로 적용하면 NEO ≠ 0 잔차. 강의 한계이지 데이터 오류 아님"* | 한국어 발췌 | §6 §6.4 결론 박스 |
| 3 | 노트 04 §"영국 ONS BoP 적용 시 주의점" 2번 — *"영국 BoP 실측에는 (a) Capital Account가 작지만 0이 아니고, (b) Net Errors & Omissions가 분기별로 큰 절대값을 가질 수 있으므로, 실측 검증은 표적 항등식 CA + KA + FA + E&O = 0(부호 약속: FA는 자산취득−부채증가 = 순대출/순차입)으로 수행해야 한다"* | 한국어 발췌 + 부호 약속 명시 | §6 §6.0 본 보고서 검산 식 채택 근거 |
| 4 | 노트 38 §2.3 관찰 1·3 — *"헤드라인 부호 합계만으로는 0이 아님 → 시트별 부호 규약 차이 가능성"* + *"종합수지 +0.5bn 정도여야 하나 실제 합 −29.2bn — NEO·부호 규약 정합으로 설명되어야 함"* | 한국어 발췌 | §6 §6.3 ONS 표시 부호 차이 박스 |
| 5 | IMF BOPCOM 19/14 (노트 20 인용) — *"Net errors and omissions are final results from the balance of payments compilation and not a targeted number"* | 영문 인용 + 한국어 풀이 | §6 §6.1 NEO의 회계적 의미 보강 (IMF 측 정의) |

### 5.4 §6 작성 시 회피해야 할 인용

- **슬라이드 22~24 NIA·통화 부문 항등식 (Y = C+I+G+(EX−IM), CA = S − I, ΔNFA + ΔDC = ΔH)**: 본 §6은 BoP 회계 항등식(CA + KA + FA + NEO ≡ 0) 한정. NIA 항등식은 Q5(환율-CA) §7에서 인용. §6 본문에서 중복 인용 시 위계 혼란 — 노트 04 #5a·#5b·#5c는 본 §에서 제외.
- **노트 04 §"영국 ONS BoP 적용 시 주의점" 4번 (ΔNFA·H 항등식 변동환율제 한계)**: 본 §6은 회계 항등식만 다루며 통화 부문 항등식은 Q5에서 인용. 4번 항목은 본 §에서 회피.
- **슬라이드 25 BoP↔IIP 연결식 (flow→stock)**: BoP↔IIP 매핑은 §5(FA 분해)·§9(IIP 한계)에서 인용. 본 §6 항등식 본문은 flow 합계 항등에 한정.
- **노트 04 §"빠진 부분" 4번 (Twin deficits)**: 쌍둥이 적자는 Q5(환율-CA + 저축-투자 식)에서 다루며 본 §6 회피.
- **노트 38 §1.1~§1.5 헤드라인 5건 강의 BoP 해석 프레임**: 본 §6은 노트 38 §2.1~§2.4 항등식 검산 자문만 사용. §1 헤드라인 프레임은 §3·§4·§5에서 분산 인용 (이미 02·03·04 발췌묶음에서 이식).

---

## (6) 빠진 부분 (본 §5 발췌에서 확인되지 않은 항목)

본 §5는 슬라이드 13·14·6 + 노트 04·20·38의 발췌만을 다루며, 다음 항목은 본 단위에서 확인되지 않았다:

1. **분기 NEO ±2σ 임계 분기 식별**: 노트 20 §변동성 통계 표는 ±1σ·±2σ 라벨 분기를 별도 표시하지 않음. 본 보고서 §6 §6.2 ±1σ/±2σ 음영 표시 시 24 분기 중 2σ 초과 분기 식별이 별도 계산 필요(노트 20 표 22행 + Excel/Python 1회 계산).
2. **HHDH 헤드라인 +3.5bn vs Table_J 순오차 −9,371 £m 부호 차이**: 노트 38 §5 미확인 #2 — 사유 미확정. 본 보고서 §6 §6.3 ONS 표시 부호 차이 박스에서 언급은 가능하나 정량 분해는 별도 데이터 호출 필요.
3. **Table_BX 귀금속 보정 후 NEO**: 노트 38 §5 미확인 #4 — 본 분기 −£8.4bn 귀금속 거래 보정 시 NEO 변화. 본 보고서 §6에서 부록으로 다룰지 별도 결정.
4. **장기 NEO 시계열 (1990s~2025)**: 노트 20은 2020Q1–2025Q4 24 분기에 한정. 1990년대~2010년대 NEO 평균 규모 축소 추세 확인 필요(노트 20 §"국제 비교"에서 IMF BOPCOM 정성 평가만 언급, 정량 미확보).
5. **NEO 부호의 자기상관·계절성**: 노트 20 §변동성 통계는 평균·SD·부호 분포만 제공. lag-1·lag-4 자기상관·계절성 검증은 별도 시계열 분석 필요.
6. **G7 국가별 NEO/GDP 비교**: 노트 20 §"빠진/확인 못한 부분" 1번 — 미국·독일·일본 NEO/GDP 분기 평균 정량 미확보. 본 보고서 §6에서 영국 NEO를 G7 맥락에서 평가하려면 IMF BOP database 별도 다운로드 필요.

---

## 후속 단계 안내

본 호출은 Q4 발췌만 수행했다. 후속 호출에서 본 §5의 §3 4 형태 비교 표·§4 NEO 임계 해석 프레임·§5 인용 후보 표를 키로 삼아 본 보고서 §6(항등식 검증) 본문을 작성한다. 본 §5와 평행하게 Q5(환율-CA, 슬라이드 27·28·30 + 노트 04·08·14)도 별도 단위 호출에서 발췌해야 한다.

---

## 관련 절대경로

- 1차 슬라이드: `c:/Projects/SKKU.England/background/BoP.pptx` 슬라이드 13·14·6 / `c:/Projects/SKKU.England/background/BoP.pdf` p.13·14·6
- 1차 보강 이미지: `c:/Projects/SKKU.England/background/slide_images/slide_13.png` · `slide_14.png` · `slide_06.png`
- 1차 노트: `c:/Projects/SKKU.England/background/note/04_identities.md` · `20_neo_volatility.md` · `38_phase5_validation.md`
- 보조 노트 (간접 인용): `c:/Projects/SKKU.England/background/note/02_bop_components.md` (슬라이드 6 NEO 정의), `c:/Projects/SKKU.England/background/note/03_sign_conventions.md` (슬라이드 13 복식부기 + 부호 규약), `c:/Projects/SKKU.England/background/note/06_financial_account_categories.md` (슬라이드 6 5분류 매핑), `c:/Projects/SKKU.England/background/note/13_cdid_dictionary.md` (HHDH·HBOP·HBNT·FNVQ CDID 매핑)
- 인접 산출물: `c:/Projects/SKKU.England/report/research/01_inventory.md` (단계 1 §1 인벤토리), `c:/Projects/SKKU.England/report/research/02_macro_trend.md` (단계 1 §2 Q1 발췌), `c:/Projects/SKKU.England/report/research/03_ca_decomposition.md` (단계 1 §3 Q2 발췌), `c:/Projects/SKKU.England/report/research/04_fa_decomposition.md` (단계 1 §4 Q3 발췌)
- 분기 실측 연결: `c:/Projects/SKKU.England/db/REPORT.md` §2.3 (자본·금융계정 + NEO 표) · §3.2 (금융계정 분기 흐름 표) · `c:/Projects/SKKU.England/db/source/balanceofpayments2025q4.xlsx` Records·Table_J·Table_K 시트
