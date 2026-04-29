# 단계 1 §4 — Q3 금융계정(Financial Account) 5 세부항목 분해 발췌 묶음

본 문서는 `report/research/01_inventory.md` (바) 표의 핵심 질문 Q3(금융계정 5 세부항목 분해 — 직접투자·증권투자·파생금융·기타투자·준비자산)에 대응하는 1차 근거를 한 곳에 모은 발췌 묶음이다. 1차 슬라이드는 `background/BoP.pptx`/`background/BoP.pdf` 페이지 6·8·17, 1차 노트는 `background/note/06_financial_account_categories.md`·`19_assets_liabilities_mapping.md`·`25_fa_categories_bpm6.md` 이며, 분기 실측 연결 시 `db/REPORT.md` §2.3·§3.2 와 `background/note/13_cdid_dictionary.md`·`19_assets_liabilities_mapping.csv` 를 보조한다. 본 호출은 Q3 발췌만 다루며, Q4(항등식 일관성)·Q5(환율-CA)는 별도 단위에서 처리한다.

## 요약 한 단락

강의 자료는 금융계정을 BPM6 표준에 따라 ① 직접투자(경영참가 동기) ② 증권투자(가치증가 목적, 주식·채권) ③ 파생금융상품(파생계약 거래) ④ 기타투자(대출·차입·무역신용·현금·예금 등 잔여) ⑤ 준비자산증감(통화당국 IR)의 5분류로 제시하고(슬라이드 6), 부호 규약은 BPM6 채택 후 "자산·부채 증감 기준"으로 변경되어 부채 부호는 종전과 동일하나 자산 부호가 반대로 뒤집혔다는 점을 강조한다(슬라이드 8). 슬라이드 17은 한국 FA 4 구성요소(준비자산 별도) 누적 막대(2000–2025, 백만 USD)로 직접·증권·기타가 주축이고 파생은 미세, 2014년 이후 양(+)전환·2024–2025 사상 최대(+12만 USD bn 근접)의 패턴을 시각화한다. 누적 노트 06은 5분류 1줄 정의를 표로 추출하고 강의 자료의 누락(10% 임계·자산-부채 양면 등)을 식별, 노트 19는 본 저장소 `balanceofpayments2025q4.xlsx`의 자산(NAFA)·부채(NIL)·순(Net) 3면 컬럼이 Table_J 부표 1/2/3, Table_D1_3/D4_6/D7_9, Table_K 에 1:1 대응함을 54행 매핑표로 정형화하며, 노트 25는 BPM6 §6.8~§6.81 + OECD BD5(2025-03)로 5분류의 영문 정의·하위 분해·영국 ONS 자료원을 보강한다. 본 보고서 §5 (FA 분해)는 5분류 정의(슬라이드 6 + 노트 25) → 부호 규약(슬라이드 8 + 노트 03) → ONS 표시 부호(노트 13 §추출 규칙) → CDID(`-MU7M`/`-HHZD`/`-ZPNN`/`-HHYR`/`-LTCV`/`-HBNT`) 매핑 → 2025 Q4 분기 실측(`db/REPORT.md` §2.3) 의 5단 구성으로 작성한다.

---

## (1) 슬라이드 6·8·17 한국어 발췌

### (1-1) 슬라이드 6 — 금융계정 5분류 1줄 정의

`background/BoP.pptx` / `background/BoP.pdf` p.6 (PPT 텍스트 추출 정상; 도식·이미지 보강용 `slide_images/slide_06.png` 멀티모달 재확인 완료).

> 2) **금융계정(Financial account)**: 자산 및 부채의 소유권 변동과 관련된 거래
>
> - **직접투자(direct investment)**: 외국기업에 자금을 투입하여 경영에 참가하기 위해 행하는 투자
> - **증권투자(portfolio investment)**: 투자자본의 가치증가를 목적으로 한 투자로 주식과 채권으로 구분
> - **파생금융상품(derivatives)**: 파생금융상품거래를 기록
> - **기타투자(other investment)**: 대출, 차입, 무역신용, 현금 및 예금 등의 금융거래
> - **준비자산증감(changes in reserve assets)**: 통화당국(중앙은행)이 일정시점에 있어서 국제유동성 수단으로 보유하고 있는 대외지급준비자산(international reserves: IR)의 증감
>   - 대외지급준비자산에는 화폐용 Gold, SDR, IMF포지션, 외화자산 등이 포함
>   - 국제수지의 불균형을 직접 보전하거나 외환시장개입을 통해 간접적으로 불균형을 조정하기 위해 사용
>
> **오차 및 누락계정**은 실제로 국제수지표를 작성하는 데 있어서 통계상의 불일치를 조정해 주기 위해서 사후적으로 기장해주는 항목임

분해의 3축: ① 투자 동기·관여도(경영참가 vs 가치증가) → 직접/증권 구분, ② 금융상품 형식(파생계약 vs 현금·예금·대출 등) → 파생/기타 구분, ③ 보유주체(통화당국 보유 여부) → 준비자산 분리. 강의 슬라이드는 **의결권 10% 임계치를 명시하지 않으며**, 자산·부채 양면 분류·하위 항목 세분도 생략한다(노트 06 §빠진 부분 참조).

### (1-2) 슬라이드 8 — BPM6 vs BPM5 부호 규약 좌우 비교

`background/BoP.pptx` p.8 — "우리나라의 국제수지표"(원문). PPT·PDF 텍스트 추출 정상, 멀티모달 `slide_images/slide_08.png` 재확인 완료.

> **우리나라의 국제수지표**
>
> - **최근 매뉴얼 기준** (BPM6)
>   - 새로운 매뉴얼에서는 **금융계정 부호표기 방식을 '자산·부채의 증감 기준'으로 변경**
>   - 이에 따라 금융계정 **부채 항목의 부호는 종전과 동일하나 자산 항목의 부호는 반대 방향으로 바뀜**
>   - 금융계정에는 **증감만을 기록**하므로 각 숫자가 **이전과 반대 부호**로 나타남
>
> - **이전 매뉴얼 기준** (BPM5)
>   - 이전 매뉴얼에서는 금융계정 부호표기 방식을 **'순유출입액 기준'으로 함**

