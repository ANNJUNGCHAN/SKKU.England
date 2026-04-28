# Phase 2.1 사전 점검 — 부표 분리 단위 ↔ 강의 BoP 위계 정합성

본 문서는 `db/CHECKLIST.md` §2.1 네 번째 항목("부표를 분리할 때 강의 자료의 BoP 항목 위계와 부표 분리 단위가 일치하는지 사전 점검") 산출물이다. 1차 근거는 `db/data/_inventory/15_master_inventory.csv`(20행 × 22열), `db/data/_inventory/16_curriculum_coverage_check.md`(강의 개념 47건 매핑), `background/note/12_xlsx_sheet_inventory.csv`(시트 인벤토리), `background/note/19_assets_liabilities_mapping.csv`(자산/부채 6축 매핑 54행), `background/note/02_bop_components.md`(BoP 5대 구성), `background/note/06_financial_account_categories.md`(FA 5분류), 그리고 `db/source/balanceofpayments2025q4.xlsx` 원본에서 직접 추출한 부표 타이틀(아래 §2 표의 `subtable_label_en` 컬럼).

## 1. 요지

- **본표 17개 시트**의 부표 분리 단위는 5가지 차원으로 수렴: ① **Cr/Dr/Bal 3분할**(Table_E·F·G·H·I + Table_C·R2 부분) ② **NAFA/NIL/Net 3분할**(Table_J ; Table_K stock의 Asset/Liability/Net 동형) ③ **IIP·Flow·Income 3분할**(Table_D1.3·D4.6·D7.9·R3) ④ **CA(SA)/CA(NSA)/FA 3분할**(Table_A·R1) ⑤ **EU/non-EU × Cr/Dr/Bal 6분할**(Table_C 단독) + **%GDP 추가 1분할**(Table_B·BX·R2의 sub4).
- 강의 자료(`background/BoP.pptx`)가 다루는 BoP 위계 (CA = G + S + PI + SI 4분류 / FA = DI + PI + FD + OI + IR 5분류 / IIP = Asset + Liability 양면)는 **시트 단위(가로 차원)** 로 표현되고, 부표는 모두 **직교(orthogonal) 차원** — 즉 위계의 "동일 항목"을 Cr/Dr/Bal 또는 자산/부채/순으로 재절단한 결과이다. 따라서 위계와 부표 차원이 **충돌하지 않으며**, 부표 분리 후에도 동일 시트 내 sub3(=Balances)·sub3(=Net)을 합산하면 강의 항등식이 그대로 검증된다.
- **충돌 케이스 0건**, **영국 특화 차원 2건**(Table_C 6 부표의 EU/non-EU 분해 + Table_R3 9 부표의 발표 회차 개정)이 강의 위계에 직접 등장하지 않아 학생용 1차 분석에서는 옵션·심화 자료로 분리 권장.
- Phase 2.1 ETL이 부표마다 별도 CSV를 생성할 때 (a) 강의 위계에 직접 매핑되는 부표(Cr/Dr/Bal·NAFA/NIL/Net·IIP·Flow·Income의 sub3 = Balances/Net 시리즈)를 **학생용 1차 분석 권장 부표**로 안내하고, (b) Table_C(EU/non-EU)와 Table_R(개정) 시리즈는 **영국 특화 / 운영 보조 자료**로 별도 섹션 분리, (c) Table_B/BX/R2 sub4(%GDP)는 단위 차이(`pct_of_GDP`) 때문에 별도 파일로 분리 — 이 3가지 권고를 본 문서 §5에서 단정.
- 결론: Phase 2.1 ETL의 "부표 = CSV 1개" 분리 단위는 강의 위계와 정합하며, 진행에 사전 차단 조건 없음. 다만 **파일명·헤더 메모에 부표의 차원을 명시**해야 학생이 강의 항등식과 1:1로 연결 가능.

## 2. 본표 17개 시트의 부표 분리 단위 카탈로그

`db/source/balanceofpayments2025q4.xlsx`의 메타 텍스트(시트 row 1~6) + 부표 타이틀 행(blank_row + 1)에서 직접 추출한 라벨이다. `subtable_dimension`은 본 점검에서 추론한 "부표 차원"의 한국어 정규명이다.

