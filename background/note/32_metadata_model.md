# 32회차 — Phase 4.1 §1 강의 자료 ECOS·메타데이터 모델 진술 점검

본 노트는 `db/CHECKLIST.md` Phase 4.1 §1번([background-search] 강의 자료에 ECOS 또는 일반 통계 메타데이터 모델이 다뤄지는지 확인) 산출물. Phase 4(ECOS 스타일 RDB 구축, 4~5 테이블) 스키마 설계 시 강의 자료(`background/BoP.pptx` 31장)에서 한국어 표현·위계 근거로 활용 가능한 진술이 있는지를 사전 정리. 외부 web-search 미사용, 본 폴더 자료 1차 근거.

---

## §1 강의 자료에서 ECOS·메타데이터 모델 진술 유무

### §1.1 키워드 등장 매트릭스 (슬라이드 1~31 전수 검색)

`background/BoP.pptx` 31장 텍스트에 메타데이터 관련 키워드 17종을 grep한 결과:

| 키워드 | 등장 | 비고 |
|---|---|---|
| **ECOS** | 0회 | 한국은행 통계포털 ECOS 자체 언급 없음 |
| **메타데이터(Metadata)** | 0회 | "메타"·"메타데이터" 단일 표제 없음 |
| **통계표 코드(STAT_CODE)** | 0회 | "Table A/B/C…" 영문 표 코드도 없음 |
| **항목 코드(P_ITEM_CODE)** | 0회 | CDID 4자리 식별자 자체 미수록 |
| **통계 위계(Hierarchy / LVL)** | 0회 | "LVL1/LVL2/LVL3"·"위계" 표현 없음 |
| **결측 사전(Missing dictionary)** | 0회 | "결측"·"x"·"공란" 처리 규칙 진술 없음 |
| **용어 사전(Glossary)** | 0회 | 본문 내 산문 정의만 |
| **SDMX·SDDS·GSBPM·UNECE CMF·DDI·GSIM** | 0회 | 통계 표준 교환 모델 일체 언급 없음 |
| **BPM5/BPM6** | 매뉴얼 명칭 표기로만 | "최근/이전 매뉴얼" 산문 표기. 약자 자체 미사용. "2010년 확정 공표한 새로운 국제수지통계 매뉴얼"(slide 5) 우회 표기 |
| **Schema·RDB·DB 모델링** | 0회 | 일체 등장 없음 |
| **CDID·Pink Book·ONS** | 0회 | ONS 표 코드·간행물 명칭 모두 강의 자료에 없음 |
| **분야 분류 코드(100/200/400번대)** | 0회 | 31회차 §2.3 재확인 |
| **표준 분류 체계(SITC·EBOPS·ISIC)** | 0회 | "운수·여행·로열티" 예시만, 12분류 체계 진술 없음 |

**결론**: 강의 자료에 **ECOS·SDMX·SDDS·GSBPM·UNECE CMF 등 일반 통계 메타데이터 모델 진술은 일체 존재하지 않는다**. 31회차 §2.3 결론을 메타데이터 모델 전반으로 확장 확인.

### §1.2 강의 자료가 다루는 통계 위계 (산문 명시)

#### §1.2.1 BoP 위계 (슬라이드 5·6·7)

```
국제수지(Balance of Payments, BoP)
├─ 경상계정(Current Account, CA)              — 슬라이드 5
│  ├─ 상품수지 / 서비스수지 / 본원소득수지(1차) / 이전소득수지(2차)
├─ 자본계정(Capital Account, KA)              — 슬라이드 5·7
└─ 금융계정(Financial Account, FA)            — 슬라이드 5·6
   └─ 직접투자 / 증권투자 / 파생 / 기타투자 / 준비자산증감
```

3계층 위계지만 **"LVL1·LVL2·LVL3" 메타 라벨로 부르지 않음**. LVL 매핑은 노트 30·31·본 노트에서 별도 부여.

#### §1.2.2 IIP 위계 (슬라이드 25)

```
국제투자대조표(IIP)
├─ 자산(Assets)        — 대외투자 잔액 (Investment abroad)
├─ 부채(Liabilities)   — 외국인의 국내투자 잔액 (Investment in the UK)
└─ 순(Net)             — Net IIP = 자산 − 부채
```