핵심: BPM6에서는 자산 증가(자국의 대외자산 취득) = +, 부채 증가(외국의 자국 부채 취득) = + 의 양면 부호 체계로 일원화. 결과적으로 **금융수지 표시 부호가 BPM5의 정반대**가 되며, 슬라이드 9의 한국 2017년 표가 신·구 매뉴얼 양면을 정량 비교(예: 신매뉴얼 직접투자 −14,628 / 구매뉴얼 +14,628, 백만 USD).

### (1-3) 슬라이드 17 — 한국 FA 4 구성요소 누적 막대 (Components of FA, million USD)

`background/BoP.pptx` p.17 — PPT 텍스트 셰이프 빈 페이지. 멀티모달 `slide_images/slide_17.png` (200 DPI 렌더링) 좌표축·계열·메시지 복원.

**좌표축 / 계열 / 단위**

- 제목: "Components of FA (million USD)"
- x축: 연도 2000 ~ 2025 (26년)
- y축: 백만 USD, 범위 −80,000 ~ +140,000, 그리드 20,000 단위
- 누적 막대 4 계열(범례 순):
  1. **Direct investment** (파란색)
  2. **Portfolio investment** (적색)
  3. **Financial derivatives, Net Assets** (연두색)
  4. **Other investment** (보라색)
- 준비자산은 본 슬라이드에 부재 (별도 슬라이드 18에서 단일 막대로 표기 — 노트 08 보강).

**좌표 정량 복원 (멀티모달 시각 판독)**

| 연도 | DI(파) | PI(적) | FD(연두) | OI(보) | FA 합 |
|---|---:|---:|---:|---:|---:|
| 2000 | -10,000 | +5,000 | ~0 | +10,000 | +5,000 |
| 2008 | +10,000 | +35,000 | ~0 | +10,000 | +50,000 |
| 2009 | +10,000 | -65,000 | ~0 | +5,000 | -55,000 |
| 2014 | +25,000 | +30,000 | ~0 | +20,000 | +75,000 |
| 2016 | +20,000 | +65,000 | +5,000 | +5,000 | +95,000 |
| 2021 | +45,000 | +25,000 | -5,000 | -20,000 | +45,000 |
| 2024 | +35,000 | +45,000 | +10,000 | +10,000 | +100,000 |
| 2025 | +25,000 | +90,000 | +10,000 | -5,000 | +120,000 |

(수치는 차트 그리드 격자 시각 판독 추정치, 강의 슬라이드는 정량 표가 별도 첨부되지 않음)

**메시지(시각 메타)**

- 2000–2005: FA 4 구성 합계가 0 부근에서 진동, 직접투자가 음(−)으로 외국인의 한국 직접투자 우위, 증권은 소액.
- 2006–2010: **글로벌 금융위기**. 2008 PI 큰 양(+) → 2009 PI 큰 음(−)로 급반전(약 70,000 USD bn 이상 진폭), 자본유출입 변동성 극대.
- 2011–2015: PI·DI 모두 양(+) 안정, FA 합계가 견조한 +50,000~+75,000 USD bn 자본 순유출(순대외자산 증가).
- 2016–2020: 직접투자가 +20,000~+45,000 USD bn 영구화, FA 양(+) 흐름 확립 = 한국이 만성 순대외자산국으로 굳어진 구간.
- 2021–2023: OI 음(−)전환·DI 강한 양(+)의 구성 변화, FA 합계는 +35,000~+74,000 USD bn 안정.
- 2024–2025: PI 다시 큰 양(+)로 회귀, FA 사상 최대 +100,000~+120,000 USD bn (강의 메시지: 한국 자본 순유출 가속).

**영국 적용 시 주의**: 한국은 만성 흑자·자본 순유출 = FA 양(+) 구조. **영국은 정반대로 만성 적자·자본 순유입 = FA 음(−)** 구조이므로, 슬라이드 17의 양(+) 누적 패턴을 영국 ONS Table_J 분기 실측에 그대로 옮길 수 없다. 영국 FA 5분해는 PI/OI 양면이 큰 음수·양수로 진폭 격렬, DI·FD·RA 는 상대적으로 작은 폭(`db/REPORT.md` §3.2 참조).

---

## (2) 노트 06·19·25 한국어 발췌

### (2-1) 노트 06 — 금융계정 5분류 정의 발췌표 + BPM6 매뉴얼 인용

`background/note/06_financial_account_categories.md` (1차 근거: 슬라이드 6·7·8·9·11·14)

핵심 발췌 — 분류별 진술표 (요지):

> | 분류 | 강의 자료 진술 | 한국어 풀이 | 분류 기준 |
> |---|---|---|---|
> | **직접투자** | "외국기업에 자금을 투입하여 경영에 참가하기 위해 행하는 투자" | 해외 기업의 경영의사결정에 영향을 미칠 목적의 자본투입. 단순 수익 추구가 아닌 지배·관여 동기. | 경영참가(control/influence) 목적. **의결권 % 기준은 본 슬라이드에 없음**(BPM6 통상 10% 기준은 외부 표준). |
> | **증권투자** | "투자자본의 가치증가를 목적으로 한 투자로 주식과 채권으로 구분" | 경영관여 없이 시세차익·이자·배당 등 금융수익을 노린 투자. 지분증권(주식)과 부채증권(채권)으로 양분. | 가치증가(수익 추구) 목적. 상품유형: 주식/채권. |
> | **파생금융상품** | "파생금융상품거래를 기록" | 옵션·선물·스왑 등 기초자산 가치 연동 계약의 거래·청산을 별도 항목으로 분리. | 상품의 형식(파생계약). **슬라이드 14는 `Net financial derivatives`라는 순액 표기를 사용**. |
> | **기타투자** | "대출, 차입, 무역신용, 현금 및 예금 등의 금융거래" | 직접·증권·파생·준비자산에 속하지 않는 잔여 금융거래. | 상품유형 잔여 분류(residual). 자산-부채 구분은 슬라이드에 없음. |
> | **준비자산증감** | "통화당국(중앙은행)이 ... 보유하고 있는 대외지급준비자산(IR)의 증감" / "대외지급준비자산에는 화폐용 Gold, SDR, IMF포지션, 외화자산 등이 포함" | 중앙은행이 외환시장 개입·국제수지 조정용으로 보유하는 대외지급수단. | 보유주체(통화당국) + 사용목적(국제수지 불균형 조정·외환개입). 하위: 화폐용 금, SDR, IMF reserve position, 외화자산. |

