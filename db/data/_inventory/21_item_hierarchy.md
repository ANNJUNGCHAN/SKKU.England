# Phase 2.2 — 통계항목 위계(ITEM_CODE2~4) 분류 트리·매핑 규칙

본 문서는 `db/CHECKLIST.md` §2.2 두 번째 항목("항목 위계를 강의 자료의 분류 트리에 맞춰 ITEM_CODE2~4 매핑 자문 요청") 산출물이다. Phase 2.2 세로형 통합 CSV의 `ITEM_CODE2`·`ITEM_CODE3`·`ITEM_CODE4`(= ECOS의 P_ITEM_CODE / LVL 대응) 컬럼을 채우기 위한 **분류 트리 자체와 매핑 규칙**을 단정한다. 17 시트 × 평균 7 CDID = 약 284 고유 CDID에 대한 LVL 일대일 라벨은 본 단계에서 작성하지 않으며, 그 작업은 Phase 3.2(명세서)로 위임한다.

1차 근거: `background/BoP.pptx` (슬라이드 4–14·21·25·26) + `background/note/02_bop_components.md`(BoP 5대 구성), `background/note/06_financial_account_categories.md`(FA 5분류), `background/note/07_glossary.md`(62 표제어 9 분류), `background/note/13_cdid_dictionary.csv`(512 행 / 284 고유 CDID), `background/note/19_assets_liabilities_mapping.csv`(54 행 5분류×양면), `db/data/_inventory/16_curriculum_coverage_check.md`(강의 개념 47건), `db/data/_inventory/18_subtable_curriculum_alignment.md`(부표 차원 5축 + 63 부표).

## 1. 요지 (5~7줄)

- 강의 자료(`background/BoP.pptx` 31 슬라이드)의 BoP 분류 트리는 **LVL 1: 6 대분류**(CA·KA·FA·IR·IIP·NEO) → **LVL 2: 14 중분류**(CA의 G·S·PI·SI 4 + FA의 DI·PI금융·FD·OI·IR 5 + IIP의 Asset·Liability·Net 3 + KA·NEO) → **LVL 3: 약 30 소분류**(SITC 5 상품군 + EBOPS 12 서비스 + Compensation/Investment income/Other PI + 직접투자 Equity·Reinvestment·Debt + 증권투자 Equity·Debt + 회사간 거래 등) → **LVL 4: 잔여 세부**(EU/non-EU·연도/분기·SA/NSA·개정여부)로 정리된다.
- ITEM_CODE1(CDID 4자) ↔ ITEM_CODE2(분류축) ↔ ITEM_CODE3(부표 차원) ↔ ITEM_CODE4(잔여 세부)의 4축 키 구조가 본 매핑 규칙의 골격이다. ITEM_CODE2·3은 **시트 단위 + 부표 단위로 자동 매핑 가능**하며, ITEM_CODE4는 **CDID 한 건씩 강의 자료·ONS 매뉴얼 직접 조회가 필요**하다.
- 17 시트 × 평균 7 CDID = 284 고유 CDID 중 **LVL 1·2(시트로 결정) 자동률 100%**, **LVL 3(시트+부표+컬럼 위치로 결정) 자동률 약 70%**, **LVL 4(잔여 세부) 자동률 약 30%**(주로 SA/NSA·연간/분기·EU/non-EU·개정여부 같은 메타 차원으로 시트 메타에서 추출 가능).
- 본 통합 CSV(Phase 2.2)에서는 **자동 매핑 가능한 LVL 1~3까지 채우고 LVL 4는 빈 값으로 남겨**, Phase 3.2 명세서 단계에서 본격 작성하도록 권고. 이 정책은 데이터 값 불변·재현 가능성을 유지하면서도 통합 CSV의 1차 활용도를 즉시 확보한다.
- 강의 미수록 차원(영국 특화 EU/non-EU 지리, 개정 R 시리즈, ONS 운영 메타) 4건은 LVL 4 또는 별도 컬럼(`ITEM_GEOGRAPHY`·`ITEM_REVISION_FLAG`)으로 처리하고, **LVL 1~3 트리 자체는 강의 자료에 1:1 정합**하도록 유지한다.

## 2. 강의 자료 BoP 분류 트리 (LVL 1~4)

`background/BoP.pptx` 슬라이드 4·5·6·14·21·25·26 + `note/02_bop_components.md`·`06_financial_account_categories.md`·`07_glossary.md`(62 표제어) 종합. 각 LVL의 **영문 코드는 ECOS·BPM6 표준에 부합하는 약어**로 신규 부여(강의 자료에는 약어 미수록 항목이 다수이므로 본 매핑 규칙에서 명시적 코드 부여).

### 2.1 LVL 1 — 6 대분류

| LVL1 코드 | 한국어 분류명 | 영문 / 약어 | 강의 1차 근거 | ONS 시트 매핑 |
|---|---|---|---|---|
| CA | 경상수지 | Current Account | slide 5·14 ; 02 | Table_A·B·BX·C·E·F·G·H |
| KA | 자본수지 | Capital Account | slide 5·7·14 ; 02 | Table_I |
| FA | 금융계정 | Financial Account | slide 6·14 ; 06 | Table_J · D1.3·D4.6·D7.9 (flow 부분) |
| IR | 준비자산 | Reserve Assets / International Reserves | slide 6·12 ; 06 | (FA 안에 통합되나 분리 추적) Table_J col11 / D 시리즈 col6 / Table_K col10 |
| IIP | 국제투자대조표 | International Investment Position | slide 25 ; 05 | Table_K · D1.3·D4.6·D7.9 (stock 부분) |
| NEO | 오차 및 누락 | Net Errors and Omissions | slide 6·13 ; 04 | Table_A 부표3 col8 (HHDH) |

