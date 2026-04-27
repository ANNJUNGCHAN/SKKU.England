# Phase 1.1 — 강의 자료 GDP 대비 비율 표기 점검

본 문서는 PLAN.md Phase 1.1 열 번째 항목("강의 자료에서 GDP 대비 비율 표기의 통상적 해석 방식 확인")의 산출물이다.

## 요약

- 31장 강의 자료 중 BoP 항목을 **GDP 대비 비율로 명시·시각화하는 장표는 슬라이드 15(Korea CA/GDP, FA/GDP) 한 장 뿐**이다. 이 차트는 항등식 `CA = FA(broad)`(슬라이드 14)를 25년 한국 분기 데이터로 시각 검증하기 위한 보조 그림이며, GDP 정규화 자체에 대한 해설(분모 정의·기간 처리·임계 비율 등)은 본문에 없다.
- 슬라이드 22·23·24의 NIA·저축-투자·통화 항등식은 **모두 절대량(level)** 으로만 적혀 있고, GDP로 양변을 나눈 정규화 형태는 등장하지 않는다.
- ONS Table_B/BX/R2의 4번째 부표(% of GDP)는 강의 자료가 **다루지 않는 영역**이므로, 강의 슬라이드 15의 한국 사례 해석을 영국에 그대로 이식할 때 분모(YBHA)·기간(분기 vs 연간)·계절조정 차이를 별도로 명시할 필요가 있다.

## GDP 대비 비율 등장 위치 (강의 자료)

| 슬라이드 | 내용 | GDP 비율 표기 형태 | 비고 |
|---|---|---|---|
| 15 | Korea CA/GDP, FA/GDP 군집막대(2000~2025) | y축 −1.00%~8.00% | 연간 추정, 분모 GDP 출처·종류 미명시 |
| 16~21 | 한국 CA·FA·준비자산·FDI/Portfolio·무역수지 차트 | **모두 USD 백만 단위**(절대량) | GDP 정규화 없음 |
| 22 | NIA 항등식 `Y = C+I+G+(X−M)` | level 식 | GDP는 좌변 Y로만 등장 |
| 23 | `CA = S − I = Spriv + Spub − I` | level 식 | %GDP 변환 없음 |
| 24 | `(X−IM) = ΔNFA`, `ΔNFA + ΔDC = ΔH` | level 식 | %GDP 변환 없음 |
| 25~26 | BoP↔IIP flow/stock 매트릭스 | 잔액·증감(절대량) | %GDP 표기 없음 |

본문 텍스트에는 "GDP" 문자열이 등장하지 않으며, GDP는 오직 **슬라이드 15 차트의 축·범례 텍스트(이미지 내부)**에서만 확인된다.

## 강의 자료에서 다뤄지지 않는 부분

1. **CA/GDP, FA/GDP의 임계 비율 해석**(예: −3% 또는 −5% 경계, IMF/EU 거시건전성 가이드)에 대한 언급 전무.
2. **만성 적자국 vs 흑자국 분류 기준**, "구조적 흑자국(독일·한국)" 같은 비교 프레임 부재. 한국 사례(슬라이드 15)는 양(+) 흑자만 시각화되며, 영국형 만성 적자국 케이스는 차트로 제시되지 않음.
3. **분모 GDP의 정의**(명목 vs 실질, 분기율화, 4분기 이동합 vs 단일 분기, current/chained price)에 대한 설명 없음.
4. **재정연도(FY) vs 캘린더년 차이**, 분기 GDP 계절조정(SA) 여부에 따른 비율 산출 차이도 강의 자료 미수록.
5. **NIA 항등식의 비율 변환**(`y = c+i+g+nx` where `nx = NX/Y`)이나 **저축률·투자율 정의**(`s = S/Y`)도 강의에 없음.

## ONS Table_B/BX/R2 4번째 부표(% of GDP) 해석 권고

- ONS Notes 시트 B10 메모: "Using series YBHA, GDP at current market prices" → **명목 GDP(현행 시장가, YBHA)** 사용.
- Table_B.4 / Table_BX.4 / Table_R2.4 모두 상품·서비스·1차소득·2차소득·경상수지 5종을 GDP 대비로 산출.

권고:

1. **분자·분모 일관성 명시**: REPORT.md BoP 비율 분석 시 "분자=BoP 항목(SA, £million), 분모=YBHA(NSA, £million 현행가)"를 표로 적시. ONS 4번째 부표가 이미 산출해 둔 값을 1차로 인용하고, 2차 가공 시 동일 분모를 사용한다고 선언.
2. **강의 슬라이드 15 비교 차트**를 영국 버전으로 재현(영국 CA/GDP, FA/GDP)할 때, 한국과 달리 영국은 양 계열이 음(−)으로 머무는 **만성 적자/순차입국**임을 명시 — 강의 자료가 보여준 "두 계열이 거의 같다"는 항등식 검증 메시지는 부호만 반대(둘 다 −2~−4%)로 동일하게 성립.
3. **임계 비율은 강의 외 출처**(IMF EBA, EU MIP −4%/+6%) 인용 시 별도 각주로 분리 — 강의 자료에는 근거 없음.
4. **분기 vs 연간 표기 통일**: ONS 분기 % of GDP는 분기 BoP/분기 YBHA(연율화 X)이므로, 강의 슬라이드 15(연간) 대비 절대 수치 폭이 달라질 수 있음을 주석.

## 빠진 부분 / 추가 자료 후보

- 강의 슬라이드 15가 사용한 **한국 GDP 분모 출처**(BOK ECOS YBHA 대응 시리즈 추정)가 자료 어디에도 명시되지 않음 → 영국 사례와 1:1 비교 시 가정으로 보충.
- IMF EBA·EU MIP scoreboard 같은 **국제기관 임계치 자료**가 background에 없음 → 필요 시 web-search 위임.

## 관련 절대경로

- `background/BoP.pptx`, `background/BoP.pdf` (슬라이드 14·15·22·23·24)
- `background/slide_images/slide_15.png` (Korea CA/GDP, FA/GDP 차트)
- `background/note/08_multimodal_slide_analysis.md` (슬라이드 15 시각 분석)
- `background/note/04_identities.md` (항등식 표 5a/5b/5c)
- `background/note/12_xlsx_sheet_inventory.md`, `13_cdid_dictionary.csv` (Table_B/BX/R2 4번째 부표 매핑)
- `background/note/15_missing.csv` (B10: YBHA 분모 메모)