추가 맥락(노트 06 본문 발췌):
- **부호규약 변화(슬라이드 8 인용)**: "새로운 매뉴얼에서는 금융계정 부호표기 방식을 ‘자산·부채의 증감 기준’으로 변경", "부채 항목의 부호는 종전과 동일하나 자산 항목의 부호는 반대 방향으로 바뀜". → BPM6 채택 영향. 분류 기준 자체는 동일하지만 표기방식 차이.
- **순액 정의(슬라이드 14)**: `Financial account = Net acquisition of foreign financial assets − Net incurrence of liabilities + Net financial derivatives` — 자산·부채 구분이 식 차원에서만 등장.
- **광의·협의 구분(슬라이드 14)**: "Financial account in a broad sense = nonreserve FA + reserve account" → 준비자산을 제외한 협의 금융수지(narrow FA)와 포함한 광의 금융수지(broad FA)를 구분.

BPM6 표준 일치 평가표(노트 06 §):

> | 항목 | 강의 자료 | BPM6 표준 | 평가 |
> |---|---|---|---|
> | 5분류 체계 | 직접·증권·파생·기타·준비자산 | 동일 | 일치 |
> | 직접투자 정의 동기 | "경영참가" | "lasting interest, significant degree of influence" | 일치(개념) |
> | 직접투자 임계치 | 명시 없음 | 의결권 **10% 이상** | **강의 자료 누락** |
> | 증권투자 정의 | "가치증가 목적, 주식·채권" | 10% 미만 지분 + 부채증권 | 일치(임계치 누락) |
> | 부호 규약 | 자산·부채 증감 기준 | 동일 | 일치(BPM6 채택) |
> | 자산·부채 양면 표시 | 식(슬라이드 14)에서만 | 모든 분류에서 양면 분리 | **강의 자료 축약** |


### (2-2) 노트 19 — NAFA·NIL·Net 3면 매핑 + ONS 표시 부호 규약

`background/note/19_assets_liabilities_mapping.md` (1차 근거: 13_cdid_dictionary.csv + 본 저장소 `balanceofpayments2025q4.xlsx`)

요지 발췌:

> - **유량(Transactions)** 양면 컬럼: Direct/Portfolio/Other 3분류 각각 자산 1·부채 1·순 1 컬럼(시트당 3개), Financial derivatives는 **순액만**(자산·부채 분리 부재), Reserve assets는 **자산 1개만**(부채 부재). 시트 Table_J, Table_D1_3, Table_D4_6, Table_D7_9에 동일 트리플이 중복 게재됨.
> - **저량(IIP)** 양면 컬럼: Direct/Portfolio/Derivatives/Other 4분류는 자산 stock·부채 stock·순 stock 3개씩, Reserve assets는 자산 stock 1개. Table_K에서 통합 게재.
> - **sign_prefix 패턴**: Table_J 부표1(자산 측)·부표3(순)과 모든 D1_3·D7_9 유량 컬럼은 **sign_prefix=true** (CSV에 공백+마이너스 prefix 부착, 부호 반전 필요). Table_J 부표2(부채 측)와 모든 D4_6, 모든 IIP 저량(stock), Table_K는 **sign_prefix=false** (그대로 사용).
> - **ONS 양면 분류 정합성**: D1_3 = NAFA(asset), D4_6 = NIL(liability), D7_9 = Net(asset−liability), Table_K = IIP 종합(자산·부채·순 전부) — Table_J 부표 1/2/3과 1:1 대응.

5분류별 핵심 CDID 발췌(`19_assets_liabilities_mapping.csv` 발췌):

| 분류 | 자산(NAFA) flow | 부채(NIL) flow | 순(Net) flow | 자산 stock | 부채 stock | 순 stock |
|---|---|---|---|---|---|---|
| Direct investment | **N2SV** (-) | **N2SA** (no prefix) | **MU7M** (-) | N2V3 | N2UG | MU7O |
| Portfolio investment | **HHZC** (-) | **HHZF** (no prefix) | **HHZD** (-) | HHZZ | HLXW | CGNH |
| Financial derivatives | (부재) | (부재) | **ZPNN** (-) | JX96 | JX97 | JX98 |
| Other investment | **XBMM** (-) | **XBMN** (no prefix) | **HHYR** (-) | HLXV | HLYD | CGNG |
| Reserve assets | **LTCV** (-) | (정의상 부재) | LTCV | LTEB | (정의상 부재) | LTEB |
| FA 합계(net) | — | — | **HBNT** (-) | — | — | HBQC |

이상점·정합성 노트:

> 1. **Financial derivatives 유량의 자산/부채 분리 부재** — Table_J·D1_3·D7_9 모두 net만 제공. ONS Pink Book에서도 양면 분리는 IIP 저량(JX96/JX97)에서만 공식 수치.
> 2. **Reserve assets 부채측 부재** — 정의상 정상이나 자동화 코드에서 NIL = NaN을 결측이 아닌 "0 by definition"으로 처리해야 BoP 항등식 검증 시 혼동 없음.
> 3. **Table_J 부표2 컬럼 위치 점프** — derivatives 행이 빠져 col 인덱스가 한 칸씩 당겨짐. 자동 매핑 시 column_position 직접 매칭 금지, **column_label 또는 CDID로 매칭 권장**.


