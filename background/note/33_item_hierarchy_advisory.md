# 33회차 — Phase 4.1 §4 통계항목 위계(P_ITEM_CODE / LVL) 자문

본 노트는 `db/CHECKLIST.md` Phase 4.1 §4번([background-search] 통계항목 위계를 BoP 항목 트리에 일관 적용할 수 있는지 자문) 산출물. 강의 슬라이드 5·6·7·25(BoP·IIP 위계) + 노트 19·30·31·32 결합으로 BoP 4계층 + IIP 3계층 위계의 RDB 적용 가능성 자문.

---

## §1 강의 자료 BoP 위계 (슬라이드 5·6·7) → LVL1·LVL2·LVL3 매핑

### §1.1~§1.3 슬라이드 발췌

슬라이드 5: 경상계정·금융계정·자본계정 1차 분류 + 경상계정 4 하위(상품·서비스·1차소득·2차소득). 슬라이드 6: 금융계정 5 하위(직접·증권·파생·기타·준비자산). 슬라이드 7: 자본계정(very small, 자본이전·NPNFA).

### §1.4 LVL1·LVL2·LVL3·LVL4 매핑 표 (BoP, 4 계층)

| LVL1 | LVL2 | LVL3 | LVL4 | 한국어 | 영문 | ITEM_CODE | P_ITEM_CODE | 1차 근거 |
|:---:|:---:|:---:|:---:|---|---|---|---|---|
| 1 | — | — | — | 국제수지 | Balance of Payments | `BOP` | NULL | slide 1·3·4·5 |
| 2 | 경상계정 | — | — | 경상계정 | Current account | `CA` | `BOP` | slide 5 |
| 2 | 자본계정 | — | — | 자본계정 | Capital account | `KA` | `BOP` | slide 5·7 |
| 2 | 금융계정 | — | — | 금융계정 | Financial account | `FA` | `BOP` | slide 5·6 |
| 3 | CA | 상품수지 | — | 상품수지 | Trade balance | `CA.G` | `CA` | slide 5 |
| 3 | CA | 서비스수지 | — | 서비스수지 | Balance on services | `CA.S` | `CA` | slide 5 |
| 3 | CA | 본원소득수지 | — | 1차소득 | Primary income | `CA.PI` | `CA` | slide 5 |
| 3 | CA | 이전소득수지 | — | 2차소득 | Secondary income | `CA.SI` | `CA` | slide 5 |
| 3 | FA | 직접투자 | — | 직접투자 | Direct investment | `FA.DI` | `FA` | slide 6 |
| 3 | FA | 증권투자 | — | 증권투자 | Portfolio investment | `FA.PI` | `FA` | slide 6 |
| 3 | FA | 파생금융상품 | — | 파생금융상품 | Financial derivatives | `FA.DR` | `FA` | slide 6 |
| 3 | FA | 기타투자 | — | 기타투자 | Other investment | `FA.OI` | `FA` | slide 6 |
| 3 | FA | 준비자산증감 | — | 준비자산증감 | Changes in reserve assets | `FA.RA` | `FA` | slide 6 |
| 4 | CA.G | — | (SITC 5분류) | 식품·원료·연료·화학·기계·기타 | (Trade in goods sub) | `CA.G.SITC*` | `CA.G` | 강의 자료 미수록 — 노트 26 |
| 4 | CA.S | — | (EBOPS 12분류) | 운수·여행·로열티·… | (Trade in services 12) | `CA.S.EBOPS*` | `CA.S` | 강의 자료 미수록 — 노트 24 |

LVL1~LVL3은 강의 자료 직접 명시. LVL4(EBOPS 12·SITC 5·NMG 보정 등)는 ONS 매뉴얼·운영 규칙 기반.

---

## §2 강의 자료 IIP 위계 (슬라이드 25) → LVL 매핑

### §2.1 슬라이드 25 발췌

> "국제수지표(B.O.P): flow 통계 / 국제투자대조표(IIP): stock 통계 / IIP의 증감내역은 거래요인과 비거래요인으로 구분 / 거래요인 = BoP 투자수지 + 준비자산증감 합계와 일치"

### §2.2 IIP LVL 매핑 표 (3 계층)

| LVL1 | LVL2 | LVL3 | LVL4 | 한국어 | 영문 | ITEM_CODE | P_ITEM_CODE | 근거 |
|:---:|:---:|:---:|:---:|---|---|---|---|---|
| 1 | — | — | — | 국제투자대조표 | IIP | `IIP` | NULL | slide 4·25 |
| 2 | 자산 | — | — | 자산 | Investment abroad / Assets | `IIP.A` | `IIP` | slide 25 |
| 2 | 부채 | — | — | 부채 | Investment in the UK / Liabilities | `IIP.L` | `IIP` | slide 25 |
| 2 | 순 | — | — | 순(자산−부채) | Net IIP | `IIP.N` | `IIP` | slide 25 산문 + Table_D7_9·K |
| 3 | IIP.A | DI~RA | — | 5분류 자산 stock | IIP …, asset | `IIP.A.{DI/PI/DR/OI/RA}` | `IIP.A` | slide 6 + Table_D1_3 |
| 3 | IIP.L | DI~OI | — | 4분류 부채 stock(RA 부채 부재) | IIP …, liability | `IIP.L.{DI/PI/DR/OI}` | `IIP.L` | 노트 19(D4_6) |
| 3 | IIP.N | DI~RA | — | 5분류 순 stock | IIP …, net | `IIP.N.{DI/PI/DR/OI/RA}` | `IIP.N` | 노트 19(D7_9·K) |

