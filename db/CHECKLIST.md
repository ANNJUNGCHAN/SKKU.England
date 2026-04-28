# 개발 체크리스트

본 문서는 `db/PLAN.md`를 실제로 구현할 때 단계별로 점검해야 할 항목들의 체크리스트이다. 모든 항목은 PLAN.md의 원칙(값 불변, CSV 전용 저장, 1 CSV = 1 평면 표, ECOS 필드 정렬, 한국어 문서)을 전제로 한다.

**배경지식 활용 원칙**: 도메인 판단·정의·해석·검증이 필요한 모든 지점에서 `background-search` 서브에이전트를 1차로 호출한다. `background/` 폴더의 강의 자료(`BoP.pptx` 등)를 우선 근거로 삼고, 결과물을 출처와 함께 인용한다. 강의 자료에서 답이 나오지 않는 항목만 별도로 `web-search` 서브에이전트에 위임한다.

---

## 0. 사전 준비 (환경·배경지식 점검)

### 0.1 환경
- [x] 저장소 루트의 가상환경 인터프리터(`env/`)가 활성화되어 있는지 확인 — 확인 완료(`env/Scripts/python.exe`, Python 3.12.10, venv 활성)
- [x] `requirements.txt`에 등록된 패키지가 모두 설치되어 있는지 확인 (`pip freeze` 비교) — 일치 확인(et_xmlfile==2.0.0, openpyxl==3.1.5 두 패키지 모두 설치됨)
- [x] 신규 패키지 설치 시 즉시 `requirements.txt` 갱신 — 현재 시점 기준 `pip freeze`와 `requirements.txt`가 완전 일치(SYNCED). 운영 원칙으로 유지
- [x] `db/source/` 원본 파일은 읽기 전용으로만 접근 (절대 수정·이동·삭제 금지) — 현 시점 원본 1건(balanceofpayments2025q4.xlsx, 678,539 bytes) 최초 추가 후 수정 이력 없음. 운영 원칙으로 유지
- [x] 작업 결과물 저장 위치는 `db/data/` 하위로만 한정 — 디렉터리 존재 확인(현재 가공 산출물 없음, 운영 원칙으로 유지)
- [x] 사용자 대상 문서는 한국어로 작성 — README/PLAN/CHECKLIST/REPORT/CLAUDE 등 주요 문서 모두 한국어 본문(한글 25~52%) 확인. 운영 원칙으로 유지