### (2-3) 노트 25 — BPM6 §6.8~§6.81 + OECD BD5 5분류 정의 보강

`background/note/25_fa_categories_bpm6.md` (1차 자료: IMF BPM6 / OECD BD5 2025-03 / Bank of England / HM Treasury / ONS / 한국은행)

5분류별 핵심 인용 발췌:

**§1 직접투자 (Direct Investment, BPM6 §6.8~§6.45)**
- BPM6 §6.8: "Direct investment is a category of cross-border investment associated with a resident in one economy having control or **a significant degree of influence on the management** of an enterprise that is resident in another economy."
- **10% 임계** (BPM6 §6.12~§6.13): "Ownership of **10 percent or more of the voting power** … is evidence of a direct investment relationship." — 50% 초과는 지배(control), 10~50%는 영향력(influence).
- **Asset/liability principle (BPM6 표준)** vs Directional principle (OECD BD5 보조 표시) 이중 구조.
- **하위 분해** (BPM6 §6.25~§6.30): Equity capital(지분자본) / Reinvestment of earnings(재투자수익) / Debt instruments(부채성 상품).
- **영국 ONS 자료원**: Annual Foreign Direct Investment Survey (AFDI) — Inward(AIFDI) + Outward(AOFDI) + 분기 FDI 조사 + BoE 은행권 자료. ONS는 BD4 권고 채택, **SPE 포함·제외 두 시리즈** 발표.

**§2 증권투자 (Portfolio Investment, BPM6 §6.54~§6.79)**
- BPM6 §6.54: "Portfolio investment is defined as cross-border transactions and positions involving **debt or equity securities**, other than those included in direct investment or reserve assets."
- 핵심 특성: 증권의 **양도가능성(negotiability)**.
- 분해: 상품별(Equity & investment fund shares ↔ Debt securities) / 만기별(Long-term ≥ 1년 ↔ Short-term < 1년) / 발행자 부문별(중앙은행/예금취급/일반정부/기타금융/비금융·가계).
- 영국 자료원: Bank of England 통계 + ONS 증권투자 조사. **영국은 만성적인 PI 부채 순증가국**.

**§3 금융파생상품 및 ESO (BPM6 §6.58~§6.62, §7.78~§7.92)**
- BPM6 §6.58: "A financial derivative contract is a financial instrument that is linked to another specific financial instrument or indicator or commodity, through which **specific financial risks … can be traded in their own right**."
- 분류: Forward-type (Futures, Forwards, Swaps) / Option-type / ESO (BPM6 §6.62).
- **순액(net) 표기 사유** — 유량은 정산금이 자산↔부채로 빈번 전환되어 gross 보고가 비현실적, BPM6 §8.34 net 보고 허용. **저량(IIP)은 시장가치 기준 자산·부채 양면(gross)** 게재.
- 영국 자료원: BoE 외환·금리 파생상품 조사, ICMA 자료. ONS Table_J 부표는 **net ZPNN 단일 컬럼**.

**§4 기타투자 (Other Investment, BPM6 §6.63~§6.79)**
- BPM6 §6.63: "Other investment is a **residual category** that includes positions and transactions other than those included in direct investment, portfolio investment, financial derivatives and employee stock options, and reserve assets."
- **6 + 1 sub-functional categories** (BPM6 §6.64): Other equity / Currency and deposits / Loans / Insurance, pension, and standardized guarantee schemes / Trade credit and advances / Other accounts receivable/payable / **SDR allocations**(부채 측만).
- **SDR 배분 처리(2009·2021)**: BPM6는 SDR 배분을 통화당국의 장기 부채로 인식. 2021-08 일반배분(USD 650bn 상당) 모두 자산 측은 준비자산(SDRs), 부채 측은 기타투자(SDR allocations) 동시 계상.
- 영국 자료원: BIS Locational Banking Statistics + Bank of England + 무역신용 조사.

**§5 준비자산 (Reserve Assets, BPM6 §6.64~§6.81)**
- BPM6 §6.64: "Reserve assets are those external assets that are **readily available to and controlled by monetary authorities** for meeting balance of payments financing needs, for intervention in exchange markets to affect the currency exchange rate, and for other related purposes."
- "Readily available" 기준: 즉시 처분 가능, 외화표시(태환 통화), 비거주자 청구권. **담보·질권·동결 자산 제외**.
- **4구성**: ① Monetary gold (BPM6 §6.78~§6.79: Gold bullion + unallocated gold accounts) / ② SDRs / ③ Reserve position in the IMF / ④ Other reserve assets(Currency·Deposits·Securities·FD net·Other claims).
- **영국 법적 보유 구조**: UK reserves는 **HM Treasury 명의의 Exchange Equalisation Account (EEA)** 보유. **Bank of England는 Treasury의 대리인(agent)** 으로 일상 운용 담당. 2025-10 정량: Net reserves = USD 112,358m (GBP 85,518m).
- **BoP/IIP 부호 비대칭**: BoP(유량)·IIP(저량) 모두 **자산 측만** 기록, 부채 측 부재(슬라이드 26 비대칭 인용).

**영국 ONS 종합 표(노트 25 §)**:

> | 분류 | BoP 유량 | IIP 저량 | 영국 자료원 | 회계 측면 |
> |---|---|---|---|---|
> | 직접투자 | 자산(NAFA) + 부채(NIL) 양면 | 자산 + 부채 양면 | ONS AIFDI/AOFDI 연차 + 분기 + BoE | BD5 준수 · SPE 포함/제외 두 시리즈 · directional 보조 |
> | 증권투자 | 자산 + 부채 양면 | 자산 + 부채 양면 | BoE 통계 + ONS 증권투자조사 | 만기·발행자부문별 · 영국은 만성 PI 부채 순증 |
> | 금융파생상품 | **순액(net)** 단일 | 자산 + 부채 양면 (시장가치) | BoE 외환·금리 파생조사 + ICMA | 정산금 회전 → BoP 유량은 net 표기 |
> | 기타투자 | 자산 + 부채 양면 | 자산 + 부채 양면 | BIS Locational Banking + BoE | SDR 배분(부채), 무역신용·예금·대출 |
> | 준비자산 | **자산 측만** | **자산 측만** | EEA(HMT 보유, BoE 운용대행) | 부채 측 부재 정상 |


---

## (3) 5 세부항목 정의·부호 규약·CDID 매핑 표

본 표는 본 보고서 §5(FA 분해) 본문에 직접 사용 가능한 **강의 측 정의(슬라이드 6) + BPM6 보강(노트 25) + ONS 표시 부호 규약(노트 13·19) + CDID 매핑(노트 19 + db/REPORT.md §2.3)**의 결합 형식이다.

| # | 분류 (한국어 / 영문) | 강의 측 1줄 정의 (슬라이드 6) | BPM6 표준 보강 핵심 (노트 25) | BPM6 부호(자산·부채 증감 기준) | 자산 측 양면? | 부채 측 양면? | Table_A col | CDID(순/Net) | ONS 표시 prefix | 2025 Q4 분기치 (£m) |
|---|---|---|---|---|---|---|---|---|---|---:|
| ① | 직접투자 / Direct Investment | "외국기업에 자금을 투입하여 경영에 참가하기 위해 행하는 투자" | BPM6 §6.8 control/significant influence + §6.12 **10% 의결권 임계**, Equity/Reinvested earnings/Debt instruments 3분해 | + = NAFA↑(영국→해외 직접투자 자산 증가), + = NIL↑(해외→영국 FDI 부채 증가), Net = NAFA−NIL | **있음** (N2SV) | **있음** (N2SA) | 3 col 2 | **`-MU7M`** | **prefix 있음** (Table_A 부표 3, Table_J 부표 3, Table_D7_9 부표 2, Table_R1 부표 3, Table_R3 부표 8) | **−1,576** (2025 Q4) |
| ② | 증권투자 / Portfolio Investment | "투자자본의 가치증가를 목적으로 한 투자로 주식과 채권으로 구분" | BPM6 §6.54 시장유통성 증권(직접·준비 제외), Equity·Debt securities + 만기 LT/ST + 발행자 부문 분해 | + = NAFA↑(영국→해외 증권 투자 자산 증가), + = NIL↑(해외→영국 증권 발행 부채 증가) | **있음** (HHZC) | **있음** (HHZF) | 3 col 3 | **`-HHZD`** | **prefix 있음** (Table_A·Table_J·Table_D7_9·Table_R1·Table_R3) | **−61,488** (2025 Q4, 2024 Q4 이후 최대 순유입) |
| ③ | 금융파생상품 / Financial Derivatives & ESO | "파생금융상품거래를 기록" | BPM6 §6.58 위험 전이 계약, Forward(Futures/Forwards/Swaps) + Option + ESO. 유량은 정산금 회전 → **net 단일 표기**, 저량은 시장가치 양면 | Net flow만, + = 영국 보유 파생자산이 부채보다 많이 증가했음 | **부재**(유량) / 있음(저량 JX96) | **부재**(유량) / 있음(저량 JX97) | 3 col 4 | **`-ZPNN`** | **prefix 있음** (Table_A·Table_J 부표 1·3·Table_D1_3·Table_D7_9·Table_R1·Table_R3) | **−1,253** (2025 Q4) |
| ④ | 기타투자 / Other Investment | "대출, 차입, 무역신용, 현금 및 예금 등의 금융거래" | BPM6 §6.63 잔여 분류, **6+1 sub-categories** (Other equity / Currency·deposits / Loans / Insurance·pension·SGS / Trade credit / Other receivables·payables / **SDR allocations** 부채 측만) | + = NAFA↑(영국→해외 대출·예금 등 자산 증가), + = NIL↑(해외→영국 차입·SDR 배분 등 부채 증가) | **있음** (XBMM) | **있음** (XBMN) | 3 col 5 | **`-HHYR`** | **prefix 있음** (Table_A·Table_J·Table_D7_9·Table_R1·Table_R3) | **+54,439** (2025 Q4) |
| ⑤ | 준비자산증감 / Reserve Assets | "통화당국(중앙은행)이 ... 보유하고 있는 대외지급준비자산(IR)의 증감" + "화폐용 Gold, SDR, IMF포지션, 외화자산 등이 포함" | BPM6 §6.64 readily available + controlled by monetary authorities. 4구성: Monetary gold / SDRs / Reserve position in IMF / Other reserve assets. **부채 측 정의상 부재**. 영국: HM Treasury **EEA** 보유, BoE 운용대행 | + = IR 자산 증가(영국 외환 매입·금 매입 등). 부채 측 정의상 0. | **있음** (LTCV) | **정의상 부재** | 3 col 6 | **`-LTCV`** | **prefix 있음** (Table_A·Table_J 부표 1·3·Table_D1_3·Table_D7_9·Table_R1·Table_R3) | **+507** (2025 Q4) |
| Σ | FA 순합계 / Net Financial Account | (슬라이드 14) `FA(broad) = NAFA − NIL + Net FD` 형태로만 등장 | BPM6 §6.5 모든 5분류 합산, 광의(reserve 포함) vs 협의(reserve 제외) 구분 | Net = ①+②+③+④+⑤ 합. + = 영국 순대외자산 형성, − = 순부채 형성 | — | — | 3 col 7 | **`-HBNT`** | **prefix 있음** (Table_A·Table_J·Table_D7_9·Table_R1·Table_R3) | **−9,371** (2025 Q4 합계, 단 NEO 제외) |

