# 한국어 용어집 초안 (background-search 7회차)

본 문서는 `db/CHECKLIST.md` §0.2 일곱 번째 항목의 산출물로, 01~06 메모를 종합해 Phase 3 명세서 작업의 1차 근거로 사용할 한국어 용어집을 작성한 결과이다.

## 요약

- 총 **62개 표제어** 추출, 6개 메모 전반에서 통합.
- 분야 분포: BoP_구성 8 / 금융계정 8 / IIP 7 / 항등식 9 / 부호규약 7 / NIA 7 / 모형 6 / ONS특화 6 / 메타 4.
- 가장 많이 인용된 슬라이드: **slide 14**(7회, 항등식 핵심)·**slide 8**(6회, 부호 규약 변경)·**slide 25**(5회, BoP↔IIP).
- 강의 자료 미수록 항목은 **15개** (BPM6 표준·ONS 특화 보강 필요), Phase 3에서 우선 보강.
- 정의는 슬라이드 원문을 한국어로 다듬되, 외부 표준 보강 항목은 "(강의 자료 미수록, 외부 매뉴얼 표준)"으로 표시.

---

## BoP_구성

| 표제어(한국어) | 영문 | 약어 | 정의 | 인접 표제어 | 1차 근거 |
|---|---|---|---|---|---|
| 국제수지표 | Balance of Payments | BoP | 일정 기간 거주자–비거주자 간 모든 경제거래를 복식부기로 기록한 flow 통계. 경상·자본·금융 3대 축으로 구성. | IIP, 복식부기 | 02 §발췌표; slide 4–7 |
| 경상수지 | Current Account | CA | 상품·서비스·1차소득·2차소득 4개 하위 합계. 흑자=생산>지출, 적자=생산<지출. | 상품수지, 1차소득 | 02; slide 5, 10, 14 |
| 상품수지 | Balance of Goods | — | 재화 수출입의 순액(net trade in merchandise goods). 슬라이드 21에서 무역수지와 별도로 표시. | 무역수지, 서비스수지 | 02; slide 5, 21 |
| 무역수지 | Balance of Trade | — | 강의 자료는 차트로만 제시; 통상 상품+서비스 합산 의미로 사용(강의 자료 미수록, 외부 매뉴얼 표준). | 상품수지 | 02 §빠진 부분; slide 21 |
| 서비스수지 | Balance on Services | — | 운수·여행·로열티 등 서비스 수출입의 순액. EBOPS 12분류는 강의 자료 미수록. | 상품수지 | 02; slide 5, 9 |
| 1차소득수지(본원소득수지) | Primary Income / Investment Income Balance | — | 노동·자본 등 생산요소 제공의 **대가성** 소득(임금송금·배당·이자) 순액. IIP 잔액에서 발생하는 수익 흐름과 연결. | 2차소득, IIP | 02; slide 5, 9, 25 |
| 2차소득수지(이전소득수지) | Secondary Income / Net Unilateral Transfers | — | 원조·국제기구출연금 등 **대가 없는(무상) 이전**의 순액. 1차소득과 대칭. | 1차소득 | 02; slide 5, 9, 14 |
| 자본계정(자본수지) | Capital Account | KA | 비생산·비금융자산 취득 처분, 채무면제·이민·투자보조금 등. 매우 작아 항등식에서 통상 0 가정. | 금융계정, E&O | 02; slide 5, 7, 14 |

## 금융계정

