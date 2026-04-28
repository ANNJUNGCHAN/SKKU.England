# Phase 2.3 부호 규약·결측 의미·귀금속·통계 개정 강의 자료 4건 일괄 산출

본 문서는 db/CHECKLIST.md 2.3 background-search 4개 항목을 일괄 산출한 결과이다. 1차 근거는 background/BoP.pptx 슬라이드 6, 8, 9, 10, 11, 12, 13, 14, 26, 21 + background/note/03_sign_conventions.md, 06_financial_account_categories.md, 07_glossary.md, 12_xlsx_sheet_inventory.md, 15_units_and_missing.md, 18_iip_revaluation.md, 22_bop_data_sources.md이며, 강의 자료에 답이 없는 항목은 명시적으로 (강의 자료 미수록)으로 표기한다(우회 추론 금지).

## 1. 요지

- 2.3.1 메모용 부호·결측 표현 권고: 강의 슬라이드 8/13에서 발췌한 BPM6 (자산·부채 증감 기준) 한 문장과, 13회차(13_missing_meaning_validation.md)에서 보정한 (미가용, not available, GAF [x]) 한 문장을 시트별 메타 메모에 그대로 인용하면 된다.
- 2.3.2 부호 규약 대조: 강의 자료의 BPM6 부호 규약과 ONS의 sign_prefix 표기는 개념 차원에서 100% 일치(이미 검증 완료). ONS는 BPM6 호환 차원에서 같은 표기 안에 일부 시리즈만 (역방향 의미)임을 알리는 운영상 보조 표기를 sign_prefix(59 행, 7 시트)로 부착하며, 강의 자료가 다루는 BPM5 vs BPM6 매뉴얼 변경과는 무관하다.
- 2.3.3 귀금속(비통화용 금): 강의 슬라이드 6은 준비자산의 하위로 (화폐용 Gold, monetary gold)만 명시하며, 비통화용 금(non-monetary gold), Table_BX의 BoP 처리 방식은 강의 자료 미수록이다(별도 web-search 위임 권고). ONS xlsx 자체 메타(Notes r14)는 (Precious metals includes: Non-Monetary Gold (NMG), Platinum, Palladium and Silver.)로 정의해 두었다.
- 2.3.4 통계 개정(revision): 강의 자료는 분기 BoP의 revision triangle, 발표 시차, Table_R1/R2/R3 활용을 직접 다루지 않는다(강의 자료 미수록). 가장 가까운 강의 인접 개념은 슬라이드 26 도식의 (비거래요인 = 가격·환율·기타조정) 분해이며, R3가 9 부표(자산/부채/순 x IIP/Flow/Income)로 그 도식의 (기타조정) 항을 직전 발표 대비 사후 추적하는 운영 자료라는 점에서 학생용 심화 보조 자료로 보존 정당화 가능.

---

## 2. 2.3.1 메모용 부호 규약 표현 권고

시트별 한국어 메타 메모(db/data/balanceofpayments2025q4_<sheet>.md)의 (부호 규약) 단락에 다음 한 문장을 그대로 사용한다(강의 슬라이드 8 본문 직접 인용 + ONS 표기 보조 안내).

> 부호 규약: 본 시트는 BPM6 매뉴얼의 (자산·부채 증감 기준)을 따른다(강의 슬라이드 8 직접 인용: 새로운 매뉴얼에서는 금융계정 부호표기 방식을 [자산·부채의 증감 기준]으로 변경 -- 자산 증가/부채 증가 모두 (+)). 단, ONS가 CDID 식별자 앞에 마이너스(-)를 부착한 시리즈는 다운로드 시 부호를 반전해야 한다(Notes 시트 note 1).

경상·서비스·소득 시트(B/BX/C/E/F/G/H/I)의 경우 슬라이드 13의 더 직관적 진술로 대체 가능:

> 부호 규약: 강의 슬라이드 13에 따라 대변(credit) = 외국에서 자국으로 자금 유입 (+), 차변(debit) = 자국에서 외국으로 자금 유출 (-)로 기재한다. 합계 차원에서는 사후 항등(전 계정 합 = 0)이 성립하나, 부분합(예: 경상수지)은 흑자/적자 가능.

근거: background/note/03_sign_conventions.md 항목별 발췌 표 슬라이드 8/13 행 / background/BoP.pptx 슬라이드 8/13.

## 3. 2.3.1 메모용 결측 의미 표현 권고