| # | sheet | classification | n_sub | subtable_label_en | subtable_dimension | 시트 단위 BoP 위계 |
|--:|---|---|---:|---|---|---|
| 1 | Table_A | summary | 3 | A.1 CA SA / A.2 CA NSA / A.3 Financial Account NSA | **CA(SA)·CA(NSA)·FA 3분할** | CA + FA 통합 요약 |
| 2 | Table_B | CA-main | 4 | B.1 CA Credits / B.2 Debits / B.3 Balances / B.4 %GDP | **Cr / Dr / Bal + %GDP** | CA 4분류 합계 |
| 3 | Table_BX | CA-main | 4 | BX.1 Cr / BX.2 Dr / BX.3 Bal / BX.4 %GDP (귀금속 제외) | **Cr / Dr / Bal + %GDP** | CA 4분류 (귀금속 제외) |
| 4 | Table_C | CA-main | 6 | C.1~C.3 EU Cr/Dr/Bal / C.4~C.6 non-EU Cr/Dr/Bal | **EU/non-EU × Cr/Dr/Bal** | CA × 지리(영국 특화) |
| 5 | Table_D1_3 | IIP | 3 | D.1 IIP abroad / D.2 FA tx abroad / D.3 Income abroad | **IIP/Flow/Income** (자산 측) | IIP·FA·1차소득 자산 |
| 6 | Table_D4_6 | IIP | 3 | D.4 IIP in UK / D.5 FA tx in UK / D.6 Income in UK | **IIP/Flow/Income** (부채 측) | IIP·FA·1차소득 부채 |
| 7 | Table_D7_9 | IIP | 3 | D.7 Net IIP / D.8 Net FA tx / D.9 Net Income | **IIP/Flow/Income** (순) | IIP·FA·1차소득 순 |
| 8 | Table_E | CA-detail | 3 | E.1 Exports / E.2 Imports / E.3 Balances of goods | **Exports/Imports/Balances** | 상품수지 (G) |
| 9 | Table_F | CA-detail | 3 | F.1 Exports / F.2 Imports / F.3 Balances of services | **Exports/Imports/Balances** | 서비스수지 (S, EBOPS 12) |
| 10 | Table_G | CA-detail | 3 | G.1 credits / G.2 debits / G.3 balances | **Cr / Dr / Bal** | 1차소득 (PI) |
| 11 | Table_H | CA-detail | 3 | H.1 credits / H.2 debits / H.3 balances | **Cr / Dr / Bal** | 2차소득 (SI) |
| 12 | Table_I | KA-FA | 3 | I.1 credits / I.2 debits / I.3 balances | **Cr / Dr / Bal** | 자본수지 (KA) |
| 13 | Table_J | KA-FA | 3 | J.1 NAFA / J.2 NIL / J.3 Net Transactions | **NAFA / NIL / Net** | 금융계정 5분류 양면 |
| 14 | Table_K | IIP | 3 | K.1 UK Assets / K.2 UK Liabilities / K.3 Net IIP | **Assets/Liabilities/Net** (stock) | IIP 양면 잔액 |
| 15 | Table_R1 | revision | 3 | R1.1 CA SA rev / R1.2 CA NSA rev / R1.3 FA rev | **CA(SA)·CA(NSA)·FA** (개정값) | 개정 운영 정보 |
| 16 | Table_R2 | revision | 4 | R2.1 Cr / R2.2 Dr / R2.3 Bal / R2.4 %GDP rev | **Cr/Dr/Bal + %GDP** (개정값) | 개정 운영 정보 |
| 17 | Table_R3 | revision | 9 | R3.1~R3.3 abroad×{IIP/FA/Income} / R3.4~R3.6 in UK×3 / R3.7~R3.9 net×3 | **{abroad/in UK/net} × {IIP/Flow/Income} 3×3** | IIP·FA·소득 양면×3 변동 |

부표 차원을 5축으로 정규화하면:

- **축 ①: Cr / Dr / Bal** — Table_B·BX·R2 sub1~3(9) + Table_E·F·G·H·I sub1~3(15) + Table_C 6 부표(EU/non-EU 직교 곱).
- **축 ②: NAFA / NIL / Net** — Table_J 3 부표. Table_K(stock)은 동일 축의 잔액 표현으로 동형(Asset/Liability/Net).
- **축 ③: IIP / Flow / Income** — Table_D1.3·D4.6·D7.9 (각 3) + Table_R3 (3축×3 = 9 부표).
- **축 ④: SA / NSA / FA** — Table_A·R1 (각 3 = 6 부표).
- **축 ⑤: %GDP** — Table_B·BX·R2의 sub4 (3 부표). 단위가 다른 분리.
- **축 ⑥: 지리(EU/non-EU)** — Table_C 단독, 축 ①을 직교 곱한 영국 특화 차원.

총 부표 수 = 3+4+4+6+3+3+3+3+3+3+3+3+3+3+3+4+9 = **63 부표**. Phase 2.1 ETL이 시트 17개로부터 63개 가로형 CSV를 생성한다.

## 3. 강의 위계 ↔ 부표 차원 정합성 매트릭스

강의 자료 3대 위계와 17 시트 × 5 부표 차원의 정합성을 ✓(직접 매핑) / ◐(부표 차원과 직교, 합산·선택으로 매핑) / ✗(영국 특화·운영 정보, 강의 위계 미수록)로 평가.

### 3.1 경상수지 4분류 (CA = G + S + PI + SI) ↔ 시트·부표

`background/note/02_bop_components.md` 슬라이드 14 항등식 `Current account = trade balance + balance on services + net primary income + net secondary income` 검증.

| 강의 항목 | 매핑 시트 | 매핑 부표 | 정합성 |
|---|---|---|---|
| 상품수지(G) | Table_E | E.3 Balances of goods | ✓ 직접 |
| 서비스수지(S) | Table_F | F.3 Balances of services | ✓ 직접 |
| 1차소득(PI) | Table_G | G.3 Primary income balances | ✓ 직접 |
| 2차소득(SI) | Table_H | H.3 Secondary income balances | ✓ 직접 |
| **CA 합계** | Table_A · Table_B(BX) | A.1 CA SA / B.3 CA Balances | ✓ 합계 시리즈 직접 제공 |
| **CA %GDP** (NIA 보조) | Table_B · BX | B.4 / BX.4 (단위: pct_of_GDP) | ✓ 직접 |

**판정**: 강의 항등식 `CA = G + S + PI + SI`는 **시트별 sub3(=Balances) 4개의 단순 합산** = Table_A의 A.1·A.2 또는 Table_B의 B.3 합계 라인으로 **이중 검증** 가능. 부표 분리 후에도 학생이 4개 CSV(`*_e_sub3.csv`, `*_f_sub3.csv`, `*_g_sub3.csv`, `*_h_sub3.csv`)를 키 결합해 합산하면 즉시 확인.

### 3.2 금융계정 5분류 양면 (FA = DI + PI + FD + OI + IR, NAFA/NIL/Net) ↔ 시트·부표

`background/note/06_financial_account_categories.md` + `background/note/19_assets_liabilities_mapping.csv` 54행 매핑 기준.

| 강의 항목 | 매핑 시트 | 매핑 부표 | 양면 분리 | 정합성 |
|---|---|---|---|---|
| 직접투자(DI) | Table_J · D1.3 · D4.6 · D7.9 | J.1·J.2·J.3 / D.2·D.5·D.8 (Flow) | NAFA/NIL/Net | ✓ 직접 |
| 증권투자(PI) | 동상 | 동상(컬럼만 다름) | 동상 | ✓ 직접 |
| 파생금융상품(FD) | 동상 | 동상 | Net only(슬라이드 14의 Net financial derivatives 표기와 정합) | ✓ 직접 (Net 단일) |
| 기타투자(OI) | 동상 | 동상 | NAFA/NIL/Net 모두 | ✓ 직접 |
| 준비자산(IR) | 동상 | J.1 col11 / D1.3 col6 / D7.9 col6 (asset-side only) | Asset only(통화당국 보유; LTCV/LTEB) | ✓ 직접 (Asset 단일) |
| **FA 합계(narrow)** | Table_J | J.3 Net Transactions에서 Reserve 제외분 | ✓ | ◐ 행 단위 추출 |
| **FA 합계(broad)** | Table_J · A.3 | J.3 합계 / A.3 FA NSA | ✓ | ✓ 직접 |
| **NAFA·NIL·Net 분할** | Table_J | J.1 / J.2 / J.3 (강의 슬라이드 14 식과 동일) | ✓ | ✓ **부표 차원이 강의 식과 1:1 동형** |