### 0.2 배경지식 사전 정리 (background-search 1회차) [항상 PDF를 참고할 것]
- [x] **[background-search]** `background/` 폴더 전체 자료 목록과 각 자료의 주제·범위·발행 시점 요약 요청 — 산출물: `db/data/_background_notes/01_inventory.md` (총 2개 파일: INDEX.md, BoP.pptx 31슬라이드. python-pptx 등 설치 후 requirements.txt 동기화 완료)
- [x] **[background-search]** `BoP.pptx`에서 다루는 BoP 5대 구성요소(상품·서비스·1차소득·2차소득·자본·금융계정)의 강의용 정의 발췌 — 산출물: `db/data/_background_notes/02_bop_components.md` (3대 축 + 경상계정 4 하위항목, 슬라이드 4~14·21 인용. 슬라이드 21·15~20·26~27 이미지 텍스트 미추출 — §0.2 신규 항목으로 이월)
- [x] **[background-search]** 강의 자료에서 사용된 부호 규약(차변·대변, 자산·부채 증감)의 한국어 진술 발췌 — 산출물: `db/data/_background_notes/03_sign_conventions.md` (대변=유입(+)/차변=유출(−), BPM6 자산·부채 증감 기준 vs 구매뉴얼 순유출입 기준 비교, 슬라이드 6~14 인용)
- [x] **[background-search]** 강의 자료에서 항등식(경상수지 + 자본수지 + 금융계정 + 순오차 ≡ 0)의 표현 방식 확인 — 산출물: `db/data/_background_notes/04_identities.md` (PPT+PDF 병행 참조. 표적 항등식은 직접 식 없음 → 슬라이드 13·14·6의 결합으로 도출. 5종 항등식 발췌 완료. pypdf==6.10.2 설치·동기화 완료)
- [x] **[background-search]** 강의 자료에서 IIP(국제투자대조표)·순대외자산 개념의 정의 발췌 — 산출물: `db/data/_background_notes/05_iip_nfa.md` (BoP↔IIP stock·flow 연결, NFA 두 정의 일관성, BoP 금융계정 5항목↔IIP 매핑, 영국 만성 순채무·재평가 우세 적용 주의점, 슬라이드 4·6·8·11·14·24·25·26 인용)
- [x] **[background-search]** 강의 자료에서 직접투자·증권투자·기타투자·준비자산의 분류 기준 발췌 — 산출물: `db/data/_background_notes/06_financial_account_categories.md` (5분류 발췌, BPM6 표준 대비 일치/축약 점검표, ONS D1_3·D4_6·D7_9·K 매핑 가이드, 슬라이드 6·7·8·9·11·14 인용)
- [x] **[background-search]** 위 발췌 결과를 한국어 용어집 초안으로 정리하여 Phase 3 명세서 작업의 1차 근거로 보관 — 산출물: `db/data/_background_notes/07_glossary.md` (총 62 표제어 9분류, 미정의 15건 우선순위표, Phase 3 활용 가이드 6항목 포함)
- [x] **[background-search]** 표나 그래프가 있는 장표의 경우, 우선 해당 파워포인트에서 이미지를 추출한 후, 해당 이미지를 claude로 분석 — PPT→PDF→PNG 31장 추출(`db/data/_background_notes/slide_images/`) 후 핵심 10장(15·16·17·18·19·20·21·26·30·31) 멀티모달 분석. 산출물: `db/data/_background_notes/08_multimodal_slide_analysis.md` (BoP↔IIP 매트릭스(슬라이드 26)·포트폴리오 접근법(슬라이드 30)·세 접근법 통합(슬라이드 31) 발견 → 07_glossary 미정의 5건 격상 가능. pymupdf==1.27.2.3 설치·동기화)
- [x] **[background-search]** 만약, 파워포인트에서 이미지(표, 그래프) 추출이 어려운 경우, 해당 파일의 pdf 문서에서 이미지(표, 그래프) 추출 후, 해당 이미지(표, 그래프)를 claude로 분석 — 점검 산출물: `db/data/_background_notes/09_pdf_fallback_check.md` (8회차에서 PDF 경유 절차로 이미 충족됨을 확인. PPT 직접 렌더링 한계·임베디드 이미지 부재·PDF 31페이지↔PPT 31슬라이드 1:1 정렬 검증 포함)
- [x] **[web-search]** 영국 ONS 특화 분류·세분류·표기 규칙 및 영국 ONS 기준 분류를 검색하고, 해당 내용을 정리하여 background_note 업로드 — 산출물: `db/data/_background_notes/10_ons_web_research.md` (高 5건·中 5건 충족, 항등식 NEO 부호 규약/FDI 10%/거주자 1년/EBOPS 12분류/CDID 4자/결측 표기/개정 정책 정량 확정. Pink Book 표 식별자는 부분 확정 — Phase 1 시트명 추출로 보강 예정)
- [x] 모든 _background_note를 background 폴더로 이관. note 폴더 내에 해당 md 파일들을 모두 넣기 — `git mv`로 노트 10건은 `background/note/`로, slide_images PNG 31장은 `background/slide_images/`로 이관 완료. 노트 본문 내 옛 경로 참조 일괄 갱신, INDEX.md 자료 목록 표도 보강
- [x] 모든 배경 지식 사전 정리를 다시 한번 점검하고, 빠진 부분이 있는지 다시 한번 검토한 후, 추가적인 사항들을 '0.2 배경지식 사전 정리' 항목에 add on 할 것 — 산출물: `background/note/11_final_review.md`. 빠진 부분 26건 중 12건 후속 회차 해소·14건 미해결 식별. Phase 1 즉시 진입 가능 평가. 신규 후보 12건(高 4·中 5·低 3) 아래 add on
- [x] **[background-search]** 高 — `db/source/balanceofpayments2025q4.xlsx`의 시트명 전체 + 시트별 상단 메타 텍스트 추출해 `background/note/12_xlsx_sheet_inventory.md`로 정리. Pink Book 챕터 1~11 구조와 매핑하고 ONS 표 코드 사전(D1.3·D4.6·D7.9·K·BX 등)을 시트명에서 직접 도출 — 산출물: `background/note/12_xlsx_sheet_inventory.md` + `12_xlsx_sheet_inventory.csv`. 시트 20개 7분류 매핑(메타 3·요약 1·CA 본표 3·CA 세부 4·자본·금융 2·IIP 4·개정 3), ONS 표 코드 매핑 17/20, CDID 8행 일관 확인. 이상점 3건(Table_J 부호 prefix·단위 혼재·R3 9 부표 적층)
- [x] **[background-search]** 高 — xlsx 시트별 CDID 행 위치·코드 목록 추출해 `background/note/13_cdid_dictionary.md`로 정리. ECOS ITEM_CODE1과 직접 매핑 가능한 1차 사전 — 산출물 3종: `background/note/13_cdid_dictionary.md` + `13_cdid_dictionary.csv` (512 행 / 고유 284 CDID / sign_prefix 59 행) + `db/code/source/extract_cdid.py` (재현용 절차, 한국어 주석 보강). Phase 2.2 ITEM_CODE1 자동 채움 가능 평가
- [x] **[background-search]** 高 — 슬라이드 28(J-curve)·29(흡수 접근법 도식) 멀티모달 분석을 8회차 누락분으로 보강 — 산출물: `background/note/14_slide_28_29_analysis.md`. J-curve(평가절하 후 시차)·환율 전가(완전/불완전)·흡수 접근법(X−M=Y−A) 본문 발췌 + 영국 적용 함의 + 07_glossary 격상 후보 4건
- [x] **[background-search]** 高 — xlsx 시트별 단위 표기(£ million·£ billion·% of GDP) 인벤토리와 결측 표기 등장 위치(`x` vs 빈 셀) 카탈로그 작성 → `background/note/14_units_and_missing.md` — 산출물 4종: `background/note/15_units_and_missing.md` + `15_units.csv`(82행) + `15_missing.csv`(546행) + `db/code/source/extract_units_missing.py`. 단위 정규화 3종(GBP_million 35·GBP_billion 22·pct_of_GDP), 결측 `x` 360건(Table_C 6부표), `..`/`-`/GAF 대괄호 미등장. ONS Service Manual 권고 대비 legacy `x` 사용 평가
- [x] **[web-search]** 中 — OECD Benchmark Definition of Foreign Direct Investment 4판(BD4)의 SPE·FATS 보강 정의 확인 — 산출물: `background/note/16_oecd_bd4.md`. BD4의 FDIR·UCP·UIC·round-tripping·SPE 6단계 식별·pass-through capital·FATS(IFATS/OFATS) 정의 확보. ONS는 BD4 완전 준수 + SPE 포함/제외 두 시리즈 발표 + IFATS/OFATS 별도 산출. UK SPE 비중 7.1% (2021). BD5 2025-03 발표 (이행 2029~2030)
- [x] **[web-search]** 中 — BoE Bankstats(Tables A–C) 또는 BoE Statistical Release에서 영국 보유 준비자산(IR) 시계열 확보. 슬라이드 24의 NFA(중앙은행)와 슬라이드 11의 Net IIP(국가 전체) 정량 분리 — 산출물: `background/note/17_uk_reserves.md`. EEA(HMT+BoE) 4구성(금·외화·SDR·IMF Reserve Position), 2025-10 net USD 112.4bn(GBP 85.5bn) vs Net IIP −£199.8bn, 두 NFA 별개 개념 정량 확정. 주요국(중국·일본·한국·미국) 비교 포함
- [x] **[background-search]** 中 — ONS Pink Book Chapter 9 (IIP) xlsx에서 영국의 재평가(가격·환율·기타) 3분해 시계열 추출 → 슬라이드 26 매트릭스 비거래요인 정량 검증 — 산출물: `background/note/18_iip_revaluation.md`. 보유 분기 xlsx 키워드 검색 0건 확인 → 별도 자료 필요. ONS Pink Book Dataset 8(연간·매년 10월) Figure 12·13에 4분해(거래·가격·환율·기타) 게재. 2024 분해 사례·2016 Brexit·2008 위기 정량 보강. 분기 단위 분해는 ONS 미공표
- [x] **[background-search]** 中 — xlsx에서 금융계정 5분류 각각의 자산(NAFA)·부채(NIL) 양면 컬럼이 어떤 시트·열에 저장되어 있는지 매핑 — 산출물: `background/note/19_assets_liabilities_mapping.md` + `19_assets_liabilities_mapping.csv` (54행). 5분류 × {asset/liability/net} × {flow/stock} 6축 매핑. Derivatives 유량 자산/부채 분리 부재(net `ZPNN`만), Reserve liability 정의상 부재, Table_J 부표2 col 점프 발견. ITEM_CODE2 차원 매핑 가능 평가
- [x] **[web-search]** 中 — ONS Errors and omissions 분기 시계열 변동성 직접 확인(BoP revision triangles 또는 분기 통계 불러틴 부록). 영국 NEO의 절대값·표준편차 수치 확보 — 산출물: `background/note/20_neo_volatility.md`. CDID HHDH, 2020Q1~2025Q4 24분기 평균 −1,503£m·SD ~6,840·절대값 평균 ~5,872(GDP 0.92%)·최대 +14,457(2024Q1)·최소 −11,752(2020Q4). 슬라이드 14 "통계불일치=0" 가정과 정량적으로 어긋남 확정
- [x] **[background-search]** 低 — 슬라이드 22~25 NIA·BoP↔IIP 도식 부분 멀티모달 정밀 분석(텍스트는 04회차에서 인용됨, 학생용 시각 자료 가치 평가) — 산출물: `background/note/21_slide_22_25_visual_check.md`. 4장 모두 텍스트 본문 위주(NIA 식 3-1~3-3, CA=S−I, ΔNFA·H 식 3-4~3-6, BoP vs IIP)로 도식·차트 없음. 04회차 인용으로 100% 커버 확인. 종결
- [x] **[web-search]** 低 — HMRC OTS·ITIS·IPS·FDI Survey·BIS 국제은행통계 등 BoP 작성 다중 출처의 발표 일정·갱신 주기 카탈로그화 — 산출물: `background/note/22_bop_data_sources.md`. 5종 자료원(월간 1·분기 3·연간 1) 발표 시점·반영 시트·CDID·개정 정책 카탈로그. ONS BoP 분기 발표 동시·시차 관계 정리. 2025 Pink Book에서 2021년 이후 전체 개정 예정
- [x] **[web-search]** 低 — ONS 국가별(geographical breakdown) Pink Book Ch.10·11 분류 체계 확보 — EU/non-EU 분해 시트 매핑 사전 — 산출물: `background/note/23_geographic_breakdown.md`. **챕터 번호 보정**: 실제 ONS 분류는 Ch.9(CA)+Ch.10(IIP). 67개 개별국 + 5대륙 + EU27 집계, Brexit(2020-02-01) EU28→EU27 전환, Table_C ↔ Pink Book Ch.9 EU 합계 라인 1:1 대응 매핑. 10·12회차 매핑표 챕터 번호 보정 권고
---

