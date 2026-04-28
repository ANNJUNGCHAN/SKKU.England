# Phase 1.3 — Phase 2 입력 사양 사용 가능 평가

본 문서는 `db/CHECKLIST.md` §1.3 세 번째 항목("Phase 2 입력 사양으로 그대로 사용 가능한 상태") 산출물이다. Phase 1.1·1.2·1.3.1·1.3.2 산출물이 Phase 2(시트 단위 가로형 CSV 분리 + 세로형 통합 CSV)의 입력 사양을 충분히 충족하는지 단정적으로 평가한다.

## 1. 요지

- **Phase 2 진입 가능**. Phase 1 산출물 17건(인벤토리 13 + 검증 보고서 4)은 Phase 2.1 ETL이 시트·부표·CDID·시점·단위·결측 정책을 한 번에 lookup 가능한 상태로 정리되었다.
- 핵심 입력 1건은 **`15_master_inventory.csv`** (시트당 1행 × 22 컬럼). Phase 2.1의 시트 단위 처리 루프가 본 표 1행을 읽어 부표 분리·단위 정규화·결측 처리 정책을 결정.
- 보조 입력 4건: 부표 단위 단위 사전(`background/note/15_units.csv`), CDID 사전(`background/note/13_cdid_dictionary.csv` 512행), 자산/부채 매핑(`background/note/19_assets_liabilities_mapping.csv`), 결측 셀 위치 정밀(`db/data/_inventory/12_missing_markers.csv`).
- Phase 2 진입 차단 조건 0건. Phase 2.1~2.2에서 자연 통합 가능한 추가 작업 5건(16회차 누락 점검 §6 권고: Table_F EBOPS / Table_J NAFA/NIL / Table_K 거래·재평가 / R1~R3 분리 / 메타 시트 한국어 메모)은 모두 진입을 막지 않는 후속 작업.

## 2. Phase 2 입력 사양 충족 매트릭스

PLAN.md Phase 2.1·2.2가 ETL 시점에 필요로 하는 메타 정보 항목과 Phase 1 산출물의 매핑.

| Phase 2 ETL 입력 요건 | Phase 1 산출 컬럼 | 출처 | 충족 |
|---|---|---|---|
| 시트 목록·차원 | sheet / n_rows / n_cols | 01·15 | ✓ |
| 시트 7분류 | classification_ko / classification_code / table_code | 02·15 | ✓ |
| 부표 분리 — CDID 행 | first_cdid_row / all_cdid_rows | 07·15 | ✓ |
| 부표 분리 — 빈 행 경계 | blank_row_positions | 11·15 | ✓ |
| 부표 수 | n_subtables | 07·15 | ✓ |
| 첫 데이터 행 | first_data_row | 07·15 | ✓ |
| 시점 포맷 (A/Q 매핑) | time_format / annual_first/last / quarter_first/last | 08·15 | ✓ |
| 단위 정규화 | unit_normalized / scale_factor | 09·15 | ✓ |
| 부표 단위 단위 차이(MIXED) | subtable_split_required + 보조 15_units.csv | 09·15 + bg/15 | ✓ |
| 결측 마커 종류·위치 | missing_markers / missing_total / missing_subtables + 보조 12_missing_markers.csv | 12·15 | ✓ |
| 결측 사유 라벨 (적재용) | suggested_meaning + 13회차 검증 | 12·13 | ✓ |
| 부호 규약 (sign_prefix) | 보조 13_cdid_dictionary.csv (sign_prefix 컬럼) | bg/13 | ✓ |
| CDID → 한국어 의미 시드 | (Phase 3에서 작성) | — | ◐ Phase 3 작업 |
| 자산/부채 5분류 매핑 | 보조 19_assets_liabilities_mapping.csv | bg/19 | ✓ |
| 메타 텍스트(부호·단위 진술) | 05_meta_text.csv (120행) + 06_sign_convention_validation.md | 05·06 | ✓ |
| 강의 개념 커버리지 | 16_curriculum_coverage_check.md (47개념 중 91% 커버) | 16 | ✓ |

15개 입력 요건 중 14개 ✓, 1개 ◐(Phase 3 본격 작업). Phase 2 ETL 자체에는 모두 충족.

## 3. Phase 2.1 시트 단위 처리 의사코드 점검