| 표제어 | 영문 | 약어 | 정의 | 인접 표제어 | 1차 근거 |
|---|---|---|---|---|---|
| 금융계정(금융수지) | Financial Account | FA | 자산·부채 소유권 변동 거래. 5분류로 세분. **광의 FA** = 비준비 FA + 준비자산. | 직접투자, 준비자산 | 06; slide 6, 14 |
| 직접투자 | Direct Investment | DI | 외국기업 **경영참가** 목적 자본투입. 의결권 10% 임계치는 강의 자료 미수록(BPM6 표준). | 증권투자 | 06; slide 6 |
| 증권투자 | Portfolio Investment | PI | 가치증가(수익) 목적 투자, 주식·채권 양분. 경영관여 없음. | 직접투자, 파생상품 | 06; slide 6 |
| 파생금융상품 | Financial Derivatives | — | 옵션·선물·스왑 등 기초자산 연동 계약 거래. 슬라이드 14에서 `Net financial derivatives` 순액 표기. | 기타투자 | 06; slide 6, 14 |
| 기타투자 | Other Investment | OI | 대출·차입·무역신용·현금·예금. 잔여(residual) 분류. 보험·연금·SDR 배분은 강의 자료 미수록. | 직접·증권·파생·준비자산 | 06; slide 6 |
| 준비자산증감 | Changes in Reserve Assets / International Reserves | IR | 통화당국이 보유하는 대외지급준비자산(화폐용 금·SDR·IMF포지션·외화자산)의 증감. 외환시장 개입·BoP 불균형 조정용. | 종합수지, 광의 FA | 06; slide 6, 12 |
| 자산취득 | Net Acquisition of Foreign Financial Assets | NAFA | 자국이 외국 금융자산을 순취득한 액수. BPM6 부호: 증가 = (+). | 부채발생, NIL | 03; slide 14 |
| 부채발생 | Net Incurrence of Liabilities | NIL | 외국이 자국 부채를 순취득한 액수. BPM6 부호: 증가 = (+). | NAFA | 03; slide 14 |

## 항등식

| 표제어 | 영문 | 약어 | 정의 | 인접 표제어 | 1차 근거 |
|---|---|---|---|---|---|
| 복식부기 | Double-entry Bookkeeping | — | 모든 거래를 차변·대변에 동시 한 번씩 기재. 사후적으로 전 계정 합 ≡ 0. | 대변, 차변 | 03; slide 13 |
| 대변(크레딧) | Credit | Cr | 외국→자국 자금 유입 거래(+). 수출·소득 유입·부채 증가 등. | 차변 | 03; slide 13 |
| 차변(데빗) | Debit | Dr | 자국→외국 자금 유출 거래(−). 수입·소득 지급·자산 증가 등. | 대변 | 03; slide 13 |
| 사후 항등성 | Ex-post Identity | — | 전 계정(경상+자본+금융) 합은 사후 항상 일치. 부분합(예: CA)만 보면 불균형 발생. | 복식부기 | 03; slide 13 |
| BoP 핵심 항등식(축약) | CA = FA(narrow) + Reserve = FA(broad) | — | E&O = KA = 0 가정 시. 광의 FA 개념 정의 포함. | OSB, E&O | 04; slide 14 |
| 표적 BoP 항등식 | CA + KA + FA + E&O ≡ 0 | — | 강의 슬라이드에 명시 식 없음. 슬라이드 13(복식부기) + 14 + 6(E&O 정의) 결합으로 도출(강의 자료 미수록, 외부 매뉴얼 표준). | E&O | 04 §발췌표 #2 |
| 종합수지(공적결제수지) | Official Settlements Balance | OSB | OSB = CA + KA + 비준비 FA. **OSB − 준비자산증감 = 0** ⇒ OSB = Reserve account. | 준비자산 | 03, 04; slide 12, 14 |
| 오차 및 누락 | Net Errors and Omissions | E&O | 통계 불일치 사후 조정 항목. 영국 ONS는 분기별 변동 큼. | 통계불일치 | 04; slide 6, 13 |
| 통계 불일치 | Statistical Discrepancy | — | E&O와 동의어로 강의 사용. 슬라이드 14 항등식에서 0 가정. | E&O | 04; slide 14 |

## 부호규약