## Phase 1. 원본 구조 정밀 조사

### 1.1 인벤토리 추출
- [x] 시트 목록과 각 시트의 행·열 수를 추출 — 산출물: `db/data/_inventory/01_sheet_dimensions.csv` + `01_sheet_dimensions.md`. 시트 20개 dimension 추출(Cover/Notes/Records 메타 3 + Table_A~K + Table_R1~R3). 12회차 background 인벤토리와 100% 일치 확인
- [x] 각 시트를 7분류(메타·주석 / 전체 잔액 요약 / 경상수지 본표 / 경상수지 세부 / 자본·금융계정 / 국제투자대조표 / 직전 발표 대비 개정) 중 하나로 분류 — 산출물: `db/data/_inventory/02_sheet_classification.csv` + `02_sheet_classification.md`. 7분류 모두 등장(메타 3·요약 1·CA 본표 3·CA 세부 4·자본·금융 2·IIP 4·개정 3 = 20). PLAN.md §1.1과 1:1 정합
- [x] **[background-search]** 위 7분류가 강의 자료의 BoP 분류 체계와 일치하는지 검증 요청. 강의 자료에 없는 분류(예: 개정 시트)는 별도로 표시 — 산출물: `db/data/_inventory/03_classification_validation.md`. 7분류 중 5개 일치(summary 부분일치) + 2개 미수록(meta_notes·revisions). 강의 자료의 자본·금융 분리 vs ONS 통합 분류 차이도 명기
- [x] **[background-search]** EU/非EU 분해 시트의 경제학적 의미를 강의 자료에서 확인 요청 — 산출물: `db/data/_inventory/04_eu_non_eu_validation.md`. 강의 자료 31장 키워드 검색 결과 EU·non-EU·지리분해·Brexit·국가명 모두 0건. 강의는 단일 카운터파트("rest of the world")만 다루며 Table_C는 ONS 운영 표기로만 의미. 학생용 학습 활용 권고 3건
- [x] 상단 메타 영역(헤더 4~5행)의 원문 텍스트 추출 — 부호 규약·단위·발표 기간 진술 포함 — 산출물: `db/data/_inventory/05_meta_text.csv` + `05_meta_text.json` + `05_meta_text.md`. 시트 20개 × 6행 = 120 메타 행 추출. 일관 구조(r1 제목·r3 단위/분기·r5 CDID 안내·r6 첫 부표 제목) 식별. Table_J `[note 1] [note 2]` 부호 마커, Table_B 4부표 단위 혼재 발견
- [x] **[background-search]** 메타 영역에 진술된 부호 규약이 강의 자료의 부호 규약과 일치하는지 대조 요청 — 산출물: `db/data/_inventory/06_sign_convention_validation.md`. ONS Notes 부호 반전 규약(Table_A·D·J·R1·R3 r5/r29/r33/r42/r51) ↔ 강의 BPM6 100% 일치 확인. sign_prefix 59행 분포 정합. Table_H FKKM 단발 예외 식별
- [x] 각 시트의 통계항목 코드(CDID) 행 위치와 첫 데이터 행 번호 기록 — 산출물: `db/data/_inventory/07_cdid_and_first_data_rows.csv` + `07_cdid_and_first_data_rows.md`. 본표 17개 모두 첫 CDID 행 = 8, 첫 데이터 행 = 9 일관. 부표 간격 일반 본표 149행, R계열 147행. 메타 시트 3개는 CDID 없음. 부표 갯수 12회차 100% 정합
- [x] 시점 컬럼 형식(연 `YYYY` / 분기 `YYYY Qn` / 월 `YYYY MMM` 등) 기록 — 산출물: `db/data/_inventory/08_time_period_formats.csv` + `08_time_period_formats.md`. 본표 17개 모두 `YYYY`(1997~2025) + `YYYY Qn`(1997Q1~2025Q4) 적층. 월간·일간 없음. R계열은 한 분기 짧음(2025Q3까지). ECOS CYCLE=A/Q 매핑 명시
- [x] 단위 표기 원문(£ million / £ billion / % of GDP 등) 기록 — 산출물: `db/data/_inventory/09_units.csv` + `09_units.md`. 시트 단위 매핑(GBP_million 9·GBP_billion 5·MIXED 3·meta 2). MIXED 시트(Table_B/BX/R2) 4번째 부표 %GDP 처리 규약 명시
- [x] **[background-search]** 강의 자료에서 GDP 대비 비율 표기의 통상적 해석 방식 확인 요청 — 산출물: `db/data/_inventory/10_gdp_ratio_validation.md`. GDP 대비 표기는 슬라이드 15(Korea CA/GDP·FA/GDP)만 등장. NIA 항등식(슬라이드 22~24) 모두 level. 분모 정의·임계비율·만성 적자국 분류는 강의 미수록. ONS Table_B/BX/R2 4번째 부표는 YBHA(명목 GDP 현행가) 분모 사용. 영국 적용 권고 4건
- [x] 빈 행으로 구분되는 부표 경계 행 번호 기록 — 산출물: `db/data/_inventory/11_subtable_boundaries.csv` + `11_subtable_boundaries.md`. 일반 본표 빈 행 154·303·452·601·750, R계열 빈 행 152·299·446·593·740·887·1034·1181. 부표 수 (빈+1) = 12회차와 100% 정합. Phase 2.1 분할 규칙 명시
- [x] 사용된 결측 표기(`x`, 빈 셀, `..` 등)의 종류와 등장 위치 기록 — 산출물: `db/data/_inventory/12_missing_markers.{csv,md}` + `db/code/source/extract_missing_markers.py`. 데이터 영역(CDID 컬럼 한정) 결측은 Table_C 6 부표의 `x` 360건이 유일. 빈 셀·`..`·`-`·GAF 4기호 모두 데이터 영역 미등장. ECOS 결측 사전 시드 6행 확보
- [x] **[background-search]** 강의 자료에서 결측 표기의 일반적 의미(비공개 vs 미산출 vs 적용 불가)에 대한 설명 발췌 요청 — 산출물: `db/data/_inventory/13_missing_meaning_validation.md`. 강의 슬라이드 본문 직접 진술 0건 확인. xlsx Notes B23 메타 정의("Cells containing x represent unavailable data.") 발견에 따라 12회차 라벨을 "비공개 → [c]"에서 "미가용 → [x]"로 보정. 12회차 csv·md·extract 스크립트 동시 갱신