LVL 1 트리는 강의 슬라이드 14의 항등식 `CA + KA + FA(broad) + NEO ≡ 0` (단순화 가정 아래 `CA = FA(narrow) + IR = FA(broad)`)에 1:1 대응한다. IIP는 BoP(flow) 항등식의 "스톡 짝패"로 분리 추적, IR은 FA 안에 포함되지만 강의(슬라이드 12)와 ONS(LTCV/LTEB CDID)가 모두 별도 추적하므로 LVL 1에서 분리.

### 2.2 LVL 2 — 14 중분류

| LVL1 | LVL2 코드 | 한국어 | 영문 / 약어 | 강의 1차 근거 | ONS 매핑 (시트·컬럼 패턴) |
|---|---|---|---|---|---|
| CA | G | 상품수지 | Balance of Goods | slide 5·21 ; 02 | Table_E (3 부표 전체); Table_B/BX col2 (BOKG·BOKH·BOKI) |
| CA | S | 서비스수지 | Balance on Services | slide 5·9 ; 02 | Table_F (3 부표 전체); Table_B/BX col3 (IKBB·IKBC·IKBD) |
| CA | PI | 1차소득 | Primary Income | slide 5·9·25 ; 02 | Table_G (3 부표 전체); Table_B/BX col5–8 |
| CA | SI | 2차소득 | Secondary Income | slide 5·14 ; 02 | Table_H (3 부표 전체); Table_B/BX col9–11 |
| KA | KAT | 자본이전 | Capital Transfers | slide 5·7 ; 02 | Table_I col2–11 (FHIT·FLWA·FNTK 합계) |
| KA | NPNF | 비생산비금융자산 취득·처분 | Non-produced Non-financial Assets | slide 5·7 ; 02 | Table_I col12 (FHJL·FLWT·FNTS) |
| FA | DI | 직접투자 | Direct Investment | slide 6 ; 06 | Table_J col2–5; D1.3·D4.6·D7.9 col2; Table_K col2–4 |
| FA | PIF | 증권투자 | Portfolio Investment | slide 6 ; 06 | Table_J col6–8; D 시리즈 col3; Table_K col5–7 |
| FA | FD | 파생금융상품 | Financial Derivatives | slide 6·14 ; 06 | Table_J col9 (ZPNN); D 시리즈 col4; Table_K col8 (JX96/97/98) |
| FA | OI | 기타투자 | Other Investment | slide 6 ; 06 | Table_J col10/9; D 시리즈 col5; Table_K col9 |
| IR | IRA | 준비자산(자산만) | Reserve Assets — Asset Side | slide 6·12 ; 06 | LTCV (flow) / LTEB (stock); Table_J col11; D1.3·D7.9 col6; Table_K col10 |
| IIP | IIPA | 대외자산 잔액 | UK External Assets | slide 25 ; 05 | Table_K 부표1 (sub1); D1.3 부표1 |
| IIP | IIPL | 대외부채 잔액 | UK External Liabilities | slide 25 ; 05 | Table_K 부표2 (sub2); D4.6 부표1 |
| IIP | NIIP | 순국제투자포지션 | Net IIP / NFA | slide 11·24·25 ; 05 | Table_K 부표3 (sub3); D7.9 부표1 |
| NEO | NEO | 오차 및 누락 | Net Errors and Omissions | slide 6·13 ; 04 | Table_A 부표3 col8 (HHDH) |

LVL 2는 강의 슬라이드 14 식 `CA = G + S + PI + SI` (4분류) 및 슬라이드 6 `FA = DI + PIF + FD + OI + IR` (5분류)에 1:1 대응. IIP의 Asset/Liability/Net 3분할은 슬라이드 25(BoP↔IIP) + Table_K 3 부표에 1:1.

### 2.3 LVL 3 — 약 30 소분류 (시트 + 부표 + 컬럼 패턴 결정)

LVL 3는 시트 가로 컬럼이 LVL 2 안에서 다시 나뉘는 차원이다. 강의 자료에 직접 등장하는 항목(✓)과 ONS 표 안에는 있지만 강의 자료에는 미수록인 항목(◐)을 구분.

#### 2.3.1 CA → G (상품수지) 소분류 (Table_E 컬럼 단위)

| LVL3 코드 | 한국어 | 영문 | 강의 근거 | CDID 예시 |
|---|---|---|---|---|
| G_FBT | 식료품·음료·담배 | Food, beverages and tobacco | ◐ ONS Pink Book Ch.2 SITC | BOPL/BQAR/ELBE |
| G_BMAT | 기초 원자재 | Basic materials | ◐ SITC 2분류 | BOPM/BQAS/ELBF |
| G_OIL | 석유 | Oil | ◐ SITC 33 | ELBL/ENXO/ENXQ |
| G_FUEL | 기타 연료 | Other fuels | ◐ SITC 32·34·35 | BOQI/BPBI/ENIW |
| G_SEMI | 반제품 | Semi-manufactured goods | ◐ SITC 5·6 | BOPO/BQAU/ELBH |
| G_FIN | 완제품 | Finished manufactured goods | ◐ SITC 7·8 | BOPP/BQAV/ELBI |
| G_UNSP | 미분류 상품 | Unspecified goods | ◐ ONS 운영 잔여 | BOQL/BQAW/BQKX |
| G_TOT | 상품수지 합계 | Total goods | ✓ slide 21 | BOKG/BOKH/BOKI |
| G_NPM | 귀금속 제외 상품 | Goods excl. precious metals | ◐ ONS 영국 특화 (Table_BX) | FUS7·FUT2·FUT5 |