마스터 인벤토리 1행이 시트 처리에 필요한 정보를 모두 담고 있는지 PLAN.md Phase 2.1 의사코드와 대조.

```python
# Phase 2.1 ETL 골격
import csv
from openpyxl import load_workbook
from pathlib import Path

SRC = Path('db/source/balanceofpayments2025q4.xlsx')
INV = Path('db/data/_inventory/15_master_inventory.csv')
OUT_DIR = Path('db/data/')

with INV.open(encoding='utf-8') as f:
    inventory = {row['sheet']: row for row in csv.DictReader(f)}

wb = load_workbook(SRC, read_only=True, data_only=True)

for sn, meta in inventory.items():
    if meta['classification_code'] == 'meta_notes':
        # 메타 시트는 한국어 메모로 별도 처리 (PLAN.md 2.1 §"메타 메모 분리").
        continue

    n_subtables = int(meta['n_subtables'])
    cdid_rows_1based = [int(x) for x in meta['all_cdid_rows'].split(';')]
    blanks_1based = [int(x) for x in meta['blank_row_positions'].split(';')] \
        if meta['blank_row_positions'] else []
    total_rows = int(meta['n_rows'])
    unit = meta['unit_normalized']
    split_required = (meta['subtable_split_required'] == 'yes')

    ws = wb[sn]
    rows = [list(r) for r in ws.iter_rows(values_only=True)]

    for k in range(n_subtables):
        cdid_idx_0based = cdid_rows_1based[k] - 1
        sub_start = cdid_idx_0based + 1
        sub_end = (blanks_1based[k] - 2) if k < len(blanks_1based) else (total_rows - 1)

        # CDID 행 → ITEM_CODE1 컬럼 채움
        cdid_row = rows[cdid_idx_0based]
        item_codes = [v for v in cdid_row[1:] if isinstance(v, str) and v.strip()]

        # 데이터 영역 추출 → 가로형 CSV 1개 생성
        out = OUT_DIR / f"balanceofpayments2025q4_{sn.lower()}_sub{k+1}.csv"
        # ... CSV 작성 ...

wb.close()
```

**점검 결과**: 마스터 인벤토리 1행만으로 부표 단위 데이터 영역(sub_start, sub_end)·ITEM_CODE1 후보·단위·결측 정책을 모두 결정 가능. 추가 lookup이 필요한 영역(부호 prefix, 자산/부채 매핑 등)은 보조 4 자료로 결합. **차단 요소 0건**.

## 4. Phase 2.2 통합 long-form CSV 입력 사양 점검

PLAN.md §2.2의 컬럼 사양(STAT_CODE / 통계표명 / ITEM_CODE1~4 / ITEM_NAME / UNIT_NAME / CYCLE / TIME / 원본 셀 / DATA_VALUE)을 본 인벤토리가 직접 채울 수 있는 컬럼 점검.

| §2.2 컬럼 | Phase 1 산출 직접 사용 | 비고 |
|---|---|---|
| STAT_CODE | table_code (A·B·BX·C·D1.3·D4.6·D7.9·E·F·G·H·I·J·K·R1·R2·R3) | ✓ 그대로 사용 |
| 통계표명(한국어) | classification_ko + 부표 머리글 (05_meta_text.csv) | ✓ 결합 사용 |
| 통계표명(원문) | 05_meta_text.csv (시트별 r1·r6 머리글 행) | ✓ |
| 부표 번호 | n_subtables · k+1 | ✓ |
| ITEM_CODE1 (CDID) | cdid_row의 셀 값 + 13회차 background CDID 사전 | ✓ |
| ITEM_CODE2~4 | (Phase 3 강의자료 매핑 자문 단계에서 생성) | ◐ |
| ITEM_NAME (원문 라벨) | rows[cdid_idx-1] 등 머리글 행 | ✓ |
| UNIT_NAME | unit_normalized + 부표 단위 단위(15_units.csv) | ✓ |
| CYCLE | A (annual_*) / Q (quarter_*)로 직접 매핑 | ✓ |
| TIME | YYYY (annual rows) / YYYYQn (quarter rows) | ✓ |
| 원본 셀 | rows[ri][ci] 그대로 보존 | ✓ |
| DATA_VALUE | 숫자만 파싱, 결측은 빈 값 (12회차 결측 정책) | ✓ |

