# Phase 1.2 — 인벤토리 산출물 형식 점검

본 문서는 `db/CHECKLIST.md` §1.2의 4개 점검 항목 자가 점검 결과이다. Phase 1.1 산출물 13건 + JSON 보조 1건이 다음 4개 원칙을 모두 충족하는지 확인한다.

1. 인벤토리 결과를 기계 판독용 형식(CSV)으로 저장
2. 동일 내용을 사람 검토용 형식(텍스트 또는 마크다운)으로도 저장
3. 인벤토리 산출물도 1 CSV = 1 평면 표 원칙 준수
4. 엑셀 다중 시트 형식으로 저장하지 않음

## 1. 산출물 카탈로그

| 회차 | 항목 | CSV (기계 판독) | MD (사람 검토) | 비고 |
|---|---|---|---|---|
| 01 | 시트별 차원 (행·열 수) | 01_sheet_dimensions.csv | 01_sheet_dimensions.md | — |
| 02 | 7분류 매핑 | 02_sheet_classification.csv | 02_sheet_classification.md | — |
| 03 | 강의 자료 분류 검증 | (검증 보고서) | 03_classification_validation.md | 검증 보고서 (CSV 적재 대상 외) |
| 04 | EU/non-EU 의미 검증 | (검증 보고서) | 04_eu_non_eu_validation.md | 검증 보고서 (CSV 적재 대상 외) |
| 05 | 메타 텍스트 추출 | 05_meta_text.csv (120행) | 05_meta_text.md | 보조: 05_meta_text.json (시트→문자열 배열 매핑, JSON) |
| 06 | 부호 규약 검증 | (검증 보고서) | 06_sign_convention_validation.md | 검증 보고서 (CSV 적재 대상 외) |
| 07 | CDID 행·첫 데이터 행 | 07_cdid_and_first_data_rows.csv | 07_cdid_and_first_data_rows.md | — |
| 08 | 시점 컬럼 형식 | 08_time_period_formats.csv | 08_time_period_formats.md | — |
| 09 | 시트별 단위 | 09_units.csv | 09_units.md | — |
| 10 | GDP 비율 표기 검증 | (검증 보고서) | 10_gdp_ratio_validation.md | 검증 보고서 (CSV 적재 대상 외) |
| 11 | 부표 경계 행 | 11_subtable_boundaries.csv | 11_subtable_boundaries.md | — |
| 12 | 결측 표기 인벤토리 | 12_missing_markers.csv (6행) | 12_missing_markers.md | — |
| 13 | 결측 표기 의미 검증 | (검증 보고서) | 13_missing_meaning_validation.md | 검증 보고서 (CSV 적재 대상 외) |

CSV: 8건 (데이터 추출 항목 모두 정형). MD: 13건(CSV가 있는 것 + 검증 보고서 단독). JSON: 1건(보조). XLSX: 0건.

## 2. 점검 결과

### 2.1 기계 판독용 형식 (CSV) — ✓ 충족

데이터 추출이 본질인 항목 8건(01, 02, 05, 07, 08, 09, 11, 12) 모두 CSV로 저장. 검증 보고서 5건(03, 04, 06, 10, 13)은 본질이 인용·해석·자문이므로 CSV 적재 대상이 아님(PLAN.md "1 CSV = 1 평면 표"는 데이터 추출 결과에 한정).

### 2.2 사람 검토용 형식 (마크다운) — ✓ 충족

13건 모두 `.md` 동반. CSV+MD 페어 8건, MD 단독 5건. 사람 검토용 본문은 모두 한국어(루트 CLAUDE.md "사용자 대상 문서는 한국어").

### 2.3 1 CSV = 1 평면 표 원칙 — ✓ 충족

8개 CSV 모두 단일 헤더 1행과 그 이하 모든 데이터 행에서 컬럼 수가 일치한다. 검증은 `python -c "import csv; ..."`로 모든 행에 대해 `len(row) == len(header)`가 성립하는지 확인했다(절차는 §4 재현 스니펫 참조).

| 파일 | 헤더 컬럼 수 | 데이터 행 수 | 평면 일관성 |
|---|---:|---:|---|
| 01_sheet_dimensions.csv | 3 | 20 | ✓ |
| 02_sheet_classification.csv | 4 | 20 | ✓ |
| 05_meta_text.csv | 3 | 120 | ✓ |
| 07_cdid_and_first_data_rows.csv | 7 | 20 | ✓ |
| 08_time_period_formats.csv | 9 | 20 | ✓ |
| 09_units.csv | 5 | 20 | ✓ |
| 11_subtable_boundaries.csv | 4 | 20 | ✓ |
| 12_missing_markers.csv | 7 | 6 | ✓ |

다중 헤더·셀 병합·분기·중첩 표 0건. 모든 CSV는 RFC 4180 호환 단일 평면 표.

### 2.4 엑셀 다중 시트 형식 미사용 — ✓ 충족

`db/data/_inventory/` 내 `.xlsx` 또는 `.xls` 산출물 0건(`ls`로 확인). 모든 산출물은 `.csv` / `.md` / `.json`.

JSON 보조 파일(`05_meta_text.json`)은 다중 시트 엑셀이 아니라, 시트→문자열 배열 매핑(키-값 구조) 보조 자료로서 (a) 동일 내용의 평면 CSV(`05_meta_text.csv` 120행)가 별도 존재하고 (b) 사람이 시트 단위로 메타 텍스트를 빠르게 훑어볼 수 있도록 보존한 부록이다. PLAN.md "1 CSV = 1 평면 표" 원칙은 CSV에만 적용되며, JSON 부록 1건은 평면 CSV의 대체물이 아니라 보조이므로 점검 위반 없음.

## 3. 종합 판정

| §1.2 점검 항목 | 충족 여부 | 근거 |
|---|---|---|
| §1.2.1 CSV 저장 | ✓ | 데이터 추출 8건 모두 CSV |
| §1.2.2 MD 저장 | ✓ | 13건 모두 MD 동반 |
| §1.2.3 1 CSV = 1 평면 표 | ✓ | 8 CSV 평면성 검증 통과 |
| §1.2.4 엑셀 다중 시트 미사용 | ✓ | xlsx 산출물 0건 |

§1.2 4개 점검 항목 **모두 충족**. Phase 1.3 종료 조건 점검 단계로 진입 가능.

## 4. 점검 절차 (재현 가능)

```bash
env/Scripts/python.exe -c "
import csv
from pathlib import Path
inv_dir = Path('db/data/_inventory')
for f in sorted(inv_dir.glob('*.csv')):
    with f.open(encoding='utf-8') as fh:
        reader = csv.reader(fh)
        header = next(reader)
        rows = list(reader)
    consistent = all(len(r) == len(header) for r in rows)
    print(f.name, len(header), len(rows), 'OK' if consistent else 'FAIL')
"
```

```bash
ls db/data/_inventory/*.xlsx 2>/dev/null | wc -l   # 0이어야 함
```

## 5. Phase 1.3 입력 사양 평가

본 형식 점검을 통해 13건 산출물이 §1.3 종료 조건의 "Phase 2 입력 사양으로 그대로 사용 가능한 상태"를 충족하기 위한 형식 요건은 모두 갖췄음을 확인. 내용 측면(시트 분류·헤더·코드·시점·단위·부표 경계·결측 표기 모두 한 표로 정리됨)은 §1.3에서 별도 점검.
