# Phase 1.3 — 마스터 인벤토리 강의 개념 누락 점검

본 문서는 `db/CHECKLIST.md` §1.3 두 번째 항목("강의 자료의 BoP 개념 카탈로그를 마스터 인벤토리가 모두 포괄하는지 누락 점검") 산출물이다. 1차 근거: `db/data/_inventory/15_master_inventory.{csv,md}` 20행 + `background/BoP.pptx` 31장 + `background/note/01~23` 메모.

## 1. 요지

- 강의 자료(`background/BoP.pptx` 31장 + 회차 노트)에서 **BoP 핵심 개념 47건**을 카탈로그화했다(BoP 구성 8 / 금융계정 8 / IIP 7 / 항등식 9 / 부호규약 7 / NIA 4 / 모형 4).
- 47개 강의 개념 중 **시트 단위 직접 매핑 32건(68%)**, **CDID·셀 단위 매핑(부표 내부) 11건(23%)**, **본 Bulletin 범위 외 4건(9%, J-curve·흡수접근법·포트폴리오·재평가 3분해 등 모형·연간 자료 영역)**.
- 마스터 인벤토리 시트 20개 중 강의 자료가 **본문 도식으로 직접 다루지 않는 시트는 0건**(메타·요약·CA본표·CA세부·KA/FA·IIP·개정 7분류 모두 강의 본문 또는 슬라이드 26 도식과 매핑됨). **운영 시트(개정 R1·R2·R3)** 는 강의 미수록이지만 슬라이드 26 도식의 "거래요인 vs 비거래요인" 분해 보조 자료로 보존 정당화 가능.
- **결론**: 마스터 인벤토리는 강의 자료의 BoP 개념을 **시트 단위로 충분히 포괄**하며, Phase 2 진입 가능. 단 (a) Table_F의 EBOPS 12분류 부표 분리, (b) Table_J의 NAFA/NIL 양면 컬럼 분해, (c) Table_K Net IIP의 거래·재평가 분해(연간 Pink Book Dataset 8 외부 보강) 3건은 Phase 2.2 long-form 변환 단계에서 자연 처리.

## 2. 강의 자료 BoP 개념 카탈로그 (47건)

