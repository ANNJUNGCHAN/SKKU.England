# Phase 1.1 — 시점 컬럼 형식 인벤토리

본 문서는 PLAN.md Phase 1.1 여덟 번째 항목("시점 컬럼 형식(연 `YYYY` / 분기 `YYYY Qn` / 월 `YYYY MMM` 등) 기록")의 산출물이다.

## 핵심 발견

- 본표 17개 시트 **모두 동일한 두 시점 형식**을 사용:
  - **`YYYY` (연간)** — 1997~2025 (29년)
  - **`YYYY Qn` (분기)** — 1997 Q1 ~ 2025 Q4 (116분기)
- 두 형식은 **한 부표 안에 수직 적층**(연간 먼저, 빈 행 1개, 그 다음 분기). 부표 단위로 (연간 + 분기)가 함께 등장.
- **월간(`YYYY MMM`)·일간(`YYYY-MM-DD`) 형식 없음**.
- Table_R 계열은 분기 시계열이 한 분기 짧음(2025 Q3까지) — 직전 발표 대비 개정 시점이 원본보다 한 분기 빠르기 때문.
- Cover_sheet/Notes/Records 메타 시트 3개에는 시점 컬럼 없음.

## 시트별 시점 형식 표

| 시트 | 형식 | 연간 행 수 | 분기 행 수 | 연간 시점 범위 | 분기 시점 범위 |
|---|---|---:|---:|---|---|
| Cover_sheet | none / meta | 0 | 0 | — | — |
| Notes | none / meta | 0 | 0 | — | — |
| Records | none / meta | 0 | 0 | — | — |
| Table_A | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_B | YYYY + YYYY Qn | 116 | 464 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_BX | YYYY + YYYY Qn | 116 | 464 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_C | YYYY + YYYY Qn | 174 | 696 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_D1_3 | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_D4_6 | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_D7_9 | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_E | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_F | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_G | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_H | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_I | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_J | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_K | YYYY + YYYY Qn | 87 | 348 | 1997~2025 | 1997 Q1~2025 Q4 |
| Table_R1 | YYYY + YYYY Qn | 84 | 345 | 1997~2024 | 1997 Q1~2025 Q3 |
| Table_R2 | YYYY + YYYY Qn | 112 | 460 | 1997~2024 | 1997 Q1~2025 Q3 |
| Table_R3 | YYYY + YYYY Qn | 252 | 1035 | 1997~2024 | 1997 Q1~2025 Q3 |

## 행 수 산출 방식

- 본표 시트의 연간 행 수 = 부표 수 × 29년.
  - 예: Table_A 3 부표 × 29 = 87 ✓
  - Table_B/BX 4 부표 × 29 = 116 ✓
  - Table_C 6 부표 × 29 = 174 ✓
- 본표 시트의 분기 행 수 = 부표 수 × 116분기.
  - 예: Table_A 3 부표 × 116 = 348 ✓
  - Table_C 6 부표 × 116 = 696 ✓
- Table_R 계열의 연간 행 수 = 부표 수 × 28년 (2024까지).
  - Table_R3 9 부표 × 28 = 252 ✓
- Table_R 계열의 분기 행 수 = 부표 수 × 115분기 (2025 Q3까지).
  - Table_R3 9 부표 × 115 = 1035 ✓

## ECOS 매핑 (Phase 2.2 통합 CSV 활용)

PLAN.md §0.2 ECOS 표준에 따라:
- 연간 시점은 `CYCLE = "A"`, `TIME = "YYYY"` (예: 2025).
- 분기 시점은 `CYCLE = "Q"`, `TIME = "YYYYQn"` (예: 2025Q4) — 공백 제거하여 ECOS 표기 통일.
- 월간·일간 시점은 본 자료에 없으므로 적용 불요.

## Phase 2.1 활용

- 시트별로 각 부표 안에서 **연간 영역(첫 29행)** + **빈 행 1개** + **분기 영역(116행)** 을 분리해 각각 CYCLE 컬럼을 다르게 부여.
- Table_R 계열은 시계열 길이가 한 분기 짧음에 주의.

## 산출 파일

- 기계 판독: `db/data/_inventory/08_time_period_formats.csv` (헤더 + 20행, 9 컬럼: sheet, formats_detected, annual_first/last, quarter_first/last, annual_rows, quarter_rows, other_samples).
- 사람 검토: 본 문서.