#### 2.3.2 CA → S (서비스수지) 소분류 (Table_F 컬럼 = EBOPS 12분류)

| LVL3 코드 | 한국어 | 영문 / EBOPS | 강의 근거 | CDID 예시 (Cr/Dr/Bal) |
|---|---|---|---|---|
| S_MFG | 제조 및 유지보수 | Manufacturing & maintenance | ◐ EBOPS 1 | MTN7/MTN6/MTN8 |
| S_TRSP | 운수 | Transport | ✓ slide 5 ("운수") | FKOA/FHME/FLYS |
| S_TRVL | 여행 | Travel | ✓ slide 5 ("여행") | FAPO/APQL/FNGY |
| S_CON | 건설 | Construction | ◐ EBOPS 4 | FDSG/FIOU/FNJM |
| S_INS | 보험·연금 | Insurance & pension services | ◐ EBOPS 5 | FDTF/FIPT/FNKF |
| S_FIN | 금융 | Financial | ◐ EBOPS 6 | FDYI/FITY/FNLQ |
| S_IP | 지식재산권 | Intellectual property (charges) | ✓ slide 5 ("로열티") | FEBA/FIVX/FNMR |
| S_TCM | 통신·컴퓨터·정보서비스 | Telecom·computer·information | ◐ EBOPS 9 | FDYQ/FIUG/FNLY |
| S_OBS | 기타 사업서비스 | Other business services | ◐ EBOPS 10 | FEHH/FIWF/FNMZ |
| S_PCR | 개인·문화·여가 | Personal, cultural & recreational | ◐ EBOPS 11 | FGXJ/FLQJ/FNRB |
| S_GOV | 정부서비스 | Government services | ◐ EBOPS 12 | FGZA/FLSA/FNRU |
| S_TOT | 서비스수지 합계 | Total services | ✓ slide 14 | IKBB/IKBC/IKBD |

강의 슬라이드 5는 "운수·여행·로열티 등"으로 3개 EBOPS 항목만 명시 인용, 나머지 9개는 ONS Pink Book Ch.3 EBOPS 12분류 표준에 따른 ◐ 보강 분류로 표시.

#### 2.3.3 CA → PI (1차소득) 소분류 (Table_G)

| LVL3 코드 | 한국어 | 영문 | 강의 근거 | CDID 예시 |
|---|---|---|---|---|
| PI_COE | 노동소득(임금송금) | Compensation of employees | ✓ slide 5·9 ("임금송금") | IJAH/IJAI/IJAJ |
| PI_INV_DI | 직접투자 수익 | Investment income — Direct | ✓ slide 5·25 ; 06 | MTX2/MTU7/MU7F |
| PI_INV_PIF_EQ | 증권투자 수익 (주식) | Investment income — Portfolio Equity | ◐ 강의 미수록 | CGDT/HGOT/CGEC |
| PI_INV_PIF_DEBT | 증권투자 수익 (채권) | Investment income — Portfolio Debt | ◐ 강의 미수록 | CGDU/CGDX/CGED |
| PI_INV_PIF_TOT | 증권투자 수익 합계 | Investment income — Portfolio Total | ✓ slide 25 ; 06 | CGDV/CGDZ/CGEE |
| PI_INV_OI | 기타투자 수익 | Investment income — Other | ✓ slide 5 ("이자") | CGDW/CGEB/CGFF |
| PI_INV_RA | 준비자산 수익 | Investment income — Reserve | ◐ 강의 미수록 | HHCC |
| PI_INV_TOT | 투자수익 합계 | Investment income — Total | ✓ slide 25 ; 06 | HBOK/HBOL/HBOM |
| PI_OTH | 기타 1차소득 | Other primary income | ◐ 강의 미수록 | MT5T/MT5V/MT5X |
| PI_TOT | 1차소득 합계 | Primary income — Total | ✓ slide 14 | HBOH/HBOI/HBOJ |

#### 2.3.4 CA → SI (2차소득) 소분류 (Table_H)

| LVL3 코드 | 한국어 | 영문 | 강의 근거 | CDID 예시 |
|---|---|---|---|---|
| SI_GG | 일반정부 (Cr) / 중앙정부 (Dr) | General/Central government | ✓ slide 5·14 ("국제기구출연금") | FHDM/FLUD/FNSV |
| SI_OS | 기타부문 | Other sectors | ✓ slide 5 ("원조") | FHIB/FLUZ/FNTC |
| SI_TOT | 2차소득 합계 | Secondary income — Total | ✓ slide 14 | IKBN/IKBO/IKBP |
| SI_EU | EU 기구 거래 (영국 특화) | EU institutions transactions | ◐ 강의 미수록 (영국 특화) | GTTA·H5U3·MUV7·MUV8·FKKM·FLMT·FZJA·CGDR |
| SI_BREXIT | EU 탈퇴협정 | Withdrawal agreement | ◐ 강의 미수록 (영국 특화) | FZJA |

#### 2.3.5 KA (자본수지) 소분류 (Table_I)