**판정**: Table_J의 부표 분리(NAFA / NIL / Net)는 **강의 슬라이드 14 식 `FA = NAFA - NIL + Net derivatives`와 정확히 동형**(부표 = 식의 항). 부표마다 별도 CSV로 분리되더라도 (a) 학생이 식의 각 항을 즉시 식별 가능하고, (b) 자산/부채 양면 분석에 그대로 사용 가능. **이 부표 분리는 강의 위계에 직접 등장하는 가장 강한 정합성 사례**.

### 3.3 IIP 양면 (Asset + Liability + Net, stock vs flow) ↔ 시트·부표

`background/note/05_iip_nfa.md` + `background/note/19_assets_liabilities_mapping.csv` 매핑.

| 강의 항목 | 매핑 시트 | 매핑 부표 | 정합성 |
|---|---|---|---|
| IIP Asset stock | Table_K · D1.3 | K.1 / D.1 | ✓ 직접 |
| IIP Liability stock | Table_K · D4.6 | K.2 / D.4 | ✓ 직접 |
| Net IIP stock (= NFA) | Table_K · D7.9 | K.3 / D.7 | ✓ 직접 |
| 거래 요인(=Flow) | D1.3 · D4.6 · D7.9 | D.2 / D.5 / D.8 | ✓ 직접 (FA flow와 동일) |
| 비거래 요인(가격·환율·기타) | (분기 자료에 없음) | — | ✗ 본 Bulletin 범위 외 (연간 Pink Book Dataset 8 필요) |
| 투자소득(연결) | G(=BoP flow) ↔ D.3 / D.6 / D.9 | G.1·G.2·G.3 / D.3·D.6·D.9 | ◐ 시트 간 결합으로 매핑 |

**판정**: IIP 양면(자산·부채·순) 분리는 **Table_K(stock)와 Table_D7_9·D1_3·D4_6(stock + flow + income)의 부표가 강의 구분과 정합**. 단 강의 슬라이드 26의 "비거래 요인 = 가격·환율·기타 3분해"는 분기 자료에는 없으며 부표 분리 단위와 무관(자료 범위 한계).

### 3.4 정합성 매트릭스 종합

| 강의 위계 | 직접 매핑 부표 수 | 합산·선택 매핑 | 미매핑 |
|---|---:|---:|---:|
| CA 4분류 (G·S·PI·SI) | 4 (E.3·F.3·G.3·H.3) + CA 합계 6 (A.1·A.2·B.3·BX.3·R1.1·R1.2) | %GDP 3 (B.4·BX.4·R2.4) | 0 |
| FA 5분류 양면 | 양면 9 (J.1·J.2·J.3 + D.2·D.5·D.8 + 공통 컬럼들) | (없음) | 비거래요인 부표 0 (분기 한계) |
| IIP 양면 stock+flow | 양면 9 (K.1·K.2·K.3 + D.1·D.4·D.7 + Flow 3) | 투자소득 결합 3 (D.3·D.6·D.9) | 가격·환율 재평가 (연간) |
| 자본계정(KA) | 3 (I.1·I.2·I.3) | (CA·FA와 별개) | 0 |
| %GDP / NIA 보조 | 3 (B.4·BX.4·R2.4) | (없음) | NIA의 Y·C·I·G (Blue Book 외부) |
| **합계** | **40 부표 직접** | **3 부표 합산** | **0 부표 충돌** |

총 63 부표 중 **40개(63%)가 강의 위계에 직접 매핑**, **3개(5%)가 합산·축 변환으로 매핑**, **20개(32%)는 영국 특화 차원**(Table_C 6 + Table_R 시리즈 16) — 이는 위계 충돌이 아니라 강의 미수록 차원으로, §4에서 별도 분석.