자산/부채/순 3계열은 슬라이드 텍스트에 직접 명시되지 않으며 **광의의 국제거래통계를 구성하는 두 요소** 산문으로만 시사. ONS Table D1.3/D4.6/D7.9·K 자산·부채·순 3분 형식은 노트 12·19에서 ONS 운영 규칙으로 별도 매핑.

#### §1.2.3 종합수지 항등식 (슬라이드 12·14)

```
종합수지(Official Settlements Balance)
= 경상계정 + 자본계정 + 금융계정(준비자산 제외)
국제수지 항등성: 종합수지 − 준비자산증감 = 0
```

위계라기보다 **항등식**으로 강의 자료가 제시. 무결성 점검 지표 임계 기준의 1차 근거(노트 04·20).

### §1.3 정직 명시

- 강의 자료에는 **위 위계의 "라벨"·"코드 체계"·"메타데이터 컬럼 정의"가 일체 등장하지 않는다**. 슬라이드 본문은 "경상계정·금융계정·자본계정" 식 산문 분류만 제시.
- Phase 4 RDB 스키마(통계표 메타·통계항목 메타·관측치·결측 사전·통계 용어 사전 4~5 테이블) 모델 구조 자체는 **강의 자료에서 직접 근거를 인용할 수 없으며**, ECOS Open API 트리·IMF SDMX-ML·UNECE GSBPM 등 외부 표준에서 가져와야 함(web-search 위임 권고 — Phase 4.1 후속 항목).

---

## §2 강의 자료 미수록 → ECOS·외부 표준 보강 필요 영역

### §2.1 통계표 메타 4축

| 메타 축 | 강의 자료 진술 | 보강 필요 |
|---|---|---|
| **통계표 메타** | 없음(단일 명칭 "국제수지표") | ECOS `STAT_NAME`·`STAT_CODE` / SDMX `Dataflow ID` / ONS Pink Book Table |
| **통계항목 메타** | 없음 | ECOS `ITEM_CODE`·`ITEM_NAME`·`UNIT_NAME`·`WGT` / SDMX `Concept Scheme` |
| **시점 메타** | "일정한 기간"(slide 4)·"(2017년)"(slide 9)만 | ECOS `CYCLE` / SDMX `TIME_PERIOD` |
| **관측치** | "단위: 백만달러"(slide 9 한국 예시)만 | ECOS `DATA_VALUE` / SDMX `OBS_VALUE` / 노트 15 본 프로젝트 단위 표 |

### §2.2 통계항목 위계(P_ITEM_CODE / LVL / WGT)

| 컬럼 | 강의 자료 진술 | 보강 필요 |
|---|---|---|
| **P_ITEM_CODE** | 없음 | ECOS `P_ITEM_CODE` + 노트 30 §ITEM_CODE 표 |
| **LVL** | 없음 | ECOS `LVL` / 노트 31 §1.2 + 노트 30 §ITEM_CODE 표 |
| **WGT** | 없음 (BoP에서 가중평균 미적용) | ECOS `WGT` (NULL 보관 권고) |

### §2.3 결측 사전 한국어 의미

| 결측 코드 | 강의 자료 진술 | 보강 필요 |
|---|---|---|
| `x` (비공개·미산출) | 없음 | 노트 15 §결측 카탈로그 (Table_C 6 부표 × 60건) |
| `..` (해당 없음) | 없음 | ONS Methodology guide |
| (empty/공란) | 없음 | 노트 15 §결측 — padding ~35,000건 |
| `[c]`·`[z]`·`[low]` | 없음 | ONS 일반 표기 — 본 데이터셋 미등장이나 사전 등록 권고 |

### §2.4 통계 용어 사전 1차 시드

| 표제어 | 강의 자료 정의 유무 | 1차 근거 |
|---|---|---|
| **BoP**(국제수지표) | ◉ 슬라이드 4 산문 정의 | 노트 02·07; slide 4 |
| **IIP**(국제투자대조표) | ◉ 슬라이드 4·25 산문 정의 | 노트 05·07; slide 4·25 |
| **경상수지(CA)** | ◉ 슬라이드 5·10·14 + 항등식 | 노트 02·04·07; slide 5·10·14 |
| **금융계정(FA)** | ◉ 슬라이드 5·6·11·14 + 5하위 | 노트 02·06·07; slide 5·6·11·14 |
| **순대외자산(NFA)** | ◉ 슬라이드 11·24 — `(X−IM) = ΔNFA` | 노트 04·05·07; slide 11·24 |
| **BPM6 부호 규약** | ◉ 슬라이드 8 산문 진술. "BPM6" 약어 미사용 | 노트 03·07; slide 8 |
| **CDID** | ✗ 강의 자료 미수록 | 노트 13(`13_cdid_dictionary.md`) — ONS 표준 |
| **귀금속 보정** | ✗ 강의 자료 미수록 | 노트 12 §Table_BX + ONS Methodology |
| **임계 기준** | ✗ 강의 자료 미수록 | 노트 20 §NEO 시계열 |

