# 슬라이드 28(J-curve) · 29(흡수 접근법) 멀티모달 분석 (background-search 14회차)

본 문서는 `db/CHECKLIST.md` §0.2 신규 高 3번 항목(슬라이드 28·29 멀티모달 분석을 8회차 누락분으로 보강)의 산출물이다. `background/slide_images/slide_28.png`, `slide_29.png`를 직접 시각 분석한 결과를 정리한다.

## 슬라이드 28 — J-curve & 환율 전가(Exchange Rate Pass-through)

### 본문 발췌

> **J-curve**: 외국화폐에 대한 자국화폐가 평가절하(depreciation)된 이후 예상과 달리 무역수지 흑자가 오히려 줄어들다가 상당한 시간이 지나서야 늘기 시작하는 현상
>
> - 참고: Price of import goods in $ (E) increases but the quantity of import goods (M) demanded changes little in the short run, so the total import payments (E×M) actually increase. Slow adjustment of quantity compared to the price changes.
>
> 실증분석 결과 시차가 지나도 탄력성으로 설명할 수 없는 무역수지의 불균형이 존재
>
> - 이는 환율의 불완전한 전가(incomplete exchange rate pass-through)로 해석가능
>
> (the pass-through of devaluation on prices of import goods is incomplete because of changes in profit margins)
>
> 환율의 완전한 전가(100% pass-through of exchange rate): the change in exchange rate is fully reflected in the price changes.
>
> **Exchange rate → Price → Demand → Trade Balance**
>           (pass-through)  (elasticities)

### 핵심 정리

| 개념 | 한국어 풀이 | 영문 |
|---|---|---|
| **J-curve** | 자국통화 평가절하 직후 무역수지가 일시 악화 → 시간 경과 후 개선되는 J자형 시계열 패턴 | J-curve effect |
| **단기 비탄력성** | 단기에는 수입 물량(M)이 가격(E) 변화에 거의 반응하지 않아 총 수입지출(E·M)이 오히려 증가 | Slow quantity adjustment |
| **불완전 전가** | 환율 변화가 수입 가격에 전부 반영되지 않는 현상 (마진 흡수) | Incomplete pass-through |
| **완전 전가** | 환율 변화가 100% 가격에 반영됨 | 100% pass-through |
| **인과 사슬** | 환율 변화 → (전가율) → 가격 변화 → (탄력성) → 수요 변화 → 무역수지 변화 | Exchange rate → Price → Demand → Trade Balance |

### 모형 구조

슬라이드 28은 탄력성 접근법(슬라이드 27)의 **시간 차원 확장**이다.

- **단기**: pass-through·탄력성 모두 작음 → 평가절하가 무역수지 악화로 나타남.
- **중기**: pass-through 진행, 탄력성도 증가 → 마샬-러너 조건(eX + eM > 1) 충족 시 무역수지 개선.
- **장기**: 완전 전가 + 충분한 탄력성 → 평가절하 효과 발현.

J-curve의 "J"는 시간(가로)·무역수지(세로) 평면에서 나타나는 곡선의 시각적 형태.

### 영국 ONS BoP 적용 시 함의

- 영국은 변동환율제이며 파운드 약세 국면(예: 2016 Brexit, 2022 미니예산 사태)에서 J-curve 검증 가능.
- 영국 수입 가격의 pass-through는 통상 60~70% 수준(BoE Working Papers)이라는 외부 자료로 보강 가능 — 본 강의 슬라이드는 정량값을 제시하지 않음.
- 본 저장소의 BoP 데이터(상품무역 시계열)와 ONS 환율 시계열(BoE effective exchange rate)을 결합하면 J-curve 실증 분석 가능.

## 슬라이드 29 — 흡수 접근법(Absorption Approach)

### 본문 발췌

> **2) 흡수 접근법(Absorption approach)**
>
> - 경제전체의 총소득과 총지출의 격차가 국제수지 불균형을 야기하는 근본적인 요인
>
> X − M = Y − (C + I + G) = Y − A, where A is absorption=total domestic spending
>
> - 즉 소득보다도 지출이 크면 수입의 증가로 인해 국제수지 적자가 유발되는 반면, 소득이 지출보다 큰 경우에는 국제수지 흑자가 나타남.
> - 따라서 평가절하 후 소득의 증가가 지출의 증가보다 크면 국제수지가 개선됨
>
> 이 접근방법은 국민경제 전체의 지출규모(즉 흡수의 크기)를 조정하여 국제수지의 불균형을 극복할 수 있다고 봄
>
> - 국제수지 적자를 극복하기 위해서는 소득을 늘리거나 흡수를 줄어야 함
> - 그러나 단기적으로 소득을 늘린다는 것은 어려우므로 흡수를 줄이는 것이 전략적 관점
> - 대부분의 정책이 일국의 지출규모를 줄이는 방향으로 진행되므로 흡수가 핵심적 역할을 함

