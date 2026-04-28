# 17 본표 시트의 한국어 STAT_NAME 권고 (background-search 산출, Phase 1.1 §2.2)

본 문서는 `db/CHECKLIST.md` §2.2 background-search 첫 번째 항목의 산출물로, Phase 2.2 세로형(long-form) 통합 CSV의 STAT_NAME(통계표명, 한국어) 컬럼에 채워 넣을 17개 본표 시트별 명칭 1차 발췌안이다. 외부 웹 검색 없이 `background/BoP.pptx`(31 슬라이드) + 강의 회차 노트 1~23(`background/note/`) 만을 1차 근거로 삼아, 강의 자료에서 사용된 한국어 명칭을 우선 채택했다.

## 1. 요지

- 강의 자료(`background/BoP.pptx`)는 한국은행 BPM6 일반론 기준이며, BoP를 **경상수지·자본수지·금융계정** 3대 축으로, 경상수지를 다시 **상품수지·서비스수지·1차소득(본원소득)·2차소득(이전소득)** 4개로 분류한다(02·07 메모 §발췌표; slide 5·9·14).
- 17개 본표 시트 중 **강의 자료에 한국어 명칭이 직접 등장**하는 것은 8개(A·B·E·F·G·H·I·J 라인의 핵심 항목과 K의 IIP). 나머지 9개는 강의 자료가 다루지 않는 **ONS 운영 차원**(귀금속 보정 BX, 지리분해 C, 자산/부채/순 분리 D1.3·D4.6·D7.9, 개정 R1·R2·R3)이므로 강의 한국어 + 보조 안내(괄호) 합성형으로 작성했다.
- 권고 STAT_NAME은 ECOS 한국어 통계표명 관행(예: "[국가명] [지표 분야]" 단순형)에 맞춰 **국가명 "영국" + 지표 분야**의 6~14자 명사형으로 통일했다.
- 강의 자료가 명시적으로 사용하는 한국어 표제어는 다음 9개로, 본 권고안의 기준 명사가 된다(07 §BoP_구성·금융계정·IIP): **국제수지표 / 경상수지 / 상품수지(=무역수지) / 서비스수지 / 1차소득수지(본원소득수지) / 2차소득수지(이전소득수지) / 자본계정(자본수지) / 금융계정(금융수지) / 국제투자대조표**.
- 본 안은 `STAT_NAME` 컬럼 1차 자동 채움용 매핑이며, Phase 2.2 통합 CSV 적재 후 ECOS 표준 명칭과 교차 검증할 것을 권고한다.

## 2. 17 시트 한국어 명칭 권고 표

