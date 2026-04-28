# Phase 1.1 - 결측 표기 의미 검증 (강의 자료 1차 근거)

본 문서는 db/CHECKLIST.md 1.1 열세 번째 항목("통계 결측 표기 의미 - 비공개·미산출·적용 불가 - 가 강의 자료에서 어떻게 정의·언급되는지 검증")의 산출물이다. background/ 폴더의 강의 자료(특히 BoP.pptx/BoP.pdf 31장과 1~23회차 노트)를 1차 근거로 삼아 세 의미 카테고리 각각에 대한 강의 자료의 진술을 발췌하고, 12회차에서 검출된 본 xlsx 결측(x 360건)의 강의용 해석 프레임을 정리한다.

## 1. 요지

- 강의 슬라이드 본문(BoP.pptx 31장)에는 통계 결측 표기 자체(x, .., [c], [x], [z] 등)의 의미를 직접 정의·논의한 진술이 없음을 확인 (env/Scripts/python.exe로 31 슬라이드 전 텍스트 추출 후 키워드 매칭 - 매칭은 모두 e[X]ports, [NA]tional, [NA]rrow 등 단어 일부 false positive였음).
- 본 의미 카테고리 3종에 대한 1차 근거는 강의 슬라이드가 아니라 background/note/10_ons_web_research.md 발췌 #9 의 ONS Service Manual / Government Analysis Function(GAF) 공식 권고 인용에서 확보된다. 동 노트는 [c](confidential), [x](not available), [z](not applicable), [low](반올림 0)의 GAF 4분류와 ONS의 legacy ../- 비권장 · NA 모호성 회피 가이드를 정리해 둠.
- 본 xlsx Table_C 6 부표 × 60셀 = 360건 x 마커(1997~1998 EU/non-EU 분해)는 강의 슬라이드에서 직접 다루지 않았으나, xlsx 자체의 메타시트(Notes B23)에 "Cells containing x represent unavailable data." 가 명시(15회차 단계에서 발견·인용 가능). 즉 출처 자체에서는 "비공개"가 아니라 "미가용(not available)" 의미로 라벨링되어 있으며, 10회차의 GAF 매핑([x])에 정합한다.
- 강의 자료가 직접 다룬 가장 가까운 방법론적 프레임은 (a) note/22_bop_data_sources.md ITIS·HMRC OTS·IPS·FDI Survey·BIS 5종 자료원의 표본·발표 시차, (b) note/23_geographic_breakdown.md Brexit 후 EU27 시계열 재계산, (c) note/20_neo_volatility.md 통계 불일치(net errors and omissions)의 잔차 해석. 이 세 자료가 1997~1998 EU 분기 분해가 공표 보류된 배경(조사 시점 표본 부족·Eurostat 분류 호환·EU15→EU27 정의 변경)을 학생에게 설명하는 가장 가까운 프레임이다.
- 결론: 본 인벤토리(12회차)에 등장한 x의 한국어 의미는 xlsx 자체의 메타 정의 "unavailable data" 에 따라 "미가용(not available) - 본 xlsx에서는 1997~1998 EU/non-EU 분해 시계열이 작성·공표되지 않음" 으로 다듬는 것이 1차 근거에 가장 부합한다(Service Manual GAF에서는 [x]에 해당). 12회차 csv의 기존 라벨 "비공개(suppressed) -> [c]"는 Notes B23 발견 이전 단계의 추정이며, 본 검증을 통해 "미가용 -> [x]"로 보정하는 것이 정확하다.

## 2. 세 의미 카테고리별 발췌

본 표는 강의 자료(BoP.pptx + 1~23회차 background 노트) 안에서 세 의미 카테고리 각각에 대해 직접·간접적으로 발견되는 진술을 정리한다. 강의 슬라이드 본문(슬라이드 1~31)에는 결측 표기 의미를 다룬 진술이 0건이며, 모든 1차 근거는 note/10_ons_web_research.md 발췌 #9 및 ONS Service Manual 인용에서 확보된다.

### 2.1 비공개(confidential / suppressed) - 응답 기관 식별 위험으로 공표 보류