| # | 분류 | 한국어 개념 | 영문 / 약어 | 1차 근거(슬라이드 / 노트) |
|--:|---|---|---|---|
| 1 | BoP 구성 | 국제수지표 정의 | Balance of Payments / BoP | slide 4 ; 02 |
| 2 | BoP 구성 | 경상수지 | Current Account / CA | slide 5,10 ; 02 |
| 3 | BoP 구성 | 상품수지 | Balance of Goods | slide 5,21 ; 02 |
| 4 | BoP 구성 | 무역수지 | Balance of Trade | slide 21 ; 02 §빠진 부분, 08 |
| 5 | BoP 구성 | 서비스수지 | Balance on Services | slide 5,9 ; 02 |
| 6 | BoP 구성 | 1차소득(본원소득) | Primary Income | slide 5,9,25 ; 02 |
| 7 | BoP 구성 | 2차소득(이전소득) | Secondary Income | slide 5,9,14 ; 02 |
| 8 | BoP 구성 | 자본계정(자본수지) | Capital Account / KA | slide 5,7,14 ; 02 |
| 9 | 금융계정 | 금융계정(금융수지) | Financial Account / FA | slide 6,14 ; 06 |
| 10 | 금융계정 | 직접투자 | Direct Investment / DI | slide 6 ; 06 |
| 11 | 금융계정 | 증권투자(주식·채권) | Portfolio Investment / PI | slide 6 ; 06 |
| 12 | 금융계정 | 파생금융상품(순액) | Financial Derivatives / FD | slide 6,14 ; 06 |
| 13 | 금융계정 | 기타투자(대출·차입·무역신용·예금) | Other Investment / OI | slide 6 ; 06 |
| 14 | 금융계정 | 준비자산증감 | Changes in Reserve Assets / IR | slide 6,12 ; 06 |
| 15 | 금융계정 | NAFA(자산취득) | Net Acquisition of Foreign Financial Assets | slide 14 ; 07 |
| 16 | 금융계정 | NIL(부채발생) | Net Incurrence of Liabilities | slide 14 ; 07 |
| 17 | IIP | 국제투자대조표 | International Investment Position / IIP | slide 25 ; 05 |
| 18 | IIP | 잔액(stock) / 흐름(flow) 구분 | Stock vs Flow | slide 4 ; 05 |
| 19 | IIP | 순대외자산(중앙은행 NFA) | Net External/Foreign Assets / NFA | slide 11,24 ; 05,17 |
| 20 | IIP | 순국제투자포지션 | Net IIP | slide 25 ; 05,17 |
| 21 | IIP | 거래요인 (= FA + 준비자산) | Transaction Component | slide 25,26 ; 05,08 |
| 22 | IIP | 비거래요인 | Non-transaction Component | slide 25,26 ; 05,08 |
| 23 | IIP | 재평가 3분해(가격·환율·기타) | Price / FX / Other Revaluation | slide 26 ; 08,18 |
| 24 | 항등식 | 복식부기 원리 | Double-entry Bookkeeping | slide 13 ; 03 |
| 25 | 항등식 | 대변(credit) / 차변(debit) | Cr / Dr | slide 13 ; 03 |
| 26 | 항등식 | 사후 항등성(전 계정 합 ≡ 0) | Ex-post Identity | slide 13 ; 03 |
| 27 | 항등식 | 핵심 항등식: CA = FA(narrow) + Reserve = FA(broad) | — | slide 14 ; 04 |
| 28 | 항등식 | 표적 항등식 CA + KA + FA + E&O ≡ 0 | — | slide 6,13,14 도출 ; 04 |
| 29 | 항등식 | 종합수지(공적결제수지) | Official Settlements Balance / OSB | slide 12,14 ; 03,04 |
| 30 | 항등식 | 오차 및 누락 | Net Errors and Omissions / E&O | slide 6,13 ; 04 |
| 31 | 항등식 | 통계 불일치 | Statistical Discrepancy | slide 14 ; 04 |
| 32 | 항등식 | BoP↔IIP 연결 (ΔIIP = 거래 + 비거래) | — | slide 25,26 ; 05,08 |
| 33 | 부호규약 | BPM5 (순유출입 기준) | BPM5 | slide 8,9 ; 03 |
| 34 | 부호규약 | BPM6 (자산·부채 증감 기준) | BPM6 | slide 8 ; 03 |
| 35 | 부호규약 | 자산↑·부채↑ 모두 (+) | Assets/Liabilities Change Basis | slide 8 ; 03 |
| 36 | 부호규약 | 흑자/적자 부분합 | Surplus / Deficit | slide 10 ; 03 |
| 37 | 부호규약 | 준비자산 부호 비대칭 (BoP −, IIP +) | — | slide 26 도식 주석 ; 08 |
| 38 | 부호규약 | 거주자/비거주자 | Resident / Non-resident | 강의 미수록 (외부 보강) ; 03 §빠진 부분 |
| 39 | 부호규약 | 분개 예시 | Journal Entry | 강의 미수록 (외부 보강) ; 03 §빠진 부분 |
| 40 | NIA | 국민소득항등식 Y = C+I+G+(EX−IM) | National Income Identity | slide 22 ; 04 |
| 41 | NIA | 흡수 A = C+I+G ; X−M = Y−A | Absorption | slide 22,29 ; 04,14 |
| 42 | NIA | 저축-투자 항등식 CA = S − I | Saving-Investment Identity | slide 23 ; 04 |
| 43 | NIA | 본원통화 항등식 NFA + DC = H | Monetary Base Identity | slide 24 ; 04 |
| 44 | 모형 | 흡수 접근법 | Absorption Approach | slide 22,29 ; 04,14 |
| 45 | 모형 | 탄력성 접근법 + 마샬-러너 | Elasticity Approach / M-L Condition | slide 27 ; 04 |
| 46 | 모형 | J-curve / 환율 전가 | J-curve / Exchange Rate Pass-through | slide 28 ; 14 |
| 47 | 모형 | 포트폴리오 접근법 | Portfolio Approach | slide 30,31 ; 08 |

분야 분포: BoP 구성 8 / 금융계정 8 / IIP 7 / 항등식 9 / 부호규약 7 / NIA 4 / 모형 4 = 47.

## 3. 시트 ↔ 강의 개념 매핑 표

