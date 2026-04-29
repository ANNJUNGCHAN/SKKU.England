# 단계 1 §7 — 5 핵심 질문 발췌 묶음 통합 정리본 (1 페이지 요약)

본 문서는 `report/PLAN.md` 단계 1 §7 산출물로, 단계 1에서 생성된 6 개 산출물(`01_inventory.md` ~ `06_exchange_rate_ca.md`)을 후속 단계(2 데이터 인벤토리 / 3 외부 환율 확보 / 4 정량+그래프 / 5 노트북+PDF)가 곧바로 참조할 수 있는 형식으로 압축·표화·인덱스화 한다. 외부 웹 검색·신규 정보 도입 없이 6 파일의 내용을 재구성한다.

---

## §1 — 5 핵심 질문 ↔ 발췌 묶음 매핑 표

5 핵심 질문 각각의 1차 슬라이드(`background/BoP.pptx`) · 1차 노트(`background/note/`) · 산출 파일 · 핵심 발췌 한 줄 · 본 보고서 본문 절(§3~§7) 매핑을 한 표로 통합한다.

| 질문 | 1차 슬라이드 | 1차 노트 | 산출 파일 | 핵심 발췌 한 줄 | 본문 절 |
|---|---|---|---|---|:---:|
| **Q1 거시 동향** (영국 만성 적자·주요 변곡점) | 10(흑/적자 의미) · 11(NFA·순차입) · 15(한국 CA/GDP 시계열, 비교 좌표축) | 02(CA 정의) · 17(영국 외환보유액·Net IIP −£199.8bn 만성 채무) · 38(헤드라인 5건 강의 BoP 해석 프레임) | `02_macro_trend.md` (205 줄) | "적자는 생산능력 이상으로 지출하기 때문에 모자라는 부분을 외국에서 수입해 지출했음을 의미"(슬10) + "영국은 음(−) 영역에 구조적으로 머무는 만성 적자국"(노트 38 §1.4) | **§3** 거시 동향 |
| **Q2 CA 4 분해** (상품·서비스·1차·2차소득) | 5(4분류 1줄 정의) · 9(한국 2017 표) · 16(한국 CA 4분해 누적 막대) | 02(4분류 한국어 정의표) · 24(EBOPS 2010 12분류 보강) · 27(1차·2차소득 BPM6 §11·12 보강) | `03_ca_decomposition.md` (390 줄) | "Current account = trade balance + balance on services + net primary income + net secondary income"(슬14) → `CA = G + S + PI + SI` (CDID `BOKI`·`IKBD`·`HBOJ`·`IKBP` ⇒ `HBOP`) | **§4** CA 분해 |
| **Q3 FA 5 분해** (직접·증권·파생·기타·준비자산) | 6(5분류 1줄 정의) · 8(BPM6 부호) · 17(한국 FA 4 구성 누적 막대) | 06(5분류 발췌표) · 19(NAFA/NIL/Net 3면 매핑 CSV 54행) · 25(BPM6 §6.8~§6.81 / OECD BD5 보강) | `04_fa_decomposition.md` (332 줄) | "금융계정: 자산 및 부채의 소유권 변동과 관련된 거래"(슬6) + ONS 표시 부호 `-` 접두 (sign_prefix) 21개 고유 CDID, 59건 부착 | **§5** FA 분해 |
| **Q4 항등식** (CA + KA + FA + NEO ≡ 0) | 13(복식부기 사후 항등성) · 14(`CA = FA(narrow) + Reserve = FA(broad)`, KA=0·NEO=0 가정) · 6(NEO 정의) | 04(항등식 3 층위 발췌) · 20(영국 NEO σ 6,840 £m, NEO/GDP 평균 0.92%, 양 11/음 13) · 38(2025 Q4 검산표) | `05_identity.md` (346 줄) | "표적 항등식 `CA + KA + FA + E&O ≡ 0`은 강의에서 직접 적지 않음. 슬13(복식부기)+슬14(단순화)+슬6(NEO 정의)의 결합으로 도출"(노트 04 #2) | **§6** 항등식 검증 |
| **Q5 환율–CA** (J-curve, Marshall–Lerner, 가격 전가, 포트폴리오) | 27(탄력성 `TB = X − E·M`, M-L `e_X + e_M > 1`) · 28(J-curve, 환율 전가 인과 사슬) · 30(포트폴리오, 미국 사례) | 04(NIA 항등식 `CA = Y − A`·`CA = S − I` 보조) · 08(슬30·31 멀티모달 보강) · 14(슬28·29 J-curve 정밀 단기·중기·장기 + BoE pass-through 60~70% 외부 단서) | `06_exchange_rate_ca.md` (392 줄) | "환율 → 가격 → 수요 → 무역수지 (pass-through · elasticities)"(슬28) + "이 세가지 접근방법은 서로 다 연관되어 있음 (환율과 이자율 채널)"(슬31) | **§7** 환율-CA |

**보조 매핑 (인벤토리 §(바))**:
- Q1·Q4 공통 보조: 슬12 (종합수지 − 준비자산증감 = 0) + 노트 03 (BPM6 부호 규약)
- Q2 보조: 슬21 (상품 vs 무역) + 노트 26 (SITC Rev.4·CIF/FOB)
- Q3 보조: 슬26 (BoP↔IIP 매트릭스, 노트 08 멀티모달) + 노트 16 (OECD BD4 SPE/FATS)
- Q5 보조: 슬23 (CA = S − I, 쌍둥이 적자) + 슬31 (세 접근법 통합)

---

## §2 — 5 발췌 묶음의 핵심 식·정의·통계 한 화면 카드

5 핵심 질문별 정의·식·통계·CDID·헤드라인을 5 카드로 압축한다.

### 카드 Q1 — 거시 동향 (만성 적자 정의)

- **만성 적자 2 차원 정의** (슬10·11 + 노트 38 §1.5 결합):
  - **flow 차원**: `Y < A` 의 구조화 — 슬10 *"적자는 생산능력 이상으로 지출"*. 영국 2025 Q4 CA = −£18.4bn (CA/GDP −2.4%).
  - **stock 차원**: Net IIP 음(−) 누적 = 순부채. 영국 2025 Q4 Net IIP = −£199.8bn (GDP 대비 약 −7%).
- **헤드라인 5건 인용** (노트 38 §1):

| 항목 | 값 (£bn) | CDID | 강의 슬라이드 |
|---|---:|---|---|
| 상품수지 G | **−65.5** (사상 최대) | BOKI | 5·22 (Y<A) |
| 서비스수지 S | **+53.3** | IKBD | 5·24 |
| 1차소득 PI | −2.7 | HBOJ | 5·9 |
| 2차소득 SI | −3.6 | IKBP | 5·9·14 |
| **CA** | **−18.4** | HBOP | 14 (CA = G+S+PI+SI) |
| CA/GDP | −2.4% | — | 15 (정규화) |
| Net IIP | −£199.8bn | — | 11·24·25 |

- **분기 변동** (노트 38 §1.5): Net IIP 2024 Q4 −172.4 → 2025 Q1 −305.7 → 2025 Q4 −199.8 — 거래 흐름만으로 설명 안 됨 ⇒ 비거래요인(가격·환율 재평가) 영향.
- **외환보유액** (노트 17): 2025-10 Net 약 1,123억 USD (£85.5bn), Net IIP 절댓값의 약 −45%.

### 카드 Q2 — CA 4 분해 항등식

- **표적 식**: `CA = G + S + PI + SI` (슬14 영문 식의 한국어 약자 환원).
- **CDID 마스터** (Table_A 부표 1 + 노트 13·27):

| 기호 | 한국어 | 영문 | CDID | 단위 |
|---|---|---|:---:|:---:|
| G | 상품수지 | Trade in goods | **`BOKI`** | GBP million |
| S | 서비스수지 | Trade in services | **`IKBD`** | GBP million |
| PI | 1차소득수지 | Primary income | **`HBOJ`** | GBP million |
| SI | 2차소득수지 | Secondary income | **`IKBP`** | GBP million |
| CA | 경상수지 | Current balance | **`HBOP`** | GBP million |

- **위계** (03_ca_decomposition §3.4):
  - L1: G·S·PI·SI 4 분해 + CA 합계 → §4 헤드라인.
  - L2: PI 3 분해 (COE `IJAJ` · Inv `HBOM` · Other `MT5X`) / SI 2 분해 (Gov `FNSV` · Other `FNTC`) → §4 보조.
  - L3: 투자소득 4 분해 (직접 `MU7F` · 증권 `CGEE` · 기타 `CGFF` · 준비 `HHCC`) → §4 부록 / §5 IIP 연결.
  - 직교: 서비스 EBOPS 12 분해 (Table_F 부표 3, 노트 24) — `MTN8`·`FLYS`·`FNGY` 등.
- **검증** (노트 38 §1.3): G + S + PI + SI = −65.5 + 53.3 + (−2.7) + (−3.6) = **−18.5 ≈ HBOP −18.4** (반올림 0.1bn 차) → 강의 항등식 ONS 실측 정합 확인.
- **영국 부호 패턴** (노트 27 §4.2): G(−)·S(+)·PI(변동, 2007 이후 흑자 축소)·SI(−).

### 카드 Q3 — FA 5 분해 (CDID 마스터 + sign_prefix)

- **표적 식** (슬14): `Financial account = Net acquisition of foreign financial assets − Net incurrence of liabilities + Net financial derivatives` ; `FA(broad) = nonreserve FA + reserve account`.
- **CDID 마스터** (Table_A 부표 3 + 노트 19·25, 모두 `-` 접두 부착):

| # | 분류 | Net CDID | 자산(NAFA) | 부채(NIL) | 2025 Q4 (£bn, ONS 표시) |
|---|---|:---:|:---:|:---:|---:|
| ① | 직접투자 | **`-MU7M`** | N2SV | N2SA | −1.6 |
| ② | 증권투자 | **`-HHZD`** | HHZC | HHZF | −61.5 (사상 최대 순유입) |
| ③ | 파생금융상품 | **`-ZPNN`** | (부재, net만) | (부재) | −1.3 |
| ④ | 기타투자 | **`-HHYR`** | XBMM | XBMN | +54.4 |
| ⑤ | 준비자산 | **`-LTCV`** | LTCV | (정의상 부재) | +0.5 |
| Σ | FA 순합계 | **`-HBNT`** | — | — | −9.5 (5분류 합) |

- **ONS 표시 부호 통계** (노트 13 §추출 규칙 + 19 §sign_prefix):
  - 부호 prefix 부착 CDID 행 **59건**, 고유 CDID **21개**.
  - prefix=true 시트: Table_A·Table_D1_3·Table_D7_9·Table_H·Table_J·Table_R1·Table_R3 (자산 측 + 순 측).
  - prefix=false 시트: Table_D4_6·IIP 저량 전부·Table_K (부채 측 + stock).
  - ONS Notes Table A note 1: *"Reverse the sign of series prefixed with a minus"*.
- **5 분류 정의 인용** (슬6, 노트 25 BPM6 §6.8~§6.81):
  - 직접투자: 경영참가, BPM6 §6.12 의결권 **10% 임계** (강의 자료 누락, BPM6 보강 필요).
  - 증권투자: 양도가능 증권(직접·준비 제외), 만기 LT/ST + 발행자 부문.
  - 파생: BPM6 §6.58, 정산금 회전 → BoP 유량은 **net 단일** 표기.
  - 기타투자: BPM6 §6.63 잔여, **6+1 sub-categories** (Other equity·Currency&deposits·Loans·Insurance·Trade credit·Other·SDR allocations).
  - 준비자산: BPM6 §6.64 readily available + monetary authorities. 영국은 HM Treasury **EEA** 보유, BoE 운용대행. 부채 측 정의상 부재.

### 카드 Q4 — 항등식 일관성

- **표적 식**: `CA + KA + FA + NEO ≡ 0` (회계 항등, NEO = 잔차).
- **강의 자료의 3 층위 표현** (노트 04 §발췌표):

| 층위 | 식 | 가정 | 슬라이드 |
|---|---|---|:---:|
| (i) 사후 항등성 | "대변 합 = 차변 합" (전 계정 합 ≡ 0) | 없음(공리적) | 13 |
| (ii) 단순화 식 | `CA = FA(narrow) + Reserve = FA(broad)` | KA=0, NEO=0 | 14 |
| (iii) 종합수지 | `OSB − 준비자산증감 = 0` ↔ `OSB = Reserve` | NEO=0 | 12·14 |
| (표적) | `CA + KA + FA + NEO ≡ 0` | (직접 식 없음, 결합 도출) | 13+14+6 |

- **NEO 임계 3 건** (노트 20 §변동성 통계, n=24 분기, 2020Q1–2025Q4):

| 임계 | 값 | 적용 의미 |
|---|---:|---|
| 평균 | −1,503 £m | 부호 편향 약함 |
| 표본 SD | **±6,840 £m** | 정상 범위 ±1σ ⇒ [−8,343, +5,337] |
| 절대값 평균 | 5,872 £m | 분기 GDP의 약 0.9% |
| **NEO/GDP 평균** | **0.92%** | 강의 가정 NEO=0 어긋남 |
| NEO/GDP 최대 | 2.16% (2020Q4) | 고변동 분기 |
| **부호 분포** | **양 11 / 음 13** | 평균 차원 부분 성립 |

- **2025 Q4 검산** (노트 38 §2.3):

| 강의 기호 | ONS 항목 | CDID | 2025 Q4 (£bn) |
|---|---|---|---:|
| CA | 경상수지 | HBOP | −18.4 |
| KA | 자본수지 | FNVQ | −0.8 |
| FA(broad, ONS 표시) | 직접+증권+파생+기타+준비 합 | (HBNT 등) | −9.5 |
| NEO | 순오차·누락 | HHDH | +3.5 |
| **합계** | | | **−25.2** |

- **검증 결과**: Phase 5.1 §3 RDB 자동 검증 (`verify_phase5.py`) **0% 차이 PASS** — 잔차 −25.2bn은 시트별 부호 규약 차이·반올림으로 설명. 본 분기 NEO +3.5bn은 1σ 안 = **정상 범위**.

### 카드 Q5 — 환율-CA (3 접근법 + 인과 사슬)

- **(a) 마샬–러너 조건** (슬27): `TB = X − E·M` ; **`e_X + e_M > 1`** (수출 가격탄력성 + 수입 가격탄력성).
- **(b) J-curve · 환율 전가 인과 사슬** (슬28):

```
Exchange rate →   Price   →   Demand   →   Trade Balance
            (pass-through)   (elasticities)
```

  - **단기**: pass-through·탄력성 모두 작음 → 평가절하가 무역수지 일시 악화 (J 좌하단).
  - **중기**: pass-through 진행, 탄력성 증가 → 마샬-러너 조건 충족 시 무역수지 개선 (J 우상승).
  - **장기**: 완전 전가 + 충분한 탄력성 → 평가절하 효과 발현.
  - 가격 전가: 완전 전가 100% / 불완전 전가(profit margin 흡수).
  - **영국 BoE pass-through 60~70%** (노트 14 §슬28 외부 단서, BoE Working Papers — 강의 자료 정량값 부재).
- **(c) 포트폴리오 접근법** (슬30): 자산 선호 변화 → FA → 항등식 `CA = FA` → CA 전이. 영국 적용: "영국 자산이 외국인에게 매력적 ⇒ 영국 FA 부채 순증(BPM6 음수) ⇒ CA 적자" (노트 08 §슬30).
- **(d) 통합 진술** (슬31, 노트 08): 환율(elasticity)·이자율(absorption)·자산선호(portfolio) 세 채널이 서로 얽혀 작동 — 단일 채널 단정 금지.
- **거시 배경식** (노트 04 §발췌표 #5a·#5b):
  - 흡수: `Y − A = EX − IM = CA` (슬22)
  - 저축-투자: `CA = S − I = S_priv + S_pub − I` (슬23, 쌍둥이 적자)
  - 통화: `(X−IM) = ΔNFA`, `NFA + DC = H` (슬24, 영국 변동환율제 직접 적용 한계).

---

## §3 — 5 발췌 묶음의 보고서 §3~§7 인용 후보 통합 표

각 발췌 묶음(02·03·04·05·06)이 산출한 본문 인용 후보의 총 건수와 본문 절(§3·§4·§5·§6·§7)별 분포 + 회피 인용 항목을 통합한다.

### §3.1 본문 절별 인용 후보 분포

| 발췌 묶음 | 본문 절 | 헤드라인 박스 | 본문 표·시각 | 영국 시사·주의 | 합계 | 회피 인용 |
|---|:---:|:---:|:---:|:---:|:---:|---|
| `02_macro_trend.md` (Q1) | §3 | 6 (슬10·11·15 + 노트 02·17·38) | 4 (4분해 검증·CA/GDP 좌표·Net IIP 변동·기축통화 IR 비교) | 6 (Brexit·팬데믹·미니예산·귀금속·연간 시계열·GBP EER) | **16** | 슬22~24 NIA·통화부문(§7로) |
| `03_ca_decomposition.md` (Q2) | §4 | 4 (슬5·14·노트 27 §4.2·노트 24 §흑자 분해) | 7 (4분해 매핑·위계·슬16 시각·영국 시각·PI 분해·SI 분해·EBOPS 12) | 5 (PI 부호 변동·G/Trade 정의·SI 영국 원인·한·영 비교·KA 분리) | **16** | 슬5 자본·금융 정의(§5로); 슬9 우측 표(BPM5, 부호 §은 §5로); 슬16 색깔 한국 그대로 옮기지 말 것; 노트 24 정량 출처 명시 |
| `04_fa_decomposition.md` (Q3) | §5 | 6 (슬6 5분류 1줄 정의 6 행) | C7~C10 (슬8 부호 + 슬9 한국 사례 + 슬14 광·협의 + NAFA/NIL/FD 식) | C11~C29 (BPM6 §6.8/§6.12·§6.54·§6.58·§6.63·§6.64 + 영국 EEA + sign_prefix 패턴 + 본 저장소 분기 실측) | **29** | (회피 명시 없음, ONS 부호 prefix 보존 원칙) |
| `05_identity.md` (Q4) | §6 | 4 (슬13·14·6 + 노트 04 #2) | 7 (4 형태 비교·위계 도식·NEO 시계열·변동성·2025 Q4 검산·헤드라인 vs 분기 흐름·임계 프레임) | 5 (NEO 강의 어긋남·NEO ≠ 0·표적 식 채택 근거·시트별 부호·IMF NEO 정의) | **16** | 슬22~24 NIA·통화부문(§7로); 노트 04 §주의점 4번; 슬25 BoP↔IIP(§5·§9로); 쌍둥이 적자(§7로); 노트 38 §1 헤드라인(§3·§4·§5에서) |
| `06_exchange_rate_ca.md` (Q5) | §7 | C1·C8·C9 (슬27 도입·슬22 흡수·슬23 저축-투자) | C2~C7 + C11·C13·C14 (M-L·J-curve·전가 도식·완전 전가·포트폴리오·통합·3 단계 동학·영국 자산 매력·자산-환율-NX) | C10·C12 + 외부 7 항목 (변동환율 한계·흡수 영국 적용·서비스 elasticity·invoicing·BoE 정량 등) | **14** | (회피 명시 없음, 단 외부 보강 7 W 항목 + 5 D 분석 위임) |
| **총계** | §3~§7 | **23** | **30+** | **39+** | **약 91 후보** | 5 항목 회피군 |

### §3.2 회피 인용 항목 4 군 (5 발췌 묶음 공통 약속)

| 회피군 | 회피 사유 | 본문에서 다룰 곳 |
|---|---|---|
| **NIA·흡수·저축-투자 항등식** (슬22~24) | 회계 항등(§6) vs 거시 항등(§7) 위계 분리 | **§7** (Q5) — `CA = Y − A`·`CA = S − I`·`(X−IM) = ΔNFA` |
| **통화 부문 항등식** (슬24, ΔNFA + ΔDC = ΔH) | 변동환율·인플레이션 타게팅 체계의 직접 적용 한계 | **§7** (Q5) 또는 §부록 — 해석적 도구로만 인용 |
| **BoP↔IIP 연결식 / 비거래요인 3분해** (슬25·26) | flow 합계 항등식(§6) vs flow→stock(§5·§9) 위계 분리 | **§5** (Q3) FA 분해 / **§9** (선택) IIP 한계 |
| **쌍둥이 적자**(슬23, twin deficits, 일본·미국 사례) | CA 분해(§4) vs 환율-CA 결정 모형(§7) 위계 분리 | **§7** (Q5) — 저축-투자 시각 보조 |

---

## §4 — 후속 단계(2~5) 위임 명세 통합

발췌 묶음 4 종(02·04·05·06)에서 명시한 외부 보강 후보를 단계 2(데이터 인벤토리 + 환율 가용성) · 단계 3(`web-search` W1~W8) · 단계 4(`data-scientist` D1~D5) 단위로 통합한다.

### §4.1 단계 2 — 데이터 인벤토리·환율 가용성 점검 위임

**진입 자료**: `db/source/balanceofpayments2025q4.xlsx`, `background/note/12_xlsx_sheet_inventory.csv` (시트 20행), `background/note/13_cdid_dictionary.csv` (CDID 512행, 고유 284), `background/note/15_units.csv`·`15_missing.csv` (단위 82행 + 결측 796행), `background/note/19_assets_liabilities_mapping.csv` (54행).

| # | 점검 항목 | 1차 키 | 산출 형태 |
|---|---|---|---|
| S1 | Q1 4분해 헤드라인 5건 ↔ Table_A 부표 1 CDID 매핑 검증 | `BOKI`·`IKBD`·`HBOJ`·`IKBP`·`HBOP` | 분기 시계열 점검 + Phase 5 검증 PASS 확인 |
| S2 | Q3 FA 5 분해 sign_prefix 21 고유 CDID·59 행 분포 검증 | `-MU7M`·`-HHZD`·`-ZPNN`·`-HHYR`·`-LTCV`·`-HBNT` 6 행 + 추가 15 (NAFA·합계군) | sign_prefix 정규식 매칭 + 셀 부호 검증 |
| S3 | Q4 항등식 검산 4 항 분기 시계열 (CA + KA + FA + NEO) | `HBOP`·`FNVQ`·`HBNT`·`HHDH` | 24 분기(2020Q1–2025Q4) 합계 0 근사 검증 |
| S4 | Pink Book Ch.9 IIP 재평가(가격·환율) 시계열 가용성 | (분기 xlsx 4개 IIP 시트 키워드 0건 — 노트 18) | Pink Book 별도 다운로드 필요성 명시 |
| S5 | 환율 시계열 외부 가용성 점검 (단계 3 W1·W2 진입 조건) | BoE EER · GBP/USD · GBP/EUR | 외부 다운로드 채널·라이선스 확인 |
| S6 | 귀금속 거래 보정 Table_BX (−£8.4bn) 정합성 점검 | Table_BX 헤드라인 vs Records | NEO 변화 점검 (노트 38 §5 #4) |

### §4.2 단계 3 — `web-search` W1~W8 위임 통합 표

| # | 위임 항목 | 1차 출처 후보 | 1 차 근거 묶음 | §7 인용 형태 |
|---|---|---|:---:|---|
| **W1** | GBP 명목·실질 실효환율(EER) 분기 시계열 (최근 20년) | BoE / BIS / OECD | 06 §4.2 | 회귀·산점·시차 상관 입력 (D1~D2) |
| **W2** | GBP/USD·GBP/EUR 분기 평균 환율 시계열 | BoE Statistical Database | 06 §4.2 | 동상 |
| **W3** | 영국 수입가격 pass-through 정량값 (부문별·시기별) | BoE Working Papers (Forbes·Hjortsoe·Nenova 등) | 06 §4.2 + 노트 14 §슬28 | §7.3 가격 전가 절 정량 — 노트 14 60~70% 단서를 1차 출처로 격상 |
| **W4** | 영국 수출·수입 가격탄력성 e_X·e_M 정량값 | OBR / BoE / IMF Article IV | 06 §4.2 | §7.1 마샬–러너 조건 절 영국 정량 |
| **W5** | 영국 무역의 서비스 비중 + 환율 반응 (서비스 elasticity) | ONS Pink Book Ch.3 / IMF / academic | 06 §4.2 | §7 별도 절 — 서비스 무역 환율 반응 |
| **W6** | 2008 GFC·2016 Brexit·2022 미니예산 후 파운드 동학 + NX 동학 | BoE / OBR / FT·Reuters 1차 자료 | 02 §4 + 06 §4.2 | §7.2 J-curve 절 영국 사례 박스 |
| **W7** | 영국 무역의 가격결정통화(invoicing currency) — USD·GBP·EUR 비중 | ECB Working Papers / BIS | 06 §4.2 | §7 환율-CA 약한 상관의 한 설명 (강의 미수록) |
| **W8** | BoE 인플레이션 타게팅 + 변동환율제 환율-CA 약화 메커니즘 | BoE Inflation Report / 학술 논문 | 06 §4.2 | §7.5 영국 변동환율 체계 강의 적용 한계 — 노트 04 §주의점 1줄 단서 격상 |

**보조 외부 보강 후보** (02 §4 추가): 1997~2025 연간 CA/GDP·Net IIP 시계열 (ONS Time Series API `HBOP`·`HBQA` 등) — Q1 §3 작성 시 W6 외 별도 호출 가능.

### §4.3 단계 4 — `data-scientist` D1~D5 위임 통합 표

| # | 분석 항목 | 입력 데이터 | 산출 형태 |
|---|---|---|---|
| **D1** | GBP EER 분기 평균 vs 상품수지/GDP 분기 시계열 산점·상관 (lag 0~8 분기) | W1 환율 + Table_B 상품/GDP | 산점도 + 시차 상관 표 |
| **D2** | 동일 분석을 서비스수지·1차소득·CA 합계에 대해 반복 | W1 + Table_B 서비스/GDP·1차소득/GDP·CA/GDP | 4 패널 산점도 |
| **D3** | 2008·2016·2022 파운드 약세 국면 ±8 분기 NX 동학 박스 차트 (J-curve 검증) | W6 정량 + Table_A 분기 시계열 | 3 박스 차트 |
| **D4** | 환율 변화 1차 차분 vs 무역수지 변화 1차 차분 회귀 | W1 + Table_A | 회귀 계수 + p-value |
| **D5** | 항등식 잔차(NEO) vs 환율 변동성 검증 — 변동성이 큰 분기에 NEO가 커지는지 | W1 + Table_A NEO 시계열 (HHDH 24분기) | 산점도 + 상관 |

**보조 D 후보**:
- D6 (Q1·02 §4): 1997~2025 연간 영국 CA/GDP·Net IIP 시계열 그래프 (ONS Time Series API 입력) — 슬15 좌표축 위에 영국 점 오버레이.
- D7 (Q4·05 §6): NEO ±1σ·±2σ 음영 분기 NEO 시계열 도표 — 노트 20 표 22행 + 자체 계산.
- D8 (Q4·05 §6): HHDH 헤드라인 +3.5bn vs Table_J 순오차 −9,371 £m 부호 차이 정량 분해 — 노트 38 §5 #2.

### §4.4 단계 5 — 노트북·PDF 진입 조건

본 통합 정리본(`07_consolidated_summary.md`)이 단계 5 노트북·PDF 작성 시:
- §1 매핑 표 → 노트북 헤더 메타 (5 질문 × 1차 슬라이드·노트 1 행씩).
- §2 카드 5개 → 노트북 §3·§4·§5·§6·§7 도입 박스로 그대로 이식.
- §3 인용 후보 분포 표 → 노트북 본문 인용 인덱스 (총 91 후보를 본문에 분산 배치).
- §4 위임 명세 → 노트북 §부록 또는 §말미 한계 단락.

---

## §5 — 강의 자료 측 한계 종합

본 절은 강의 자료(BoP.pptx 31 슬라이드 + 노트 39 회차)가 **직접 다루지 않아** 본 보고서가 외부 자료·정량 검증으로 보강해야 할 항목을 5 묶음에서 추출·통합한다.

### §5.1 영국 변곡점 4 건 부재 (Q1·`02_macro_trend.md` §4)

| 변곡점 | 강의 자료 수록 | 외부 보강 채널 |
|---|---|---|
| **2008 글로벌 금융위기** | 슬15 한국 시계열 2008 데이터 포인트만 (한국 사례) | 영국 직접 사례 부재 — ONS BoP Time Series + IMF Article IV |
| **2016 Brexit 국민투표** | 0건 | ONS BoP Time Series · BoE Quarterly Bulletin (W6) |
| **2020 팬데믹** | 0건 (노트 17·38은 2025 분기만) | ONS · IMF Article IV (운수·여행 EBOPS) |
| **2022 미니예산 (Truss 사태)** | 0건 (노트 14 후보 시점 1줄 제안) | BoE / OBR / FT · Reuters (W6) |
| **2025 귀금속 충격** | 0건 (노트 38 §5 #4 Table_BX 존재만 확인) | ONS Statistical Bulletin / FT (S6) |

### §5.2 정량값 부재 항목 5 건 (Q5·`06_exchange_rate_ca.md` §3.4)

| 항목 | 강의 수록 여부 | 외부 채널 |
|---|---|---|
| 영국 수출의 가격탄력성 e_X | **불수록** | W4 (BoE / OBR / IMF) |
| 영국 수입의 가격탄력성 e_M | **불수록** | W4 |
| 영국 수입가격 pass-through (60~70% BoE 단서) | **부분** (노트 14 외부 단서 1줄) | W3 (BoE Working Papers — 정확한 인용 격상) |
| 영국 무역의 서비스 elasticity | **불수록** (강의는 상품 무역 위주) | W5 (ONS Pink Book Ch.3 / IMF) |
| 영국 무역의 가격결정통화(invoicing currency) USD 비중 | **불수록** | W7 (ECB / BIS) |

### §5.3 정량 분해 부재 항목 4 건 (Q3·`04_fa_decomposition.md` §빠진 부분)

| 항목 | 본 저장소 가용성 | 외부 보강 |
|---|---|---|
| 영국 FDI **SPE 포함/제외** 두 시리즈 분기 실측 | xlsx 부재 (분리 컬럼 없음) | ONS Pink Book Ch.4 별도 다운로드 (노트 16·22) |
| 영국 직접투자 하위 3분해 (Equity·Reinvested earnings·Debt instruments) | Table_J 부표 3 col 2~4 (`HBWN`·`HBWT`·`MU7L`) — 잠재 가용 | 단계 2 §S1 추가 추출 |
| 영국 증권투자 만기 LT/ST 분해 | xlsx 부재 | ONS Pink Book Ch.4 별도 시트 |
| 영국 파생금융상품 옵션·선물·스왑 분해 | xlsx 부재 (ZPNN net 단일) | (분해 불가, 외부 BoE 파생조사 별도) |

### §5.4 NEO·항등식 한계 4 건 (Q4·`05_identity.md` §빠진 부분)

| 항목 | 강의 수록 여부 | 보강 채널 |
|---|---|---|
| 강의 가정 "통계 불일치 = 0" vs 영국 NEO σ ±6,840 £m | **명시적 한계** (노트 04 §주의점 2번) | 노트 20 정량으로 §6 §6.2 영국 어긋남 박스 |
| HHDH 헤드라인 +3.5bn vs Table_J 순오차 −9,371 £m 부호 차이 | 미확정 (노트 38 §5 #2) | D8 정량 분해 + 단계 2 §S2 검증 |
| 장기 NEO 시계열 (1990s~2025) | 노트 20은 2020Q1~2025Q4 24분기만 | IMF BOP database + ONS Time Series |
| G7 국가별 NEO/GDP 비교 | 노트 20 §빠진 부분 1번 — 미확보 | IMF BOP database |

### §5.5 BoP↔IIP 비거래요인 3 분해 부재 (Q1·Q3·노트 18)

본 저장소 분기 xlsx 4개 IIP 시트(D1_3·D4_6·D7_9·K) 모두에서 *revaluation*·*exchange rate change* 키워드 0건 매칭 — Pink Book Ch.9 IIP 재평가 3 분해(가격·환율·기타) 시계열은 **별도 다운로드 필수**. 슬26 매트릭스 표(노트 08 멀티모달 보강)의 비거래요인 정량 검증은 본 저장소 데이터로는 불가.

### §5.6 강의 자료 측 한계 종합 (단계 5 PDF 한계 단락 입력)

본 보고서는 강의 자료(BoP.pptx + 노트 39회차)가 **이론 프레임**(BPM6 정의·BoP 항등식·세 결정 접근법)을 풍부하게 제공하나, **영국 적용 정량·사례·시계열**은 거의 수록하지 않는다는 한계를 인정하고, **하이브리드 구조**(강의 측 정의·식 + 외부 정량·사례 + 본 저장소 분기 실측)로 §3~§7을 작성한다. 외부 보강은 단계 3 W1~W8(8 항목) 및 단계 4 D1~D5(+D6~D8 보조, 8 항목)로 위임된다.

---

## §6 — 단계 1 마감 선언

`PLAN.md` 단계 1 §4의 7 항목 산출이 모두 완료되었다 — `01_inventory.md`(폴더 인벤토리·5 핵심 질문 ↔ 슬라이드·노트 1차 근거 매핑) · `02_macro_trend.md`(Q1 거시 동향 발췌, 슬10·11·15 + 노트 02·17·38, 205줄) · `03_ca_decomposition.md`(Q2 CA 4 분해 발췌 + CDID 마스터 `BOKI`·`IKBD`·`HBOJ`·`IKBP`·`HBOP` + 위계 도식, 390줄) · `04_fa_decomposition.md`(Q3 FA 5 분해 발췌 + 부호 prefix 21 고유 CDID·59 행 통계 + ONS sign_prefix 해설, 332줄) · `05_identity.md`(Q4 항등식 4 형태 비교 + NEO 임계 3건 + 2025 Q4 검산표, 346줄) · `06_exchange_rate_ca.md`(Q5 환율-CA 3 접근법 + 인과 사슬 + 외부 보강 W1~W8·D1~D5 위임 명세, 392줄) · `07_consolidated_summary.md`(본 통합 정리본). 단계 1 산출은 **강의 자료 1차 근거 발췌·체계화**에 한정되며, 단계 2(데이터 인벤토리·환율 가용성 점검, `data-scientist` 주도)는 §4.1 진입 자료(분기 xlsx + 노트 12·13·15·19 정형 CSV)와 §4.2~§4.3 외부 보강 후보 표를 키로 삼아 시작한다. 단계 2 진입 조건은 (a) 본 정리본 §3 인용 후보 분포 91건이 §3~§7 본문 골격에 정확히 매핑되어 있을 것, (b) §4 위임 명세 16 항목(S1~S6 + W1~W8 + D1~D5)이 본 저장소 데이터·외부 자료의 가용성으로 분리되어 있을 것, (c) §5 강의 한계 종합 4 묶음(변곡점·정량값·정량 분해·NEO·IIP 비거래요인)이 보고서 한계 단락 입력으로 정리되어 있을 것이며, 본 통합 정리본은 세 진입 조건을 모두 충족한다. 단계 1 종료, 단계 2 진입 가능.

---

## 관련 절대경로

- 입력 발췌 묶음 (단계 1 §1~§6 산출): `c:/Projects/SKKU.England/report/research/01_inventory.md` · `02_macro_trend.md` · `03_ca_decomposition.md` · `04_fa_decomposition.md` · `05_identity.md` · `06_exchange_rate_ca.md`
- 1 차 근거 폴더: `c:/Projects/SKKU.England/background/BoP.pptx` (31 슬라이드) · `c:/Projects/SKKU.England/background/BoP.pdf` · `c:/Projects/SKKU.England/background/slide_images/slide_01.png ~ slide_31.png` · `c:/Projects/SKKU.England/background/note/01_*.md ~ 39_*.md` (39 회차) + 정형 CSV 5건 (노트 12·13·15·19)
- 분기 실측 연결: `c:/Projects/SKKU.England/db/source/balanceofpayments2025q4.xlsx` · `c:/Projects/SKKU.England/db/REPORT.md` (§2.1·§2.3·§3.1·§3.2·§3.3)
- 본 산출물: `c:/Projects/SKKU.England/report/research/07_consolidated_summary.md`
- 후속 단계 진입: `c:/Projects/SKKU.England/report/PLAN.md` 단계 2 (데이터 인벤토리·환율 가용성, `data-scientist` 주도)