## 4. 잠재적 충돌 케이스 분석

부표 분리 단위와 강의 위계가 직접 일치하지 않는 시트 3개(Table_C·Table_J·Table_R3)를 정밀 평가했다. **3 시트 모두 위계 충돌은 없으며**, Table_C·R3는 강의 미수록 차원(영국 특화·운영 정보), Table_J는 강의 슬라이드 14 식과 오히려 **가장 강한 정합성**을 보인다.

### 4.1 Table_C (CA × EU/non-EU 6 부표)

- 부표 차원: `EU / non-EU` × `Cr / Dr / Bal` 6분할.
- 강의 위계: **EU/non-EU 지리 분해는 강의 자료에 등장하지 않음** (`16_curriculum_coverage_check.md` §5 "과잉 커버리지" 행).
- 충돌 평가: 강의 위계가 다루는 CA 4분류(G·S·PI·SI)는 시트 가로 컬럼으로 표현되고, 부표는 EU/non-EU × Cr/Dr/Bal로 직교 분리. 따라서 **위계와 충돌 없음** — Table_C.3과 Table_C.6의 행 합계 = Table_B.3 (전체 CA Balances) 항등성으로 검증 가능.
- **학생용 학습 모듈 가능성**: 슬라이드 9의 한국 사례에는 없는 **Brexit 후 영국 특화 차원**으로, "1차소득 EU vs non-EU 분해"·"서비스수지의 EU 의존도 변화"·"상품 vs 서비스의 지리 비대칭" 같은 영국 사례 분석 모듈을 학생용 심화 과제로 활용 가능. `background/note/23_geographic_breakdown.md` Pink Book Ch.10·11과 1:1 정합.
- **결론**: 충돌 0, 학생용 심화 모듈 후보로 **별도 섹션 분리 권장**.

### 4.2 Table_J (FA NAFA / NIL / Net 3 부표)

- 부표 차원: `NAFA / NIL / Net Transactions` 3분할(자산취득 / 부채발생 / 순거래).
- 강의 위계: 슬라이드 14의 `Financial account = Net acquisition of foreign financial assets - Net incurrence of liabilities + Net financial derivatives` 식이 **부표 분리 단위와 정확히 동형**.
- 충돌 평가: **충돌 없음. 정합성 최강** — 부표 J.1·J.2·J.3은 식의 NAFA·NIL·(좌변 합) 항에 1:1 대응. `background/note/06_financial_account_categories.md` 추가 맥락에 명시된 "광의·협의 구분"과 결합하면 부표 J.3이 광의 FA(준비자산 포함), J.3에서 "Reserve assets" 행 제외분이 협의 FA임을 식별 가능.
- **양면 회계 정합성**: `background/note/19_assets_liabilities_mapping.csv` 5분류 × {asset/liability/net} × {flow/stock} 6축 매핑이 Table_J 컬럼·부표 위에서 그대로 검증됨(54행 모두 sheet=Table_J 또는 Table_D·K로 매핑됨).
- **결론**: 충돌 0, **강의 항등식 검증 1차 시트**로 학생 분석에 가장 우선 사용 권장.

### 4.3 Table_R3 (IIP 개정 9 부표)

- 부표 차원: `{abroad / in UK / net}` × `{IIP stock / FA flow / Income}` 3×3 = 9분할 (개정값).
- 강의 위계: 슬라이드 26 도식의 "거래요인 vs 비거래요인" 분해와 부분 정합 — `(in_UK FA flow)` + `(abroad FA flow)` = 거래요인 / `(IIP_t - IIP_t-1 - flow)` = 비거래요인. 단 슬라이드 26은 BoP→IIP 1방향 도식이고, R3는 **개정값(직전 발표 대비 차이)** 이므로 **강의 도식의 직접 표현은 아님**.
- 충돌 평가: **충돌 없음**. R3 9 부표는 (a) IIP·FA·Income 3축을 양면(자산·부채·순) × 3 = 9로 분리하는 ONS 운영 차원으로, 강의 위계의 어떤 항목과도 모순되지 않음. 학생용 학습 부담 측면에서는 9개 CSV를 다 읽을 필요는 없고, **R3.7 Net IIP 개정** 1개만 슬라이드 26 비거래요인 분해 보조 자료로 활용 가능.
- **학생용 학습 부담**: 9 부표는 강의 1차 분석에서 제외 권장. Phase 2.1 ETL은 9개 CSV를 모두 생성하되 학생용 README에서 "심화 / 운영 자료" 섹션으로 분리.
- **결론**: 충돌 0, 학습 부담 고려 별도 섹션 분리 권장.

