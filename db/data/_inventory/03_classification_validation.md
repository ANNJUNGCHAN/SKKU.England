# Phase 1.1 — 시트 7분류의 강의 자료 정합성 검증

본 문서는 PLAN.md Phase 1.1 세 번째 항목("위 7분류가 강의 자료의 BoP 분류 체계와 일치하는지 검증. 강의 자료에 없는 분류(예: 개정 시트)는 별도로 표시")의 산출물이다.

## 요약

- 강의 자료(`background/BoP.pptx`)는 BoP를 **경상계정 / 자본계정 / 금융계정** 3대 축 + **종합수지(잔액)** + **국제투자대조표(IIP)** 로 분류하며, 이는 본 인벤토리의 7분류 중 `summary`, `current_main`, `current_detail`, `capital_financial`, `iip` 5개와 직접 대응한다.
- 반면 `meta_notes`(메타·주석)와 `revisions`(직전 발표 대비 개정)는 강의 자료에 명시적 분류로 등장하지 않는, **ONS 발표물 운영상 발생하는 분류**다.
- 강의 자료의 **종합수지(Overall balance of payment, 슬라이드 12)** 가 ONS의 `Table_A`(전체 잔액 요약)에 해당하는 것으로 매핑할 수 있어, `summary` 분류명은 강의의 "종합수지" 또는 "전체 잔액 요약"으로 부연 표기하면 정합성이 높아진다.
- 결론: 7분류 중 5개는 강의와 직접 일치, 2개(`meta_notes`, `revisions`)는 강의에 없는 운영성 분류로 별도 명기 필요.

## 7분류별 강의 자료 매핑 표

| 코드 | 한국어 명칭 | 강의 자료 인용(슬라이드) | 강의 자료의 명칭 | 일치도 |
|---|---|---|---|---|
| `meta_notes` | 메타·주석 | — (강의 자료 미수록) | (없음) | **없음** |
| `summary` | 전체 잔액 요약 | 슬라이드 12 "제2절 국제수지의 종류: 종합수지 (Overall balance of payment)"; 슬라이드 9의 "우리나라의 국제수지표(2017년)" 표 전체(경상·자본·금융수지·오차누락이 한 표에 적층) | 종합수지 / 공적결제수지 (Official settlement balance) | **부분일치** (개념은 존재하나 ONS의 `Table_A` 같은 "Summary" 표 명칭은 미사용) |
| `current_main` | 경상수지 본표 | 슬라이드 5 "1) 경상계정(Current account): 재화 및 용역의 실물거래 기록" + 4개 하위; 슬라이드 10 "제2절 국제수지의 종류: 경상수지"; 슬라이드 14 항등식 `Current account = trade balance + balance on services + net primary income + net secondary income` | 경상수지(Current account) | **일치** |
| `current_detail` | 경상수지 세부 | 슬라이드 5의 4개 하위항목(상품수지·서비스수지·본원소득수지·이전소득수지) 정의 — 각 항목이 ONS Table_E~H(Trade in goods/services/Primary income/Secondary income)에 1:1 대응 | 상품수지·서비스수지·본원소득수지·이전소득수지 | **일치** (강의는 "본표 vs 세부"라는 ONS식 분리는 하지 않으나, 4개 하위 분해는 동일) |
| `capital_financial` | 자본·금융계정 | 슬라이드 5 "2) 금융계정(Financial account)" + 5개 하위(직접·증권·파생·기타·준비자산); 슬라이드 6 "3) 자본계정(Capital account)"; 슬라이드 11 "제2절 국제수지의 종류: 금융수지"; 슬라이드 14 식 `Financial account = Net acquisition of foreign financial assets − Net incurrence of liabilities + Net financial derivatives` | 자본계정(Capital account) + 금융계정(Financial account) | **일치** (단, 강의는 두 계정을 분리해서 다루며 "자본·금융계정"으로 묶은 합성 명칭은 사용하지 않음 → ONS Table_I/J 통합 처리에 부합) |
| `iip` | 국제투자대조표 | 슬라이드 4 "참고: 국제투자대조표(international investment position; IIP)는 일정한 시점에서 일국의 대외자산 및 부채를 기록한 스톡(stock)개념"; 슬라이드 25 "국제수지(B.O.P) vs 국제투자대조표(IIP)" — "B.O.P는 flow 통계, IIP는 stock 통계" | 국제투자대조표(IIP) | **일치** |
| `revisions` | 직전 발표 대비 개정 | — (강의 자료 미수록) | (없음) | **없음** (cf. `background/note/07_glossary.md`: "ONS 분기별 사후 개정. 강의 자료 미수록, ONS 표준") |