12개 컬럼 중 11개 ✓, 1개 ◐(Phase 3 본격 작업). Phase 2.2도 자체는 진입 가능.

## 5. 잔여 위험·후속 권고

Phase 2 진입을 차단하지 않지만, Phase 2.1~2.2에서 자연 처리해야 할 5건(16회차 §6 권고 요약).

| 항목 | 위치 | Phase 2 대응 |
|---|---|---|
| Table_F EBOPS 12분류 부표 분리 | 시트 내 부표 3개 + CDID 12계열 | Phase 2.1 부표 분리 + Phase 2.2 ITEM_CODE2 채움 |
| Table_J NAFA/NIL 양면 컬럼 분해 | 시트 내 부표 3개 (자산·부채·순) | Phase 2.1 부표 분리 자연 처리 |
| Table_K 거래·재평가 분해 (연간 Pink Book Dataset 8 보강) | 본 Bulletin 범위 외 — 별도 자료 | Phase 5 확장 단계 |
| Table_R1·R2·R3 학생용 분석 분리 | classification_code='revisions' | Phase 4 ECOS 분야 분류로 별도 섹션 |
| 메타 시트 한국어 메모 (Cover_sheet·Notes·Records) | classification_code='meta_notes' | Phase 2.1 한국어 메모 별도 작성 |

위 5건은 모두 Phase 2 진입 후 ETL이 자연스럽게 다룰 영역으로, **Phase 1 종료 조건 충족을 막지 않는다**.

## 6. 종합 평가

| §1.3 종료 조건 항목 | 충족 | 근거 |
|---|---|---|
| §1.3.1 모든 시트의 분류·헤더·코드·시점·단위·부표 경계·결측 표기가 한 표로 정리됨 | ✓ | 15_master_inventory.{csv,md} 22 컬럼 × 20행 |
| §1.3.2 강의 자료 BoP 개념 누락 점검 | ✓ | 16_curriculum_coverage_check.md (강의 개념 47건 중 91% 커버) |
| §1.3.3 Phase 2 입력 사양으로 그대로 사용 가능한 상태 | ✓ | 본 문서 §2~§4 매트릭스 전수 충족 |

**Phase 1 종료 조건 3개 항목 모두 충족**. Phase 2 진입 승인.

## 7. 산출 파일 (Phase 1 최종)

| 회차 | 파일 | 역할 |
|---|---|---|
| 01 | `01_sheet_dimensions.{csv,md}` | 시트별 차원 |
| 02 | `02_sheet_classification.{csv,md}` | 7분류 |
| 03 | `03_classification_validation.md` | 강의 자료 분류 검증 |
| 04 | `04_eu_non_eu_validation.md` | EU/non-EU 의미 검증 |
| 05 | `05_meta_text.{csv,json,md}` | 메타 텍스트 |
| 06 | `06_sign_convention_validation.md` | 부호 규약 검증 |
| 07 | `07_cdid_and_first_data_rows.{csv,md}` | CDID 행 |
| 08 | `08_time_period_formats.{csv,md}` | 시점 포맷 |
| 09 | `09_units.{csv,md}` | 단위 |
| 10 | `10_gdp_ratio_validation.md` | GDP 비율 검증 |
| 11 | `11_subtable_boundaries.{csv,md}` | 부표 경계 |
| 12 | `12_missing_markers.{csv,md}` | 결측 표기 |
| 13 | `13_missing_meaning_validation.md` | 결측 의미 검증 |
| 14 | `14_format_compliance_check.md` | 형식 점검 |
| 15 | `15_master_inventory.{csv,md}` | **Phase 2 진입 마스터 표** |
| 16 | `16_curriculum_coverage_check.md` | 강의 개념 누락 점검 |
| 17 | `17_phase2_readiness.md` | **본 문서 — Phase 2 진입 평가** |

스크립트 (재현용): `db/code/source/{inspect_bop,extract_latest,extract_cdid,extract_units_missing,extract_missing_markers,build_master_inventory}.py` (6개).

## 8. 다음 단계

Phase 2.1 (시트 단위 가로형 CSV 분리) 진입. 처리 단위 = 마스터 인벤토리 1행. 출력 = `db/data/balanceofpayments2025q4_<시트명>_sub<번호>.csv` 패턴(20시트 × 평균 3.4 부표 ≈ 60~70개 CSV) + 시트별 한국어 메타 메모.