### 핵심 정리

| 개념 | 한국어 풀이 | 식·영문 |
|---|---|---|
| **흡수(A)** | 한 국가의 국내 총지출 = 소비 + 투자 + 정부지출 | A = C + I + G |
| **흡수 항등식** | 무역수지 = 소득 − 흡수 | X − M = Y − A |
| **적자의 의미** | Y < A이면 흡수가 소득을 초과해 부족분을 수입으로 충당 → 무역수지 적자 | Trade deficit ⇔ Y < A |
| **흑자의 의미** | Y > A이면 잉여 생산이 수출로 흘러감 → 무역수지 흑자 | Trade surplus ⇔ Y > A |
| **평가절하 효과 조건** | 평가절하 후 소득 증가폭 > 흡수 증가폭이어야 무역수지 개선 | ΔY > ΔA |
| **정책 함의** | 단기에 소득 증대는 어려우므로 흡수 감축이 핵심 정책 도구 | Reduce A by policy |

### 모형 구조

슬라이드 22(Y = C + I + G + (EX − IM))의 재진술을 정책 도구 관점에서 다시 본 것.

- **탄력성 접근법(슬라이드 27)**: 환율 변화 → 가격·수요 변화 → 무역수지
- **흡수 접근법(슬라이드 29)**: 평가절하 정책의 효과는 소득(Y) vs 흡수(A) 격차 변화에 의존
- **포트폴리오 접근법(슬라이드 30)**: 자산 선호 변화 → FA → CA

세 접근법은 슬라이드 31에서 통합 진술됨(환율·이자율·자산선호 채널을 통해 상호 연결).

### 영국 ONS BoP 적용 시 함의

- 영국의 만성적 경상수지 적자(GDP 대비 −2~−4%)는 흡수 접근법 관점에서 **A > Y** 상태가 구조화되어 있음을 시사.
- 영국 정부의 재정정책(G 조정), 가계 저축률(C 조정), 기업 투자(I 조정)가 모두 흡수에 영향 → 정책 분석 시 본 식의 분해가 유용.
- 본 저장소 데이터로 직접 검증 가능: `Table_A` 경상수지 + ONS GDP 시계열(외부 자료 필요) → A − Y 격차 시계열화.

## 종합 — 세 접근법 통합(슬라이드 31)에서 본 28·29의 위치

| 슬라이드 | 접근법 | 주 변수 | 영국 적용 핵심 |
|---|---|---|---|
| 27 | 탄력성 | 환율·가격·탄력성(eX, eM) | 마샬-러너 조건 점검 |
| **28** | **탄력성의 시간 확장(J-curve, pass-through)** | 환율 → 가격 → 수요(시간 축) | 파운드 약세 국면의 J-curve 실증 |
| **29** | **흡수** | 소득(Y) − 흡수(A) | 만성 CA 적자의 흡수 분해 |
| 30 | 포트폴리오 | 자산 선호 → FA → CA | 영국 자산의 외국인 매력도 |
| 31 | 통합 | 환율·이자율·자산선호 채널 | 종합 정책 시각 |

본 28·29 분석으로 `07_glossary.md`의 "J-curve"·"환율 전가(Exchange Rate Pass-through)"·"흡수 접근법" 표제어 모두 강의 자료 정의로 확정 가능. 11회차 §미해결 中순위 "J-curve / 환율 전가 정의(빈 슬라이드 28·29)" 항목 해소.

## 07_glossary.md 격상 후보

| 표제어 | 기존 분류 | 격상 근거 | 새 1차 근거 |
|---|---|---|---|
| J-curve 효과 | 中순위 미정의(빈 슬라이드 추정) | 슬라이드 28 본문 추출 성공, 단기 비탄력성·시간 차원 명시 | slide 28 |
| 환율 전가(Pass-through) | 中순위 미정의(빈 슬라이드 추정) | 슬라이드 28 본문 추출 성공, 완전·불완전 전가 정의 명시 | slide 28 |
| 흡수 접근법 (확정) | 강의 자료 인용(슬라이드 22·29 산문) | 슬라이드 29의 정책 함의(흡수 감축 우선) 및 X−M=Y−A 식 명시 | slide 22, 29 |
| 인과 사슬(환율→가격→수요→무역수지) | 신규 표제어 | 슬라이드 28에 명시적 도식 | slide 28 |

## 관련 절대경로

- 1차 근거 이미지: `background/slide_images/slide_28.png`, `slide_29.png`
- 1차 근거 PDF: `background/BoP.pdf` (페이지 28·29)
- 인접 산출물: `background/note/04_identities.md`, `07_glossary.md`, `08_multimodal_slide_analysis.md`, `11_final_review.md`