## 강의 자료에 없는 분류 목록

1. **`meta_notes` (메타·주석)** — Cover_sheet / Notes / Records 3개 시트 대상. 강의 자료는 데이터 파일의 메타 영역(표지·각주·기록 시트)을 다루지 않는다. ONS 발표 xlsx 운영상 필수 분류이므로 강의 분류 체계 밖이지만 데이터 인벤토리 차원에서는 유지 필수.
2. **`revisions` (직전 발표 대비 개정)** — Table_R1/R2/R3 3개 시트 대상. 강의 자료는 BoP의 항등식·구성·flow vs stock 같은 개념 정의에 집중하며, ONS의 분기별 사후 개정(revision triangles, 12개월 사전공개 정책)에는 침묵한다.
3. **`summary` (전체 잔액 요약) — 부분일치 주의** — 강의의 "종합수지"(슬라이드 12)는 *경상+자본+금융(준비자산 제외)* 의 합으로 정의되는 **수지 개념**이며, ONS의 `Table_A`처럼 "모든 잔액을 한 표로 요약"하는 **표(table) 개념**과는 결이 다르다. 분류명 자체는 ONS 명세에 충실하되, 보조 설명에 "강의 자료의 종합수지(Overall balance) 개념이 함께 적층된 요약표"라고 부기 권고.

## 강의 자료와 본 분류의 미세 차이

- 강의는 **자본계정과 금융계정을 분리**해서 다루지만(슬라이드 5의 1)/2)/3) 구조), 본 인벤토리는 ONS Table_I/J 두 시트를 함께 묶어 `capital_financial` 단일 분류로 처리. → ONS Pink Book 챕터 7~8(자본·금융)의 실무 분류에 부합하므로 통합 자체는 정당하나, **강의 분류와 1:1 대응이 아님**을 인벤토리 메모에 명기 필요.
- 강의는 **"본표 vs 세부"** 라는 ONS식 분리(`current_main` vs `current_detail`)를 사용하지 않음. ONS Table_B/BX/C(요약 본표) vs Table_E~H(EBOPS·기능별 세부)의 운영상 구분이며, 강의 분류 체계에는 없는 ONS 고유 층위.

## 보강 권고

1. **본 검증 문서에 "강의 분류 vs ONS 분류" 매트릭스 명기** — 5개 일치 분류는 강의 슬라이드 번호를 함께 적어 학생이 추적 가능하게.
2. **`meta_notes`와 `revisions`에는 "ONS 발표물 운영성 분류(강의 자료 외)" 표지** 부착 — 학습용 분석 대상에서 제외할지 판단 근거로 활용.
3. **`summary` 분류명에 "= 강의의 종합수지(Overall BoP) 개념을 표로 요약"이라는 보조 라벨** 추가 — 슬라이드 12 인용으로 정합성 강화.
4. **`capital_financial` 분류는 강의에서 두 계정으로 분리됨**을 메모로 부기 — 후속 분석에서 `Table_I`(자본계정)와 `Table_J`(금융계정)를 별도 처리할 가능성 열어둠.
5. 강의 자료에서 다루지 않는 ONS 고유 층위(본표 vs 세부, EBOPS 12분류, revision triangles)는 `background/note/10_ons_web_research.md`·`07_glossary.md`로 보완 가능 — 이미 본 저장소에 정리되어 있으므로 검증 문서에서 교차 참조만 추가하면 충분.

## 관련 절대경로

- 1차 근거: `background/note/02_bop_components.md`, `background/BoP.pptx` (슬라이드 4~14, 25)
- 검증 대상: `db/data/_inventory/02_sheet_classification.csv`
- 보조 근거: `background/note/07_glossary.md`, `background/note/12_xlsx_sheet_inventory.md`
- 슬라이드 이미지: `background/slide_images/slide_04.png` ~ `slide_14.png`, `slide_25.png`