| 위치 | 인용 원문(영문) | 한국어 번역·풀이 |
|---|---|---|
| background/BoP.pptx 슬라이드 1~31 본문 | (해당 진술 없음) | 강의 자료 미수록 |
| background/note/10_ons_web_research.md 발췌 표 항목 #9 | "ONS Service Manual: .., - 사용 비권장 -> Government Analysis Function의 표 기호 가이드를 따르고 대괄호 표기[ ] 사용 권고. ... 결측 사유는 별도 열 또는 표지(cover sheet)에 기재." | ONS는 legacy ../- 를 권장하지 않고 GAF의 대괄호 표기를 권고. 결측 사유(예: confidential)는 별도 컬럼·표지에 기록하라고 명시. |
| background/note/10_ons_web_research.md 추가 발견 5번 | "Government Analysis Function 표기 가이드가 ONS 데이터셋 표준임 - 향후 db/data/에서 결측을 Excel 셀에 남길 때 [c](confidential), [low](반올림 0), [x](불가용) 등 대괄호 코드 사용을 검토할 가치." | 비공개 = [c](confidential). 응답 기관 식별 위험으로 공표 보류된 셀에 사용. |
| background/note/15_units_and_missing.md "ONS Service Manual 권고와 실제 표기 차이" 표 | "비공개 / GAF 권장 = [c] / 본 xlsx 실제 = x / legacy 형식 유지" | BoP Bulletin xlsx는 GAF 권장 [c] 미전환 상태이며 legacy x로 통합 표기. |
| db/data/_inventory/12_missing_markers.md (본 Phase 산출물) | "x / 360 / ONS 비공개(suppressed): 응답 기관 식별 위험. GAF 권고 기호 [c]로 단일 통합 가능" | 12회차에서 x를 비공개로 라벨링했으나, 본 검증에서 xlsx Notes B23의 "unavailable data" 정의가 발견되어 보정 권고(4 참조). |

### 2.2 미산출(not available) - 데이터 자체가 작성되지 않음

| 위치 | 인용 원문(영문) | 한국어 번역·풀이 |
|---|---|---|
| background/BoP.pptx 슬라이드 1~31 본문 | (해당 진술 없음) | 강의 자료 미수록 |
| background/note/10_ons_web_research.md 발췌 표 항목 #9 | ".. - 사용을 권장하지 않으며, NA 표현도 모호성 사유로 회피하라는 자체 콘텐츠 가이드를 보유." | ONS legacy 미가용 표기는 ..(점 두 개), -(하이픈)이며 모두 비권장. NA는 "Not Available/Not Applicable" 양 의미로 모호하므로 회피. |
| background/note/10_ons_web_research.md 추가 발견 5번 | "[x](불가용) 등 대괄호 코드 사용을 검토할 가치." | 미가용 = [x](GAF 표기). 데이터 작성 자체가 안된 셀. |
| db/source/balanceofpayments2025q4.xlsx Notes 시트 B23 (15회차 결측 카탈로그에서 추출, 본 12회차에도 적층 인용) | "Cells containing x represent unavailable data." | xlsx 자체의 1차 메타 정의: x는 "unavailable data"(미가용)을 의미한다고 ONS가 명시. -> GAF [x]와 정합. -> 12회차 라벨 "비공개"는 보정 대상. |
| background/note/15_units_and_missing.md 결측 표기 카탈로그 표 | "x / 6 (Table_C) / 360 / ONS confidential / suppressed - EU 1997-1998 비공개" | 15회차는 12회차와 동일하게 "비공개"로 분류했으나 Notes B23 인용은 별도 행("Cells containing x represent unavailable data.")에 그대로 보존되어 있어 보정 가능. |

### 2.3 적용 불가(not applicable) - 항목 정의상 해당 셀에 값이 존재하지 않음