13회차(db/data/_inventory/13_missing_meaning_validation.md)의 검증 결과를 반영해, 본 xlsx에 등장하는 결측 마커 x 360건(Table_C 6 부표 x 60셀, 1997 Q1~1998 Q4)에 한정한 한 문장 표현은 다음과 같다.

> 결측 의미: 본 시트의 셀 x는 ONS Notes 시트 note 5의 정의(Cells containing [x] represent unavailable data.)에 따라 (미가용, not available) 의미이며, GAF(Government Analysis Function) 권고 기호로는 [x]에 해당한다. (비공개, suppressed) 또는 (적용 불가, not applicable)와 의미가 다르므로 단일 라벨로 통합하지 않는다. Table_C 1997 Q1~1998 Q4 EU/non-EU 분기 분해는 ITIS 분기 조사 표본, EU15 -> EU27 정의 변경 등의 사유로 작성·공표되지 않은 구간이다.

x가 등장하지 않는 시트(Table_A, B, BX, D, E, F, G, H, I, J, K, R1, R2, R3)는 다음 짧은 안내로 충분:

> 결측 의미: 본 시트의 빈 셀(empty)은 데이터 영역 외 padding이며 결측이 아니다(15회차 검증). x, .., - 마커는 본 시트에 등장하지 않으며, 만약 발견되면 GAF 권고에 따라 별도 컬럼으로 사유를 기재한다.

근거: db/data/_inventory/13_missing_meaning_validation.md 2~4 / background/note/15_units_and_missing.md 결측 카탈로그 / Notes 시트 r14, r23 직접 인용.

---

## 4. 2.3.2 강의 부호 규약 vs ONS 부호 규약 차이

이미 db/data/_inventory/06_sign_convention_validation.md에서 객관 확인된 정합성 결과를 요약·재확인한다.

### 4.1 대조 표

| 차원 | 강의 자료(BoP.pptx) | ONS xlsx 실제 표기 | 일치/불일치 |
|---|---|---|---|
| 매뉴얼 채택 | BPM6 (자산·부채 증감 기준) 슬라이드 8 | BPM6 일관 적용 (Notes r5/29/33/42/51) | 일치 (개념 100%) |
| 자산 증가 부호 | (+) 슬라이드 8 | (+) Table_J/D 등 | 일치 |
| 부채 증가 부호 | (+) 슬라이드 8 | (+) 동상 | 일치 |
| 매뉴얼 변경 사실 | BPM5(순유출입 기준) -> BPM6 변경, 자산항목 부호 반전(슬라이드 8~9) | ONS는 BPM6 단독 사용. BPM5 표기는 미사용 | 부분 불일치 -- 강의는 변경 이력 설명, ONS는 결과만 적용 |
| sign_prefix(-) | 강의 자료 미수록 | CDID 앞 마이너스: 59 행, 7 시트(Table_A, D1_3, D7_9, H, J, R1, R3), Notes note 1로 안내 | 강의 미수록(운영 보조 표기) |
| 종합수지·준비자산 부호 비대칭 | 슬라이드 26 도식: 준비자산이 증가할 경우 국제수지표에서는 음(-), 국제투자대조표에서는 양(+) | Table_J(BoP flow) vs Table_K(IIP stock) 부호가 정합 | 일치 |
| Cr/Dr 정의 | 슬라이드 13: 대변(+)=유입, 차변(-)=유출 | Table_B/BX/C/E/F/G/H/I sub1/sub2 분리 | 일치 |
| NEO 부호 | 슬라이드 6 정의: 오차 및 누락계정은 통계상의 불일치를 조정해 주기 위해서 사후적으로 기장 | Table_A note 2: converse of current+capital balances (HBOG, FKMJ) and net financial account transactions (HBNT) | 개념 일치 |

### 4.2 정량 평가