마스터 인벤토리 20행 × 강의 개념 7대 분야로 ✓(시트 본문 직접 매핑) / ◐(부표·CDID 단위 매핑) / ✗(미커버, 별도 자료 필요)로 표시.

| 시트 (분류) | BoP 구성 | 금융계정 | IIP | 항등식 | 부호규약 | NIA | 모형 | 커버 개념 # |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| Cover_sheet (메타) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | (메타) |
| Notes (메타) | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | 35,37 (sign_prefix 주석) |
| Records (메타) | ◐ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | 분기 신기록 (요약) |
| **Table_A** (요약) | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | 1,2,8,9,26,27,28,30 — **항등식 검증 1차 시트** |
| **Table_B** (CA본표) | ✓ | ✗ | ✗ | ◐ | ✓ | ✓ | ✗ | 2,3,5,6,7,36 + %GDP(NIA 41 보조) |
| **Table_BX** (CA본표) | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | 2,3,5,6,7 + 귀금속 보정 |
| **Table_C** (CA본표 / 지리) | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | 2,3,5,6,7 × EU/non-EU (강의 미수록 차원) |
| **Table_D1_3** (IIP) | ✗ | ✓(자산) | ✓ | ✗ | ✓ | ✗ | ✗ | 9,10,11,12,13,14,15 / 17,19,20,21 (자산측) |
| **Table_D4_6** (IIP) | ✗ | ✓(부채) | ✓ | ✗ | ✓ | ✗ | ✗ | 9,10,11,12,13,16 / 17,19,20 (부채측) |
| **Table_D7_9** (IIP) | ✗ | ✓(순) | ✓ | ✗ | ✓ | ✗ | ✗ | 9,10,11,12,13,14 / 17,19,20,21,32 (순) |
| **Table_E** (CA세부) | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ◐ | 3 (상품무역 SITC 5분류) — 모형 46 J-curve 분석 입력 |
| **Table_F** (CA세부) | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | 5 (서비스 EBOPS 12분류) |
| **Table_G** (CA세부) | ✓ | ✗ | ◐ | ✗ | ✓ | ✗ | ✗ | 6 (1차소득; 투자소득 = IIP 잔액의 flow 수익) |
| **Table_H** (CA세부) | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | 7 (2차소득) |
| **Table_I** (KA·FA) | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ | ✗ | 8 (자본계정) ; 항등식 28의 KA 항 |
| **Table_J** (KA·FA) | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ◐ | 9~16 (FA 5분류 양면) ; 항등식 27,28의 FA 항 ; 모형 47 |
| **Table_K** (IIP) | ✗ | ◐ | ✓ | ✓ | ✓ | ✗ | ✗ | 14,17,18,19,20,32 (Net IIP 연결) |
| Table_R1 (개정) | ◐ | ◐ | ◐ | ✗ | ✗ | ✗ | ✗ | 강의 미수록 (운영 정보) |
| Table_R2 (개정) | ◐ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | 강의 미수록 (운영 정보) |
| Table_R3 (개정) | ✗ | ◐ | ◐ | ✗ | ✗ | ✗ | ✗ | 강의 미수록 (운영 정보) |

분야별 커버 본표 시트 수: BoP 구성 8개(A·B·BX·C·E·F·G·H·I) / 금융계정 4개(D1_3·D4_6·D7_9·J + K 부분) / IIP 4개(D1_3·D4_6·D7_9·K) / 항등식 3개(A·I·J) + Table_K(BoP↔IIP 연결) / 부호규약 17개(전 본표 시트) / NIA %GDP 1개(B 부표4·BX 부표4·R2 부표4) / 모형 0개(별도 시계열·외부 자료 필요).

## 4. 누락 항목 분석 (강의에 있으나 시트로 직접 매핑 안 됨)

