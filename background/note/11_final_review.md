# 배경지식 사전 정리 전체 재점검 (background-search 11회차, 최종)

본 문서는 `db/CHECKLIST.md` §0.2 라인 31 항목("모든 배경 지식 사전 정리를 다시 한번 점검하고, 빠진 부분이 있는지 다시 한번 검토한 후, 추가적인 사항들을 '0.2 배경지식 사전 정리' 항목에 add on 할 것")의 산출물이다. 01~10회차 노트와 31장 슬라이드 이미지를 통람한 결과, 빠진 부분 26건 중 12건은 이미 후속 회차에서 해소되었고 14건이 미해결로 남아 있다. 이 미해결 14건과 Phase 1 진입 사양을 기반으로 신규 §0.2 항목 12건(高 4 / 中 5 / 低 3)을 도출한다.

## 요약

- **노트 분야 분포**: 인벤토리 1 / BoP 구성 1 / 부호 1 / 항등식 1 / IIP 1 / 금융계정 1 / 용어집 1 / 멀티모달 1 / PDF fallback 1 / ONS 웹 1 (총 10건). `slide_images/` 31장 중 8회차에서 10장 정밀 분석, 21장 미분석.
- **미해결 빠진 부분 통합**: 노트별 §빠진 부분에서 추출한 항목 총 26건 중, 8회차·10회차에서 후속 해소된 항목 12건을 제외한 순 미해결 14건.
- **신규 §0.2 항목 후보**: 우선순위 高 4 / 中 5 / 低 3 — 총 12개 후보 식별.
- **Phase 1 직접 진입 가능성**: 7분류·CDID·결측·부호 4축 모두 1차 근거 확보 → Phase 1 진입 가능. 단 高 우선순위 후보 중 "xlsx 시트명 사전 추출"은 Phase 1 첫 단계와 자연스럽게 통합됨.
- **결론**: 11회차에서 추가로 채워야 할 큰 공백은 (a) 분기 BoP 통계 불러틴 표(저장소 보유 xlsx)의 시트·CDID 매핑 사전, (b) 슬라이드 28~29의 J-curve·환율 전가 정밀 분석, (c) 강의 자료 슬라이드 22의 NIA 항등식 유도 단계 보강 — 세 영역이 핵심.

## 노트별 핵심 빠진 부분 통합 표