---

## §3 ONS Table → LVL 매핑 일관성 점검 (17 본표)

| 시트 | 표 코드 | 분류 | LVL 범위 | 비고 |
|---|---|---|:---:|---|
| Table_A | A | summary | LVL1~LVL3 요약 | BoP 잔액 요약 |
| Table_B | B | CA-main | LVL2~LVL3 + 부표 4=`%GDP` 별 차원 | %GDP는 LVL이 아닌 차원 |
| Table_BX | BX | CA-main | LVL2~LVL3 + `precious_metals_treatment=excluded` | 별 차원 |
| Table_C | C | CA-main | LVL2~LVL3 + `geo_breakdown=EU/non-EU` | 별 차원 |
| Table_D1_3 | D1.3 | IIP-asset | LVL2(`IIP.A`) + LVL3(DI/PI/DR/OI/RA) | 노트 19 |
| Table_D4_6 | D4.6 | IIP-liability | LVL2(`IIP.L`) + LVL3(DI/PI/DR/OI) | RA 부채 부재 |
| Table_D7_9 | D7.9 | IIP-net | LVL2(`IIP.N`) + LVL3(DI/PI/DR/OI/RA) | DI=NAFA−NIL |
| Table_E~H | E~H | CA-detail | LVL3(`CA.G/S/PI/SI`) + LVL4 | LVL4 강의 미수록 |
| Table_I | I | KA | LVL2(`KA`) + LVL3 | slide 7 |
| Table_J | J | FA | LVL2(`FA`) + LVL3(DI~RA) + 부표 1·2·3 양면 차원 | sign_prefix 별 메타 |
| Table_K | K | IIP 종합 | IIP LVL1~LVL3 sub1·sub2·sub3 | BoP↔IIP 부호 비대칭 Reserve만 |
| Table_R1·R2·R3 | R | revision | LVL + `revision_flag` 별 차원 | 개정은 별 차원 |

17 본표 모두 LVL1~LVL3 매핑 가능. ONS 추가 분해(EU/non-EU·BX·%GDP·개정)는 LVL이 아닌 별도 차원으로 분리.

---

## §4 P_ITEM_CODE 부모 키 운영 권고

### §4.1 부모 키 결정 규칙

1. **루트(LVL=1)**: `P_ITEM_CODE = NULL` — `BOP`·`IIP` 두 루트 병렬.
2. **LVL=2**: `P_ITEM_CODE = LVL1 루트` (`BOP` 또는 `IIP`).
3. **LVL=3**: `P_ITEM_CODE = LVL2 부모` (예: `CA.G` → `CA`).
4. **LVL=4**: `P_ITEM_CODE = LVL3 부모`.
5. **합계 라인**: 자기 자신을 부모로 두지 않고, 합계 행은 해당 LVL의 root이고 세부 라인이 그 root을 부모로 가리킴.

### §4.2 합계 라인 vs 세부 라인 (강의 슬라이드 14 항등식)

> "Current account = trade balance + balance on services + net primary income + net secondary income"
> "Financial account = NAFA − NIL + Net financial derivatives"

CA(LVL=2) ← {CA.G·CA.S·CA.PI·CA.SI}(LVL=3) 4 자식. P_ITEM_CODE=`CA` 일관. FA(LVL=2) ← {FA.DI·PI·DR·OI·RA}(LVL=3) 5 자식.

### §4.3 LVL=4 ITEM_CODE4 위임 권고

강의 자료 직접 근거 부족 → **ITEM_CODE4 컬럼**으로 별도 식별자 부여. LVL=4 정수 운영은 가능하되 ECOS 관행상 표준은 외부 검증 필요.

### §4.4 ECOS `P_ITEM_CODE` NULL 정책

| 행 유형 | LVL | P_ITEM_CODE |
|---|:---:|---|
| 루트 (BOP, IIP) | 1 | NULL |
| 1차 분류 | 2 | LVL1 코드 |
| 2차 분류 | 3 | LVL2 코드 |
| 3차 분류 (LVL4) | 4 | LVL3 코드 |

---

## §5 강의 자료 위계와 ONS Table 위계의 충돌 점검

### §5.1 슬라이드 5 vs Table_E·F·G·H — 1:1 정합 ✓