### 4.4 그 외 점검 — Table_B/BX/R2 sub4 (%GDP)

- 부표 차원: `%GDP` (단위: pct_of_GDP, scale_factor 다름).
- 강의 위계: 슬라이드 22 NIA 항등식 `Y = C + I + G + (EX - IM)`에서 GDP 분모 시계열 보조. 강의 직접 도식은 없으나 NIA(흡수 A = C+I+G ; X-M = Y-A) 적용 시 비교 기준.
- 충돌 평가: **단위 차이로 인한 분리만 필요**. 위계와 충돌은 없으나 **단위가 다른 부표를 같은 long-form CSV에 합치면 데이터 값 의미가 깨짐** → Phase 2.1 ETL의 `subtable_split_required=yes` 플래그로 이미 식별됨(`15_master_inventory.csv` 컬럼). 분리 처리 필수.

## 5. Phase 2.1 ETL 권고사항

본 §은 부표마다 별도 CSV를 생성하는 Phase 2.1 단계에서 **학생용 1차 분석을 위한 부표 분류**와 **파일명·메모 규칙**을 단정한다.

### 5.1 학생용 분석 우선순위 분류

| 우선순위 | 분류 | 부표 (n=63) | 강의 매핑 | Phase 2.1 출력 처리 |
|---|---|---|---|---|
| **1차** | CA 4분류 항등식 검증 | E.3·F.3·G.3·H.3 + B.3·BX.3 + A.1·A.2 = **8 부표** | 슬라이드 14 `CA = G+S+PI+SI` | README "1차 분석 권장" |
| **1차** | FA 양면 회계(슬라이드 14 식) | J.1·J.2·J.3 + A.3 = **4 부표** | 슬라이드 14 `FA = NAFA-NIL+Net deriv` | 동일 |
| **1차** | IIP 양면 stock | K.1·K.2·K.3 = **3 부표** | 슬라이드 25 BoP↔IIP | 동일 |
| **1차** | KA | I.3 = **1 부표** | 슬라이드 5·14 KA | 동일 |
| **2차** | IIP·FA·Income 결합 | D.1·D.2·D.3·D.4·D.5·D.6·D.7·D.8·D.9 = **9 부표** | 슬라이드 25·26 도식 | "거래요인 1차 분석은 Table_J 우선, IIP↔FA 연결 검증용" |
| **2차** | CA Cr/Dr 상세 | E.1·E.2·F.1·F.2·G.1·G.2·H.1·H.2·I.1·I.2 + B.1·B.2·BX.1·BX.2 = **14 부표** | 슬라이드 13 복식부기 Cr/Dr | 동일 |
| **심화** | %GDP NIA 보조 | B.4·BX.4·R2.4 = **3 부표** | 슬라이드 22 NIA | 단위 `pct_of_GDP` 헤더 명시, GBP CSV와 결합 금지 |
| **심화** | 영국 특화 지리 분해 | C.1~C.6 = **6 부표** | (강의 미수록) | "영국 특화 / Brexit 분석" 섹션 분리 |
| **운영** | 개정 정보 | R1.1·R1.2·R1.3 + R2.1~R2.3 + R3.1~R3.9 = **15 부표** | (강의 미수록) | "ONS 분기 개정" 섹션, 학생 1차 미포함 |

총 63 부표 = 1차 16 + 2차 23 + 심화 9 + 운영 15 = 63.

### 5.2 파일명 규칙