| 위치 | 인용 원문(영문) | 한국어 번역·풀이 |
|---|---|---|
| background/BoP.pptx 슬라이드 1~31 본문 | (해당 진술 없음) | 강의 자료 미수록 |
| background/note/10_ons_web_research.md 발췌 표 항목 #9 (간접) | (적용 불가 = [z] 명시는 발췌 표에 없으나 추가 발견 5번에 [z] 명시 부재) | 강의 자료 미수록(별도 web-search로 위임 권고) - GAF 권고 4기호 중 본 노트는 [c]/[low]/[x]만 인용했고 [z](not applicable)는 명시되지 않음. |
| db/data/_inventory/12_missing_markers.md 결측 표기 종류 표 | "[c] / [x] / [z] / [low] / 0 / GAF 권고 기호 - 본 xlsx 미사용(legacy 형식 유지)" | 12회차는 GAF 4기호를 한 행에 묶어 0건으로 처리. [z](적용 불가)의 정의는 본 인벤토리 어디에서도 직접 인용되지 않음 - 강의 자료 미수록. |
| 강의 자료 슬라이드 26 (note/08_multimodal_slide_analysis.md 인용) | "준비자산이 증가할 경우 국제수지표에서는 음(-)으로 표시하며, 국제투자대조표에서는 양(+)으로 표시" | 적용 불가에 대한 직접 정의는 아니지만, 강의 자료가 다룬 가장 가까운 의미적 인접 사례: BoP에서 준비자산은 "자산 면"에만 정의되고 "부채 면"은 항목 자체가 없음 -> IIP 매트릭스의 "준비자산 부채" 셀은 정의상 비어 있음(이는 GAF의 [z] 적용 불가에 해당하는 개념). 본 도식이 강의 자료 안에서 [z] 의미와 가장 가까운 인접 진술이며, [z] 자체의 정의는 미수록. |

## 3. xlsx Table_C x 360건의 강의용 해석

강의 자료에 결측 표기 의미가 직접 다뤄지지 않았으므로, 본 절은 강의 자료의 가장 가까운 개념(조사 방법론·국제비교·통계 잔차)을 1차 근거로 인용해 학생용 한 단락 설명을 작성한다.

> 본 xlsx의 Table_C(EU/non-EU 분해, 6 부표)에서 1997 Q1 ~ 1998 Q4 기간 8 분기 × 6 부표 = 360셀은 모두 x로 표기되어 있으며, ONS는 동 파일의 Notes 시트 B23에 "Cells containing x represent unavailable data."(셀의 x는 미가용 데이터를 의미)라고 명시한다(즉 "공표 보류"가 아니라 "데이터 자체가 작성되지 않음"). 이 미가용 구간은 두 가지 강의 프레임으로 해석할 수 있다. 첫째, 조사 방법론과 표본 한계 프레임이다. note/22_bop_data_sources.md의 카탈로그에 따르면 BoP는 HMRC OTS(상품무역, 월간), ITIS(서비스무역, 분기, 1990년대 중반 도입), IPS(여행수지, 분기), FDI Survey(연간), BIS 국제은행통계(분기) 5종 자료원의 결합이며, 1997~1998년은 ITIS 분기 조사가 EU·non-EU 분기 분해를 작성할 만큼 표본을 확보하지 못했던 초기 단계로 추정된다. 따라서 EU·non-EU 합계 라인은 분기로 만들 수 있어도, 그 하위(상품·서비스·1차소득·2차소득의 EU/non-EU 분해)는 분기 단위로 신뢰성 있게 작성되지 못했다. 둘째, 국제비교·정의 변경 프레임이다. note/23_geographic_breakdown.md는 Brexit 이후(2020-02-01부터) EU 정의가 EU28 -> EU27로 전환되었고, ONS가 시계열을 EU27 기준으로 일관성 있게 재계산하고 있음을 정리한다. 1997~1998 시점은 EU 회원국이 15국(EU15) 시기였으며, 이를 현행 EU27 정의로 소급 재계산할 수 없는(원자료 부재 또는 회원국 단위 분해 부재) 셀이 다수 발생했을 가능성이 크다. 결론적으로 본 xlsx Table_C x 360셀은 (a) 조사 표본·방법론이 안정화되기 전의 초기 시계열 + (b) 정의 변경(EU15->EU27)으로 인한 소급 재계산 불가가 결합된 미가용 구간으로 해석되며, 이를 ECOS 적재 시 0이나 NaN으로 치환하면 항등식 CA = FA(broad)(슬라이드 14)나 통계 잔차 분석(note/20_neo_volatility.md의 분기당 절대 약 5.9 십억 파운드 NEO)에서 1997~1998 분기를 유효 데이터로 오인하는 오류가 생긴다. 적재 규약은 value_raw="x" + value_numeric=NULL + missing_reason="not_available" (GAF [x]) 3-컬럼 패턴을 권장하며, 분석 단계에서는 동 구간 EU 시계열을 1999 Q1 이후로 한정해 사용하는 것이 강의 자료의 항등식·잔차 프레임과 정합한다.

## 4. 결측 사전(Phase 4 ECOS 결측 사전 시드) 권고

12회차(db/data/_inventory/12_missing_markers.csv)에 등장한 마커 x의 한국어 의미는 본 검증 결과 다음과 같이 다듬는다.