### §2.5 무결성 점검 지표 임계 기준

강의 자료는 **"통계 불일치 = 0 가정"**(slide 14)·**"종합수지 − 준비자산증감 = 0"**(slide 12)의 이론적 항등식만 제시. 영국 분기 실측 잔차 허용 임계는 강의 자료 없음. 노트 20 NEO 분기 시계열(절대값 평균 약 5,872 £m, |NEO|/GDP 평균 0.92%)을 1차 근거로 별도 정해야 함.

---

## §3 Phase 4 스키마 설계에 강의 자료가 제공하는 한국어 표현 근거

### §3.1 통계표 메타 — `STAT_NAME` (한국어)

| 시트 | 강의 자료 한국어 표기 | 슬라이드 |
|---|---|---|
| Table_A | "국제수지표"·"잔액 요약" | 4·5 |
| Table_B/BX | "경상수지"·"경상계정" | 5·9·10 |
| Table_C | "경상수지(EU/non-EU)" | 5 + 노트 23 |
| Table_E | "상품수지"·"재화의 수출입" | 5·21 |
| Table_F | "서비스수지"·"운수·여행·로열티" | 5 |
| Table_G | "본원소득수지"·"1차소득" | 5·14 |
| Table_H | "이전소득수지"·"2차소득" | 5·14 |
| Table_I | "자본계정"·"자본수지" | 5·7·14 |
| Table_J | "금융계정"·"금융수지" | 5·6·11 |
| Table_D1_3/D4_6/D7_9/K | "국제투자대조표(IIP)" | 4·25 |

노트 12·20·specification.csv·statcatalog.csv가 이미 슬라이드 5·6·7·9·25 표기와 1:1 정합 적용.

### §3.2 통계항목 메타 — 부호 규약(BPM6 자산·부채 증감 기준)

슬라이드 8 발췌:
> "새로운 매뉴얼에서는 금융계정 부호표기 방식을 '자산·부채의 증감 기준'으로 변경. … 자산 항목의 부호는 반대 방향으로 바뀜. … 이전 매뉴얼에서는 금융계정 부호표기 방식을 '순유출입액 기준'으로 함."

슬라이드 11:
> "금융수지(준비자산 제외)의 흑자(surplus)는 대외순자산 증가, 적자(deficit)는 순차입 증가."

→ Phase 4 통계항목 메타 테이블 `SIGN_CONVENTION` 컬럼 한국어 값을 슬라이드 8·11에서 직접 인용.

### §3.3 IIP 위계 (슬라이드 25)

> "국제수지표(B.O.P): flow 통계 / 국제투자대조표(IIP): stock 통계 / IIP의 증감내역은 거래요인과 비거래요인으로 구분 / 거래요인 = BoP 투자수지 + 준비자산증감 합계와 일치"

→ 통계항목 메타에 `STOCK_FLOW_TYPE` 컬럼(`flow`/`stock`) 권고. 한국어 라벨 "흐름(플로우)"·"잔액(스톡)"은 노트 07 §IIP 표제어 정의.

### §3.4 BoP 위계 (슬라이드 5)

> "국제수지표의 구성: 크게 경상계정(Current account), 금융계정(Financial account), 자본계정(Capital account)으로 분류. 경상계정: 상품수지(Trade balance), 서비스수지(Balance on services), 본원소득수지(Primary income), 이전소득수지(Secondary income)."

→ LVL1/LVL2/LVL3 매핑의 한국어/영문 라벨은 슬라이드 5에서 그대로 인용 가능.

---

## §4 Phase 4 §1.4(통계항목 위계 자문) 준비 사항

### §4.1 슬라이드 5 위계 ↔ 본 프로젝트 LVL1/LVL2/LVL3 1:1 매핑

