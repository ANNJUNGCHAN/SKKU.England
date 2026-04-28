# Phase 1.3 — 마스터 인벤토리 (시트당 1행)

본 문서는 `db/CHECKLIST.md` §1.3 첫 번째 항목("모든 시트의 분류·헤더·코드·시점·단위·부표 경계·결측 표기가 한 표로 정리됨") 산출물이다. Phase 1.1의 8개 인벤토리 CSV(01·02·05·07·08·09·11·12)를 (sheet) 키로 LEFT JOIN해 시트당 1행의 마스터 표를 생성한다.

## 1. 컬럼 사양

22 컬럼 × 20행. 시트 순서는 원본 xlsx 시트 순서를 유지(메타 3 + Table_A~K 14 + Table_R1~R3 3 = 20).

| 컬럼 | 의미 | 출처 인벤토리 |
|---|---|---|
| sheet | 시트명 | 01 |
| classification_ko | 한국어 7분류 | 02 |
| classification_code | 영문 분류 코드 | 02 |
| table_code | ONS 표 코드(A·B·BX·C·D1.3 등) | 02 |
| n_rows / n_cols | 시트 차원 | 01 |
| first_cdid_row / first_data_row | 첫 부표의 CDID 행·첫 데이터 행 | 07 |
| all_cdid_rows | 전체 부표의 CDID 행 위치(세미콜론) | 07 |
| n_subtables | 부표 수 | 07 |
| blank_row_positions | 부표 경계 빈 행 위치(세미콜론) | 11 |
| time_format | 시점 포맷 압축 표현 | 08 |
| annual_first / annual_last | 연간 시작·끝 | 08 |
| quarter_first / quarter_last | 분기 시작·끝 | 08 |
| unit_normalized | 단위 정규화 라벨 | 09 |
| scale_factor | 단위 환산 배수 | 09 |
| subtable_split_required | 부표 단위 분리 필요 여부(MIXED 시트) | 09 |
| missing_markers | 결측 마커 종류(세미콜론) | 12 |
| missing_total | 결측 셀 총합 | 12 |
| missing_subtables | 결측이 등장한 부표 번호(세미콜론) | 12 |

## 2. 시트별 핵심 요약 (사람 검토용)

| 시트 | 분류 | 부표 수 | 단위 | 결측 |
|---|---|---:|---|---:|
| Cover_sheet | 메타·주석 | 0 | — | 0 |
| Notes | 메타·주석 | 0 | — | 0 |
| Records | 메타·주석 | 0 | GBP_billion | 0 |
| Table_A | 전체 잔액 요약 | 3 | GBP_million | 0 |
| Table_B | 경상수지 본표 | 4 | MIXED (£m + %GDP) | 0 |
| Table_BX | 경상수지 본표 | 4 | MIXED (£m + %GDP) | 0 |
| Table_C | 경상수지 본표 | 6 | GBP_million | **360 (`x`)** |
| Table_D1_3 | 국제투자대조표 | 3 | GBP_billion | 0 |
| Table_D4_6 | 국제투자대조표 | 3 | GBP_billion | 0 |
| Table_D7_9 | 국제투자대조표 | 3 | GBP_billion | 0 |
| Table_E | 경상수지 세부 | 3 | GBP_million | 0 |
| Table_F | 경상수지 세부 | 3 | GBP_million | 0 |
| Table_G | 경상수지 세부 | 3 | GBP_million | 0 |
| Table_H | 경상수지 세부 | 3 | GBP_million | 0 |
| Table_I | 자본·금융계정 | 3 | GBP_million | 0 |
| Table_J | 자본·금융계정 | 3 | GBP_million | 0 |
| Table_K | 국제투자대조표 | 3 | GBP_billion | 0 |
| Table_R1 | 직전 발표 대비 개정 | 3 | GBP_million | 0 |
| Table_R2 | 직전 발표 대비 개정 | 4 | MIXED (£m + %GDP) | 0 |
| Table_R3 | 직전 발표 대비 개정 | 9 | GBP_billion | 0 |

분류 분포: 메타·주석 3 / 전체 잔액 요약 1 / 경상수지 본표 3 / 경상수지 세부 4 / 자본·금융계정 2 / 국제투자대조표 4 / 직전 발표 대비 개정 3 = 20.

## 3. Phase 2.1 ETL 활용 규약

본 마스터 인벤토리 1행이 Phase 2.1 ETL의 시트 단위 처리 단위에 1:1 대응된다.

```python
# Phase 2.1 ETL 의사코드 (예시)
import csv
with open('db/data/_inventory/15_master_inventory.csv', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        if row['classification_code'] == 'meta_notes':
            continue                                  # 메타 시트는 별도 한국어 메모로 처리
        n_subtables = int(row['n_subtables'])
        cdid_rows = [int(x) for x in row['all_cdid_rows'].split(';')]
        blanks = [int(x) for x in row['blank_row_positions'].split(';')] if row['blank_row_positions'] else []
        unit = row['unit_normalized']
        if row['subtable_split_required'] == 'yes':
            unit = 'subtable_specific'                # 부표 단위로 단위 판별
        missing_subtables = set(row['missing_subtables'].split(';')) if row['missing_subtables'] else set()
        for k in range(n_subtables):
            sub_start = cdid_rows[k] + 1              # 데이터 시작 행(1-based)
            sub_end = (blanks[k] - 1) if k < len(blanks) else int(row['n_rows'])
            # 시트·부표·CDID 행·데이터 영역·단위·결측 정책이 본 표 한 행으로 모두 결정.
```

## 4. 종료 조건 §1.3.1 충족 근거

§1.3.1 ("모든 시트의 분류·헤더·코드·시점·단위·부표 경계·결측 표기가 한 표로 정리됨")의 항목별 충족 표:

| §1.3.1 요소 | 마스터 컬럼 | 충족 |
|---|---|---|
| 분류 | classification_ko / classification_code | ✓ |
| 헤더 (CDID 행 위치) | first_cdid_row / all_cdid_rows | ✓ |
| 코드 (ONS 표 코드) | table_code | ✓ |
| 시점 | time_format / annual_first/last / quarter_first/last | ✓ |
| 단위 | unit_normalized / scale_factor / subtable_split_required | ✓ |
| 부표 경계 | n_subtables / blank_row_positions | ✓ |
| 결측 표기 | missing_markers / missing_total / missing_subtables | ✓ |

7개 요소 모두 한 표(15_master_inventory.csv)에 일관 컬럼으로 정리됨.

## 5. CDID 단위 사전(부표 내부 정밀도)

본 마스터 인벤토리는 시트 단위 1행으로 압축한다. 부표·CDID 단위 정밀 정보는 별도 자료에서 보존:

- 부표 단위 단위 정보: `background/note/15_units.csv` (82행)
- CDID 코드 단위 사전: `background/note/13_cdid_dictionary.csv` (512행, 고유 284 CDID, sign_prefix 59건)
- 결측 셀 위치 정밀: `db/data/_inventory/12_missing_markers.csv` (6행, B9~G790)
- 자산/부채 5분류 매핑: `background/note/19_assets_liabilities_mapping.csv` (54행)

Phase 2.2 통합 CSV(세로형 long-form) 적재 시 본 마스터 + 위 보조 4개 자료를 결합 사용.

## 6. 산출 파일

- 기계 판독: `db/data/_inventory/15_master_inventory.csv` (헤더 + 20행, 22 컬럼).
- 사람 검토: 본 문서.
- 생성 스크립트: `db/code/source/build_master_inventory.py` (env/Scripts/python.exe로 재현).