| # | sheet | 영문 부표 라벨(대표) | 강의 한국어 명칭 (직접 인용) | 권고 STAT_NAME (한국어) | 1차 근거(슬라이드/노트) |
|---:|---|---|---|---|---|
| 1 | Table_A | Summary of Balance of Payments, Balances (net transactions) | 국제수지표 / 경상수지·자본수지·금융수지 합산 잔액 | 영국 국제수지 요약 (잔액) | slide 5·14; 02 §발췌표; 07 §BoP_구성 1행; 12 §인벤토리 |
| 2 | Table_B | Current account, seasonally adjusted | 경상수지 (상품·서비스·1차소득·2차소득 합) | 영국 경상수지 (전체, 계절조정) | slide 5·9·14; 02 §발췌표; 07 §BoP_구성 2행 |
| 3 | Table_BX | Current account excluding precious metals | (강의 미수록) → 가장 가까운 강의명: 경상수지 | 영국 경상수지 (귀금속 제외, 계절조정) | slide 5; 07 §메타 4행("귀금속 보정"=강의 미수록); 12 §매핑 BX |
| 4 | Table_C | Current account, EU and non-EU | (강의 미수록) → 가장 가까운 강의명: 경상수지 | 영국 경상수지 (EU/non-EU 지리분해) | slide 5; 23 §1·2·4 (Pink Book Ch.9, Brexit 후 EU27 기준); 12 §매핑 C |
| 5 | Table_D1_3 | IIP / FA / investment income — Investment abroad | 국제투자대조표·금융계정·1차소득(본원소득) — 해외투자(자산) | 영국 대외투자 (자산: IIP·금융거래·투자소득) | slide 6·14·25; 05 §매핑표; 06 §ONS 매핑 D1_3; 07 §ONS특화 |
| 6 | Table_D4_6 | Same — Investment in the UK | 국제투자대조표·금융계정·1차소득 — 대내투자(부채) | 영국 대내투자 (부채: IIP·금융거래·투자소득) | slide 6·14·25; 05 §매핑표; 06 §ONS 매핑 D4_6 |
| 7 | Table_D7_9 | Same — Net investment | 국제투자대조표·금융계정·1차소득 — 순(자산−부채) | 영국 순대외투자 (순포지션: IIP·금융거래·투자소득) | slide 6·11·25; 05 §매핑표; 06 §ONS 매핑 D7_9 |
| 8 | Table_E | Trade in goods | 상품수지(=무역수지), 재화의 수출입 | 영국 상품무역 (수출·수입·수지) | slide 5·9·21; 02 §발췌표 행1; 07 §BoP_구성 3행 |
| 9 | Table_F | Trade in services (EBOPS 2010 12 categories) | 서비스수지 (운수·여행·로열티 등 12분류) | 영국 서비스무역 (수출·수입·수지, 12분류) | slide 5·9; 02 §발췌표 행2; 07 §BoP_구성 5행("EBOPS 12분류는 강의 자료 미수록") |
| 10 | Table_G | Primary income | 1차소득(본원소득) — 임금송금·배당·이자 | 영국 1차소득 (본원소득: 보수·투자소득·기타) | slide 5·9·25; 02 §발췌표 행3; 07 §BoP_구성 6행 |
| 11 | Table_H | Secondary income | 2차소득(이전소득) — 무상이전, 원조·국제기구출연금 | 영국 2차소득 (이전소득: 정부·기타부문) | slide 5·9·14; 02 §발췌표 행4; 07 §BoP_구성 7행 |
| 12 | Table_I | Capital account | 자본계정(자본수지) — 비생산·비금융자산, 자본이전 | 영국 자본수지 (자본이전·비생산비금융자산) | slide 5·7·14; 02 §발췌표 행5; 07 §BoP_구성 8행 |
| 13 | Table_J | Financial account, NSA | 금융계정(금융수지) — 직접·증권·파생·기타·준비자산 5분류 | 영국 금융계정 (계절미조정) | slide 5·6·8·14; 02 §발췌표 행6; 06 §분류표; 07 §금융계정 |
| 14 | Table_K | International investment position end-of-period | 국제투자대조표(IIP) — 분기말 잔액 stock 통계 | 영국 국제투자대조표 (분기말 잔액) | slide 25; 05 §발췌표 IIP 정의; 07 §IIP 1행; 12 §매핑 K |
| 15 | Table_R1 | Revisions summary — balances | (강의 미수록) → 강의 일반 명칭: 국제수지·잔액 | 영국 국제수지 개정 요약 (잔액) | slide 5·14; 07 §메타 3행("개정(리비전)"=강의 미수록); 12 §매핑 R1 |
| 16 | Table_R2 | Current account revisions | (강의 미수록) → 가장 가까운 강의명: 경상수지 | 영국 경상수지 개정 (계절조정) | 07 §메타 3행; 12 §매핑 R2 |
| 17 | Table_R3 | International investment revisions (9 sub-tables) | (강의 미수록) → 강의 일반 명칭: 국제투자(IIP·금융계정) | 영국 국제투자 개정 (IIP·금융계정·투자소득) | 07 §메타 3행; 12 §매핑 R3 |

### 2.1. 강의 직접 발췌 인용 (권고 명칭의 핵심 근거 5선)

권고 STAT_NAME의 본 라벨이 강의 자료에서 어떤 한국어 표현으로 등장하는지 짧게 발췌한다.

1. **경상수지** (slide 5·9, 02 §발췌표): "경상계정의 첫 하위항목" / "Current account = trade balance + balance on services + net primary income + net secondary income" — 02 §발췌표 행1·2·3·4 합계로 정의. → Table_B/BX/C/R2의 본 라벨로 채택.
2. **상품수지(=무역수지)** (slide 5·9·21, 02 §발췌표 행1): "재화의 수출입, net trade in merchandise goods" — 02 §발췌표는 "상품수지(=무역수지)"라는 동일 표제어로 묶어 표기. 슬라이드 21은 차트 제목 "Balance of Goods and Trade Balance"로 두 시리즈를 동시 비교(02 §빠진 부분 1번에 따르면 텍스트 정의 차이는 강의 미수록). → Table_E의 본 라벨 "상품무역" 채택.
3. **서비스수지** (slide 5·9, 02 §발췌표 행2): "운수, 여행, 로열티 등 포함" — EBOPS 12분류는 강의 미수록이므로 권고안에서는 "12분류"만 보조 안내(07 §BoP_구성 5행). → Table_F.
4. **1차소득(본원소득)** vs **2차소득(이전소득)** (slide 5·14, 02 §발췌표 행3·4): "본원소득은 노동·자본 제공이라는 대가가 있는 반면, 이전소득은 '아무런 대가 없이 제공'" — 강의 자료의 동의어 처리: "본원소득" = "1차소득", "이전소득" = "2차소득". 권고안은 ONS 영문 헤더("Primary/Secondary income")와의 직역 일관성을 위해 **1차소득·2차소득**을 본 라벨로, 괄호에 보조 표기. → Table_G·H.
5. **금융계정(금융수지)** (slide 6·14, 06 §분류표): "직접투자(direct investment) / 증권투자(portfolio investment) / 파생금융상품(derivatives) / 기타투자(other investment) / 준비자산증감(changes in reserve assets)" — 5분류 명칭 자체는 강의 자료에서 한국어로 등장. → Table_J 본 라벨 "금융계정"; 단, 영국 ONS의 D1.3·D4.6·D7.9 자산/부채/순 양면 분리는 강의 식 차원(slide 14)에서만 등장하므로 D 라인 3개 시트는 보조 안내 합성(아래 §3-1번).