### 1.2 산출물 형식
- [x] 인벤토리 결과를 기계 판독용 형식(CSV)으로 저장 — 데이터 추출 8건(01·02·05·07·08·09·11·12) 모두 CSV. 점검 보고서: `db/data/_inventory/14_format_compliance_check.md`
- [x] 동일 내용을 사람 검토용 형식(텍스트 또는 마크다운)으로도 저장 — 13건 모두 .md 동반(CSV+MD 페어 8건 + MD 단독 검증 보고서 5건)
- [x] 인벤토리 산출물도 1 CSV = 1 평면 표 원칙 준수 — 8 CSV 평면 일관성(`len(row)==len(header)`) 검증 통과. RFC 4180 호환
- [x] 엑셀 다중 시트 형식으로 저장하지 않음 — `db/data/_inventory/` 내 .xlsx/.xls 산출물 0건. JSON 보조 1건(05_meta_text.json)은 평면 CSV의 부록(키-값 매핑) 정당화

### 1.3 종료 조건
- [x] 모든 시트의 분류·헤더·코드·시점·단위·부표 경계·결측 표기가 한 표로 정리됨 — 산출물: `db/data/_inventory/15_master_inventory.{csv,md}` + `db/code/source/build_master_inventory.py`. 22 컬럼 × 20행. 8개 입력 인벤토리 LEFT JOIN. Phase 2.1 ETL 1차 입력 사양
- [x] **[background-search]** 정리된 인벤토리가 강의 자료에서 다루는 BoP 개념을 모두 포괄하는지 누락 점검 요청 — 산출물: `db/data/_inventory/16_curriculum_coverage_check.md`. 강의 개념 47건 카탈로그 → 시트 단위 직접 매핑 32(68%) + CDID 단위 11(23%) + 본 Bulletin 범위 외 4(9%, J-curve·흡수접근법·포트폴리오·재평가 3분해). 마스터 인벤토리는 강의 개념 91% 커버
- [x] Phase 2 입력 사양으로 그대로 사용 가능한 상태 — 산출물: `db/data/_inventory/17_phase2_readiness.md`. 입력 요건 15건 중 14 ✓ + 1 ◐(ITEM_CODE2~4는 Phase 3 본격 작업). 잔여 위험 5건 모두 Phase 2.1~2.2 자연 통합 가능. **Phase 2 진입 승인**