| LVL3 코드 | 한국어 | 영문 | 강의 근거 | CDID 예시 |
|---|---|---|---|---|
| KA_CG_DF | 중앙정부 채무면제 | Central gov debt forgiveness | ✓ slide 7 ("채무면제") | FHIV/FLWD/FNTM |
| KA_CG_OTH | 중앙정부 기타 자본이전 | Central gov other capital transfers | ✓ slide 7 ("이민·투자보조금") | FHJA/FLWH/FNTN |
| KA_OS_DF | 기타부문 채무면제 | Other sectors debt forgiveness | ✓ slide 7 | FHJD/JCWM/FNTQ |
| KA_OS_OTH | 기타부문 기타 자본이전 | Other sectors other transfers | ✓ slide 7 | EBGO/FLWQ/FNTR |
| KA_NPNF | 비생산비금융자산 | Non-produced non-financial assets | ✓ slide 5·7 ("토지·지하자원") | FHJL/FLWT/FNTS |
| KA_TOT | 자본수지 합계 | Capital balance — Total | ✓ slide 14 | FHLD/FLYL/FNVQ |

#### 2.3.6 FA → DI (직접투자) 소분류 (Table_J col2–4 / Table_K col2–3)

| LVL3 코드 | 한국어 | 영문 | 강의 근거 | CDID 예시 |
|---|---|---|---|---|
| DI_EQ_NRE | 지분자본 (재투자수익 제외) | Equity capital excl. reinvestment | ◐ 강의 미수록 (BPM6 표준) | HJYM/HJYR/HBWN |
| DI_RE | 재투자수익 | Reinvestment of earnings | ◐ 강의 미수록 (BPM6 표준) | HDNY/CYFV/HBWT |
| DI_DEBT | 부채성 거래 (회사간 대출) | Debt instruments / Intercompany | ◐ 강의 미수록 (BPM6 표준) | N2RN/N2R7/MU7L |
| DI_EQ_FUND | IIP 지분 잔액 (Equity & investment fund shares) | Equity & investment fund shares (stock) | ◐ 강의 미수록 (Table_K 전용) | CGMO/HBUY/HBSH |
| DI_TOT | 직접투자 합계 | Direct investment — Total | ✓ slide 6 | N2SV/N2SA/MU7M (flow); N2V3/N2UG/MU7O (stock) |

#### 2.3.7 FA → PIF (증권투자) 소분류 (Table_J col6–7 / Table_K col5–6)

| LVL3 코드 | 한국어 | 영문 | 강의 근거 | CDID 예시 |
|---|---|---|---|---|
| PIF_EQ | 지분증권 | Equity & investment fund shares | ✓ slide 6 ("주식") | HBVI/XBLW/HBWV (flow); HEPX/HLXX/CGNE (stock) |
| PIF_DEBT | 부채증권 | Debt securities | ✓ slide 6 ("채권") | XBMW/XBLX/HBWX (flow); HHZX/HLXY/CGNF (stock) |
| PIF_TOT | 증권투자 합계 | Portfolio investment — Total | ✓ slide 6 | HHZC/HHZF/HHZD (flow); HHZZ/HLXW/CGNH (stock) |

#### 2.3.8 FA → FD / OI / IR 소분류

| LVL3 코드 | 한국어 | 영문 | 강의 근거 | CDID 예시 |
|---|---|---|---|---|
| FD_NET | 파생금융상품 (순액) | Financial derivatives — Net | ✓ slide 6·14 | ZPNN (flow only) |
| FD_A_STOCK | 파생 IIP 자산 잔액 | Derivatives — Asset stock | ◐ 강의 미수록 (IIP 전용) | JX96 |
| FD_L_STOCK | 파생 IIP 부채 잔액 | Derivatives — Liability stock | ◐ 강의 미수록 (IIP 전용) | JX97 |
| FD_NET_STOCK | 파생 IIP 순잔액 | Derivatives — Net stock | ◐ 강의 미수록 (IIP 전용) | JX98 |
| OI_TOT | 기타투자 합계 | Other investment — Total | ✓ slide 6 | XBMM/XBMN/HHYR (flow); HLXV/HLYD/CGNG (stock) |
| IR_TOT | 준비자산 합계 | Reserve assets — Total | ✓ slide 6·12 | LTCV (flow); LTEB (stock) |

기타투자 하위(대출·차입·무역신용·예금)는 분기 BoP Bulletin Tables에서 별도 행으로 분리 게재되지 않음 (`note/06_financial_account_categories.md` §빠진 부분 6번). 분리는 ONS Pink Book Ch.6 또는 별도 Methodology 문서 필요.

### 2.4 LVL 4 — 잔여 세부 (CDID 단위 직접 조회 필요)

LVL 4는 LVL 1~3로 결정되지 않는 잔여 차원이며, 본 통합 CSV 단계에서는 빈 값으로 남기고 Phase 3.2에서 CDID 1건씩 라벨링하도록 위임한다. 정리상 다음 7가지 잔여 차원이 식별됨.