- **기본 규칙**: `<원본어간>_<table_code_lower>_sub<n>.csv` 패턴. 예:
  - `balanceofpayments2025q4_e_sub1.csv` (E.1 Exports of goods)
  - `balanceofpayments2025q4_e_sub2.csv` (E.2 Imports of goods)
  - `balanceofpayments2025q4_e_sub3.csv` (E.3 Balances of goods) ← **학생용 1차 분석 권장**
- Table_D 계열은 D1_3 / D4_6 / D7_9 어간 유지(원본 시트명) → `..._d1_3_sub2.csv`(D.2 FA flow abroad) 등.
- Table_C 6 부표 → `..._c_sub1.csv` ~ `..._c_sub6.csv` (EU Cr·EU Dr·EU Bal·non-EU Cr·non-EU Dr·non-EU Bal).
- Table_R3 9 부표 → `..._r3_sub1.csv` ~ `..._r3_sub9.csv`.
- 메타 시트(Cover_sheet·Notes·Records)는 long-form CSV 미생성, 한국어 메모 `db/data/balanceofpayments2025q4_meta.md`로 통합.
- 모두 **영문 소문자·숫자·언더스코어**만 사용 (`db/data/CLAUDE.md` 파일 명명 규칙 준수).

### 5.3 동반 메모(`<csv명>.md`) 필수 기재 항목

`db/data/CLAUDE.md` "산출물에 함께 남길 정보" 규칙을 본 부표 분리 맥락으로 구체화:

1. **원본 위치**: `db/source/balanceofpayments2025q4.xlsx` 시트 `<sheet>` 부표 라벨, 행 범위.
2. **부표 차원**: 본 §2 표의 `subtable_dimension` 값 (예: "Cr / Dr / Bal 3분할").
3. **강의 위계 매핑**: 본 §3 표에서 직접 매핑되는 강의 항목 (예: "강의 슬라이드 5·14의 1차소득 PI" / "Table_J = 슬라이드 14 식 NAFA·NIL·Net 동형").
4. **단위·기간**: `unit_normalized` (`GBP_million` / `GBP_billion` / `pct_of_GDP`), `time_format` (annual + quarterly 적층 등).
5. **결측 표기**: 원본의 `..` / `-` / 공란 의미 (`12_missing_markers.csv`·`13_missing_meaning_validation.md` 인용).
6. **부호 규약**: BPM6 기준 `+`/`-` 의미. Table_J의 경우 CDID 공백+마이너스 prefix 안내(`background/note/13_cdid_dictionary.csv`).
7. **항등식 연결**: 1차 분석 권장 부표(16개)의 경우 강의 항등식 1개 명시 — 예: "이 CSV의 sub3(E.3) + F.3 + G.3 + H.3 = Table_B.3 = CA 합계".
8. **재현 스크립트**: `db/code/<spec>.py` (Phase 2.1 ETL 스크립트 경로).

### 5.4 학생용 README(`db/data/README.md`) 권고 섹션 구조

```
## Phase 2.1 가공 산출물 안내

### 1차 분석 권장 (강의 항등식 직접 검증) — 16 CSV
- balanceofpayments2025q4_a_sub1.csv (CA SA 합계, A.1)
- balanceofpayments2025q4_a_sub2.csv (CA NSA 합계, A.2)
- balanceofpayments2025q4_a_sub3.csv (FA NSA, A.3)
- balanceofpayments2025q4_b_sub3.csv (CA Balances, B.3)
- balanceofpayments2025q4_bx_sub3.csv (귀금속 제외 CA, BX.3)
- balanceofpayments2025q4_e_sub3.csv (상품수지 G, E.3)
- balanceofpayments2025q4_f_sub3.csv (서비스수지 S, F.3)
- balanceofpayments2025q4_g_sub3.csv (1차소득 PI, G.3)
- balanceofpayments2025q4_h_sub3.csv (2차소득 SI, H.3)
- balanceofpayments2025q4_i_sub3.csv (자본수지 KA, I.3)
- balanceofpayments2025q4_j_sub1.csv (NAFA, J.1)
- balanceofpayments2025q4_j_sub2.csv (NIL, J.2)
- balanceofpayments2025q4_j_sub3.csv (Net FA, J.3)
- balanceofpayments2025q4_k_sub1.csv (UK Assets stock, K.1)
- balanceofpayments2025q4_k_sub2.csv (UK Liabilities stock, K.2)
- balanceofpayments2025q4_k_sub3.csv (Net IIP stock, K.3)

### 2차 분석 (IIP·FA flow·Income 통합 검증 + Cr/Dr 상세) — 23 CSV
... D 계열 9 + Cr/Dr 상세 14 ...

### 심화 / 영국 특화 — 9 CSV
- balanceofpayments2025q4_b_sub4.csv (CA %GDP, 단위 주의)
- balanceofpayments2025q4_bx_sub4.csv
- balanceofpayments2025q4_c_sub1.csv ~ c_sub6.csv (EU/non-EU 지리 분해)

### 운영 정보 (ONS 개정값) — 15 CSV
- balanceofpayments2025q4_r1_sub1.csv ~ r3_sub9.csv
```

