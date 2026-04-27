# Phase 1.1 — 시트별 단위 표기 인벤토리

본 문서는 PLAN.md Phase 1.1 아홉 번째 항목("단위 표기 원문(£ million / £ billion / % of GDP 등) 기록")의 산출물이다. 15회차 background 카탈로그를 Phase 1 영역으로 정식화하면서 부표 단위 차이가 있는 시트(Table_B/BX/R2)를 별도 명시한다.

## 시트별 단위 표

| 시트 | 단위 정규화 | scale_factor | 부표 분리 필요 |
|---|---|---|---|
| Cover_sheet | unknown | — | no |
| Notes | unknown | — | no |
| Records | GBP_billion | 1e9 | no |
| Table_A | GBP_million | 1e6 | no |
| Table_B | MIXED (3×GBP_million + 1×pct_of_GDP) | mixed | **yes** |
| Table_BX | MIXED (3×GBP_million + 1×pct_of_GDP) | mixed | **yes** |
| Table_C | GBP_million | 1e6 | no |
| Table_D1_3 | GBP_billion | 1e9 | no |
| Table_D4_6 | GBP_billion | 1e9 | no |
| Table_D7_9 | GBP_billion | 1e9 | no |
| Table_E | GBP_million | 1e6 | no |
| Table_F | GBP_million | 1e6 | no |
| Table_G | GBP_million | 1e6 | no |
| Table_H | GBP_million | 1e6 | no |
| Table_I | GBP_million | 1e6 | no |
| Table_J | GBP_million | 1e6 | no |
| Table_K | GBP_billion | 1e9 | no |
| Table_R1 | GBP_million | 1e6 | no |
| Table_R2 | MIXED (3×GBP_million + 1×pct_of_GDP) | mixed | **yes** |
| Table_R3 | GBP_billion | 1e9 | no |

## 단위 분포

| 단위 | 시트 수 |
|---|---:|
| GBP_million | 9 (Table_A, C, E, F, G, H, I, J, R1) |
| GBP_billion | 5 (Records, D1_3, D4_6, D7_9, K, R3) — Records 포함 시 6 |
| MIXED (£m + %GDP) | 3 (Table_B, BX, R2) |
| unknown / meta | 2 (Cover_sheet, Notes) |

## 단위 혼재 시트 처리 규약

Table_B / Table_BX / Table_R2의 4번째 부표가 % of GDP 단위. 메타 r3 진술:

> "The first three tables are in pounds million, the fourth table displays percentages of GDP."

Phase 2.1 가공 시 부표마다 단위가 다른 사실을 (sheet, sub_table, unit) 트리플로 명시 보존. 통합 CSV의 UNIT_NAME 컬럼은 부표 단위로 채우되, 부표 4개의 단위 차이를 단일 시트 내에서 자동 판별하도록 처리.

## scale_factor 사용 규칙

- `1e6` (GBP_million): 원본 값에 1,000,000 곱하면 GBP 단위 절대값.
- `1e9` (GBP_billion): 원본 값에 1,000,000,000 곱하면 GBP 단위 절대값.
- `NA` (pct_of_GDP): 단위 환산 없음(이미 비율).
- `mixed`: 시트 내 부표마다 다름 → 부표 단위 판별 필요.

본 단계에서는 단위 환산을 적용하지 않고 메타 정보로만 보존(db/CLAUDE.md "값 불변" 원칙).

## 산출 파일

- 기계 판독: `db/data/_inventory/09_units.csv` (헤더 + 20행, 5 컬럼).
- 사람 검토: 본 문서.

## 15회차와의 관계

- 15회차 `background/note/15_units.csv`는 부표별 행 단위로 정리(82행). 본 산출물은 시트 단위(20행)로 압축하면서 MIXED 시트 식별을 강화.
- 두 산출물은 상호 보완 관계 — 시트 단위(본 문서)는 빠른 매핑 lookup용, 부표 단위(15회차)는 정밀 처리용.
