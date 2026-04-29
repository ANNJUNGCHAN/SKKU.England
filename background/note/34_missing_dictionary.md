# 34회차 — Phase 4.1 §8 결측 사전 한국어 의미 진술

본 노트는 `db/CHECKLIST.md` Phase 4.1 §8번([background-search] 결측 사전의 한국어 의미 문장을 강의 자료 표현 또는 통계 일반론적 정의에 맞춰 작성 요청) 산출물. Phase 4 RDB 스키마의 결측 사전 테이블(`missing_dict`)에 등록할 결측 코드(`x`, (empty), `..` 등)별 한국어 의미 표준 문장 정리. 외부 web-search 미사용, `background/` 폴더 자료(노트 13·15·32 + 노트 10 §발췌 #9) 1차 근거.

---

## §1 강의 자료 결측 표기 진술 유무

### §1.1 키워드 등장 매트릭스 (슬라이드 1~31 전수)

| 키워드 | 등장 횟수 |
|---|---|
| 결측 / 공란 / 비공개 / 미가용 | **0회** |
| 비밀유지 / `[c]` | **0회** |
| 의미상 0 / `[z]` | **0회** |
| 정확도 낮음 / `[low]` | **0회** |
| 해당 없음 / `..` | **0회** |
| 자료 없음 / `-` | **0회** |
| `x` 마커 단일 진술 | **0회** |

**결론**: 강의 자료에는 **결측 표기 의미·처리 규칙·기호 약속이 일체 등장하지 않음**(노트 13·32에서 이미 확정). Phase 4 결측 사전의 한국어 의미 표준 문장은 **강의 자료에서 직접 인용할 근거가 없으며**, ONS Service Manual(노트 10 §발췌 #9) + Government Analysis Function 표기 가이드 + 노트 15 §결측 카탈로그를 1차 근거로 활용.

### §1.2 강의 자료 미수록의 함의

강의는 BoP 개념·항등식·부호 규약 중심이며 데이터 적재·표기 규약은 통계 운영 매뉴얼 영역. Phase 4 RDB 결측 사전 한국어 라벨은 ONS Methodology + 노트 15(영국 BoP 분기 본 데이터 실측) 기준으로 작성하고, 강의 자료의 한국어 표현이 그 의미와 자연스럽게 들어맞는지만 검증.

---

## §2 노트 15 §결측 카탈로그 정량 분포 (본 데이터셋 실측)

### §2.1 마커별 누적 셀 수

| 마커 | 누적 셀 수 | 등장 시트/부표 | 의미 카테고리 |
|---|---:|---|---|
| **`x`** | **360** | Table_C 부표 1~6 (각 60건) | ONS confidential / suppressed |
| **(empty)** | **약 35,000** | 모든 시트(메타·본표 padding 포함) | 시리즈 시작 이전 또는 자료 없음 |
| `..` | 0 | 미등장 | (legacy 미사용) |
| `-` | 0 | 미등장 | (legacy 미사용) |
| `[c]`·`[z]`·`[low]`·`[x]` | 0 | 미등장 | (GAF 기호 미적용) |

### §2.2 `x` 마커 위치 (Table_C, 6 부표 × 60 셀)

| 부표 | 첫 등장 위치 | 셀 수 |
|---:|---|---:|
| 1 (EU Credits) | B9 | 60 |
| 2 (EU Debits) | B158 | 60 |
| 3 (EU Balances) | B307 | 60 |
| 4 (non-EU Credits) | B456 | 60 |
| 5 (non-EU Debits) | B605 | 60 |
| 6 (non-EU Balances) | B754 | 60 |

각 60건 = 1997 Q1 ~ 1998 Q4 (8 분기) × 7~8 컬럼 = EU/non-EU 지역분해 시계열 1997-1998 미공개. ONS Notes 시트 11번: *"Cells containing 'x' represent unavailable data."*

### §2.3 (empty)의 두 가지 유형

(empty) 약 35,000건 = (a) 시트 padding(빈 행/열, 메타·본표 레이아웃 공백) + (b) 데이터 영역 시리즈 시작 이전 셀.

- (a) Cover_sheet 515 + Notes 327 + Records 44 + 본표 padding — **결측 아님**
- (b) 데이터 영역의 (empty) — **시리즈 시작 이전 또는 결측**

Phase 4 적재 시 (a)는 row_index 자체 미생성 → 사전 등록 의미 없음. (b)만 `value_raw=NULL`로 적재되며 한국어 의미는 **"시리즈 시작 이전 또는 자료 없음"**.

---

## §3 ONS Service Manual + GAF 결측 표기 표준

> ONS Service Manual: `..`, `-` 사용 비권장 → Government Analysis Function 표 기호 가이드 따라 **대괄호 표기**(`[c]`·`[z]`·`[low]`) 권고. "NA"는 의미 모호(Not Available/Not Applicable)하므로 회피.

| 의미 | GAF 권장 | 본 xlsx 실제 | 평가 |
|---|---|---|---|
| 비공개 | `[c]` | `x` | legacy 형식 유지 |
| 미산출 | `[x]` | 사용 사례 없음 | `x`로 통합 사용 |
| 진정한 0 | `[z]` | 0 그대로 | 회피 OK |
| 반올림 0 | `[low]` | 0 또는 작은 값 | OK |
| 모호 | NA/n/a 회피 | 미사용 | OK |
| legacy 미가용 | `..` 비권장 | 미사용 | 권장 부합 |
| legacy nil | `-` 비권장 | 미사용 | 권장 부합 |

본 BoP Bulletin은 GAF 권장 `[c]` 미전환 상태이나, 단일 `x` 마커만 사용해 모호성은 낮음. ECOS 결측 사전과는 표기 체계가 다르므로 직접 비교 불가 — 한국어 의미 라벨은 ONS·GAF 정의를 한국어로 풀어 적용.

---

## §4 Phase 4 결측 사전 테이블 시드 데이터

| missing_code | meaning_kr | meaning_en | source |
|---|---|---|---|
| `x` | 비공개·미가용 (ONS 비밀유지 또는 미산출) | unavailable, suppressed (confidential or not produced) | ONS Notes 시트 11번; `background/note/15_units_and_missing.md` §결측 카탈로그 |
| (empty) | 시리즈 시작 이전 또는 자료 없음 (데이터 영역 한정) | not available / not yet observed (data region only) | `background/note/15_missing.csv`; ONS Methodology |
| `..` | 해당 없음(개념상 정의 불가) | not applicable | ONS Service Manual; `background/note/10_ons_web_research.md` §발췌 #9 |
| `[c]` | 비밀유지 (GAF 권장 표기) | confidential | Government Analysis Function table symbols guidance |
| `[z]` | 의미상 0 (정확히 0인 진정한 영) | true zero | Government Analysis Function table symbols guidance |
| `[low]` | 정확도 낮음 (반올림 결과 0에 근접) | low precision (rounded to near zero) | Government Analysis Function table symbols guidance |

### §4.1 한국어 의미 진술 작성 원칙

1. 강의 자료 직접 인용 표현 부재 → ONS·GAF 표준 영문 정의를 한국어 통계 일반론 표현으로 풀어 작성.
2. ECOS 결측 사전과 직접 1:1 대응 시도 금지(노트 32 §6.4 정직 명시).
3. 영문 라벨은 괄호 병기로 원본 표현 보존.
4. (empty)는 (a) 레이아웃 공백·(b) 데이터 결측 구분 → 한국어 라벨은 데이터 결측 영역에 한정.

---

## §5 본 데이터셋 등록 권고

### §5.1 필수 등록(2행)

| missing_code | 등장 빈도 | Phase 4 적재 처리 |
|---|---:|---|
| `x` | 360건 (Table_C 6 부표) | `value_raw='x'` + `value_numeric=NULL` + `missing_reason='confidential'` |
| (empty, 데이터 영역) | 시계열 시작 이전 셀 | `value_raw=NULL` + `value_numeric=NULL` + `missing_reason='not_available'` |

### §5.2 사전 등록 권고(4행)

| missing_code | 등록 사유 |
|---|---|
| `..` | ONS legacy — 다른 ONS 데이터셋 적재 시 대비 |
| `[c]` | GAF 권장 — 가공 단계에서 `x` → `[c]` 전환 검토 |
| `[z]` | GAF 권장 — `value_raw='[z]'` + `value_numeric=0`로 진정한 0과 결측 구분 |
| `[low]` | GAF 권장 — 반올림 0과 진정한 0 구분 |

### §5.3 처리 정책

ONS는 `x`를 비공개로 명시 → 적재 시 `value_raw + value_numeric + missing_reason` 3-컬럼 패턴 권장. 결측을 0/NA로 치환하지 않음(`db/CLAUDE.md` §3 결측 보존 원칙).

---

## §6 출처 카탈로그

| 자료 | 본 노트 사용 |
|---|---|
| `background/BoP.pptx` (전 31장) | §1 결측 진술 0회 확인 |
| `background/note/13_cdid_dictionary.md` | §1 cross-ref |
| `background/note/15_units_and_missing.md` | §2·§3·§5 (1차 근거) |
| `background/note/15_missing.csv` | §2.1·§2.2 정량 집계 |
| `background/note/10_ons_web_research.md` §발췌 #9 | §3 ONS·GAF 표준 인용 |
| `background/note/32_metadata_model.md` §1.1·§2.3 | §1.1 매트릭스 + §4.1 정직 명시 |

---

## §7 확인하지 못한 부분 (정직 명시)

1. **ECOS 결측 사전 한국어 의미 표준** — 강의 자료 미수록. ECOS Open API 응답 스키마(예: `,`·`-`·`*` 코드)와 ONS `x`·(empty) 코드의 1:1 대응 여부 본 폴더 자료로 확인 불가.
2. **GAF 표기 가이드 본문** — 노트 10 §발췌 #9에 ONS Service Manual 인용은 있으나, GAF 가이드 본문 PDF 직접 인용 없음. `[c]`·`[z]`·`[low]` 정확한 한국어 표준 번역어 미확인.
3. **(empty) 데이터 영역 vs 레이아웃 공백 분리** — 정확한 분리 행/열 인덱스 매트릭스는 별도 코드로 산출 필요(Phase 2.2 가공 단계).
4. **`x` 360건의 1997-1998 EU 시계열 미공개 사유** — Notes 시트 11번 단순 "unavailable data" 진술만, 미공개 사유(응답률·EU 통계 보호·표본 크기)에 대한 ONS 상세 설명 없음.
5. **결측 코드 우선순위(ECOS 관행)** — `missing_code` PK 단일이어야 하는지, 다중 결측 사유 발생 시 우선순위는 어떤지 강의 자료·노트 진술 없음.