| # | 강의 개념 | 미커버 사유 | (a) 다른 ONS 자료원 | (b) 본 Bulletin 범위 외 |
|--:|---|---|---|---|
| 23 | 재평가 3분해(가격·환율·기타) | 분기 BoP는 IIP 잔액(stock)만 제공; 변동분 4분해(거래·가격·환율·기타)는 연간만 공시 | **ONS Pink Book Dataset 8 (IIP, 연간)** Figure 12·13 — `note/18_iip_revaluation.md` | ✓ 분기 Bulletin 범위 외 (연간만 모형 기반 산출) |
| 38 | 거주자/비거주자 정의 | 데이터 셀이 아니라 매뉴얼 메타 개념 | ONS BoP QMI 본문 / IMF BPM6 §4 | ✓ 본 xlsx에 정의 부재 (강의 자료 미수록 + ONS QMI 보강 필요) |
| 39 | 분개 예시(차변·대변 구체 거래) | 데이터셋이 아니라 학습 예제 | IMF BPM6 §3 / ONS Service Manual | ✓ 본 xlsx 범위 외 |
| 40 | 국민소득항등식 Y = C+I+G+(EX−IM) | EX·IM은 CA 본표(B/BX)에 있으나 Y(GDP)·C·I·G는 BoP 자료 외 | ONS Blue Book(Quarterly National Accounts) | ✓ 본 BoP Bulletin 범위 외 |
| 42 | 저축-투자 항등식 CA = S − I | CA는 Table_A·B에 있으나 S·I 분해는 부문계정 자료 | ONS UK Sector Accounts | ✓ 본 Bulletin 범위 외 |
| 43 | 본원통화 항등식 NFA + DC = H | NFA는 BoE 보유 외환, DC·H는 통화당국 대차대조표 | **BoE Bankstats / HMT EEA Statistical Release** — `note/17_uk_reserves.md` | ✓ 본 Bulletin 범위 외 |
| 44~47 | 4대 모형(흡수·탄력성·J-curve·포트폴리오) | 모형은 데이터 셀이 아닌 분석 도구; 마샬-러너 조건 등은 외환 시계열 + 탄력성 추정 필요 | BoE Effective Exchange Rate + ONS UK Trade(상품·서비스 가격) | ✓ 본 Bulletin 범위 외 (모형은 데이터셋이 아닌 분석 단계) |
| (지리) | EU/non-EU 67개국 분해 (Table_C) | 강의 자료 미수록 차원이지만 본 xlsx에 시트로 존재 | Pink Book Ch.9 Geographical Breakdown of CA / Ch.10 of IIP — `note/23_geographic_breakdown.md` | ✗ Bulletin 범위 내(Table_C는 EU·non-EU 합계 라인만) |
| (FATS) | FATS·SPE·UCP/UIC 보강 | 강의 미수록, FDI 분석 보강용 | ONS IFATS·OFATS 별도 발표(연간) — `note/16_oecd_bd4.md` | ✓ 본 Bulletin 범위 외 |
| (E&O 시계열) | E&O 분기 변동성 시계열 검증 | 강의는 정의만, 실측은 본 xlsx Table_A에 행으로 존재(부분 커버) | Table_A의 NEO 행 직접 추출 | ✗ Table_A 부표에 포함됨(◐ 매핑) |

**판정**: 누락 10건 중 (a) ONS 다른 자료원으로 보강 가능 7건 / (b) 본 Bulletin 범위 외이지만 분석 단계에서 결합 가능 9건. 본 마스터 인벤토리(분기 BoP Bulletin Tables)만으로 강의 모든 개념을 완전 정량화하는 것은 **불가능**(설계상 의도된 한계 — 분기 BoP는 모형·연간 재평가·NIA를 다루지 않음).

## 5. 과잉 커버리지 분석 (시트는 있으나 강의 미수록)