---

## Phase 2. 정형 CSV 가공

### 2.1 시트 단위 가로형 CSV 분리
- [x] 원본 시트 1개 = CSV 1개 매핑 준수 — 메타 시트 3은 한국어 메모로 별도 분기, 본표 17시트는 부표 단위로 분리. 가공 스크립트: `db/code/source/split_subtables.py`. 산출 63개 CSV: `db/data/balanceofpayments2025q4_<table_code>_sub<n>.csv`
- [x] 한 시트에 부표가 여럿이면 부표마다 별도 CSV로 분리 — 마스터 인벤토리 `n_subtables` 합계 63 = 산출 CSV 63개와 정합
- [x] 한 CSV에 둘 이상의 시트나 부표를 결합하지 않음 — ETL 로그(`db/data/_etl_log/phase2_1_split_log.csv`) 66행으로 시트·부표 단일성 확인
- [x] **[background-search]** 부표를 분리할 때 강의 자료의 BoP 항목 위계(예: 경상수지 → 상품·서비스·1차소득·2차소득)와 부표 분리 단위가 일치하는지 사전 점검 요청 — 산출물: `db/data/_inventory/18_subtable_curriculum_alignment.md` (260행 6 섹션). 본표 17시트 63 부표가 모두 강의 위계와 **직교 차원**(orthogonal)으로 충돌 0건. 부표 차원 5축(Cr/Dr/Bal·NAFA/NIL/Net·IIP/Flow/Income·SA/NSA/FA·%GDP·지리)으로 정규화. 학생용 1차 분석 권장 16 CSV·2차 23·심화 9·운영 15. Table_J NAFA/NIL/Net 3 부표는 슬라이드 14 식 `FA = NAFA − NIL + Net derivatives`와 1:1 동형
- [x] 상단 메타 영역(부호 규약·단위·발표 기간 진술)을 별도 한국어 메모로 분리 보존 — 시트별 한국어 메모 20건: `db/data/balanceofpayments2025q4_<table_code|sheet>.md`. 생성 스크립트: `db/code/source/write_sheet_memos.py`
- [x] **[background-search]** 메타 메모의 부호 규약 해설을 강의 자료 표현으로 작성하도록 요청 — 산출물: `db/data/_inventory/19_signs_gold_revisions.md` (206행 7 섹션). 메모용 부호 규약 표현 1~2 문장(슬라이드 8/13 직접 인용) + 결측 의미 1~2 문장(13회차 검증 인용) 권고. 메모 20건이 분류별로 자동 분기 사용
- [x] 좌측 식별자 열을 통계항목 코드(ECOS의 ITEM_CODE 대응)로 표준화 — CDID 행이 컬럼 헤더가 됨. 좌측 첫 컬럼은 시점(`time_period`), 둘째 컬럼부터 ONS CDID 4자 코드(소문자) = ECOS ITEM_CODE1
- [x] 시점 열을 시점(ECOS의 TIME 대응)으로 표준화 — `time_period` 컬럼이 첫 컬럼 고정. 연간 `YYYY` / 분기 `YYYYQn` ECOS 규약 정규화. 정규식 `(\d{4})(?: Q([1-4]))?` 적용
- [x] 그 외 열 이름은 ASCII 소문자·숫자·언더스코어로만 정리 — 285개 고유 컬럼 모두 `^[a-z0-9_]+$` 통과. sign_prefix(`-`) 행은 `_neg_<cdid>`로 변환해 부호 반전 의미 보존
- [x] 결측 표기(`x`, 빈 셀 등)는 원문 그대로 문자열로 보존 — Phase 2.4 §1 검증 결과 원본 `x` 360건 = 가공 CSV `x` 360건 (Table_C 6 부표). 빈 셀은 빈 문자열로 보존
- [x] 셀 값 변경·반올림·치환·환산·합산·보간 없음 — Phase 2.4 §1 셀 수 검증 통과: 원본 83,684셀 = 가공 CSV 83,684셀 (시트별 17개 모두 일치)

### 2.2 세로형 통합 CSV
- [ ] 모든 시트·계열을 단일 CSV에 결합 (CSV 자체는 단일 평면 표)
- [ ] 컬럼 순서를 PLAN.md 2.2의 사양과 동일하게 고정
- [ ] 통계표 코드(STAT_CODE) 컬럼 채움
- [ ] 통계표명(STAT_NAME) 컬럼 채움
- [ ] **[background-search]** 한국어 통계표명 작성 시 강의 자료에서 사용한 한국어 명칭 우선 채택을 요청
- [ ] 시트·부표 컬럼 채움 (단일 표인 경우 부표는 "1")
- [ ] 통계항목 코드 1~4단계(ITEM_CODE1~4) 채움. 영국 자료는 ITEM_CODE1에 ONS CDID 사용
- [ ] **[background-search]** 항목 위계(예: 경상수지 → 상품무역 → 비귀금속 상품)를 강의 자료의 분류 트리에 맞춰 ITEM_CODE2~4 매핑 자문 요청
- [ ] 통계항목명(ITEM_NAME)에 원문 라벨 보존
- [ ] 단위(UNIT_NAME) 원문 그대로 보존
- [ ] 주기(CYCLE)는 A·S·Q·M·SM·D 중 하나로만 기록
- [ ] 시점(TIME) 표기를 ECOS 규약(YYYY / YYYYQn / YYYYMM 등)으로 통일
- [ ] 원본 셀 컬럼에 원본 셀 문자열 그대로 보존(결측 포함)
- [ ] 관측치(DATA_VALUE)는 숫자로 파싱 가능한 경우만 채움, 그 외 빈 값

