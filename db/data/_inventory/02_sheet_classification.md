# Phase 1.1 — 시트 7분류 매핑

본 문서는 PLAN.md Phase 1.1 두 번째 항목("각 시트를 7분류 중 하나로 분류")의 산출물이다. 12회차 background 인벤토리에서 매핑한 분류를 PLAN.md Phase 1 영역의 표준 분류 코드로 정식화한다.

## 분류 코드 표준

| code | 한국어 명칭 | PLAN.md §1.1 대응 |
|---|---|---|
| `meta_notes` | 메타·주석 | (가) |
| `summary` | 전체 잔액 요약 | (나) |
| `current_main` | 경상수지 본표 | (다) |
| `current_detail` | 경상수지 세부 | (라) |
| `capital_financial` | 자본·금융계정 | (마) |
| `iip` | 국제투자대조표 | (바) |
| `revisions` | 직전 발표 대비 개정 | (사) |

## 시트 분류 표

| 시트 | classification_ko | classification_code | ONS 표 코드 |
|---|---|---|---|
| Cover_sheet | 메타·주석 | `meta_notes` | (none) |
| Notes | 메타·주석 | `meta_notes` | (none) |
| Records | 메타·주석 | `meta_notes` | (none) |
| Table_A | 전체 잔액 요약 | `summary` | A |
| Table_B | 경상수지 본표 | `current_main` | B |
| Table_BX | 경상수지 본표 | `current_main` | BX |
| Table_C | 경상수지 본표 | `current_main` | C |
| Table_D1_3 | 국제투자대조표 | `iip` | D1.3 |
| Table_D4_6 | 국제투자대조표 | `iip` | D4.6 |
| Table_D7_9 | 국제투자대조표 | `iip` | D7.9 |
| Table_E | 경상수지 세부 | `current_detail` | E |
| Table_F | 경상수지 세부 | `current_detail` | F |
| Table_G | 경상수지 세부 | `current_detail` | G |
| Table_H | 경상수지 세부 | `current_detail` | H |
| Table_I | 자본·금융계정 | `capital_financial` | I |
| Table_J | 자본·금융계정 | `capital_financial` | J |
| Table_K | 국제투자대조표 | `iip` | K |
| Table_R1 | 직전 발표 대비 개정 | `revisions` | R1 |
| Table_R2 | 직전 발표 대비 개정 | `revisions` | R2 |
| Table_R3 | 직전 발표 대비 개정 | `revisions` | R3 |

## 분류 분포

| 분류 | 시트 수 |
|---|---:|
| `meta_notes` | 3 |
| `summary` | 1 |
| `current_main` | 3 |
| `current_detail` | 4 |
| `capital_financial` | 2 |
| `iip` | 4 |
| `revisions` | 3 |
| **합계** | **20** |

PLAN.md §1.1의 7분류 모두 등장하며, 메타 3 + 요약 1 + CA 본표 3 + CA 세부 4 + 자본·금융 2 + IIP 4 + 개정 3으로 구성.

## 산출 파일

- 기계 판독: `db/data/_inventory/02_sheet_classification.csv` (헤더 + 20행, 4 컬럼).
- 사람 검토: 본 문서.

## 12회차와의 관계

12회차 background 인벤토리의 `classification` 컬럼(영문 약어: meta·summary·CA-main·CA-detail·KA-FA·IIP·revision)을 Phase 1 표준 코드(snake_case)로 1:1 변환. 시트 매핑 자체는 동일.