- 개념 차원 일치율 100% (BPM6 채택, 자산증가/부채증가 모두 +, Cr/Dr 정의, 종합수지·준비자산 부호 정합).
- 운영 표기 차이 1건: ONS의 sign_prefix(59 행)는 강의 자료에 직접 다뤄지지 않은 ONS 운영상 보조 표기. 본 표기 자체가 BPM5/BPM6 차이는 아니며, 같은 BPM6 표기 안에서 일부 시리즈만 (역방향 의미)임을 메타 차원에서 알리는 표시로, 강의 자료의 부호 규약과 충돌하지 않는다.
- 강의 미수록 1건: ONS의 sign_prefix 운영 표기는 강의 슬라이드 8~14에서 직접 다뤄지지 않으므로, 학생용 분석에서는 별도 컬럼(sign_prefix=true)으로 보존하고 분석 단계에서 -1 곱할지 별도 메타로 둘지 선택하도록 안내(db/CLAUDE.md 값 불변 원칙에 따라 후자 권장).
- 예외 단발 1건: Table_H의 FKKM (General government, Payment to EU institutions, Less abatement)은 sign_prefix=true이지만 Notes 시트에 별도 명시가 없는 단발 예외 -- Table_C note 7 (Includes transactions with international organisations other than European Union institutions)과 연관된 EU 분담금 차감 계열로 추정되며, 가공 시 별도 메모 부기 필요.

### 4.3 한 줄 요약

강의 자료의 BPM6 부호 규약과 ONS xlsx의 부호 표기는 BPM6 호환 차원에서 100% 일치하며, ONS의 sign_prefix는 강의 자료가 다루지 않은 ONS 운영상 보조 표기일 뿐이다. 학생용 메모에는 2의 한 문장(슬라이드 8 또는 13 인용 + ONS sign_prefix 안내)이면 충분하다.

근거: db/data/_inventory/06_sign_convention_validation.md 결론 / background/note/03_sign_conventions.md 슬라이드 8/13 행 / background/note/13_cdid_dictionary.csv sign_prefix 컬럼 59 행.

---

## 5. 2.3.3 귀금속(비통화용 금) BoP 처리 방식

### 5.1 강의 자료 발췌

강의 슬라이드 6의 준비자산(Reserve Assets) 정의에서 (화폐용 Gold, monetary gold)가 명시적 하위 항목으로 등장한다.

> 슬라이드 6 발췌(직접 인용): 준비자산증감(changes in reserve assets): 통화당국(중앙은행)이 일정시점에 있어서 국제유동성 수단으로 보유하고 있는 대외지급준비자산(international reserves: IR)의 증감 / 대외지급준비자산에는 화폐용 Gold, SDR, IMF포지션, 외화자산 등이 포함 (background/note/06_financial_account_categories.md 행 20)

비통화용 금(non-monetary gold), precious metals, Table_BX 보조표의 BoP 처리 방식에 대해서는 강의 자료 미수록이다. 슬라이드 1~31 본문에 (비통화용), (non-monetary gold), (precious metals), (귀금속) 키워드가 등장하지 않으며, background/note/07_glossary.md 행 120도 명시적으로 (귀금속 보정 / Non-monetary Gold Adjustment / 비통화용 금 거래 별도 보정 (강의 자료 미수록, ONS 표준))으로 분류해 두었다.

### 5.2 Table_BX와 Table_B의 관계 (ONS xlsx 자체 메타)

강의 자료가 답하지 못하는 부분을 ONS xlsx 자체의 메타 텍스트로 보강한다(이는 db/data/_inventory/05_meta_text.csv, 12_missing_markers 등에서 이미 인용된 1차 근거이며, 외부 web-search가 아닌 본 저장소 보유 자료이다).

| 시트 | xlsx 메타 텍스트(직접 인용) | 의미 |
|---|---|---|
| Table_B | Table B: Current account, seasonally adjusted (4 부표: Cr/Dr/Bal/%GDP) | 영국 경상수지 본표(전체) -- 상품수지 안에 비통화용 금, 플래티넘, 팔라듐, 은이 모두 포함된 거래 흐름 |
| Table_BX | Table BX: Current account excluding precious metals [note 1], seasonally adjusted (4 부표 동일 구조) | 동상에서 귀금속(NMG, Pt, Pd, Ag)을 제외한 보조표 |
| Notes r14 (BX note 1) | Precious metals includes: Non-Monetary Gold (NMG), Platinum, Palladium and Silver. | BX가 제외하는 4개 귀금속의 명시적 정의 |

Table_BX와 Table_B의 관계 -- 한국어 풀이:

- Table_B(본표)는 BPM6 표준에 따라 비통화용 금(NMG), 플래티넘, 팔라듐, 은의 거주자-비거주자 간 거래를 (상품수지, Trade in goods)의 일부로 포함한다. 즉, 영국 거주자가 외국으로부터 비통화용 금을 매입하면 Table_B의 상품수입(B.2)에, 외국에 매각하면 상품수출(B.1)에 기재된다.
- Table_BX(보조표)는 동일 기간에서 위 4개 귀금속 거래를 제외한 경상수지를 별도로 제시한다. 이는 영국 BoP의 특수 사정(런던 금시장(London Bullion Market)의 글로벌 귀금속 거래 거점 역할로 인해 분기 상품수지가 귀금속 단일 품목 변동에 크게 흔들리는 현상)을 보정해 (기조적, underlying) 경상수지를 보여주는 ONS 운영 표이다.
- 데이터 처리 권고(강의 자료 미수록 보강): Table_B와 Table_BX의 차이값(B - BX)이 곧 영국의 귀금속 4종 순거래액. 학생 분석에서 (기조 경상수지 추세)를 보고 싶으면 Table_BX, (총 거주자 거래)를 보고 싶으면 Table_B를 선택. 부호 규약은 양 시트 동일(Cr +, Dr -).
- 본 Bulletin 범위 외: 비통화용 금이 어떤 BPM6 절(10 Trade in goods)에 정의되는지, 화폐용 금(준비자산)과 비통화용 금(상품)을 분리하는 기준이 무엇인지에 대한 강의·xlsx 메타 진술은 본 저장소 자료에 없음 -> 별도 web-search로 BPM6 10/14 또는 ONS UK Trade QMI 본문 직접 인용 필요.

### 5.3 한 줄 요약

강의 슬라이드 6은 (화폐용 금)만 준비자산 하위로 다루며, 비통화용 금(Table_BX의 4개 제외 품목)의 BoP 처리 방식은 강의 자료 미수록이다. Table_BX는 영국의 런던 금시장 거점성 때문에 ONS가 운영상 추가한 (귀금속 제외 경상수지) 보조표이며, Notes r14가 4개 품목(NMG, Pt, Pd, Ag)을 명시한다. 학생 분석 시 Table_B(전체) vs Table_BX(귀금속 제외) 차이가 곧 4개 귀금속 순거래액이다.

근거: background/BoP.pptx 슬라이드 6 / background/note/06_financial_account_categories.md 행 20 / background/note/07_glossary.md 행 120 / db/source/balanceofpayments2025q4.xlsx Notes r14 / db/data/_inventory/05_meta_text.csv Table_BX 행.

---

## 6. 2.3.4 통계 개정(revision) 거시지표 해석 의미

### 6.1 강의 자료 발췌

강의 자료(background/BoP.pptx 슬라이드 1~31 본문 + 회차 노트 23종)에서 분기 BoP의 통계 개정(revision), revision triangle, 발표 시차, Table_R1/R2/R3 활용에 대한 직접 진술은 0건이다. background/note/07_glossary.md 행 119는 명시적으로 (개정(리비전) / Revision / ONS 분기별 사후 개정. 항등식 잔차에 영향(강의 자료 미수록, ONS 표준))으로 분류했고, 행 139의 (보강 영역) 표에서도 (결측 표기, 개정, 귀금속 보정 / 우선순위 低 / 강의 미수록 / ONS Methodology)로 위임 분류되어 있다.

가장 가까운 강의 인접 개념 3개(강의 자료에 등장하는 인접 진술이며, revision 자체의 정의는 아님):

| 인접 개념 | 강의 위치 | 인용 |
|---|---|---|
| 비거래요인 = 가격, 환율, 기타조정 | 슬라이드 26 도식 | 거래요인에 의한 증감액은 국제수지표의 투자수지 및 준비자산증감의 합계와 일치 / 비거래요인은 가격변동, 환율변동, 기타조정 (note/05_iip_nfa.md 슬라이드 25 행) |
| 오차 및 누락(NEO)의 사후 기장 | 슬라이드 6 정의 | 오차 및 누락계정은 실제로 국제수지표를 작성하는 데 있어서 통계상의 불일치를 조정해 주기 위해서 사후적으로 기장해 주는 항목임 (note/03_sign_conventions.md, 슬라이드 6 본문) |
| 사후 항등성 | 슬라이드 13 | 국제수지표상 대변의 총합과 차변의 총합은 사후적으로 항상 일치 (note/03_sign_conventions.md 슬라이드 13 행) |

이 세 개념 모두 (발표 후 사후 조정)이라는 시간 구조를 공유하지만, 공식 발표 -> 직전 발표 대비 개정값 산출(revision triangle)이라는 ONS 운영 절차 자체는 강의에서 다뤄지지 않는다.