| 표제어 | 영문 | 약어 | 정의 | 인접 표제어 | 1차 근거 |
|---|---|---|---|---|---|
| BPM5 | IMF BoP Manual 5th ed. | BPM5 | 과거 매뉴얼: 금융계정을 **순유출입액 기준**으로 표기. 자산 항목 부호가 BPM6와 반대. | BPM6 | 03; slide 8 |
| BPM6 | IMF BoP Manual 6th ed. | BPM6 | 현행 매뉴얼: 금융계정을 **자산·부채 증감 기준**으로 표기. 자산↑ = (+), 부채↑ = (+). | BPM5 | 03; slide 8 |
| 자산·부채 증감 기준 | Assets/Liabilities Change Basis | — | BPM6 부호 규약. 자국의 대외자산 취득 = +, 외국의 자국 부채 취득 = +. | NAFA, NIL | 03; slide 8 |
| 순유출입 기준 | Net In/Outflow Basis | — | BPM5 부호 규약. 자본 유출 = −, 유입 = +. 강의 슬라이드 9의 "이전 매뉴얼" 표 기준. | BPM5 | 03; slide 8 |
| 거주자/비거주자 | Resident / Non-resident | — | 강의 자료 미수록(외부 매뉴얼 표준). BoP 거래 주체 구분 기준(주된 경제이익 중심지). | — | 03 §빠진 부분 |
| 흑자/적자(부분합) | Surplus / Deficit | — | 경상수지 + = 생산>지출(순수출), − = 생산<지출(순수입). 부분합 차원에서만 정의. | CA, OSB | 03; slide 10 |
| 분개 예시 | Journal Entry Example | — | 강의 자료 미수록(외부 매뉴얼 표준). 예: 상품 수출 시 상품수지 Cr + 대외자산 Dr. | 복식부기 | 03 §빠진 부분 |

## IIP

| 표제어 | 영문 | 약어 | 정의 | 인접 표제어 | 1차 근거 |
|---|---|---|---|---|---|
| 국제투자대조표 | International Investment Position | IIP | 특정 시점(예: 분기말)의 대외투자 잔액 + 외국인의 자국 투자 잔액 표. **stock 통계**. | BoP, NFA | 05; slide 25 |
| 잔액(스톡) | Stock | — | 특정 시점의 누적 보유량(자산·부채·준비자산). | 흐름(플로우) | 05; slide 4 |
| 흐름(플로우) | Flow | — | 일정 기간의 거래량·변화량(수출입·수지·잔액 변화). 순(net) 개념. | 잔액 | 05; slide 4 |
| 순대외자산 | Net External Assets / Net Foreign Assets | NFA | 대외자산 − 대외부채. 비준비 FA 흑자 ⇒ NFA 증가. (X−IM) = ΔNFA(슬라이드 24). | Net IIP | 05; slide 11, 24 |
| 순국제투자포지션 | Net IIP | — | IIP 차원의 NFA 동의어. = 총자산 − 총부채. 영국은 만성적 음(-). | NFA, 재평가 | 05; ONS 매핑표 |
| 거래요인 | Transaction Component | — | ΔIIP 중 BoP 거래에서 발생한 부분. = FA + 준비자산증감. | 비거래요인 | 05; slide 25 |
| 비거래요인 | Non-transaction Component | — | ΔIIP 중 가격·환율 재평가, 기타조정 등 거래 외 요인. 영국 분기 변동의 주요인. | 거래요인, 재평가 | 05; slide 25 |

## NIA

| 표제어 | 영문 | 약어 | 정의 | 인접 표제어 | 1차 근거 |
|---|---|---|---|---|---|
| 국민소득항등식 | National Income Identity | — | Y = C + I + G + (EX − IM). 개방경제 GDP 분해. | 흡수, CA | 02, 04; slide 22 |
| 흡수 | Absorption | A | A = C + I + G(국내 총지출). Y − A = EX − IM = CA. | 흡수접근법 | 04; slide 22, 29 |
| 저축-투자 항등식 | Saving-Investment Identity | — | CA = S − I = S_private + S_public − I. 경상수지를 거시 자금조달 관점에서 분해. | 쌍둥이 적자 | 04; slide 23 |
| 쌍둥이 적자 | Twin Deficits | — | 재정적자 + 경상수지 적자 동시 발생. 일본·미국 사례 언급(수치는 미제시). | S − I | 04; slide 23 |
| 본원통화 항등식 | Monetary Base Identity | — | NFA + DC = H, ΔNFA + ΔDC = ΔH. 통화당국 대차대조표를 통한 BoP–통화 연결. | NFA, DC, H | 04; slide 24 |
| 국내여신 | Domestic Credit | DC | 통화당국의 국내 부문에 대한 신용. 본원통화 = NFA + DC. | H, NFA | 04; slide 24 |
| 본원통화 | High-powered Money / Monetary Base | H | 통화당국 부채 측면 본원통화. ΔH = ΔNFA + ΔDC. | DC, NFA | 04; slide 24 |