| 마커 | 12회차 라벨(현행) | 본 검증 권고 라벨(보정안) |
|---|---|---|
| x | "비공개(공표 보류) - 응답 기관 식별 가능성" | "미가용(not available) - 1997~1998 EU/non-EU 분기 분해 미작성. 출처 메타(Notes B23): Cells containing x represent unavailable data. Government Analysis Function 권고 기호로는 [x]에 해당." |
| (empty) | "데이터 영역 외(부표 padding) - 결측이 아니므로 ECOS 적재 대상 외" | (변경 없음) |

한 문장 권고: ECOS 결측 사전 시드의 x 의미는 강의 자료의 부속 노트(note/10_ons_web_research.md 발췌 #9 + ONS Service Manual GAF 권고)와 출처 xlsx의 Notes 시트 B23을 1차 근거로 삼아 "미가용 데이터(not available, GAF [x]) - 본 BoP Bulletin에서 1997~1998 분기 EU/non-EU 분해 시계열이 작성되지 않은 셀" 로 표기하며, "비공개(suppressed, [c])"·"적용 불가(not applicable, [z])"와는 의미가 다르므로 단일 라벨로 통합하지 않는다.

## 5. 출처

### 강의 자료 1차 근거 (background/)

- background/BoP.pptx 슬라이드 1~31 (본문 텍스트 추출 - 결측 표기 의미 직접 진술 0건 확인)
- background/BoP.pdf 31 페이지 (PDF 본 - 동일)
- background/slide_images/slide_26.png (강의 자료가 다룬 가장 가까운 인접 개념 = "준비자산이 증가할 경우 국제수지표에서는 음(-), 국제투자대조표에서는 양(+)" 도식. note/08_multimodal_slide_analysis.md 슬라이드 26에서 인용)
- background/note/01_inventory.md (BoP.pptx 메타·구성 인벤토리)
- background/note/03_sign_conventions.md (부호 규약 슬라이드 8~14 발췌)
- background/note/08_multimodal_slide_analysis.md (빈 슬라이드 멀티모달 분석 - 슬라이드 26 매트릭스 도식 발견)
- background/note/10_ons_web_research.md 발췌 표 항목 #9, 추가 발견 5번 (ONS Service Manual / GAF 권고 1차 근거)
- background/note/15_units_and_missing.md (xlsx 단위·결측 카탈로그, 15회차 광역 검사)
- background/note/15_missing.csv 행 44 (Notes 시트 B23 인용: "Cells containing x represent unavailable data.")
- background/note/20_neo_volatility.md (NEO 잔차 변동성 - 분기당 절대 약 5.9 십억 파운드)
- background/note/22_bop_data_sources.md (HMRC OTS·ITIS·IPS·FDI·BIS 5종 자료원의 표본·발표 시차)
- background/note/23_geographic_breakdown.md (Brexit EU28->EU27 정의 전환·시계열 재계산)

### 본 인벤토리 산출물 (db/data/_inventory/)

- db/data/_inventory/12_missing_markers.md (Phase 1.1 12회차 산출물 - 본 검증의 직접 입력)
- db/data/_inventory/12_missing_markers.csv (6행, x 360건 위치 카탈로그)

### 빠진 부분 (강의 자료 미수록 -> 별도 위임 권고)

- GAF 4기호 중 [z](not applicable)의 정의: note/10_ons_web_research.md 추가 발견 5번이 [c]/[low]/[x]만 인용하고 [z]는 명시하지 않음. 강의 슬라이드에서도 적용 불가 의미의 직접 정의는 없음. -> 별도 web-search로 위임 권고(GAF Tables in Statistics 가이드 또는 ONS Service Manual의 [z] 정의 페이지 직접 인용 필요).
- xlsx Notes B23의 정확한 작성 의도(공표 보류 vs 작성 불가의 구분 - ONS가 동일 시기 BoP 자료에서 x를 양 의미로 사용한 이력 여부): 강의 자료 미수록. -> 별도 web-search로 위임 권고.
- 1997~1998 EU 분해 시계열 미가용의 공식 사유 문서: note/22_bop_data_sources.md·note/23_geographic_breakdown.md의 일반 설명만 있고, ONS Pink Book 또는 BoP QMI 본문에서 동 구간 미가용을 명시한 문구는 미확보. -> 별도 web-search로 위임 권고.