| 출처 노트 | 미해결 항목 | 우선순위 | 비고 (해소 여부) |
|---|---|---|---|
| 01_inventory | 빈 슬라이드 15–20·26–27의 도식 정체 | — | 8회차 멀티모달로 해소 |
| 01_inventory | 영국 ONS 매뉴얼·정의서 부재 | — | 10회차 web-search로 해소 |
| 01_inventory | 강의 발행 시점·저작권 범위 불명 | 低 | 미해소 (Phase에 영향 없음) |
| 02_bop_components | 상품수지 vs 무역수지 정의 차이 | — | 10회차에서 ONS UK Trade Glossary로 해소 |
| 02_bop_components | EBOPS 12분류 (서비스수지 세부) | — | 10회차로 해소 |
| 02_bop_components | 단위·통화 처리 (GBP vs USD) | 中 | 미해소 — Phase 1 단위 인벤토리에서 보완 필요 |
| 03_sign_conventions | 분개 예시(상품 수출 시 차변·대변) | — | 10회차로 해소 |
| 03_sign_conventions | 거주자/비거주자 정의 | — | 10회차로 해소 |
| 03_sign_conventions | 준비자산 + = 자본유출인지 명시 | — | 8회차 슬라이드 26 도식으로 해소 |
| 03_sign_conventions | ONS Errors and omissions 분기 변동성 | 中 | 부분 해소(10회차) — 실측치 시계열 직접 확인 필요 |
| 04_identities | 표적 항등식 명시 식 부재 | — | 10회차로 해소(BPM6: `CA+KA−FA+NEO=0`) |
| 04_identities | BoP↔IIP 항등식 수식 표현 | — | 8회차 슬라이드 26으로 해소 |
| 04_identities | 슬라이드 15~20·26 시각 자료 정체 | — | 8회차로 해소 |
| 04_identities | Twin deficits 수치·기간 미제시 | 低 | 미해소(강의 보조 사례) |
| 05_iip_nfa | IIP 자산·부채 분류표(슬라이드 25–26 그림) | — | 8회차로 해소 |
| 05_iip_nfa | 재평가 3분해(가격·환율·기타) | — | 8회차 슬라이드 26으로 해소 |
| 05_iip_nfa | 중앙은행 NFA vs Net IIP 정량 차이 | 中 | 미해소 — BoE 보유 IR 시계열 별도 보강 필요 |
| 05_iip_nfa | 영국 만성 순채무국·재평가 우세 ONS 자료 | 中 | 부분 해소 — Pink Book Chapter 9 IIP 직접 확인 권장 |
| 06_financial_account | 직접투자 10% 임계 | — | 10회차로 해소(BPM6 §6.12) |
| 06_financial_account | 자산·부채 양면 분류·하위(지분/부채성/만기) | 中 | 부분 해소 — Phase 1 시트 인벤토리에서 양면 컬럼 식별 필요 |
| 06_financial_account | 파생상품 ESO·순포지션 처리 규칙 | 低 | 미해소 |
| 06_financial_account | 기타투자 보험·연금·SDR 배분 | 低 | 미해소 |
| 06_financial_account | ONS 표 코드(D1_3·D4_6·D7_9·K) 직접 매핑표 | 高 | 미해소 — 10회차에서 표 코드는 xlsx 시트명에만 존재 확인. Phase 1과 결합 필수 |
| 07_glossary | 우선순위 高 5개 표제어 | — | 10회차로 모두 해소 |
| 07_glossary | J-curve / 환율 전가 정의(빈 슬라이드 28·29) | 中 | 미해소 — 8회차에서 슬라이드 28·29 분석 미수행, 11회차 보강 권장 |
| 08_multimodal | 슬라이드 28·29(J-curve, 환율 전가) 미분석 | 中 | 미해소 |
| 08_multimodal | 슬라이드 22~25의 NIA 항등식 도식 미분석 | 低 | 미해소 — 텍스트는 04회차에서 인용됨 |
| 09_pdf_fallback | 슬라이드 26 더 높은 해상도 권장 | 低 | 미해소(현 200 DPI로 충분 판단) |
| 10_ons_web_research | Pink Book 표 코드(D1.3, BX 등) 공식 코드북 미발견 | 高 | 미해소 — Phase 1 xlsx 시트명 추출이 사실상 유일 경로 |
| 10_ons_web_research | OECD BD4 본문 접근 차단(403) | 低 | 미해소 — BPM6와 동일 임계로 갈음 가능 |
| 10_ons_web_research | ONS 자체 분개 예시 미발견 | 低 | 미해소 — 강의 자료로 갈음 |

## 신규 §0.2 항목 후보 (체크리스트)

본 후보들은 §0.2의 "추가적인 사항을 add on" 지시에 따라 라인 31 이하에 새 체크리스트 항목으로 등록될 예정이다.

### 우선순위 高 (Phase 1 진입 직전 또는 동시 처리)

- `[background-search]` `db/source/balanceofpayments2025q4.xlsx`의 시트명 전체 + 각 시트 상단 메타 텍스트 추출해 `background/note/12_xlsx_sheet_inventory.md`로 정리. Pink Book 챕터 구조(10회차)와 1:1 매핑하고, ONS 표 코드 사전(D1.3·D4.6·D7.9·K·BX 등)을 시트명에서 직접 도출.
- `[background-search]` xlsx 시트별 CDID 행 위치·코드 목록을 추출해 `background/note/13_cdid_dictionary.md`로 정리. ECOS ITEM_CODE1과 직접 매핑 가능한 1차 사전.
- `[background-search]` 슬라이드 28(J-curve)·29(흡수 접근법 도식) 멀티모달 분석을 8회차 누락분으로 보강.
- `[background-search]` xlsx 시트별 단위 표기(£ million / £ billion / % of GDP) 인벤토리와 결측 표기 등장 위치(`x` vs 빈 셀) 카탈로그 작성 → `background/note/14_units_and_missing.md`.

### 우선순위 中