## 모형

| 표제어 | 영문 | 약어 | 정의 | 인접 표제어 | 1차 근거 |
|---|---|---|---|---|---|
| 흡수 접근법 | Absorption Approach | — | X − M = Y − A. 경상수지 = 소득과 흡수의 차. | NIA | 04; slide 22, 29 |
| 탄력성 접근법 | Elasticity Approach | — | TB = X − E·M. 환율 변동이 무역수지에 미치는 영향을 수출·수입 탄력성으로 분석. | 마샬-러너 | 04; slide 27 |
| 마샬-러너 조건 | Marshall-Lerner Condition | M-L | eX + eM > 1. 자국통화 평가절하가 무역수지를 개선하기 위한 탄력성 조건. | 탄력성 접근법 | 04; slide 27 |
| J-커브 효과 | J-curve | — | 평가절하 직후 무역수지가 일시 악화 후 개선되는 시계열 패턴(강의 자료 도식 위주, 슬라이드 텍스트 미수록). | 탄력성 접근법 | 01; slide 28(추정) |
| 환율 전가 | Exchange Rate Pass-through | — | 환율 변동이 수입·수출 가격에 반영되는 정도(강의 자료 도식 위주). | 탄력성 접근법 | 01; slide 28(추정) |
| 포트폴리오 접근법 | Portfolio Approach | — | 자본자산 선택 관점에서 BoP·환율 결정 설명(강의 자료 §3 후반, 슬라이드 텍스트 미추출). | 흡수·탄력성 | 01; slide 30–31(추정) |

## ONS특화

| 표제어 | 영문 | 약어 | 정의 | 인접 표제어 | 1차 근거 |
|---|---|---|---|---|---|
| CDID | Code for Data Identification | CDID | ONS 시리즈 식별 4자리 코드(강의 자료 미수록, ONS 표준). | Pink Book | 01 §빠진 부분; ONS |
| Pink Book | UK Balance of Payments — The Pink Book | — | ONS의 연간 종합 BoP·IIP 보고서(강의 자료 미수록, ONS 표준). | CDID | 06; ONS |
| Table D1_3 | Direct Investment | — | ONS BoP 직접투자(자산·부채, 지분·부채성 거래). 강의 ①과 매핑. | 직접투자 | 06; 05 §매핑표 |
| Table D4_6 | Portfolio Investment | — | ONS BoP 증권투자(지분·부채증권, 만기·발행자별). 강의 ②와 매핑. | 증권투자 | 06; 05 §매핑표 |
| Table D7_9 | Other Investment + Derivatives | — | ONS BoP 기타투자·파생상품 묶음. 강의 ③·④가 합쳐진 형태. | 기타투자, 파생 | 06; 05 §매핑표 |
| Table K | Reserve Assets / Net IIP | — | ONS 준비자산 + Net IIP 잔액. 강의 ⑤와 매핑. | 준비자산, Net IIP | 06; 05 §매핑표 |

## 메타