| LVL4 차원 | 코드 패턴 | 의미 | 적용 시트·CDID 사례 | 강의 근거 |
|---|---|---|---|---|
| 시계열 조정 | SA / NSA | Seasonally adjusted vs non-SA | Table_A 부표1=SA, 부표2=NSA (Table_R1 동일) | ◐ 강의 미수록 (ONS 운영) |
| 양면 회계 | A (NAFA) / L (NIL) / N (Net) | 자산취득·부채발생·순 | Table_J 부표1·2·3, Table_D1.3·D4.6·D7.9, Table_K 부표1·2·3 | ✓ slide 14 식 ; 19_assets_liabilities_mapping |
| 흐름·잔액 | T (transaction/flow) / P (position/stock) / Y (income) | 유량·저량·수익 | Table_D1.3 부표1=stock·2=flow·3=income | ✓ slide 4·25 stock vs flow |
| 지리 | EU / NEU / TOT | EU·non-EU·합계 | Table_C 6 부표 | ◐ 강의 미수록 (영국 특화) |
| 개정 상태 | RAW / R1 / R2 / R3 | 발표값·개정값(직전 발표 대비 차이) | Table_R1·R2·R3 vs 비R 시트 | ◐ 강의 미수록 (ONS 운영) |
| 단위 | GBP_M / GBP_B / PCT_GDP | 단위 정규화 | Table_B/BX/R2 부표4 = pct_of_GDP | ◐ 강의 미수록 (단위 메타) |
| 귀금속 보정 | INCL / EXCL | 귀금속 포함·제외 | Table_BX 전체 = EXCL precious metals | ◐ 강의 미수록 (ONS 영국 특화) |

LVL 4는 1개 CDID에 다중 차원이 동시 적용되는 경우가 많아 단일 컬럼이 아닌 **여러 메타 컬럼**으로 분해 권장 (`ITEM_SA_FLAG`·`ITEM_SIDE`·`ITEM_TIME_FORM`·`ITEM_GEOGRAPHY`·`ITEM_REVISION_FLAG`·`ITEM_UNIT_FORM`·`ITEM_GOLD_FLAG`).

## 3. 시트별 ITEM_CODE2~3 자동 매핑 규칙

`db/data/_inventory/15_master_inventory.csv` (시트당 1행) + `background/note/13_cdid_dictionary.csv` (512 행) + `background/note/19_assets_liabilities_mapping.csv` (54 행)를 left-join 키로 사용하면, **(sheet, sub_table, column_position) 트리플**로 ITEM_CODE2·3을 자동 결정 가능하다.

### 3.1 시트 단위 LVL 1·2 자동 결정 규칙

| 시트 | classification (15) | LVL1 자동 | LVL2 자동 (시트 내 가로 구조에서 결정) | 자동률 |
|---|---|---|---|---|
| Table_A 부표1·2 | summary (CA SA·NSA) | CA | G·S·PI·SI 4 컬럼 위치로 결정 | 100% |
| Table_A 부표3 | summary (FA NSA + NEO) | FA + NEO | DI·PIF·FD·OI·IR (col2–6) + NEO (col8) | 100% |
| Table_B / BX | CA-main | CA | col2=G·col3=S·col5–8=PI·col9–11=SI | 100% |
| Table_C | CA-main (EU/non-EU) | CA | 동일 + LVL4 EU/NEU 분기 | 100% (LVL2 + LVL4) |
| Table_D1_3 부표1 | IIP (asset) | IIP | DI·PIF·FD·OI·IR (col2–6) + IIP_TOT (col7) | 100% |
| Table_D1_3 부표2 | IIP (asset) | FA | 동일 + FA_TOT | 100% |
| Table_D1_3 부표3 | IIP (asset) | CA → PI (income) | DI·PIF·OI·IR (col2–5) + PI_INV_TOT | 100% |
| Table_D4_6 / D7_9 | IIP (liability/net) | IIP / FA / CA→PI (부표 1·2·3) | 동일 패턴, 부표 차원만 LVL4의 side로 다름 | 100% |
| Table_E | CA-detail (G) | CA | LVL2=G; col2–9 = LVL3 9 SITC | 100% |
| Table_F | CA-detail (S) | CA | LVL2=S; col2–13 = LVL3 12 EBOPS | 100% |
| Table_G | CA-detail (PI) | CA | LVL2=PI; col2–11 = LVL3 PI 10 항목 | 100% |
| Table_H | CA-detail (SI) | CA | LVL2=SI; col2–8 = LVL3 SI 5 항목 (Table_H 부표1·2 내부 위계 多) | 100% |
| Table_I | KA-FA (KA only) | KA | col2–11 = LVL3 KA 6 항목 | 100% |
| Table_J | KA-FA (FA flow) | FA + IR | col2–4=DI 하위, col5=DI_TOT, col6–7=PIF 하위, col8=PIF_TOT, col9=FD, col10=OI, col11=IR, col12=FA_TOT | 100% |
| Table_K | IIP (stock all) | IIP + IR | col2=DI_EQ, col3=DI_DEBT, col4=DI_TOT, col5=PIF_EQ, col6=PIF_DEBT, col7=PIF_TOT, col8=FD, col9=OI, col10=IR, col11=IIP_TOT | 100% |
| Table_R1 | revision (CA SA·NSA·FA) | CA / FA / NEO | Table_A와 동일 패턴 + LVL4 R1 플래그 | 100% |
| Table_R2 | revision (CA Cr·Dr·Bal·%GDP) | CA | Table_B와 동일 패턴 + LVL4 R2 플래그 | 100% |
| Table_R3 | revision (IIP·FA·Income × abroad/UK/net) | IIP / FA / CA→PI | Table_D1.3·D4.6·D7.9 패턴 결합 + LVL4 R3 플래그 | 100% |

→ **시트 단위로 LVL 1·2 자동 매핑 100% 가능**. 메타 시트(Cover_sheet·Notes·Records) 3개는 LVL 1~4 부여 대상이 아니므로 통합 CSV 행 자체에서 제외(이미 `note/15_master_inventory` `classification_code='meta_notes'` 분기 규칙으로 처리됨).

### 3.2 부표 단위 ITEM_CODE3 자동 결정 규칙

부표 차원 5축(`note/18_subtable_curriculum_alignment.md` §1)을 ITEM_CODE3 카테고리로 매핑.