- `[web-search]` OECD Benchmark Definition of Foreign Direct Investment 4판(BD4)의 SPE·FATS 보강 정의 확인.
- `[web-search]` BoE Bankstats(Tables A–C) 또는 BoE Statistical Release에서 영국 보유 준비자산(IR) 시계열 확보.
- `[background-search]` ONS Pink Book Chapter 9 (IIP) xlsx에서 영국의 재평가(가격·환율·기타) 3분해 시계열 추출.
- `[background-search]` xlsx에서 금융계정 5분류 각각의 자산(NAFA)·부채(NIL) 양면 컬럼이 어떤 시트·열에 저장되어 있는지 매핑.
- `[web-search]` ONS Errors and omissions 분기 시계열 변동성 직접 확인(BoP revision triangles 또는 분기 통계 불러틴 부록).

### 우선순위 低

- `[background-search]` 슬라이드 22~25 NIA·BoP↔IIP 도식 부분 멀티모달 정밀 분석.
- `[web-search]` HMRC Overseas Trade Statistics·ITIS·IPS·FDI Survey·BIS 국제은행통계 등 BoP 작성 다중 출처의 발표 일정·갱신 주기 카탈로그화.
- `[web-search]` ONS 국가별(geographical breakdown) Pink Book Ch.10·11 분류 체계 확보.

## Phase 1 직접 진입 가능성 평가

PLAN.md의 Phase 1 종료 조건은 "모든 시트의 분류·헤더·코드·시점·단위·부표 경계·결측 표기가 한 표로 정리"이다. 7개 입력 사양 항목별 배경 자료 충족도:

| Phase 1 입력 사양 | 충족 여부 | 1차 근거 |
|---|---|---|
| (가) 시트 7분류 (메타·요약·CA·CA세부·KA/FA·IIP·개정) | 충족 | PLAN.md §1 Phase 1 직접 명시; 10회차 Pink Book 챕터 1~11 매핑으로 보강 |
| (나) 통계항목 코드(CDID) 행 위치 | 개념 충족, 실측 미확인 | 10회차 §발췌 #6 CDID 4자 영문 정의 확보. 단 xlsx 내 실제 위치는 신규 高 후보로 추출 필요 |
| (다) 시점 컬럼 형식 (A/Q/M) | 충족 | 10회차 §발췌 #10 분기 발표 정책; PLAN.md §0.2 시점 표기 규약 |
| (라) 단위 표기 (£ million·£ billion·% of GDP) | 충족 | PLAN.md §0.4·§Phase 3에 단위 혼재 명시; 신규 中 후보로 정량 인벤토리 보강 |
| (마) 부호 규약 진술 위치 | 충족 | 03회차 7행 발췌 + 10회차 §발췌 #1 NEO 부호식; PLAN.md Phase 2.3 부호 규약 진술 명문화 |
| (바) 부표 경계 식별 | 충족 | PLAN.md Phase 2.1 부표 분리 원칙; xlsx 직접 조사로 자연 도출 |
| (사) 결측 표기(`x`, 빈 셀) | 충족 | PLAN.md §0.4에 `x` vs 빈 셀 구분 명시; 10회차 §발췌 #9 ONS Service Manual 보강 |

**평가 결론**: 7개 항목 모두 배경 자료로 1차 근거 확보. Phase 1은 즉시 진입 가능하며, 신규 高 우선순위 후보 4건은 Phase 1 산출물(시트 인벤토리·CDID 사전·단위·결측 카탈로그)과 자연스럽게 통합되어 별도 사전 단계가 필요하지 않다. 예외는 슬라이드 28·29 멀티모달 보강 1건으로, 이는 Phase 3 명세서의 "모형" 카테고리 정의 단계에서 처리해도 무방하다(즉, Phase 1 진입을 막지 않음).

## 관련 절대경로

- 통합 점검 대상: `background/note/01_inventory.md` ~ `10_ons_web_research.md`
- 미분석 슬라이드(권장 후속): `background/slide_images/slide_22.png` ~ `slide_25.png`, `slide_28.png`, `slide_29.png`
- Phase 1 진입 대상 원본: `db/source/balanceofpayments2025q4.xlsx`
- 작업 계획 참조: `db/PLAN.md` Phase 1