## 3. 강의 미수록 시트의 처리 방침

본 매핑에서 강의 자료가 직접 다루지 않는 ONS 운영 차원 9개 시트(BX·C·D1.3·D4.6·D7.9·R1·R2·R3, 그리고 D 라인 양면 분리)에는 다음 두 보조 원칙을 적용했다.

1. **(a) 강의 한국어 명칭 + 괄호 보조 안내** — 강의 자료가 다루는 가장 가까운 한국어 명칭(예: "경상수지", "국제투자대조표")을 본 라벨로 두고, ONS가 추가한 운영 차원(귀금속 제외·EU/non-EU·자산/부채/순·개정)은 괄호로 보조 표기.
   - 예: Table_BX → "영국 경상수지 (귀금속 제외, 계절조정)" — 강의 슬라이드 5의 "경상수지" 명칭 + 보조 "귀금속 제외".
   - 예: Table_C → "영국 경상수지 (EU/non-EU 지리분해)" — 강의 명칭 "경상수지" + 보조 "EU/non-EU 지리분해" (`23_geographic_breakdown.md` §1).
   - 예: Table_D1_3 → "영국 대외투자 (자산: IIP·금융거래·투자소득)" — 강의 슬라이드 6·11·25에서 사용된 "대외자산"·"국제투자대조표" 어휘 합성. 강의는 자산/부채를 식 차원(slide 14)에서만 분리하므로 보조 안내 필수(`06_financial_account_categories.md` §빠진 부분 2번).
   - 예: Table_R1 → "영국 국제수지 개정 요약 (잔액)" — "국제수지"는 강의 표제어, "개정/잔액"은 ONS 운영 차원의 괄호 보조.

2. **(b) 강의 자료가 다루지 않는 ONS 운영 차원의 명시** — 다음 4개 차원은 본 권고안 채택 시 데이터 명세서에 "강의 자료 미수록(ONS 표준)"임을 각주로 병기할 것을 권고한다(중복 적용 가능).
   - **귀금속 보정(non-monetary gold)**: Table_BX. 07 §메타 4행 "귀금속 보정" 항목이 "강의 자료 미수록, ONS 표준"으로 분류됨.
   - **지리분해 EU/non-EU(Brexit 후 EU27 기준)**: Table_C. 23 §2 "Brexit 이후(2020-02-01부터) EU27 기준". 강의 자료에는 지리분해 자체가 등장하지 않음.
   - **자산/부채/순 양면 분리**: Table_D1_3·D4_6·D7_9. 06 §빠진 부분 2번 "자산·부채 양면 분류 … 분류별 구체 사례 없음". 강의는 식 차원(slide 14)에서만 분리.
   - **개정(revision)**: Table_R1·R2·R3. 07 §메타 3행 "개정(리비전): ONS 분기별 사후 개정 … 강의 자료 미수록, ONS 표준". 강의 자료에는 개정 개념 자체가 없음.

3. **명명 일관성 규칙** — 본 권고안은 다음 ECOS 관행 형식을 통일적으로 적용했다.
   - 접두 "영국": 모든 17개 시트에 부착(국가 식별자, ECOS 한국어 통계표명 표준).
   - 본 라벨: 강의 한국어 명칭(7~14자) — 경상수지·금융계정 등 강의 자료의 표제어 우선.
   - 괄호 보조: ONS 운영 차원(귀금속 제외/EU·non-EU/계절조정 등)은 괄호 안에 짧게.
   - 단위·기간 표기는 STAT_NAME에 포함하지 않음(별도 컬럼 `UNIT_NAME`·`PERIOD` 운용).
   - 동의어 처리: "1차소득"="본원소득수지", "2차소득"="이전소득수지", "자본계정"="자본수지", "금융계정"="금융수지" — 강의 자료에서 두 표기가 병용되므로(02 §발췌표·07 §BoP_구성) 본 라벨에는 IMF BPM6 영문 직역에 가까운 "1차소득·2차소득·자본수지·금융계정"을 채택하고, 한국은행 전통 표기 "본원소득·이전소득"은 괄호에 보조 병기.