| 표제어 | 영문 | 약어 | 정의 | 인접 표제어 | 1차 근거 |
|---|---|---|---|---|---|
| 단위(파운드 백만) | GBP million | — | 영국 BoP 표준 단위. 강의 한국 예시는 USD million → 환산·표기 차이 주의. | — | 02 §빠진 부분 |
| 결측 표기 | Missing Code (`..`, `-`, 공란) | — | ONS 원본의 의미 다름(임시·해당없음·공란). 임의 NA·0 치환 금지(`db/CLAUDE.md`). | — | db 규칙 |
| 개정(리비전) | Revision | — | ONS 분기별 사후 개정. 항등식 잔차에 영향(강의 자료 미수록, ONS 표준). | E&O | 03 §주의점 4 |
| 귀금속 보정 | Non-monetary Gold Adjustment | — | 비통화용 금 거래 별도 보정(강의 자료 미수록, ONS 표준). | 상품수지 | — |

---

## 미정의·우선순위 (Phase 3 보강 대상)

| 우선순위 | 표제어 | 사유 | 보강 출처 후보 |
|---|---|---|---|
| 高 | 표적 항등식 `CA+KA+FA+E&O≡0` | 슬라이드 명시 식 없음. 실측 검증 필수 | IMF BPM6 §2 |
| 高 | 직접투자 10% 임계치 | 강의 정의에 없음 | OECD BD4 |
| 高 | 거주자/비거주자 | 부호 규약 전제 | BPM6 §4 |
| 高 | 분개 예시 | 학생 학습용 필수 | BPM6 §3 |
| 高 | 무역수지 정의 | 슬라이드 21 차트만 있음 | ONS Pink Book |
| 中 | 자산·부채 양면 분류 | 5분류 각각의 자산/부채 | BPM6 §6 |
| 中 | 재평가 3분해(가격·환율·기타) | 비거래요인 세부 | BPM6 §9 |
| 中 | EBOPS 12분류 | 서비스수지 세부 | MSITS 2010 |
| 中 | 중앙은행 NFA vs Net IIP | 슬라이드 11·24 모호 | BoE FSR |
| 中 | CDID·Pink Book 표 식별 규칙 | ONS 표준 | ONS 가이드 |
| 中 | J-curve / 환율 전가 / 포트폴리오 접근법 정의 | 빈 슬라이드 15–20·26–27·30–31 도식만 | 외부 교과서 |
| 低 | 결측 표기·개정·귀금속 보정 | ONS 운영 규칙 | ONS Methodology |
| 低 | 파생상품 ESO·순포지션 규칙 | 강의 자료 축약 | BPM6 §7 |
| 低 | 기타투자 보험·연금·SDR 배분 | 강의 자료 부분 누락 | BPM6 §8 |
| 低 | 영국 변동환율·인플레이션 타게팅 맥락 | NIA 항등식 적용 한계 | BoE 정책보고서 |

---

## Phase 3 활용 가이드

1. **명세서 정의 컬럼**에 본 용어집의 "정의" 열을 그대로 인용하되, 출처 표기는 `[07_glossary §<분류>]` + 슬라이드 번호 병기.
2. **ONS 표 매핑** 작업(`Table_D1_3` 등) 시, ONS특화 섹션을 1차 인덱스로 사용하고 금융계정 5분류 정의와 교차 검증.
3. **부호 검증** 자동화 절차에서 BPM6 = "자산↑·부채↑ 모두 +" 규칙을 상수로 고정. BPM5 표기와 혼용 금지.
4. **항등식 잔차 표** 생성 시 표적 항등식(미정의 표제어 1번)을 정식 식으로 채택하고, 슬라이드 14의 단순화 가정과 차이를 REPORT.md 각주에 명시.
5. **미정의 우선순위 高 5개**(표적 항등식·10% 임계치·거주자·분개·무역수지)를 Phase 3 첫 스프린트 보강 대상으로 우선 처리; 외부 보강은 `web-search` 서브에이전트로 위임.
6. **인접 표제어** 컬럼을 활용해 명세서 컬럼 분류표와 용어집을 양방향 링크(예: 명세서 셀에 `→ 07_glossary#NFA`).

## 관련 절대경로

- 1차 근거: `background/note/01_inventory.md` ~ `06_financial_account_categories.md`, `background/BoP.pptx`, `background/BoP.pdf`