### 2.3 시트별 메타 메모
- [x] 각 가로형 CSV 옆에 한국어 메모(원본 위치·구조 변경 절차·컬럼 정의·결측 의미·부호 규약·생성 절차) 작성 — 시트 단위로 메모 1건씩 20건 생성. 본표 17 메모 7~8 섹션 + 메타 시트 3 메모 시트 역할 안내. 부표 ↔ CSV 매핑 표 포함
- [x] **[background-search]** 메모의 부호 규약·결측 의미 문구를 강의 자료 표현으로 다듬어 줄 것을 요청 — 19회차 §2·§3에서 권고한 한국어 표현을 메모 작성 스크립트가 분류별로 분기 사용(`capital_financial`/`iip`/`summary`는 슬라이드 8 인용, `current_main`/`current_detail`은 슬라이드 13 인용)
- [x] 영국 국제수지의 부호 규약(+ 유입 / − 유출, 경상수지는 + 흑자 / − 적자) 명시 — 메모 20건 모두 §6에 기재. CA 시트(B/BX/C/E/F/G/H/I)는 슬라이드 13 Cr/Dr 정의 직접 인용
- [x] **[background-search]** 강의 자료의 부호 규약과 ONS의 부호 규약 사이 차이가 있는지 대조 요청 — 산출물: `19_signs_gold_revisions.md` §4 대조 표(8 차원 비교). 개념 차원 일치율 100%(BPM6 채택, 자산·부채 증가 +, Cr/Dr 정의, 종합·준비자산 부호 정합). 운영 표기 차이 1건(sign_prefix 59행, 강의 미수록 — `_neg_<cdid>` 컬럼명으로 ETL 보존)
- [x] 귀금속 보정 표와 본표의 관계 명시 — Table_BX 메모 §8에 기재. ONS Notes r14 직접 인용으로 Precious metals = NMG + Platinum + Palladium + Silver 4종 정의 + Table_B − Table_BX = 4종 귀금속 순거래액 관계 명시
- [x] **[background-search]** 강의 자료에서 귀금속(비통화용 금) 거래의 BoP 처리 방식이 다뤄지는지 확인 요청 — 산출물: `19_signs_gold_revisions.md` §5. 강의 슬라이드 6은 통화용 금(monetary gold)만 명시, 비통화용 금(non-monetary gold)·Table_BX의 BoP 처리 방식은 **강의 자료 미수록**(별도 web-search로 BPM6 §10·§14 본문 위임 권고)
- [x] 직전 발표 대비 개정 시트의 역할 명시 — Table_R1·R2·R3 메모 §8에 기재. 운영 보조 자료임을 명시하고 본표와 직접 합산·환산 금지 안내
- [x] **[background-search]** 강의 자료에서 통계 개정(revision)의 거시지표 해석상 의미가 다뤄지는지 확인 요청 — 산출물: `19_signs_gold_revisions.md` §6. 강의 자료는 분기 BoP의 revision triangle·발표 시차·R1/R2/R3 직접 진술 0건. 가장 가까운 인접 개념: 슬라이드 26 "비거래요인 = 가격·환율·기타조정" 분해. R3 9 부표가 슬라이드 26 도식의 "기타조정" 항을 사후 추적하는 학생용 심화 보조 자료로 보존 정당화

### 2.4 검증
- [x] 원본 셀 수와 가공 후 CSV 셀 수의 합이 일치 — 자동 점검 결과 원본 83,684셀 = 가공 CSV 83,684셀 (차이 0). 시트별 17개 모두 일치. 결측 `x` 360건 보존도 동일성 확인. 검증 스크립트: `db/code/source/verify_phase2_1.py`. 결과: PASS
- [ ] 통합 CSV에서 (통계표 코드·부표·통계항목 코드 1~4·시점) 조합의 유일성 자동 점검 통과
- [ ] **[background-search]** 통합 CSV의 표본 5건을 추출해 강의 자료의 BoP 정의와 일치하는지(예: "경상수지" 라벨이 강의에서 정의한 경상수지 합계와 같은 개념인지) 교차 점검 요청

---

## Phase 3. 데이터 명세서 작성 (background-search 핵심 단계)

### 3.1 시트별 정의 수집 (시트마다 background-search 호출)
- [ ] **[background-search]** 전체 잔액 요약 시트의 한국어 정의·부호 규약·다른 변수와의 관계 작성 요청
- [ ] **[background-search]** 경상수지 본표의 한국어 정의·구성 항목·계산식(상품 + 서비스 + 1차소득 + 2차소득) 요청
- [ ] **[background-search]** 경상수지 귀금속 제외 보조표의 한국어 정의·본표와의 차이·도입 배경 요청
- [ ] **[background-search]** EU/非EU 분해 표의 한국어 정의·분해 기준·해석상 유의점 요청
- [ ] **[background-search]** 상품무역 시트의 한국어 정의·세부 항목(귀금속·非귀금속 등)·측정 단위 요청
- [ ] **[background-search]** 서비스무역 시트의 한국어 정의·세부 항목(여행·운송·금융·기타비즈니스 등)·측정 단위 요청
- [ ] **[background-search]** 1차소득 시트의 한국어 정의·세부 항목(직접투자수익·증권투자수익·기타투자수익·근로자보수)·부호 해석 요청
- [ ] **[background-search]** 2차소득 시트의 한국어 정의·세부 항목(이전소득의 종류)·부호 해석 요청
- [ ] **[background-search]** 자본계정 시트의 한국어 정의·자본이전·비생산비금융자산 거래 의미 요청
- [ ] **[background-search]** 금융계정 시트의 한국어 정의·자산/부채 부호 해석(음수 = 영국으로의 순자본 유입) 요청
- [ ] **[background-search]** 직접투자·증권투자·금융파생상품·기타투자·준비자산 각 항목의 한국어 정의와 BoP 매뉴얼상 분류 기준 요청
- [ ] **[background-search]** 국제투자대조표(IIP) 시트의 한국어 정의·자산/부채/순대외자산 개념·BoP 거래 흐름과의 관계 요청
- [ ] **[background-search]** 직전 발표 대비 개정 시트들의 한국어 정의·개정 발생 원인·해석 시 유의점 요청
- [ ] **[background-search]** 메타·주석 시트의 한국어 정의·역할 요청