4. **D 라인 3개 시트의 본 라벨 선택 사유** — Table_D1_3 / D4_6 / D7_9는 ONS가 (a) IIP 잔액 (b) 금융거래 (c) 투자소득의 3차원을 자산·부채·순 3면으로 교차 적층한 구조다. 강의 자료에는 이 3면 적층이 없고(slide 14 식에만 등장), 명세서 라벨로는 "대외투자(자산)·대내투자(부채)·순대외투자(순)" 의 슬라이드 11·24의 NFA 어휘가 가장 가깝다(05 §발췌표 NFA 정의 ①·②). 따라서 본 권고안은:
   - Table_D1_3 → "영국 대외투자(자산)" — 슬라이드 11 "대외순자산", 슬라이드 25 "대외투자 잔액" 어휘.
   - Table_D4_6 → "영국 대내투자(부채)" — 슬라이드 25 "외국인의 국내투자 잔액" 어휘.
   - Table_D7_9 → "영국 순대외투자(순)" — 슬라이드 11·24 "NFA·순외화자산" 어휘.

## 4. 출처

- 1차 근거(강의 자료 본체): `background/BoP.pptx` 슬라이드 4·5·6·7·8·9·10·11·14·21·22·23·24·25·26 (`background/BoP.pdf` 동일 페이지 병행 확인).
- 강의 회차 발췌 노트:
  - `background/note/02_bop_components.md` (BoP 5대 구성요소 강의 정의 발췌, slide 5·9·14·21 인용)
  - `background/note/03_sign_conventions.md` (부호 규약, BPM5/BPM6 비교, slide 8·13)
  - `background/note/04_identities.md` (BoP 항등식, slide 13·14·22·23·24)
  - `background/note/05_iip_nfa.md` (IIP·NFA 정의 발췌, slide 11·24·25)
  - `background/note/06_financial_account_categories.md` (금융계정 5분류, slide 6·8·9·14, ONS D1_3·D4_6·D7_9·K 매핑)
  - `background/note/07_glossary.md` (62 표제어 한국어 용어집, BoP_구성·금융계정·IIP·메타 분류)
  - `background/note/12_xlsx_sheet_inventory.md` + `12_xlsx_sheet_inventory.csv` (시트 인벤토리 + Pink Book 챕터 매핑, title_ko 1차 안)
  - `background/note/13_cdid_dictionary.md` + `13_cdid_dictionary.csv` (CDID 사전, 시트별 부표·컬럼 라벨)
  - `background/note/23_geographic_breakdown.md` (Pink Book Ch.9·10 지리분해, EU27 정의, Brexit 영향)
- 인접 산출물(저장소 내): `db/data/_inventory/02_sheet_classification.md`(시트 7분류 표), `db/data/_inventory/15_master_inventory.md`(마스터 인벤토리), `db/REPORT.md` §1.1·§3.3.
- 본 산출 절대경로: `C:\Projects\SKKU.England\db\data\_inventory\20_korean_statname.md`.

## 5. 빠진 부분 / 후속 작업 권고