### 5.5 Phase 2.1 ETL 진입 단정

본 점검 결과 **부표 분리 단위와 강의 BoP 위계 사이 충돌 0건**, 영국 특화·운영 정보 차원은 별도 섹션 분리로 학생 학습 부담 경감 가능. 따라서 `db/CHECKLIST.md` §2.1 네 번째 항목은 **사전 점검 통과**, Phase 2.1 ETL 진입 가능.

## 6. 출처

### 1차 근거 (저장소 내)

- `db/data/_inventory/15_master_inventory.csv` — 시트당 1행 × 22 컬럼 (n_subtables · all_cdid_rows · blank_row_positions · subtable_split_required 등).
- `db/data/_inventory/16_curriculum_coverage_check.md` — 강의 개념 47건 ↔ 시트 매핑 표(시트 단위 91% 커버).
- `db/data/_inventory/11_subtable_boundaries.csv` — 부표 경계 빈 행 위치(20행).
- `db/data/_inventory/09_units.csv` — 시트별 단위·`subtable_split_required` 플래그.
- `db/data/_inventory/05_meta_text.csv` — 시트 row 1~6 메타 텍스트 120행("This worksheet contains N tables...").
- `db/data/_inventory/17_phase2_readiness.md` — Phase 2 입력 사양 충족 매트릭스.

### 강의 자료 (1차 근거)

- `background/BoP.pptx` (31 슬라이드) — 슬라이드 5(BoP 5대 구성) / 6(FA 5분류) / 13(복식부기 Cr/Dr) / 14(항등식 `CA = FA(narrow)+Reserve = FA(broad)`, `FA = NAFA - NIL + Net deriv`) / 25(BoP↔IIP) / 26(거래·비거래요인 도식).
- `background/note/02_bop_components.md` — BoP 5대 구성 강의 발췌.
- `background/note/06_financial_account_categories.md` — FA 5분류 발췌 + BPM6 정합성.
- `background/note/05_iip_nfa.md` — IIP·NFA 정의.
- `background/note/12_xlsx_sheet_inventory.csv` — 시트 인벤토리 + Pink Book 챕터 매핑.
- `background/note/19_assets_liabilities_mapping.csv` — 5분류 × {asset/liability/net} × {flow/stock} 6축 매핑 54행.
- `background/note/23_geographic_breakdown.md` — Pink Book Ch.9·10 EU/non-EU 분해 (Table_C 영국 특화 근거).

### 부표 타이틀 추출

- `db/source/balanceofpayments2025q4.xlsx` (read-only, openpyxl 3.1.5) — 17 본표 시트 × 부표 타이틀 행(blank_row+1) 직접 추출. 본 문서 §2 `subtable_label_en` 컬럼이 추출 결과.
- 추출 로직: blank_row 위치(`master_inventory.blank_row_positions`)에서 +1 ~ +6 범위 첫 셀이 "Table X.n" 패턴이면 부표 타이틀로 인식.

### 관련 규칙

- `db/CLAUDE.md` — 가공 원칙(데이터 값 불변·구조만 조정).
- `db/data/CLAUDE.md` — 가공본 파일 명명·메모 규칙.
- `CLAUDE.md` (루트) — 한국어 유지·`env/` 가상환경 사용.