### 3.2 통계항목(CDID) 단위 정의
- [ ] **[background-search]** 인벤토리에서 추출한 모든 CDID 목록을 시트별로 묶어 강의 자료 기반 한국어 명칭·정의 작성을 일괄 요청
- [ ] CDID마다 한국어 정의가 채워졌는지 확인. 누락 CDID는 별도 목록으로 정리
- [ ] **[background-search]** 1차 정의 결과에서 강의 자료에 등장하지 않는 CDID는 명시적으로 표시되었는지 확인
- [ ] **[web-search]** 강의 자료에 정의가 없는 CDID에 대해 ONS Time Series 페이지·BoP 매뉴얼(IMF BPM6 등) 출처 보강 요청
- [ ] 보강 출처를 명세서의 근거 컬럼에 기록

### 3.3 도메인 맥락 정리
- [ ] **[background-search]** 단위 혼재(£ million·£ billion·% of GDP)의 강의 자료 표현 방식 확인 요청
- [ ] 단위 정리 표 별도 작성
- [ ] **[background-search]** 결측 표기 분류('x' = 비공개·미산출 / 빈 셀 = 계열 시작 이전 또는 자료 없음)의 강의 자료 또는 통계 일반론적 근거 요청
- [ ] **[background-search]** BoP 항등식의 거시경제학적 의의(경상수지 적자의 자금조달 측면 해석)를 명세서 도입부에 인용할 한국어 문장으로 작성 요청
- [ ] **[background-search]** 금융계정 음수가 영국으로의 순자본 유입을 의미한다는 부호 해석을 강의 자료 표현으로 정리 요청

### 3.4 명세서 산출물
- [ ] 명세서 컬럼 구성: STAT_CODE / 통계표명 / ITEM_CODE1~4 / 원문 라벨 / 한국어 명칭 / 정의 / UNIT_NAME / CYCLE / START_TIME / END_TIME / 결측 의미 / 부호 규약 / 근거
- [ ] 모든 통계항목 코드 행에 한국어 정의 채움
- [ ] 모든 정의에 출처 인용 동반 (강의 자료 슬라이드 번호 또는 외부 출처 URL)
- [ ] **[background-search]** 명세서 초안에 대한 1차 감수 요청 — 강의 자료의 정의와 어긋나는 항목, 부호 규약 오기, 단위 표기 오류 점검
- [ ] 전체 통계표 카탈로그 문서(ECOS 통계표 목록 서비스 대응) 작성
- [ ] **[background-search]** 카탈로그 분야 분류명(국제수지·GDP·물가 등)을 강의 자료에서 사용한 한국어 분야명과 일치시키도록 요청

---

## Phase 4. ECOS 스타일 관계형 데이터베이스 구축

### 4.1 스키마 설계 점검
- [ ] **[background-search]** 강의 자료에 ECOS 또는 일반 통계 메타데이터 모델이 다뤄지는지 확인 요청 (있다면 스키마 설계의 한국어 표현 근거로 활용)
- [ ] 통계표 메타 테이블에 STAT_CODE(고유 키)·STAT_NAME·원문 통계표명·분야 분류·ORG_NAME·자료원·갱신 주기·START_TIME·END_TIME·출처 URL·발표일·가공 시각·한국어 설명 컬럼 포함
- [ ] 통계항목 메타 테이블에 자동 증가 식별자·통계표 외래 키·ITEM_CODE1~4·ITEM_NAME1~4·한국어 명칭·정의·P_ITEM_CODE·LVL·WGT·UNIT_NAME·CYCLE·START_TIME·END_TIME·부호 규약 컬럼 포함
- [ ] **[background-search]** 통계항목 위계(P_ITEM_CODE/LVL)를 BoP 항목 트리에 일관 적용할 수 있는지(예: 경상수지 LVL=1, 상품무역 LVL=2, 비귀금속 상품 LVL=3) 자문 요청
- [ ] 통계항목 메타에 (통계표·ITEM_CODE1~4) 유일성 제약 부여
- [ ] 관측치 테이블에 통계항목 외래 키·TIME·원본 셀·DATA_VALUE 컬럼, (통계항목·시점) 기본 키 부여
- [ ] 결측 사전 테이블에 'x'(비공개·미산출), 빈 문자열(계열 시작 이전 또는 자료 없음) 등록
- [ ] **[background-search]** 결측 사전의 한국어 의미 문장을 강의 자료 표현 또는 통계 일반론적 정의에 맞춰 작성 요청
- [ ] 통계 용어 사전 테이블 구성 (용어 식별자·용어명 한국어·원문·정의·출처)
- [ ] **[background-search]** 통계 용어 사전의 1차 시드(BoP·IIP·CDID·경상수지·금융계정·순대외자산·귀금속 보정·BPM6 등)에 대한 한국어 정의·출처 요청
- [ ] 인덱스: ITEM_CODE1, TIME, (통계항목·TIME) 복합 키