### 6.2 Table_R1/R2/R3 학생용 활용 권고

db/data/_inventory/16_curriculum_coverage_check.md 5(과잉 커버리지 분석) + 18_subtable_curriculum_alignment.md 4.3 평가 결과를 단정 권고로 재정리한다.

| 시트 | 부표 수 | 차원 | 학생용 1차 분석 활용 | 학생용 심화 모듈 활용 | 강의 매핑 |
|---|---:|---|---|---|---|
| Table_R1 (잔액 개정 요약) | 3 | CA(SA), CA(NSA), FA x 개정값 | 제외 -- 발표값과 혼동 위험 | 슬라이드 14 항등식 잔차의 일부가 ONS 분기 개정 효과임을 보여주는 보조 자료. R1.3(FA 개정) - R1.1(CA SA 개정) 차이로 분기 개정 폭 추정 가능 | 슬라이드 14 항등식 잔차 분석 보조(인접 개념) |
| Table_R2 (CA 개정 + %GDP) | 4 | Cr/Dr/Bal/%GDP x 개정값 | 제외 -- NIA 분모(YBHA) 개정도 함께 들어와 학생 1차 분석에서 분리 어려움 | NIA 항등식(슬라이드 22 Y = C+I+G+(EX-IM))에서 GDP 분모 시계열 안정성 검증 보조 | 슬라이드 22 NIA 인접(분모 안정성) |
| Table_R3 (IIP 개정, 9 부표) | 9 | {abroad/in UK/net} x {IIP/Flow/Income} | 제외 -- 9 부표 구조로 학생 학습 부담 큼 | 슬라이드 26 비거래요인 분해 보조: R3.7(Net IIP 개정) - R3.8(Net FA flow 개정) 차이 = (기타조정, other changes) 부분 추정 가능 | 슬라이드 26 도식 비거래요인 부분 정합 |

### 6.3 학생용 활용 권고 (3원칙)

16_curriculum_coverage_check.md 6 + 18_subtable_curriculum_alignment.md 5.4의 3원칙을 메모용으로 단정:

1. 분리 원칙: Phase 2.1 ETL이 Table_R1/R2/R3을 별도 long-form CSV(balanceofpayments2025q4_r1_sub1.csv 등 총 16 CSV)로 분리하며, 학생용 README의 (운영 정보 / ONS 분기 개정) 섹션에 배치. 1차/2차 분석 권장 부표(16_curriculum_coverage_check.md 6 카탈로그)에는 포함하지 않는다.
2. 메모 명시 원칙: 각 R 시트 메모(db/data/balanceofpayments2025q4_r1.md 등)에 (ONS 분기 개정 운영 자료. 강의 자료 미수록(별도 web-search 위임 권고: ONS National Accounts Revisions Policy + Pink Book/Bulletin 발표 시차). 본 시트의 값은 직전 분기 발표(2025 Q3 발표) 대비 본 분기(2025 Q4 발표) 차이.) 한 줄을 헤더에 명시.
3. 인접 개념 안내 원칙: 학생이 R 시리즈를 보고 싶을 때 R3.7(Net IIP 개정)이 슬라이드 26의 (비거래요인 -> 기타조정)과 부분 정합한다는 인접 매핑을 메모에서 안내해, (발표 시차 -> 기타조정 일부)라는 거시지표 해석을 학생 스스로 도출 가능하도록 한다.

### 6.4 강의 자료에서 답이 없는 부분(별도 web-search 위임 권고)

본 저장소 background/ 폴더 자료만으로 답할 수 없는 항목 -- 모두 외부 위임:

- ONS National Accounts Revisions Policy 본문 (정량 정의: open period, closed period, 12개월 사전공지 등)
- Pink Book 연간 통합 개정 vs Bulletin 분기 개정의 시점 차이 (Pink Book 매년 10~11월에 직전 2개 연도 분기 시계열 일괄 개정)
- revision triangle xlsx 위치 (https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsrevisiontriangles -- note/10_ons_web_research.md에서 URL만 확인됨)
- 2025 Bulletin이 적용한 2021년 이후 전 기간 개정 사유 본문 (note/22_bop_data_sources.md에서 사실만 확인, 사유 본문은 미인용)