**해석 키 (영국 부호 → 자본 흐름)**

- 강의 자료가 한국 사례를 다루므로 슬라이드 17의 양(+) 누적 패턴을 영국에 그대로 옮기면 안 된다. **영국은 만성 경상수지 적자국(2025 Q4 −£18.4bn) → CA(−) ⇒ FA(−) ⇒ NIL이 NAFA보다 빠르게 증가 = 순자본 유입 = 영국 외부에서 영국 부채 자산을 매입**하는 구조.
- `db/REPORT.md` 표 §2.3 의 부호 해석 주석: "음수(−)는 영국으로의 **순자본 유입**(자산 감소·부채 증가). 2025 Q4에는 증권투자에서 큰 순유입(−£61.5bn)이 발생해, 경상수지 적자(−£18.4bn)와 자본수지 적자(−£0.8bn)를 자금조달 측면에서 상쇄."


---

## (4) ONS 표시 부호 규약 해설 (Table_A 의 `-` 접두 보존 사유)

본 절은 **`db/source/balanceofpayments2025q4.xlsx` Table_A·Table_J·Table_D1_3·Table_D7_9·Table_R1·Table_R3 셀 `[B-G]` 헤더에 보이는 `-` 접두 라벨**(예: `-MU7M`, `-HHZD`, `-ZPNN`, `-HHYR`, `-LTCV`, `-HBNT`)이 어떤 의미이고 왜 그렇게 보존되는지 한국어로 정리한다. 1차 근거: `background/note/13_cdid_dictionary.md` §추출 규칙·§부호 prefix CDID 목록 + `background/note/19_assets_liabilities_mapping.md` §sign_prefix 패턴.

### (4-1) 정의 — sign_prefix 란?

ONS Notes (Table A note 1, 본 저장소 `Notes` 시트에 동봉) 원문 가이던스:

> "**Reverse the sign of series prefixed with a minus.**"

즉, ONS 본 저장소 분기 xlsx 의 일부 컬럼 헤더는 CDID 4자(예: `MU7M`) 앞에 **공백+마이너스 부호**(`- MU7M` 또는 `-MU7M`)를 부착해 게재한다. 이 `-` 접두는 **셀 값의 부호가 BPM6 표시 부호와 반대**라는 표시이며, 사용자는 시계열 사용 시 **부호를 반전(× −1)** 해야 한다는 ONS 공식 규약이다.

노트 13 §추출 규칙:

> 부호 반전 prefix 정규식: `^\s*-\s*[A-Z0-9]{4}\s*$`. Notes Table A note 1: "reverse the sign of series prefixed with a minus".

### (4-2) 통계 — 본 저장소 분기 xlsx 의 sign_prefix 분포

`background/note/13_cdid_dictionary.md` §요약 통계:

- **부호 prefix 부착 CDID 행: 59건 (고유 CDID 21개)**
- 부호 prefix 등장 시트: **Table_A, Table_D1_3, Table_D7_9, Table_H, Table_J, Table_R1, Table_R3** (7개 시트)
- prefix=true 시트는 모두 **자산 측 또는 순(net) 측**, prefix=false 시트는 모두 **부채 측 또는 IIP 저량(stock)** 측. 비대칭 패턴이 명확.

### (4-3) 왜 자산·순 측만 prefix 가 붙고 부채·저량 측은 안 붙는가?

**원인**: ONS는 BPM5 시기의 **"순유출입액 기준"** 표기 관습을 1997 ~ 현재까지 동일 시계열 ID(CDID)로 발표 지속하고자, BPM6 채택 후에도 시계열 값은 그대로 두고 **헤더 라벨에 `-` 접두를 부착해 부호 반전**을 알리는 방식을 택했다. 그 결과:

| 측면 | BPM5 표시(과거) | BPM6 표시(현재 표준) | ONS xlsx 셀 부호 | 헤더 표기 |
|---|---|---|---|---|
| 자산 측 (NAFA) | + (자산 증가 = 자본 유출) | + (자산 증가) | BPM5와 동일 부호 | **`-CDID`** (사용자가 반전해야 BPM6 표준에 맞음) |
| 부채 측 (NIL) | − (부채 증가 = 자본 유입) | + (부채 증가) | BPM6 표준 부호 | `CDID` (그대로 사용) |
| 순(Net = NAFA−NIL) | + (순유출) | NAFA−NIL = − (영국은 만성 음수) | BPM5와 동일 부호 | **`-CDID`** |
| IIP 저량(stock) | (BPM5도 자산·부채 양면) | 동일 | 동일 | `CDID` (그대로 사용) |

따라서 **`-MU7M`/`-HHZD`/`-ZPNN`/`-HHYR`/`-LTCV`/`-HBNT` 가 의미하는 바는** 다음과 같다:
- 셀 값을 그대로 분기 시계열 분석에 사용하면 **BPM5 시기의 "순유출입액 기준" 부호**가 된다.
- BPM6 표준 부호("자산·부채 증감 기준")로 해석하려면 **셀 값에 −1 을 곱해야** 한다.
- 즉, ONS Bulletin Tables 의 Table_A 부표 3 (금융계정 합계)에서 **`-HBNT` 가 양수(+)로 나오면, BPM6 기준으로는 음수(−)** = 영국이 순자본을 유입받았다는 뜻이다.

### (4-4) 본 보고서가 채택할 표시 방식

**원본 무수정 원칙**(`db/CLAUDE.md` §가공 원칙 1번)에 따라 본 보고서는 셀 값을 그대로 인용하되, 다음 표기 규칙을 따른다:

1. **CDID 열 표기**: `-MU7M`, `-HHZD`, `-ZPNN`, `-HHYR`, `-LTCV`, `-HBNT` 와 같이 ONS 헤더 그대로 인용 (prefix 보존).
2. **분석 시 부호 해석**: 본 보고서 §5의 분기 실측값(예: `db/REPORT.md` §2.3 의 직접투자 −1,576 등)은 이미 ONS xlsx 셀 값 그대로(=BPM5 부호)이므로, 한국 강의 사례 슬라이드 9의 신매뉴얼 표(직접투자 −14,628)와 부호 방향이 일관되도록 **그대로 음수로 인용**하고, "음수 = 영국으로의 순자본 유입(자산 감소·부채 증가)"이라는 BPM5 부호 → 자본흐름 직관 해설을 함께 부기.
3. **양면(NAFA/NIL) 분해 시 주의**: Table_J 부표 1(NAFA, prefix=true: N2SV·HHZC·XBMM·LTCV)과 Table_J 부표 2(NIL, prefix=false: N2SA·HHZF·XBMN)는 **부호 체계가 다르므로** 직접 가감산 금지. 노트 19의 **Net 컬럼(MU7M·HHZD·HHYR)을 그대로 사용**하는 것이 안전하다(이미 prefix=true 로 BPM5 정합).

### (4-5) 요약 (3줄)

- **`-` 접두는 ONS 의 BPM5↔BPM6 호환 표시이며, 셀 값에 −1을 곱하면 BPM6 표준 부호가 된다.**
- 21개 고유 CDID(주로 자산 측 NAFA + 순 Net + 합계 HBNT/HBNR)에 부착되어 있고, 부채 측 NIL과 IIP 저량(stock) 컬럼에는 부착되지 않는다.
- 본 보고서는 원본 셀 값을 그대로 인용하므로 사용자에게 보이는 모든 분기 FA 5분해 수치는 **"BPM5 순유출입액 기준" 부호** 이다 — "음수 = 자본 유입"의 직관이 그대로 적용된다.


---

## (5) 보고서 §5 (FA 분해) 본문 인용 후보 표

본 표는 **단계 2 보고서 §5 본문 작성 시 직접 인용·재배치할 수 있는 발췌 단편 모음**이다. 각 행은 (인용 위치 / 짧은 한국어 발췌 / 본문에서의 활용 의도) 세 컬럼으로 구성된다.

| # | 인용 위치 | 짧은 한국어 발췌 | 본문 §5 활용 의도 |
|---|---|---|---|
| C1 | 슬라이드 6 (PPTX p.6) | "금융계정(Financial account): 자산 및 부채의 소유권 변동과 관련된 거래" | §5 도입부, FA 정의의 첫 줄. |
| C2 | 슬라이드 6 | "직접투자: 외국기업에 자금을 투입하여 경영에 참가하기 위해 행하는 투자" | §5.1 직접투자 도입, 강의 정의 인용. |
| C3 | 슬라이드 6 | "증권투자: 투자자본의 가치증가를 목적으로 한 투자로 주식과 채권으로 구분" | §5.2 증권투자 도입. |
| C4 | 슬라이드 6 | "파생금융상품: 파생금융상품거래를 기록" | §5.3 파생 도입(짧음 → 노트 25 §3 보강 권장). |
| C5 | 슬라이드 6 | "기타투자: 대출, 차입, 무역신용, 현금 및 예금 등의 금융거래" | §5.4 기타투자 도입. |
| C6 | 슬라이드 6 | "준비자산증감: 통화당국(중앙은행)이 ... 보유하고 있는 대외지급준비자산(IR)의 증감 ... 화폐용 Gold, SDR, IMF포지션, 외화자산 등이 포함" | §5.5 준비자산 도입, 4구성 자연 인용. |
| C7 | 슬라이드 8 | "새로운 매뉴얼에서는 금융계정 부호표기 방식을 ‘자산·부채의 증감 기준’으로 변경" / "부채 항목의 부호는 종전과 동일하나 자산 항목의 부호는 반대 방향으로 바뀜" | §5 부호 규약 절(BPM6 도입), §4 ONS 표시 부호와 연결. |
| C8 | 슬라이드 9 (한국 2017 표) | "최근 매뉴얼 기준: 직접투자 −14,628 / 증권투자 −57,847 / 파생 +8,253 / 기타 −18,523 / 준비 −4,360" | §5 부호 규약 예시(영국 부호 음수 = 자본 유입의 한국판 정합 사례). |
| C9 | 슬라이드 14 | "Financial account in a broad sense = nonreserve FA + reserve account" | §5 광의·협의 구분 도입(준비자산 분리 근거). |
| C10 | 슬라이드 14 | "Financial account = Net acquisition of foreign financial assets − Net incurrence of liabilities + Net financial derivatives" | §5 NAFA/NIL/FD 양면 식 인용. |
| C11 | 노트 06 §일치 평가 | "직접투자 임계치: 강의 자료 명시 없음 → BPM6 의결권 10% 이상" | §5.1 강의 누락 보완 + BPM6 보강 시그널. |
| C12 | 노트 25 §1.1 | "BPM6 §6.8: Direct investment is a category … having control or a significant degree of influence on the management" | §5.1 BPM6 영문 정의 인용. |
| C13 | 노트 25 §1.2 | "Ownership of 10 percent or more of the voting power" (BPM6 §6.12) | §5.1 의결권 10% 임계 정량 보강. |
| C14 | 노트 25 §1.5 | "Equity capital / Reinvestment of earnings / Debt instruments" | §5.1 직접투자 3분해 명시. |
| C15 | 노트 25 §2.1 | "BPM6 §6.54: Portfolio investment is defined as cross-border transactions and positions involving debt or equity securities" | §5.2 BPM6 영문 정의. |
| C16 | 노트 25 §2.2 | "Long-term ≥ 1년 ↔ Short-term < 1년" (BPM6 §5.103, §6.65) | §5.2 만기 분해. |
| C17 | 노트 25 §3.1 | "BPM6 §6.58: A financial derivative contract … specific financial risks … can be traded in their own right" | §5.3 BPM6 영문 정의. |
| C18 | 노트 25 §3.3 | "정산금이 자산↔부채로 빈번 전환 → BPM6 §8.34 net 보고 허용" | §5.3 net 단일 표기 사유. |
| C19 | 노트 25 §4.1 | "BPM6 §6.63: Other investment is a residual category" | §5.4 잔여 분류 도입. |
| C20 | 노트 25 §4.2 | "6+1 sub-functional categories: Other equity / Currency·deposits / Loans / Insurance·pension·SGS / Trade credit / Other receivables·payables / SDR allocations" | §5.4 7분해 도입. |
| C21 | 노트 25 §5.1 | "BPM6 §6.64: Reserve assets are those external assets that are readily available to and controlled by monetary authorities" | §5.5 BPM6 영문 정의. |
| C22 | 노트 25 §5.3 | "UK reserves는 HM Treasury 명의의 Exchange Equalisation Account(EEA)에 보유. Bank of England는 Treasury의 대리인(agent)으로 일상 운용 담당. 2025-10 Net reserves = USD 112,358m" | §5.5 영국 특화 사실(보유 구조·정량). |
| C23 | 노트 19 §sign_prefix 패턴 | "Table_J 부표1(자산)·부표3(순)과 모든 D1_3·D7_9 유량 컬럼은 sign_prefix=true (CSV에 공백+마이너스 prefix 부착, 부호 반전 필요). Table_J 부표2(부채)와 모든 D4_6, 모든 IIP 저량(stock), Table_K는 sign_prefix=false (그대로 사용)." | §5 부호 규약·§4 표시 부호와 연결, 자동화 코드 기준. |
| C24 | 노트 19 §이상점 1번 | "Financial derivatives 유량의 자산/부채 분리 부재" | §5.3 net 단일 표기와 본 저장소 정합 확인. |
| C25 | 노트 19 §이상점 2번 | "Reserve assets 부채측 부재 — 정의상 정상" | §5.5 자산 측 일변도 사유. |
| C26 | 노트 13 §추출 규칙 | "부호 반전 prefix 정규식: ^\s*-\s*[A-Z0-9]{4}\s*$. Notes Table A note 1: ‘reverse the sign of series prefixed with a minus’." | §4 ONS 표시 부호 1차 근거 인용. |
| C27 | `db/REPORT.md` §2.3 | "직접투자 −1.6 / 증권투자 −61.5 / 파생 −1.3 / 기타투자 +54.4 / 준비자산 +0.5 (2025 Q4, £bn)" | §5 5분해 표 분기 실측 헤드라인 (단계 2 본문 핵심 수치). |
| C28 | `db/REPORT.md` §2.3 부호 해석 | "음수(−)는 영국으로의 순자본 유입(자산 감소·부채 증가). 2025 Q4에는 증권투자에서 큰 순유입이 발생해, 경상수지 적자(−£18.4bn)와 자본수지 적자(−£0.8bn)를 자금조달 측면에서 상쇄." | §5 마무리 — CA·KA·FA 자금조달 정합성 진술. |
| C29 | `db/REPORT.md` §3.2 | (분기 시계열 표 2024 Q4 ~ 2025 Q4 직접·증권·파생·기타·준비·NEO) | §5 분기 추세 보강 (5분기 시계열). |