### §5.2 슬라이드 6 vs Table_J·D·K — 1:1 정합

단 **Derivatives flow 자산·부채 분리 부재**(net only) + **Reserve 부채 측 부재**(BPM6 정의)는 ITEM_CODE 트리상 결측으로 운영 권고.

### §5.3 ONS의 추가 분해 — 강의 위계에 부재 (별도 차원으로 처리)

| ONS 추가 분해 | 시트 | 권고 차원 컬럼 |
|---|---|---|
| EU vs non-EU 지리 | Table_C | `geo_breakdown` (`total`/`EU`/`non-EU`) |
| 귀금속 제외 보정 | Table_BX | `precious_metals_treatment` (`included`/`excluded`) |
| % of GDP | Table_B/BX/R2 부표 4 | `unit_variant` (UNIT_NAME 분리) |
| 개정 | Table_R1/R2/R3 | `revision_flag` (`current`/`revision`) |

LVL은 BoP·IIP 산문 위계만 담고, ONS 운영 차원은 LVL 외 컬럼으로 분리.

---

## §6 ECOS LVL·P_ITEM_CODE 컬럼 명세

| 컬럼 | 데이터형 | NULL | 권고값 |
|---|---|:---:|---|
| `LVL` | INTEGER (1·2·3·4) | NOT NULL | 1~4 |
| `P_ITEM_CODE` | VARCHAR(64) | NULL 허용 (루트만) | 루트 NULL |
| `ITEM_CODE` | VARCHAR(64) | NOT NULL UNIQUE | §1·§2 표기 |
| `ITEM_NAME_KO` | VARCHAR(255) | NOT NULL | slide 5·6·7·25 한국어 |
| `ITEM_NAME_EN` | VARCHAR(255) | NOT NULL | slide 5·6·7·25 영문 |

ECOS 표준 데이터형(LVL=INT, P_ITEM_CODE=STR)·NULL 정책은 강의 자료 미수록 → 외부 검증 필요.

---

## §7 출처 카탈로그

| 자료 | 본 노트 사용 |
|---|---|
| `BoP.pptx` slide 5·6·7·25 | §1·§2·§3·§4 |
| `note/02_bop_components.md` | §1.4 |
| `note/12_xlsx_sheet_inventory.md` | §3 |
| `note/19_assets_liabilities_mapping.md` | §2.2·§5.2 |
| `note/21_slide_22_25_visual_check.md` | §2.1 |
| `note/30_specification_review.md` | §1.5·§3·§5.3 |
| `note/31_field_classification.md` | §1.5·§5.3 |
| `note/32_metadata_model.md` | §1.5·§4.4·§6 |

---

## §8 확인 못한 부분 (정직 명시)

1. **ECOS Open API `LVL` 데이터형·표기 규약** — 강의 자료 미수록.
2. **ECOS `P_ITEM_CODE` 빈 문자열 vs NULL 관행** — 한국은행 ECOS 화면·Open API 응답 실측 필요.
3. **LVL=4 정수 표기 표준성** — ECOS 5 이상 확장 여부 본 폴더로 결정 불가.
4. **EBOPS·SITC 자체의 ITEM_CODE 표기 규약** — 노트 24·26은 분류 명칭만 정리.
5. **강의 자료 한국어("본원소득수지") vs IMF/한국은행 매뉴얼("1차소득") 차이** — 노트 31 §6.6과 정합.
6. **부문별 분해(LVL4)** — 강의 자료 미수록(노트 22·23). Pink Book Ch.11 보강 필요.
7. **Table_K BoP↔IIP 부호 비대칭의 LVL 트리 영향** — SIGN_CONVENTION 별도 컬럼으로 분리 가능하나 ECOS 관행 미확인.
8. **개정(Revisions) ECOS 표준 처리** — 별도 STAT_CODE 적재 vs `revision_flag` 컬럼 통합 — 외부 검증 필요.

---

## §9 종합 자문 결과

**강의 자료 슬라이드 5·6·7·25 위계는 BoP 4계층(LVL1~LVL4) + IIP 3계층(LVL1~LVL3)으로 P_ITEM_CODE/LVL에 일관 적용 가능**. ONS 17 본표 모두 LVL1~LVL3 정합.

**4 운영 결정 필요**:
1. ONS 추가 분해(EU/non-EU·BX·%GDP·개정)는 LVL이 아닌 별 차원 컬럼으로 분리.
2. LVL=4(EBOPS·SITC)는 ITEM_CODE4 컬럼 + 선택적 LVL=4 정수 운영.
3. 합계 라인은 자기 자신의 ITEM_CODE를 LVL 부모 코드로 두고 평면 트리.
4. Derivatives flow 자산·부채 분리 부재 / Reserve 부채 부재는 NULL 정책.

**자문 결론**: **조건부 가능**. ECOS Open API 컬럼 표기·NULL 관행은 외부 web-search 추가 검증 후 Phase 4 ETL 진입 권장.