- **ECOS 공식 한국어 통계표명과의 교차 검증**: 본 안은 강의 자료 한국어 명칭을 우선 채택했으므로, ECOS가 영국 BoP를 등재할 때 사용하는 표준 명칭(예: "영국 국제수지" / "영국 국제투자대조표")과 다를 수 있다. Phase 2.2 적재 후 web-search 서브에이전트 또는 ECOS 사이트에서 1회 교차 검증 권고(외부 웹 검색 위임 필요).
- **Table_BX·R1·R2·R3의 "잔액(net)" vs "흑자/적자(surplus/deficit)" 표기 통일**: 강의 자료는 두 표현을 혼용(slide 10·11). 본 권고안에서는 "잔액"으로 통일했으나 실제 데이터 컬럼 라벨과의 정합 점검 필요.
- **Table_J 부호 prefix 22행**: `Table_J`는 NSA(계절미조정)이며 CDID 22개에 부호 반전 prefix가 부착된다(13 §부호 prefix 표). STAT_NAME 자체에는 부호 정보를 담지 않되, 명세서 비고란에 "CDID prefix 마이너스 = 부호 반전"을 별도 명시 권고.
- **Table_C 6 부표의 정확한 영문 명칭**: 23 §빠진 부분에 따르면 부표별 영문 명칭은 시트 헤더 직접 추출이 필요(현재 "추정 매핑"). STAT_NAME 권고는 합산 라벨 1개만 제공하므로 부표 단위 STAT_NAME_SUB가 필요할 시 추가 작업 요망.
- **Table_R3 9개 부표 단위 STAT_NAME 세분**: 13 §13_cdid_dictionary.md §Table_R3 표에서 부표 1·2·3 = 자산 측(IIP·FA·투자소득), 4·5·6 = 부채 측, 7·8·9 = 순. STAT_NAME 컬럼만으로는 9 부표를 식별하지 못하므로 부표 식별자(SUB_TABLE_NO 또는 SUB_LABEL)와 결합한 복합 키 운용 필수.
- **강의 자료 미수록 항목의 보강 출처**: 07 §미정의·우선순위 高 5건(표적 항등식·DI 10% 임계치·거주자/비거주자·분개 예시·무역수지 정의)와 中 EBOPS 12분류 등은 BPM6/OECD BD4/ONS Pink Book 등 외부 자료에서 보강 필요 — 본 STAT_NAME 권고와는 별개로 명세서 정의 컬럼 작성 시 활용.

## 6. 부록: STAT_NAME 17행 단정 권고안 (1줄 명칭 리스트)

본 §의 단정 명칭은 §2 표의 권고 STAT_NAME 컬럼을 그대로 옮긴 것이며, Phase 2.2 통합 CSV 좌측 STAT_NAME 컬럼에 sheet 키로 left-join하면 자동 채움된다.

| sheet | 권고 STAT_NAME |
|---|---|
| Table_A | 영국 국제수지 요약 (잔액) |
| Table_B | 영국 경상수지 (전체, 계절조정) |
| Table_BX | 영국 경상수지 (귀금속 제외, 계절조정) |
| Table_C | 영국 경상수지 (EU/non-EU 지리분해) |
| Table_D1_3 | 영국 대외투자 (자산: IIP·금융거래·투자소득) |
| Table_D4_6 | 영국 대내투자 (부채: IIP·금융거래·투자소득) |
| Table_D7_9 | 영국 순대외투자 (순포지션: IIP·금융거래·투자소득) |
| Table_E | 영국 상품무역 (수출·수입·수지) |
| Table_F | 영국 서비스무역 (수출·수입·수지, 12분류) |
| Table_G | 영국 1차소득 (본원소득: 보수·투자소득·기타) |
| Table_H | 영국 2차소득 (이전소득: 정부·기타부문) |
| Table_I | 영국 자본수지 (자본이전·비생산비금융자산) |
| Table_J | 영국 금융계정 (계절미조정) |
| Table_K | 영국 국제투자대조표 (분기말 잔액) |
| Table_R1 | 영국 국제수지 개정 요약 (잔액) |
| Table_R2 | 영국 경상수지 개정 (계절조정) |
| Table_R3 | 영국 국제투자 개정 (IIP·금융계정·투자소득) |

## 7. 인접 산출물과의 비교 (검증)

`background/note/12_xlsx_sheet_inventory.md` §시트별 인벤토리 표의 `title_ko` 컬럼은 본 §2 권고와 같은 17개 시트에 대해 1차 한국어 라벨을 이미 할당해 두었다. 두 라벨의 차이를 정리하면 다음과 같다.

- 일치: Table_E·F·G·H·I·J·K (BoP 5대 구성요소·IIP의 기준 명사 동일).
- 보강(접두 `영국 ` 추가): 본 권고안은 ECOS 관행에 맞춰 모든 시트에 국가 식별자를 부착했고, 12 §title_ko는 국가명을 생략한 형태(예: `상품무역`).
- 보강(괄호 보조 안내 추가): Table_BX·C·D1_3·D4_6·D7_9·R1·R2·R3는 12 §title_ko가 짧은 형태(예: `경상수지 (귀금속 제외)`)이고, 본 권고안은 ONS 운영 차원을 더 명시적으로 풀어 적었다(예: `영국 경상수지 (귀금속 제외, 계절조정)`).
- 결과: 본 권고안의 STAT_NAME은 12 §title_ko의 슈퍼셋(superset)으로, Phase 2.2 STAT_NAME 컬럼에 그대로 채택 가능하며 12 §title_ko와의 호환성도 유지된다.