### 4.2 적재
- [ ] 메타 정보(통계표 메타·통계항목 메타·결측 사전·용어 사전)를 모두 CSV 형태로 미리 정형화 (각 메타도 1 CSV = 1 평면 표)
- [ ] 빈 데이터베이스 생성 후 스키마 적용
- [ ] 기존 데이터베이스 파일이 있으면 백업 후 새로 생성 (멱등 동작)
- [ ] 메타 CSV → 통계표 메타·통계항목 메타에 적재
- [ ] 세로형 통합 CSV → 관측치 테이블에 적재
- [ ] 결측 사전·용어 사전 적재
- [ ] 무결성 점검 지표(관측치 수·시리즈 수·결측 비율·시작·종료 시점 일관성) 산출
- [ ] **[background-search]** 무결성 점검 지표의 임계 기준(예: 결측 비율이 50% 이상이면 경고)에 대한 통계 일반론적 가이드 자문 요청

### 4.3 사용자 조회 인터페이스
- [ ] 통계항목 코드(ITEM_CODE1) 단일 조회 예시 제공
- [ ] 분야·키워드(한국어/원문) 통계표 검색 예시 제공
- [ ] 통계표 단위 항목 트리 조회(부모-자식·레벨·가중치 포함) 예시 제공
- [ ] 선택 계열 CSV 내보내기(1 CSV = 1 평면 표 준수) 예시 제공
- [ ] **[background-search]** 조회 예시에 사용할 시범 CDID(가장 많이 인용되는 변수, 예: 경상수지 합계·상품무역 합계·서비스무역 합계·순대외자산 등)를 강의 자료에서 추천 요청
- [ ] 사용자 안내 문서에 호출 예시 결과·갱신 절차 함께 기록

---

## Phase 5. 검증·문서화·확장 준비

### 5.1 검증
- [ ] 원본 셀 수와 데이터베이스 적재 후 관측치 수 일치 자동 비교
- [ ] 무작위 표본 10건의 원본 셀 문자열을 원본 엑셀과 직접 대조
- [ ] 사전 분석 보고서 헤드라인 수치를 데이터베이스 조회로 재계산하여 일치 확인
  - [ ] 상품무역 −£65.5bn (2025 Q4)
  - [ ] 서비스무역 +£53.3bn (2025 Q4)
  - [ ] 경상수지 −£18.4bn (2025 Q4)
  - [ ] 경상수지/GDP −2.4% (2025 Q4)
  - [ ] 순대외자산 −£199.8bn (2025 Q4 말)
- [ ] **[background-search]** 위 헤드라인 수치가 강의 자료의 BoP 해석 프레임에서 어떻게 읽히는지 한국어 설명 작성 요청 (검증 보고서 부록용)
- [ ] **[background-search]** 항등식(경상수지 + 자본수지 + 금융계정 + 순오차 ≡ 0)을 2025 Q4 데이터로 검산했을 때 강의 자료에서 기대하는 해석과 일치하는지 자문 요청

### 5.2 문서화
- [ ] 사용자 안내 문서에 데이터베이스 스키마 다이어그램 포함
- [ ] ECOS 표준과 본 프로젝트 필드 매핑 표 포함
- [ ] 호출 예시·갱신 절차 정리
- [ ] **[background-search]** 사용자 안내 문서의 도입부(BoP 데이터 활용 의의)를 강의 자료의 BoP 도입부 표현에 맞춰 작성 요청
- [ ] 분석 보고서 문서와 데이터 인프라 안내 문서를 역할별로 분리

### 5.3 확장 준비
- [ ] 새 원본 자료 추가 시 Phase 1 → 2 → 3 → 4 절차의 동일 패턴 재실행 가능 여부 확인
- [ ] 통계표 식별자에 분야 접두를 두어 분류 (영국 국제수지·GDP·물가 등)
- [ ] **[background-search]** 강의 자료에서 다뤄지는 다른 거시지표(GDP·물가·고용·통화 등)의 우선순위와 강의 비중 자문 요청 (다음 데이터셋 선정 근거로 활용)
- [ ] ECOS 분야 분류 규약과 충돌 없는 별도 접두 규약 유지
- [ ] 영국 국제수지의 경우 매 분기 발표 시 직전 발표 대비 개정 시트 함께 적재
- [ ] 개정 이력 추적 가능 여부 확인
- [ ] **[background-search]** 개정 이력 분석을 강의 사례로 활용할 수 있는지(예: 통계 신뢰성 강의 모듈 연계 가능성) 자문 요청

---

## 전 단계 공통 점검

### 데이터 무결성
- [ ] 셀 값을 어떤 단계에서도 변경·반올림·치환·환산·합산·보간하지 않음
- [ ] 결측 표기('x' vs 빈 셀)를 별개의 결측 코드로 구분 보존
- [ ] 단위 혼재를 통일하지 않고 원문 보존

### 산출물 형식
- [ ] 모든 가공 산출물 데이터는 CSV로만 저장 (엑셀 다중 시트 형식 금지)
- [ ] 모든 CSV는 단일 평면 표(1 CSV = 1 시트)
- [ ] 부표가 여럿이면 부표마다 별도 CSV

### 재현성
- [ ] 손으로 편집한 산출물 없음 (모든 결과물이 동일 절차로 재생성 가능)
- [ ] 적재 절차는 멱등적
- [ ] 가상환경 인터프리터 고정 사용

### 문서화
- [ ] 사용자 대상 문서는 한국어
- [ ] 새 패키지 설치 시 `requirements.txt` 즉시 갱신
- [ ] 외부 출처는 공식 다운로드 페이지 URL 함께 기록

### 배경지식 활용 (전 단계 공통 원칙)
- [ ] 도메인 판단·정의·해석·검증이 필요한 모든 지점에서 `background-search`를 1차 호출
- [ ] `background-search` 결과는 출처(파일명·슬라이드 번호)와 함께 기록
- [ ] 강의 자료에 답이 없는 항목만 `web-search`로 위임
- [ ] `background-search` 호출 이력(요청 내용·반환 요약·인용 위치)을 작업 기록에 누적 보관
- [ ] 동일 질의를 반복하지 않도록, 1회차에서 정리한 한국어 용어집을 후속 단계에서 재활용
