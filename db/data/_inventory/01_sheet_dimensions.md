# Phase 1.1 — 시트 목록과 행·열 수 인벤토리

본 문서는 PLAN.md Phase 1.1 첫 항목("시트 목록과 각 시트의 행·열 수를 추출")의 산출물이다. `db/source/balanceofpayments2025q4.xlsx`에서 직접 추출한 시트 20개의 dimension을 기록한다.

## 시트 dimension 표

| 시트 | 행 수 | 열 수 | 분류(12회차 매핑) |
|---|---:|---:|---|
| Cover_sheet | 30 | 19 | 메타·주석 |
| Notes | 51 | 8 | 메타·주석 |
| Records | 35 | 5 | 메타·주석 |
| Table_A | 451 | 19 | 잔액 요약 |
| Table_B | 600 | 12 | 경상수지 본표 |
| Table_BX | 600 | 12 | 경상수지 본표(귀금속 제외) |
| Table_C | 898 | 20 | 경상수지 본표(EU/non-EU 분해) |
| Table_D1_3 | 451 | 13 | IIP·금융계정 종합 |
| Table_D4_6 | 451 | 11 | IIP·금융계정 종합 |
| Table_D7_9 | 451 | 13 | IIP·금융계정 종합 |
| Table_E | 451 | 9 | 경상수지 세부(상품무역) |
| Table_F | 451 | 13 | 경상수지 세부(서비스무역) |
| Table_G | 451 | 11 | 경상수지 세부(1차소득) |
| Table_H | 451 | 14 | 경상수지 세부(2차소득) |
| Table_I | 451 | 14 | 자본·금융계정(자본) |
| Table_J | 451 | 14 | 자본·금융계정(금융) |
| Table_K | 451 | 11 | IIP |
| Table_R1 | 445 | 13 | 직전 발표 대비 개정 |
| Table_R2 | 592 | 13 | 직전 발표 대비 개정 |
| Table_R3 | 1327 | 7 | 직전 발표 대비 개정 |

## 핵심 관찰

- **시트 20개 / 분류 7개**(메타 3·요약 1·CA 본표 3·CA 세부 4·자본·금융 2·IIP 4·개정 3) — `background/note/12_xlsx_sheet_inventory.md` 매핑과 일관.
- 본표(시계열) 17개의 행 수가 대부분 451 — 1997~2025 분기·연간 시계열 + 메타 8행 구조에서 기인.
- Table_C(898행), Table_B/BX(각 600행), Table_R3(1327행)은 부표가 여럿이라 행 수 큼.
- 행 수가 가장 많은 Table_R3(1327행)은 9 부표 적층 구조(12회차 발견).

## 12회차 결과와의 정합성

본 추출은 `background/note/12_xlsx_sheet_inventory.csv`의 `rows`·`cols` 컬럼과 100% 일치. 12회차는 background 영역에 보관되어 있고, 본 산출물은 PLAN.md Phase 1 산출물 위치(`db/data/_inventory/`)에 별도 정식 사본으로 보관한다.

## 산출 파일

- 기계 판독: `db/data/_inventory/01_sheet_dimensions.csv` (헤더 + 20행, 3 컬럼)
- 사람 검토: `db/data/_inventory/01_sheet_dimensions.md` (본 문서)

## 추출 절차

원본 무수정. `openpyxl.load_workbook(read_only=True, data_only=True)`로 열고 `iter_rows`로 순회하여 행·열 수 집계.
