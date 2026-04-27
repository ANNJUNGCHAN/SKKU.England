# Phase 1.1 — EU/non-EU 분해(Table_C) 강의 자료 점검

본 문서는 PLAN.md Phase 1.1 네 번째 항목("EU/非EU 분해 시트의 경제학적 의미를 강의 자료에서 확인")의 산출물이다.

## 요약

- **강의 자료(`background/BoP.pptx` 31장)는 BoP의 지리적·국가별 분해를 다루지 않는다.** 31장 전체 텍스트와 PDF 추출본을 키워드로 전수 검색한 결과 "EU", "non-EU", "geographical", "Brexit", "USA", "China", "지리분해", "국가별" 어느 것도 본문에 등장하지 않음.
- 슬라이드 4의 정의문이 "with the rest of the world"라는 단일 카운터파트로 표현하고, 슬라이드 4의 부주("지리적 거주지보다는 경제활동의 본거지가 중요")는 거주자(resident) 개념을 강조할 뿐 **지리분해와는 무관**.
- 슬라이드 9의 한국 2017년 사례 표도 경상·금융·자본·오차누락의 **수직 분해만 제공**, 국가·지역 축은 없음.
- 따라서 ONS Table_C의 EU/non-EU 2분 축은 **강의 자료가 다루지 않는 영역**이며, ONS Pink Book Ch.9(지리분해 데이터셋)과 Brexit 후 EU27 재정의 맥락에서만 의미를 가지는 **운영 표기**임.

## 키워드 검색 결과 표

| 키워드 | BoP.pptx | BoP.pdf | 비고 |
|---|---|---|---|
| `EU` | 0건 | 0건 | 강의 자료 어디에도 등장하지 않음 |
| `non-EU` | 0건 | 0건 | — |
| `geographic`/`Geographic` | 0건 | 0건 | — |
| `Brexit` | 0건 | 0건 | — |
| `USA`/`China`/`미국`/`중국`(국가명) | 0건 (정의·예시) | 0건 | 슬라이드 30 포트폴리오 접근법 본문은 "US assets/foreigners"로 일반화된 표현(특정 양자관계 분해 아님) |
| `country`/`countries` | 1건 (슬라이드 4 일반 정의) | 동일 | "Record of a country's trade ... with the rest of the world" — 단일 거주국 vs 세계 전체 |
| `world` | 1건 | 동일 | "rest of the world" 단일 카운터파트 |
| `지리` | 1건 (슬라이드 4) | 동일 | "지리적 거주지보다는 경제활동의 본거지" — 거주자 개념(BPM6 §4)이지 지리분해 아님 |
| 슬라이드 9 한국 2017년 표 | — | — | 경상·자본·금융·오차누락 4행 합계만, 국가별 열 없음 |

## 강의 자료 vs ONS Table_C 의의 비교

| 측면 | 강의 자료(BoP.pptx) | ONS Table_C |
|---|---|---|
| 분해 축 | **수직(항목별)** 만: 경상수지 4분 + 금융계정 5분 + 자본수지 + 오차누락 | **수평(지역별)** 추가: EU vs non-EU × (상품·서비스·1차·2차소득) |
| 카운터파트 | "rest of the world" 단일 합계 | EU27 vs non-EU27 2분 |
| Brexit 영향 | 언급 없음 | 2020-02-01 부로 EU28→EU27 재정의, 시계열 일관성 위해 과거 구간도 EU27으로 재계산(`background/note/23_geographic_breakdown.md` §2) |
| 학습 목적 | BoP 정의·항등식·접근법 | ONS 운영상 통합 무역권 노출도 모니터링(분기 EU 의존도 추적) |
| Pink Book 매핑 | 해당 없음 | Pink Book Ch.9(지리분해)의 EU 합계 라인을 분기로 디스어그리게이션(`background/note/23_geographic_breakdown.md` §4) |

## 학생용 학습 활용 권고

1. **수업 범위에서는 Table_C를 부속 자료로 안내하되 핵심 분석 대상은 Table_A·B**(전체 BoP, 항등식 검증)로 제한 권고. 강의가 다루는 5대 구성요소·항등식·접근법은 EU/non-EU 축과 직교(orthogonal)이므로 핵심 학습목표 달성에는 불필요.
2. **추가 학습 욕구가 있는 학생**에게는 (a) Pink Book Ch.9 67개국 분해 데이터셋 안내, (b) Brexit 전후 EU 정의 변경(EU28→EU27)을 사례로 한 **시계열 단절·재정의 이슈**를 부교재로 제시. 이는 강의의 "사후적 항등식 검증"과 다른 차원의 이슈(분류 체계 변경의 통계적 처리)임.
3. **영국 BoP 분석 보고서 작성 시**: Table_C는 본문이 아니라 **부록(Appendix) 또는 한정된 참고**로 다루고, 항등식·접근법 분석 본문에는 Table_A/B를 사용하는 것이 강의 프레임과 일치.

## 빠진 부분

- 강의 자료에 영국 ONS 또는 Pink Book Ch.9·10 자체에 대한 명시적 언급이 없어, EU/non-EU 분해의 학습적 위치 부여는 본 폴더 자료만으로는 불가. 보완하려면 **ONS Balance of Payments QMI**(방법론) 또는 **Pink Book 2025 본문 §9**의 한국어 요약 자료를 `background/`에 추가 권고.
- Brexit가 분류 체계에 미친 영향에 대한 강의용 한국어 보충 자료(`background/note/23_geographic_breakdown.md`이 사실 정리 수준)는 학생 친화 형식(슬라이드/요약표)이 아직 없음.

## 관련 절대경로

- 1차 근거: `background/BoP.pptx`(31장 전체), `background/BoP.pdf`
- 슬라이드 9 한국 사례 이미지: `background/slide_images/slide_09.png`
- 강의 자료 인벤토리: `background/note/01_inventory.md`, `background/note/08_multimodal_slide_analysis.md`
- ONS 지리분해 1차 정리: `background/note/23_geographic_breakdown.md`
- 시트 인벤토리(Table_C 메타): `background/note/12_xlsx_sheet_inventory.md`