근거: background/note/07_glossary.md 행 119/139 / background/note/22_bop_data_sources.md 자료원별 카탈로그/Pink Book 연례 통합 개정 행 / db/data/_inventory/16_curriculum_coverage_check.md 5 / db/data/_inventory/18_subtable_curriculum_alignment.md 4.3.

---

## 7. 출처

### 강의 자료 (1차 근거, background/)

- background/BoP.pptx 슬라이드 6 (FA 5분류, 준비자산, NEO 정의)
- background/BoP.pptx 슬라이드 8 (BPM5 -> BPM6 부호 규약 변경)
- background/BoP.pptx 슬라이드 9 (한국 2017 BoP 표, 신/구 매뉴얼 비교)
- background/BoP.pptx 슬라이드 10 (흑자/적자 의미)
- background/BoP.pptx 슬라이드 11 (NFA 해석)
- background/BoP.pptx 슬라이드 12 (종합수지 = Reserve)
- background/BoP.pptx 슬라이드 13 (복식부기 Cr/Dr, 사후 항등성)
- background/BoP.pptx 슬라이드 14 (CA = FA(narrow) + Reserve = FA(broad), FA = NAFA - NIL + Net deriv)
- background/BoP.pptx 슬라이드 21 (상품수지 vs 무역수지 차트)
- background/BoP.pptx 슬라이드 26 (BoP <-> IIP 거래/비거래요인 도식; 준비자산 부호 비대칭)
- background/slide_images/slide_06.png, slide_08.png, slide_26.png (시각 검증)

### 회차 노트 (1차 근거, background/note/)

- 01_inventory.md (강의 슬라이드 범위 메타)
- 03_sign_conventions.md (부호 규약 슬라이드 8/13 발췌)
- 06_financial_account_categories.md (FA 5분류, 준비자산 하위 화폐용 금)
- 07_glossary.md 행 119 (개정/강의 미수록), 행 120 (귀금속 보정/강의 미수록), 행 139 (보강 영역 표)
- 12_xlsx_sheet_inventory.md, 12_xlsx_sheet_inventory.csv (Table_BX 행, Table_R1/R2/R3 행)
- 15_units_and_missing.md (결측 카탈로그, GAF 권고 vs 실제 표기)
- 15_missing.csv 행 44 (Notes r23 인용)
- 18_iip_revaluation.md (재평가 3분해는 분기 자료 외, 슬라이드 26 매트릭스 정합성)
- 22_bop_data_sources.md (BoP 다중 자료원 발표 일정, Pink Book 연례 통합 개정)

### 본 저장소 인접 산출물 (db/data/_inventory/)

- 05_meta_text.csv, 05_meta_text.json (Table_BX 메타)
- 06_sign_convention_validation.md (부호 규약 정합성 검증 결과: 100% 일치)
- 12_missing_markers.md, 12_missing_markers.csv (결측 마커 360건)
- 13_missing_meaning_validation.md (결측 의미 검증, x -> 미가용 보정안)
- 13_cdid_dictionary.csv 위치 -- background/note/13_cdid_dictionary.csv (sign_prefix 59 행)
- 16_curriculum_coverage_check.md 5 과잉 커버리지(Table_R1/R2/R3 보존 정당화)
- 18_subtable_curriculum_alignment.md 4.3 (Table_R3 9 부표 학생 분석 권고)

### ONS xlsx 자체 메타 (db/source/balanceofpayments2025q4.xlsx)

- Notes 시트 r5/r29/r33/r42/r51 (sign reverse 진술, 5개 시트 적층)
- Notes 시트 r6/r43 (NEO 정의: converse of HBOG/FKMJ/HBNT)
- Notes 시트 r14 (귀금속 정의: Precious metals includes: Non-Monetary Gold (NMG), Platinum, Palladium and Silver.)
- Notes 시트 r23 (결측 정의: Cells containing [x] represent unavailable data.)
- Table_BX 시트 r1 (Table BX: Current account excluding precious metals [note 1], seasonally adjusted)

### 강의 자료 미수록(별도 web-search 위임 권고)

- 비통화용 금(non-monetary gold)의 BPM6 10/14 정의 본문
- ONS National Accounts Revisions Policy 본문 (open/closed period 정의)
- Pink Book 연간 통합 개정 vs Bulletin 분기 개정 시점 차이 본문
- ONS revision triangle xlsx의 시계열 구조, CDID
- 2025 Bulletin이 적용한 2021년 이후 전 기간 개정 사유 본문