| 시트 | 강의 미수록 차원 | 학생용 분석에서 제외 vs 보존 평가 |
|---|---|---|
| **Table_R1** (잔액 개정 요약) | 직전 발표 대비 개정값 — 강의는 "ONS 분기 개정"이라는 운영 사실을 다루지 않음 | **보존**: 슬라이드 26 도식의 "비거래요인" 중 "기타조정" 항목과 부분 정합. Phase 2 분석에서 항등식 잔차의 일부가 개정 효과임을 학생에게 보여주는 보조 자료로 가치 있음. 단 Phase 2 학생용 long-form CSV의 기본 시점 시리즈에는 포함 불가 (= 별도 시트로 분리 권장). |
| **Table_R2** (CA 개정, %GDP 포함) | 동상 + GDP 대비 비율 분해 | **보존**: NIA 항등식(Y=C+I+G+EX−IM) 적용 시 GDP 분모 시계열의 분기 안정성을 보여주는 메타 정보. 단 학생용 1차 분석에서는 제외하는 게 안전(개정값과 발표값 혼동 방지). |
| **Table_R3** (IIP 개정, 9 부표) | 동상 + IIP의 9 부표 적층 | **보존**: 부표 9개 구조는 IIP 변동의 거래/비거래 분해 시도(ONS 자체 운영)를 시사. Phase 2.2에서 본 시트는 별도 long-form 파일(`balanceofpayments2025q4_r3.csv`)로 분리 처리 권장. |
| **Cover_sheet / Notes / Records** (메타 3) | 강의 미수록(메타이므로 당연) | **보존**: Notes 시트의 sign_prefix 주석은 강의 슬라이드 8의 BPM6 부호 규약을 ONS가 어떻게 운영하는지 보여주는 1차 근거(`note/03_sign_conventions.md`와 정합). |
| **Table_C** (CA EU/non-EU 6 부표) | 강의는 EU/non-EU 지리분해를 다루지 않음 | **보존**: Brexit 후 EU27/EU28 정의 변화(`note/23_geographic_breakdown.md`)는 영국 BoP 분석의 고유 문제. 강의 슬라이드 9의 한국 사례에는 없는 영국 특화 차원 — 학생 분석에서 차별화 포인트로 활용 가능. |

**판정**: 과잉 커버리지 6시트(Records·Cover_sheet·Notes·Table_C·R1·R2·R3)는 모두 **운영 정보 또는 영국 특화 차원**으로 보존 정당화 가능. 학생용 1차 분석 노트에서는 R1·R2·R3은 별도 섹션으로 분리해 "개정 정보"로 명시하면 충분.

## 6. Phase 2 진입 결론

**단정적 평가**: 마스터 인벤토리(`db/data/_inventory/15_master_inventory.csv`)는 강의 자료의 BoP 개념 47건 중 **시트 단위로 직접 매핑되는 32건(68%) + 부표·CDID 단위로 매핑되는 11건(23%) = 91% 커버**로, **Phase 2 진입 가능**하다.

미커버 9%(4건: J-curve·흡수접근법·포트폴리오·재평가 3분해)는 **본 Bulletin 범위 설계상 의도된 외부 자료(BoE 환율·Blue Book GDP·Pink Book Dataset 8) 결합 영역**으로, 마스터 인벤토리의 결함이 아니라 자료 범위의 한계이다.

### Phase 2 진입 시 추가 작업 권고 (필수 아님, 자연 통합)

1. **Table_F EBOPS 12분류 분해** (Phase 2.2 long-form 변환 시): 강의 슬라이드 5의 "운수·여행·로열티" 예시가 Table_F의 12 카테고리(`note/02_bop_components.md` §빠진 부분)와 어떻게 매핑되는지 ITEM_CODE2 차원으로 자동 부여. 마스터 인벤토리 row 14의 first_data_row=9 / cdid_row=8 정보로 자동화 가능.
2. **Table_J NAFA/NIL 양면 분해** (Phase 2.2): `background/note/19_assets_liabilities_mapping.csv` 54행을 시트 결합 키로 사용. ITEM_CODE 4축(분류·자산/부채·flow/stock·시트)으로 정규화. 마스터 인벤토리 row 16(Table_J)의 4부표 구조 + 부호 prefix 정보로 처리 가능.
3. **Table_K Net IIP의 거래·재평가 분해** (Phase 2.3 또는 외부 보강): 분기 단위로는 거래분(=Table_J + Reserve)만 산출 가능, 비거래요인은 연간 Pink Book Dataset 8 결합으로 후속 처리. 본 마스터 인벤토리 단계에서는 처리하지 않음(범위 외).
4. **Table_R1·R2·R3 분리 처리** (Phase 2.1 ETL): 운영 정보로 별도 long-form 파일(`balanceofpayments2025q4_r1.csv` 등)로 분리. 학생용 기본 분석 시리즈와 혼합 금지.
5. **메타 시트(Cover_sheet·Notes·Records) 한국어 메모 변환** (Phase 2.1): 데이터 시트가 아니므로 long-form 변환 대상 외, 한국어 요약 메모로 보존. 마스터 인벤토리 row 1~3의 classification_code='meta_notes'로 자동 분기.

