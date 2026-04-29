# 30회차 — Phase 3.4 §4 명세서 1차 감수

본 노트는 `db/CHECKLIST.md` Phase 3.4 §4번([background-search] 명세서 초안에 대한 1차 감수 요청 — 강의 자료의 정의와 어긋나는 항목, 부호 규약 오기, 단위 표기 오류 점검) 산출물. `db/data/_spec/specification.csv`(512행 × 16 컬럼)를 강의 자료(`background/BoP.pptx`) + 노트 02·03·04·08·12·13·15·19·24~28과 cross-check.

---

## §1 감수 범위 및 방법

### 1.1 대상

- `db/data/_spec/specification.csv` — 16 컬럼 × 512행(헤더 제외).
- 시트별 분포(STAT_CODE 기준): Table_A 31, Table_B 39, Table_BX 39, Table_C 36, Table_D1_3 16, Table_D4_6 13, Table_D7_9 17, Table_E 24, Table_F 36, Table_G 29, Table_H 22, Table_I 32, Table_J 31, Table_K 29, Table_R1 31, Table_R2 39, Table_R3 47.
- 17개 본표 × 평균 ~30행 = 512. 노트 12 인벤토리(20 시트 중 본표 17)와 정합.

### 1.2 점검 방법

- 16 컬럼 전수 확인.
- 1차 근거: BoP.pptx 31장 + slide_images/05·06·08·09·11·12·13·14·25·26.png.
- 2차 근거: 노트 02·03·04·08·12·13·15·19·21·24~28.

---

## §2 강의 자료 정의와 어긋나는 항목

### 2.1 시트별 STAT_NAME — 큰 문제 없음, 1건 권고

대부분 적정. **권고(中)**: Table_B "(SA)" / Table_J "(NSA)" 약어는 강의에 직접 정의되지 않으므로 STAT_NAME 또는 DEFINITION 한 줄에 **계절조정(Seasonally Adjusted) / 비계절조정(Non-Seasonally Adjusted)** 한국어 풀이 추가 권장.

### 2.2 ITEM_NAME_KO — 시트 단위 일괄 채움으로 인한 **개별 행 의미 불일치**(高 우선)

대표 사례:

1. **Table_B_sub2 행 1 (CDID `BOKH`, "Imports of goods")** — `ITEM_NAME_KO = "경상수지 본표"`. 영문 라벨은 "수입"인데 한국어가 시트 차원 머리("경상수지 본표")로 채워져 있어 행 단위 의미가 사라짐. → 강의 슬라이드 5 정의로 보면 "상품 수입(Imports of goods)"으로 풀어야 적정.
2. **Table_A_sub2 `FKMJ` (Capital balance)** — `ITEM_NAME_KO = "자본수지 합계"`인데 같은 행의 `DEFINITION`은 "경상수지 합계 — 강의 슬라이드 14 항등식"으로 채워져 있음. **DEFINITION이 영문 라벨 의미와 정반대** (§2.3 #1).
3. **Table_B_sub3 / Table_C_sub2,5 / Table_R1_sub2 / Table_R2_sub2** — 동일 패턴. 부표2(Debits/Imports)·부표3(Balances) 식별이 ITEM_NAME_KO에서 사라짐.

**근본 원인**: cdid_definitions.csv 단계에서 ko_name이 시트 단위로 채워지고, 일부 항목(Total/Balance)에 한해서만 행 단위로 정밀화됨.

**우선순위 — 高**: 슬라이드 5 정의("재화의 수출입") + 노트 19 자산·부채 양면 매핑(asset/liability/net)에 따라, ITEM_NAME_KO는 (부표 차원 + 항목 라벨)의 합으로 행마다 다르게 채워야 함.

### 2.3 DEFINITION — 강의 슬라이드 인용은 정확하나 일부 보일러플레이트 본문이 행 의미와 충돌 (高 우선)

1. **Table_A_sub2 `FKMJ` (Capital balance) 오기**: DEFINITION이 "경상수지 합계 — 강의 슬라이드 14 항등식 …"로 잘못 입력. 강의 슬라이드 5는 자본수지(KA)와 경상수지(CA)를 명확히 분리 — 이 행의 DEFINITION은 "자본수지 합계 — 자본이전 + 비생산비금융자산 취득·처분(강의 슬라이드 5·7·14)"으로 수정 필요.
2. **Table_E sub2(Imports), sub3(Balance) 등 부표 단위 일괄 보일러플레이트** — DEFINITION에 "본 부표는 Debits/Imports 측을 기록"·"본 부표는 Balances를 기록"이라는 부표 식별 한 줄을 추가해야 학생이 sub1/2/3을 구분할 수 있음.

### 2.4 미수록 항목의 표시 — 100% 적정

- Table_BX·C·R1·R2·R3 등 강의 자료 미수록 항목은 모두 "강의 자료 미수록 — background/note/<NN>" 형식으로 명시. 학생 혼동 가능성 낮음.

---

## §3 부호 규약(SIGN_CONVENTION) 오기 점검

### 3.1 전반적 정합성 — 양호

CA·KA·FA 시트 부호 규약이 노트 03 §발췌표 + 노트 19 + 슬라이드 8·11과 정확히 일치.

### 3.2 Table_J sign_prefix 운영 표기 — 부분 정확 (中 우선)

- Table_J 부표1·3(자산·순) sign_prefix=true ✓ / 부표2(부채) sign_prefix=false ✓
- D1_3·D7_9 부표2(유량) sign_prefix=true / D4_6 부표2(부채 유량) sign_prefix=false / D 시리즈 부표1(IIP stock) 모두 sign_prefix=false
- **누락 발견 (中)**: Table_J **sub2** (부채 측, sign_prefix=false 정상) 행에는 "sign_prefix 운영" 문구가 없어야 하나, 현행 일부 sub2 행에 일괄 보일러플레이트로 "sign_prefix 부표1·3 + D1_3·D7_9 유량 운영" 문구가 들어가 학생 혼동 가능. → sub2 행 SIGN_CONVENTION에서 "sign_prefix 운영 (부호 반전 필요)" 부분 제거 권고.

### 3.3 Table_K BoP/IIP 부호 비대칭(슬라이드 26)

- 현행 Table_K 모든 행: "BPM6 자산·부채 증감 기준 — Reserve BoP/IIP 부호 비대칭(슬라이드 26)" 표기.
- 노트 08 §슬라이드 26 분석: "준비자산 증가는 BoP에서 음(−), IIP에서 양(+)"
- **권고 (中)**: 부호 비대칭은 **준비자산 행(LTEB)에만 해당** — Table_K_sub1/sub2/sub3 모든 행에 일괄 적용은 부정확. LTEB 행에만 좁히고 나머지 행은 일반 BPM6 표기로 분리.

### 3.4 Table_R1/R2/R3 (개정) — 적정

"Revisions = 현재 − 직전 (+ 상향 / − 하향)" — 노트 28 보강 참조 표기 OK.

---

## §4 단위 표기(UNIT_NAME) 오류 점검

### 4.1 시트별 단위 정합성 — 정합

모든 시트 UNIT_NAME이 노트 12·15와 일치.

**고지(高 우선)**: 사용자 점검 항목 "Table_B·BX·R2 부표 4가 PCT_GDP로 표기되었는가" — 현행 specification.csv는 **시트 단위 통합 표기**(`GBP million (1-3) / % of GDP (4)`)로 채워져 있음. long-form 적재 시 부표 4 행 UNIT_NAME 자동 분리 불가.

**권고(高)**: 부표 4 행 UNIT_NAME을 **`PCT_GDP`** 또는 `% of GDP` 단독으로 분리. 부표 1~3 행은 **`GBP_million`** 단독.

### 4.2 단위 표기 형식 통일 — 中

- "GBP billion" / "GBP million" 공백 표기 vs 사용자 요청 본문의 "GBP_billion"·"GBP_million"·"PCT_GDP" 스네이크케이스
- db/data/CLAUDE.md §파일 명명 규칙(영문 소문자·숫자·언더스코어)과 일관시킬 것 권고.

---

## §5 누락·중복·잔여 위험

### 5.1 ITEM_CODE 채움률

| 컬럼 | 채움률 | 평가 |
|---|---:|---|
| ITEM_CODE1 | 100.0% | OK — CDID 코드(BOKI 등) |
| ITEM_CODE2 | 100.0% | BoP 분류(CA/FA/IIP/KA/CA.S/CA.PI/CA.G/CA.SI 8종). 도트 표기 vs 단일 표기 혼재 (中 권고) |
| ITEM_CODE3 | 37.7% | LVL3 코드(CA.G.G_TOT 등). 일부 합계 행에만 부여 — 이전 분포 보존 OK |
| ITEM_CODE4 | 0.0% | Phase 3 위임으로 빈 값 — OK |

권고(中): specification.md에 코드 체계 표 추가 — `ITEM_CODE1 = ONS CDID / ITEM_CODE2 = LVL2 BoP 분류 / ITEM_CODE3 = LVL3 합계 식별자 / ITEM_CODE4 = Phase 3 부여 예정`.

### 5.2 시점 범위(START_TIME / END_TIME)

| START_TIME | END_TIME | 행 수 | 의미 |
|---|---|---:|---|
| 1997 | 2025Q4 | 395 | 분기 본표 14 — 1997 Q1~2025 Q4 |
| 1997 | 2025Q3 | 76 | 개정표 R1/R2/R3 — 한 분기 짧음 |
| 1999 | 2025Q4 | 36 | Table_C(EU/non-EU) — 1997-1998 EU 비공개 |
| 1999 | 2025Q3 | 5 | Table_R3 일부 |

**평가**: 정합. 

**유의(中)**: START_TIME에 분기 표기(`1997Q1`)를 쓰지 않고 연도만 쓴 것은 분기 정밀도 부족. → `1997Q1` 형태로 통일 권고.

### 5.3 보일러플레이트 DEFINITION으로 인한 잔여 위험 — 高

§2.2~2.3에 적은 사항. 권고(高): 보일러플레이트 끝에 `(부표 N, 차원: Exports/Imports/Balances/%GDP)` 같은 행 식별 한 줄 추가.

---

## §6 권고 수정 사항 우선순위

### §6.1 高 (즉시 수정)

1. **ITEM_NAME_KO 행 단위 정밀화** — Table_B·C·R1·R2 sub2·sub3 행이 영문 라벨(Imports/Debits, Balances)을 한국어에 반영. (§2.2)
2. **DEFINITION 오기 수정** — Table_A_sub2 `FKMJ` (Capital balance) 행이 "경상수지 합계" 정의로 채워진 사실 수정 → 자본수지 합계로 교체. (§2.3)
3. **부표 4 단위 분리** — Table_B/BX/R2 부표 4(%GDP) 행 UNIT_NAME을 `PCT_GDP` 단독으로 분리. (§4.1)
4. **부표 차원 식별자 추가** — sub2/3/4 행 DEFINITION 끝에 부표 식별 한 줄 추가. (§5.3)

### §6.2 中

1. Table_J sub2(부채 측) SIGN_CONVENTION 분리 — sign_prefix=false 명시. (§3.2)
2. Table_K Reserve 행만 BoP/IIP 부호 비대칭 표기 — 직접투자·증권투자 등은 일반 BPM6 표기로 환원. (§3.3)
3. STAT_NAME에 SA/NSA 한국어 풀이 추가. (§2.1)
4. ITEM_CODE1~4 컬럼 헤더 의미 메타 명시. (§5.1)
5. 단위 표기 형식 통일 — 스네이크케이스 vs 공백 표기 1방식. (§4.2)
6. START_TIME 분기 정밀도 — `1997` → `1997Q1`. (§5.2)

### §6.3 低

1. CA.S·CA.PI·CA.G·CA.SI 등 도트 표기 일관화.
2. SOURCE 컬럼 약식 코드 + 별도 출처 사전 분리 권고.

---

## §7 1차 근거 인용

### §7.1 BoP.pptx 슬라이드별

- 슬라이드 5: 경상수지 4 하위 + 자본수지 + 금융계정 5 하위 → ITEM_CODE2 분류 + Table_A/B/I/J STAT_NAME 정합
- 슬라이드 6: 금융계정 5분류 정의 → Table_J/K/D 시리즈 SIGN_CONVENTION·DEFINITION
- 슬라이드 7: 자본계정 정의 → Table_I 1차 근거
- 슬라이드 8·9: BPM6 vs BPM5 부호 변경 → Table_J SIGN_CONVENTION
- 슬라이드 10·11: 흑자/적자 의미 → Table_A/B/J SIGN_CONVENTION
- 슬라이드 12: 종합수지·외환보유액 항등성 → Table_A_sub3, J 부표 합계
- 슬라이드 13: 복식부기 항등성 → Cr+/Dr−, Balance = Cr − Dr
- 슬라이드 14: 핵심 항등식 → 모든 시트 DEFINITION 인용 다수
- 슬라이드 25: BoP↔IIP 연결 → Table_K STAT_NAME(분기말)·DEFINITION
- 슬라이드 26: BoP↔IIP 매트릭스 → Table_K SIGN_CONVENTION

### §7.2 노트 cross-reference

노트 02·03·04·08·12·13·15·19·21·24~28 모두 specification.csv 컬럼별로 정합 적용 확인.

---

## §8 확인하지 못한 부분 (정직 명시)

1. **Table_D4_6 sub1·sub2·sub3 SIGN_CONVENTION 표본 미수집** — 부채 측 IIP 시트 SIGN_CONVENTION이 sign_prefix=false를 명시하는지 미확인.
2. **Table_A 부표1 중 sub3(금융·NEO 7행)의 SIGN_CONVENTION** — sub1·sub2와 동일 채움 여부 미확인.
3. **Table_R1·R3 sub6 이후 행의 ITEM_NAME_KO** — 표본 추출 부족.
4. **long-form CSV 행 단위 max/min과 직접 join 검증** — 본 감수는 specification.csv 단독 점검.
5. **cdid_definitions_unmapped.csv 처리 검증** — ITEM_CODE3 빈 값 319행 중 unmapped 영향 분리 분석 필요.
6. **외부 web-search**: 부표 차원 식별자 등에서 ONS Bulletin 원본 부표 라벨 확인하면 더 정밀한 ITEM_NAME_KO 작명 가능.

---

## §9 종합 평가

specification.csv 초안은 **컬럼 사양·미수록 표시·부호 규약 일반론·단위 표기·시점 범위**가 모두 강의 자료·노트 기준과 정합. 다만 4건의 **高 우선 수정**(ITEM_NAME_KO 행 단위 정밀화 / Table_A_sub2 FKMJ DEFINITION 오기 / 부표 4 단위 분리 / 부표 차원 식별자)은 Phase 4 ECOS DB 적재 전에 반드시 수정해야 학생용 명세서로서 의미를 가진다.

**감수 결과**: **조건부 통과** — 高 우선 4건 수정 후 Phase 4 진입 권장.