---

## 빠진 부분 (본 §4 묶음에서 확인되지 않은 항목)

1. **영국 FDI SPE 포함/제외 두 시리즈의 분기 실측치**: 노트 25 §1.6에서 ONS BD4 준수·SPE 비중 7.1%(2021)만 확보. 본 저장소 `balanceofpayments2025q4.xlsx`는 SPE 분리 컬럼 부재 → ONS Pink Book Ch.4 별도 다운로드 권고(노트 16·22 web-search 보강 필요).
2. **영국 직접투자 하위 3분해(Equity·Reinvested earnings·Debt instruments) 분기 시계열**: Table_J 부표 3의 col 2~4 (HBWN·HBWT·MU7L)에 존재하나, 본 보고서 §5에서 사용할지 여부는 단계 2에서 결정. 노트 19는 Total(MU7M) 만 다룸.
3. **영국 증권투자 만기 LT/ST 분해**: 노트 25 §2.2에서 BPM6 §5.103 정의만 확보, 본 저장소 xlsx 시트에는 만기 분해 컬럼 부재. ONS Pink Book Ch.4 별도 시트 필요.
4. **영국 파생금융상품 옵션·선물·스왑 분해**: 강의 슬라이드 6은 "거래를 기록"으로만 처리, 노트 25 §3.2 BPM6 분류 정의만 확보. 본 저장소는 ZPNN net 단일 컬럼만 → 분기 분해 불가.
5. **2025 Q4 FA 5분해 분기치의 BPM6 표준 부호 환산**: 본 §4는 ONS 셀 값 그대로(BPM5 부호) 인용. 단계 2 §5 본문 작성 시 BPM6 표준 부호로 환산해 함께 보여줄지(부호 반전 적용) 결정 필요.
6. **슬라이드 17의 정량 시계열 원본**: 강의 슬라이드는 차트만 제공, 한국 BoP 4분해 정량 표가 별도 첨부되지 않아 본 §4 (1-3) 표는 멀티모달 시각 판독 추정치. ECOS API 등 별도 웹 조회 필요(외부 위임).

## 후속 단계 안내

본 호출은 Q3(FA 5분해) 발췌만 수행했다. 다음 호출에서 Q4(항등식 일관성 CA + KA + FA + NEO ≡ 0)·Q5(환율-CA 관계 J-curve, Marshall-Lerner)를 별도 단위로 추출한다. 본 §4의 산출물은 단계 2 보고서 §5 본문 작성 시 (3) CDID 매핑 표 + (5) 인용 후보 표를 1차 키로 사용하고, (4) ONS 표시 부호 해설은 보고서 부록 또는 §5 도입 박스에 압축 인용한다.