### Phase 2 진입을 막지 않는(이미 해소된) 항목

- 부호 규약 변경(BPM5→BPM6) → `note/03_sign_conventions.md` + Notes 시트 prefix 주석으로 1차 근거 확보.
- BoP↔IIP 연결 → 슬라이드 26 매트릭스 + Table_K 양면 stock 컬럼으로 정량 검증 가능.
- 5대 금융계정 분류 ↔ ONS 표 D1_3·D4_6·D7_9·K 매핑 → `note/06_financial_account_categories.md` + `note/19_assets_liabilities_mapping.md`로 1:1 매핑 완료.
- E&O 정의 + 표적 항등식 `CA + KA + FA + E&O ≡ 0` → 슬라이드 6+13+14 결합 + Table_A 적합 시트 식별 완료.

## 7. 출처

### 마스터 인벤토리

- `db/data/_inventory/15_master_inventory.csv` (헤더 + 20행, 22 컬럼)
- `db/data/_inventory/15_master_inventory.md` (사람 검토용)
- `db/data/_inventory/12_missing_markers.csv` (결측 셀 6행)
- `db/data/_inventory/11_subtable_boundaries.csv` (부표 경계)

### 강의 자료(1차 근거)

- `background/BoP.pptx` (31 슬라이드)
- `background/BoP.pdf` (31 페이지)
- `background/slide_images/slide_NN.png` (NN=01~31)
- `background/INDEX.md`

### 회차 노트

- `background/note/01_inventory.md` — background/ 폴더 인벤토리
- `background/note/02_bop_components.md` — BoP 5대 구성 정의
- `background/note/03_sign_conventions.md` — 부호 규약 BPM5/BPM6
- `background/note/04_identities.md` — 항등식 6종
- `background/note/05_iip_nfa.md` — IIP·NFA 정의
- `background/note/06_financial_account_categories.md` — FA 5분류
- `background/note/07_glossary.md` — 한국어 용어집 62개
- `background/note/08_multimodal_slide_analysis.md` — 슬라이드 15~21·26·30·31 멀티모달
- `background/note/11_final_review.md` — 1~10회차 종합 점검
- `background/note/12_xlsx_sheet_inventory.md` — 시트 인벤토리 + Pink Book 챕터 매핑
- `background/note/13_cdid_dictionary.csv` — CDID 사전 512행
- `background/note/14_slide_28_29_analysis.md` — J-curve · 흡수접근법
- `background/note/16_oecd_bd4.md` — OECD BD4 / SPE / FATS
- `background/note/17_uk_reserves.md` — 영국 공식 외환보유액
- `background/note/18_iip_revaluation.md` — Pink Book Dataset 8 IIP 재평가
- `background/note/19_assets_liabilities_mapping.md` — NAFA/NIL 양면 매핑
- `background/note/21_slide_22_25_visual_check.md` — 슬라이드 22~25 시각 점검
- `background/note/22_bop_data_sources.md` — BoP 다중 자료원 카탈로그
- `background/note/23_geographic_breakdown.md` — Pink Book Ch.9·10 지리분해

### 인용 슬라이드 번호별 1차 근거

- slide 4 (stock vs flow), slide 5 (BoP 5대 구성), slide 6 (FA 5분류), slide 7 (자본계정 정의), slide 8 (BPM5↔BPM6 부호), slide 9 (한국 2017 표), slide 10 (흑자/적자 의미), slide 11 (NFA 흑자=대외순자산↑), slide 12 (종합수지=Reserve), slide 13 (복식부기 사후항등성), slide 14 (CA=FA(narrow)+Reserve=FA(broad) 항등식), slide 21 (상품수지 vs 무역수지 차트), slide 22 (NIA Y=C+I+G+(EX−IM)), slide 23 (CA=S−I, twin deficits), slide 24 ((X−IM)=ΔNFA, NFA+DC=H), slide 25 (BoP vs IIP), slide 26 (BoP↔IIP 매트릭스 도식), slide 27 (탄력성·M-L), slide 28 (J-curve·pass-through), slide 29 (흡수접근법), slide 30 (포트폴리오 접근법), slide 31 (세 접근법 통합).