| 시트 패턴 | 부표 차원 (`subtable_dimension`) | ITEM_CODE3 매핑 규칙 |
|---|---|---|
| Table_E·F·G·H·I·B·BX·C·R2 | Cr / Dr / Bal | sub1 → CR(대변/credit), sub2 → DR(차변/debit), sub3 → BAL(balance/순) |
| Table_J | NAFA / NIL / Net | sub1 → ASSET, sub2 → LIAB, sub3 → NET |
| Table_K | UK Assets / UK Liab / Net IIP (stock) | sub1 → ASSET_STOCK, sub2 → LIAB_STOCK, sub3 → NET_STOCK |
| Table_D1_3 / D4_6 / D7_9 | IIP / Flow / Income (3 부표) | sub1 → STOCK, sub2 → FLOW, sub3 → INCOME (+ LVL4 SIDE: D1_3=ASSET·D4_6=LIAB·D7_9=NET) |
| Table_A · R1 | CA SA / CA NSA / FA | sub1 → SA, sub2 → NSA, sub3 → NSA (FA는 SA 미공시 → NSA 통일) ; 추가 LVL4 SA_FLAG |
| Table_C | EU/non-EU × Cr/Dr/Bal (6 부표) | sub1·2·3 → EU+CR/DR/BAL, sub4·5·6 → NEU+CR/DR/BAL (LVL3 = CR/DR/BAL, LVL4 = EU/NEU) |
| Table_R3 | {abroad/in UK/net} × {IIP/Flow/Income} 9 부표 | sub1~3 → ABROAD+STOCK/FLOW/INCOME, sub4~6 → INUK+동상, sub7~9 → NET+동상 |
| Table_B/BX/R2 부표4 | %GDP | LVL3는 합계 패턴 그대로, LVL4 UNIT_FORM = PCT_GDP |

→ **부표 단위로 ITEM_CODE3 자동 매핑 100% 가능**. Table_J 부표2의 컬럼 위치 점프(derivatives 행 부재)는 column_label 또는 CDID로 매칭하면 우회 가능 (`note/19_assets_liabilities_mapping.md` §빠진 부분 3).

### 3.3 컬럼 패턴(LVL 3 합계 vs 하위) 자동 결정 규칙

CDID 컬럼 위치(col 2~13)가 LVL3의 "합계" vs "하위 항목"을 결정. 다음 패턴 룰셋으로 자동 분류 가능.

1. **합계 라인** 식별: column_label에 "Total"·"balance"·"Net total" 포함 → LVL3 = LVL2_TOT (예: G_TOT, PIF_TOT). `13_cdid_dictionary.csv`에서 정규식 `(?i)(total|balance|net total)` 매칭.
2. **양면 분리** 식별: 시트=Table_J·D1_3·D4_6·D7_9·K + column_label에 "abroad" → ASSET 측, "in the UK" → LIAB 측, "Net" → NET 측. LVL4 SIDE 컬럼 자동 부여.
3. **하위 분류** 식별: column_label이 LVL3 코드표(§2.3)의 영문명과 정확히 또는 부분 일치 (예: "Travel" → S_TRVL). 매칭률 약 70%.
4. **잔여 처리**: 위 3개 룰로 매칭 안 되는 컬럼은 LVL3=BLANK, Phase 3.2 명세서에서 수작업 매핑 위임.

자동 매칭률 추정:
- LVL2 합계 라인(예: HBOJ=PI Total): **100%** (Total/Net total 정규식)
- LVL3 표준 카테고리(SITC·EBOPS·5분류): **약 80%** (column_label 영문명 직접 매칭)
- LVL3 영국 특화/잔여(SI_EU·G_NPM·DI_EQ_NRE 등): **약 30%** (수작업 보강 필요)

전체 추정 자동률(LVL3): **약 70%** = 284 고유 CDID 중 약 200개 자동 라벨링 가능, 나머지 약 84개 CDID는 Phase 3.2에서 CDID·column_label·강의/ONS 매뉴얼 직접 조회로 라벨링.

## 4. CDID 단위 ITEM_CODE4 매핑 가이드 (Phase 3.2 위임 영역)

본 통합 CSV(Phase 2.2) 단계에서는 LVL 4를 빈 값으로 남기고, **Phase 3.2 명세서 단계로 위임**한다. Phase 3.2 작업 가이드는 다음과 같다.

### 4.1 LVL 4 매핑 작업 단위

- **단위**: CDID 1건 × 시트·부표 발생 인스턴스 = 약 512 행 (`13_cdid_dictionary.csv` 전체).
- **고유 CDID**: 284개. 95개 CDID는 ≥2 시트에 등장하므로, 같은 CDID라도 시트가 다르면 LVL 4(특히 SA_FLAG·REVISION_FLAG·SIDE)가 달라진다 → **(CDID, sheet, sub_table) 트리플 기준으로 라벨링**.
- **사전 확보 자료**: `13_cdid_dictionary.csv` 512행 + `19_assets_liabilities_mapping.csv` 54행(LVL4 SIDE 자동) + `note/02·06_*.md` 정의 + `note/07_glossary.md` 62 표제어.

### 4.2 LVL 4 라벨 항목별 결정 규칙