| LVL1 | LVL2 | LVL3 | 한국어 | 영문 | ITEM_CODE2 |
|:---:|:---:|:---:|---|---|---|
| BoP | CA | — | 경상계정 | Current account | `CA` |
| BoP | CA | TG | 상품수지 | Trade balance | `CA.G` |
| BoP | CA | SV | 서비스수지 | Balance on services | `CA.S` |
| BoP | CA | PI | 본원소득수지(1차소득) | Primary income | `CA.PI` |
| BoP | CA | SI | 이전소득수지(2차소득) | Secondary income | `CA.SI` |
| BoP | KA | — | 자본계정 | Capital account | `KA` |
| BoP | FA | DI | 직접투자 | Direct investment | `FA.DI` |
| BoP | FA | PI | 증권투자 | Portfolio investment | `FA.PI` |
| BoP | FA | DR | 파생금융상품 | Financial derivatives | `FA.DR` |
| BoP | FA | OI | 기타투자 | Other investment | `FA.OI` |
| BoP | FA | RA | 준비자산증감 | Changes in reserve assets | `FA.RA` |
| IIP | A | — | 자산(대외투자 잔액) | Investment abroad | (Table_D1_3) |
| IIP | L | — | 부채(외국인 국내투자) | Investment in the UK | (Table_D4_6) |
| IIP | N | — | 순(Net IIP) | Net IIP | (Table_D7_9·K) |

### §4.2 cross-ref 권고

- LVL1/LVL2/LVL3 컬럼명·정수 인코딩은 ECOS Open API 표준(`LVL` 정수, `P_ITEM_CODE` 부모 키)을 따르되, **한국어/영문 라벨은 슬라이드 5(BoP)·25(IIP)에서 직접 인용**.
- WGT 컬럼은 BoP에서 통상 사용하지 않으므로 NULL 보관(노트 30 §0.0% 처리 방식 참고).
- ITEM_CODE4(노트 30 LVL4) 컬럼은 추후 EBOPS 12분류·SITC 5자리 등 세부 분해 추가 시 채울 수 있음.

---

## §5 출처 카탈로그

| 자료 | 본 노트 사용 |
|---|---|
| `background/BoP.pptx` (전 31장) | §1·§3·§4 |
| `background/note/02_bop_components.md` | §1.2.1·§3.1·§4.1 |
| `background/note/07_glossary.md` | §2.4 |
| `background/note/12_xlsx_sheet_inventory.md` | §3.1·§4 |
| `background/note/21_slide_22_25_visual_check.md` | §3.3 |
| `background/note/30_specification_review.md` | §2.2·§4.1 |
| `background/note/31_field_classification.md` | §1.1·§1.2·§4 |
| `background/note/15_units_and_missing.md` | §2.3 |
| `background/note/20_neo_volatility.md` | §2.5 |

본 노트가 인용한 슬라이드: 4·5·6·7·8·11·12·14·25.

---

## §6 확인 못한 부분 (정직 명시)

1. **ECOS Open API 분야 트리 / 컬럼 표준 표기 자체의 정확성** — 강의 자료에 진술 없음 → 한국은행 ECOS 사이트 + ECOS Open API 응답 스키마로 별도 검증 필요(web-search 위임 권고).
2. **SDMX-ML / SDDS Plus / GSBPM 적용 가능성** — 본 프로젝트는 4~5 테이블 RDB로 시작하므로 SDMX 풀 모델은 과도. 다만 통계항목 코드 체계 표준화 시 SDMX `Concept Scheme`·`Codelist`를 부분 차용 가치.
3. **WGT 컬럼의 BoP NULL 처리**가 ECOS 관행에 부합하는지 강의 자료로 결정 불가.
4. **결측 표기 한국어 의미** — ONS Methodology vs ECOS 결측 코드(`,`·`-`·`*`)의 의미 1:1 대응 여부 강의 자료 미수록.
5. **무결성 점검 임계 기준의 정량 수치** — 노트 20 영국 분기 실측 분포(0.92% 평균)를 참고할 수 있으나 강의 자료의 권장 임계는 없음.
6. **Phase 4 스키마 PK/FK/인덱스 설계** — 강의 자료 RDB 모델링 미수록.
7. **CYCLE 컬럼 한국어 라벨** — ECOS는 `D/M/Q/A` 영문 코드. 강의 자료는 산문 표기만 ("분기"·"연간").