| LVL4 컬럼 | 결정 규칙 | 자동률 |
|---|---|---|
| ITEM_SA_FLAG (SA / NSA) | 시트=Table_A 부표1·Table_R1 부표1 → SA, 그 외 → NSA | 100% (시트로 결정) |
| ITEM_SIDE (A/L/N) | `19_assets_liabilities_mapping.csv` join → A/L/N + 결측은 N | 100% (table 매핑) |
| ITEM_TIME_FORM (T/P/Y) | Table_D 시리즈 부표1=P, 부표2=T, 부표3=Y; Table_K=P; Table_J=T; 그 외 CA 시트=T | 100% (시트·부표로 결정) |
| ITEM_GEOGRAPHY (TOTAL/EU/NEU) | Table_C 부표1·2·3 → EU, 부표4·5·6 → NEU; Table_H의 EU 관련 CDID(GTTA·H5U3·MUV7·MUV8·FKKM·FZJA·CGDR·GTTB·GTTX·GTTY 등) → EU; 그 외 → TOTAL | 80% (Table_C는 100%, Table_H 안의 EU 항목은 column_label 직접 검사 필요) |
| ITEM_REVISION_FLAG (RAW/R1/R2/R3) | 시트명에 'R1'/'R2'/'R3' 포함 → 동상, 그 외 → RAW | 100% (시트명) |
| ITEM_UNIT_FORM (GBP_M/GBP_B/PCT_GDP) | `15_master_inventory.unit_normalized` + 부표 단위 (`subtable_split_required` MIXED 시트는 부표4가 PCT_GDP) | 100% (인벤토리 join) |
| ITEM_GOLD_FLAG (INCL/EXCL) | 시트=Table_BX → EXCL, 그 외 → INCL | 100% (시트명) |

**LVL 4 7개 메타 컬럼 중 6개는 자동률 100%**, GEOGRAPHY 1개만 column_label 직접 검사가 필요한데 이 부분도 정규식 룰셋(`(?i)EU institutions?|regional development fund|agricultural fund|social fund`)으로 약 80% 자동화 가능.

### 4.3 강의 자료·ONS 매뉴얼 직접 조회가 필요한 영역

LVL 4가 아닌 LVL 3의 잔여 30% (약 84개 CDID)에 대해 다음 직접 조회가 필요하다.

1. **ONS Pink Book Ch.2 SITC 분류 표**: Table_E 9 SITC 코드(Food, beverages...)와 ONS 공식 한국어/영문 표준명 대조.
2. **ONS Pink Book Ch.3 EBOPS 12분류 표**: Table_F 12 서비스 카테고리 표준명 대조 (강의 슬라이드 5는 3개만 인용).
3. **OECD BD4 표준** (`note/16_oecd_bd4.md`): Table_J col2–4 직접투자 하위(Equity / Reinvestment / Debt) 정의 보강.
4. **ONS BoP QMI**: Table_H의 EU institutions 거래 7개 CDID (MUV7·MUV8·FKKM·FZJA 등)의 Withdrawal Agreement·Abatement 의미 확인.
5. **Table_R3 9 부표**: 개정값 의미(직전 발표 대비 차이 vs 누적 개정) 확인 — 본 단계 자료에서 진위 미확정.

## 5. 본 통합 CSV 단계의 ITEM_CODE2~4 채움 정책 권고

### 5.1 단정 권고

본 Phase 2.2 통합 CSV 단계에서는 다음 정책을 권고한다.

1. **ITEM_CODE1 = CDID 4자**: `13_cdid_dictionary.csv` 전체 512 행 그대로 자동 부여. 본 단계의 1차 키.
2. **ITEM_CODE2 = LVL 1·2 합성 코드** (예: `CA.G`, `CA.PI`, `FA.DI`, `FA.IR`, `IIP.NIIP`, `KA.KAT`, `NEO`):
   - 자동률 **100%** (§3.1 규칙).
   - 통합 CSV 모든 행에 채움.
3. **ITEM_CODE3 = LVL 3 합성 코드** (예: `CA.G.G_TOT`, `CA.S.S_TRVL`, `FA.DI.DI_TOT`, `IIP.NIIP.PIF_EQ`):
   - 자동률 **약 70%** (§3.2~3.3 규칙).
   - **자동 매칭된 행만 채우고**, 매칭 실패 행(약 84개 CDID)은 빈 값(`null`/공백)으로 남김.
   - 매칭 실패 사례를 `db/data/_inventory/22_item_code3_unmapped.csv` (Phase 2.2 후속)에 별도 인벤토리로 기록.
4. **ITEM_CODE4 = LVL 4 메타 차원 다중 컬럼**:
   - 본 단계에서는 **빈 값**으로 남김.
   - Phase 3.2 명세서 단계에서 7개 메타 컬럼(SA_FLAG·SIDE·TIME_FORM·GEOGRAPHY·REVISION_FLAG·UNIT_FORM·GOLD_FLAG)을 별도 컬럼으로 부여.
5. **메타 컬럼 분리 권장**: ITEM_CODE4를 단일 컬럼으로 합치지 말고, 위 7개 메타를 분리 컬럼으로 두면 `db/CLAUDE.md` "데이터 값 불변" 원칙 + 재현성 둘 다 충족하면서 분석 단계에서 자유롭게 결합·필터 가능.

### 5.2 예시 (Table_E 부표3 col4 ELBL = Oil 상품수지)

| 컬럼 | 값 | 결정 근거 |
|---|---|---|
| ITEM_CODE1 | ELBL | CDID 직결 |
| ITEM_CODE2 | CA.G | sheet=Table_E → LVL2=G ; LVL1=CA |
| ITEM_CODE3 | CA.G.G_OIL | column_label="Oil" 정규식 매칭 |
| ITEM_CODE4 (메타 분해) | SA_FLAG=NSA, SIDE=N, TIME_FORM=T, GEOGRAPHY=TOTAL, REVISION_FLAG=RAW, UNIT_FORM=GBP_M, GOLD_FLAG=INCL | Phase 3.2에서 부여 |

### 5.3 예시 (Table_J 부표1 col5 N2SV = Direct investment abroad Total)

| 컬럼 | 값 | 결정 근거 |
|---|---|---|
| ITEM_CODE1 | N2SV | CDID 직결 |
| ITEM_CODE2 | FA.DI | sheet=Table_J + column_label "Direct investment" → LVL2=DI |
| ITEM_CODE3 | FA.DI.DI_TOT | column_label에 "Total" 포함 → 합계 라인 |
| ITEM_CODE4 | SA_FLAG=NSA, SIDE=A (`19_assets_liabilities_mapping`), TIME_FORM=T, GEOGRAPHY=TOTAL, REVISION_FLAG=RAW, UNIT_FORM=GBP_M, GOLD_FLAG=INCL | Phase 3.2 |

### 5.4 강의 자료 정합성 보장 검증

본 매핑 규칙으로 통합 CSV가 채워지면 다음 강의 항등식이 자동 검증 가능하다.

- **CA = G + S + PI + SI** (slide 14): `ITEM_CODE2 ∈ {CA.G, CA.S, CA.PI, CA.SI} ∧ ITEM_CODE3 = *_TOT ∧ SIDE=BAL`로 필터 → 4 시리즈 합 = `IKBJ + HBOJ + IKBP` (또는 `HBOP` Current balance) 직접 검증.
- **FA = DI + PIF + FD + OI + IR** (slide 6+14): `ITEM_CODE2 ∈ {FA.*} ∧ SIDE=N ∧ TIME_FORM=T` 필터 → 5 시리즈 합 = `HBNT` 직접 검증.
- **CA = FA(narrow) + IR = FA(broad)** (slide 14): `IKBJ + HBOJ + IKBP + HBOP` (CA balance) ≈ `HBNT - LTCV` (FA narrow) + `LTCV` (Reserve) — `19_signs_gold_revisions.md` 부호 보정 후.
- **NIIP = IIPA - IIPL** (slide 25): `ITEM_CODE2 ∈ {IIP.IIPA, IIP.IIPL, IIP.NIIP} ∧ ITEM_CODE3=*_TOT ∧ TIME_FORM=P` 필터 → `HBQA - HBQB = HBQC`.

→ 본 매핑 규칙은 강의 자료 항등식의 **정량 검증 자동화에 즉시 활용 가능**하며, 이는 Phase 2.2 통합 CSV의 핵심 가치이다.

### 5.5 단계별 작업 분담 요약

| 단계 | LVL 1 | LVL 2 | LVL 3 | LVL 4 | 산출물 |
|---|---|---|---|---|---|
| Phase 2.2 (본 단계) | 자동 100% | 자동 100% | 자동 약 70% (나머지 빈 값) | 빈 값 | 통합 CSV (`balanceofpayments2025q4_long.csv`) + `22_item_code3_unmapped.csv` |
| Phase 3.2 (명세서) | 검증만 | 검증만 | 잔여 30% 수작업 | 7개 메타 자동 100% (GEOGRAPHY만 일부 수작업) | 명세서 (`db/data/_spec/`) |
| Phase 4 (분석) | 검증만 | 항등식 검증 | 항등식·세부 분석 | 필터·집계 | 분석 노트북 |

## 6. 출처

### 강의 자료 (1차 근거)

- `background/BoP.pptx` (31 슬라이드) — 슬라이드 4·5·6·14·21·25·26 중심
- `background/BoP.pdf` (병행 참조)
- `background/INDEX.md`

### 회차 노트 (1차 근거)

- `background/note/02_bop_components.md` — BoP 5대 구성 강의 발췌
- `background/note/03_sign_conventions.md` — BPM5/BPM6 부호 규약
- `background/note/04_identities.md` — 항등식 6종
- `background/note/05_iip_nfa.md` — IIP·NFA 정의
- `background/note/06_financial_account_categories.md` — FA 5분류
- `background/note/07_glossary.md` — 한국어 용어집 62 표제어 9 분류
- `background/note/13_cdid_dictionary.csv` (512 행) / `13_cdid_dictionary.md`
- `background/note/19_assets_liabilities_mapping.csv` (54 행) / `19_assets_liabilities_mapping.md`

### 인접 인벤토리 (1차 근거)

- `db/data/_inventory/15_master_inventory.csv` (20 행 × 22 컬럼) / `15_master_inventory.md`
- `db/data/_inventory/16_curriculum_coverage_check.md` — 강의 개념 47건 ↔ 시트 매핑
- `db/data/_inventory/18_subtable_curriculum_alignment.md` — 부표 차원 5축 + 63 부표 정합성
- `db/data/_inventory/09_units.csv` — 단위 정규화 (UNIT_FORM 결정용)
- `db/data/_inventory/19_signs_gold_revisions.md` — Table_BX 귀금속 보정 (GOLD_FLAG)

### 관련 규칙

- `db/CLAUDE.md` — 가공 원칙 (값 불변, 구조만 조정)
- `db/data/CLAUDE.md` — 가공본 명명·메모 규칙
- `CLAUDE.md` (루트) — `env/` 가상환경 사용
- `db/CHECKLIST.md` §2.2 — 본 산출 항목 정의

### 원본

- `db/source/balanceofpayments2025q4.xlsx` (read-only)
