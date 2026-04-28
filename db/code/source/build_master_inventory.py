"""Phase 1.3 §1.3.1 마스터 인벤토리 생성 스크립트.

목적
----
Phase 1.1에서 산출한 8개 인벤토리 CSV(01·02·05·07·08·09·11·12)를 (sheet) 키로
LEFT JOIN해 시트당 1행의 마스터 인벤토리 표를 생성한다. Phase 2(시트 단위
가로형 CSV 분리)의 1차 입력 사양으로 그대로 사용 가능하도록 컬럼을 재정렬한다.

산출
----
- 기계 판독: db/data/_inventory/15_master_inventory.csv (헤더 + 20행, 22 컬럼)
- 사람 검토: 별도 .md 문서로 동시 기록(스크립트 외부에서 작성)

설계 의도
----------
시트 1개 = 마스터 표 1행. 부표 단위가 아닌 시트 단위로 압축한다(부표 단위
정밀 정보는 13/15 등 background 노트에서 별도 보존). Phase 2.1 ETL은 본 표를
읽어 시트별 분류·CDID 행·부표 경계·단위·결측 위치를 한 번에 lookup 가능.

원본 보존
----------
입력은 모두 기존 인벤토리 CSV이며 db/source/* 원본은 직접 읽지 않는다.
값 가공·치환 없음 — 단순 join + 컬럼 재정렬.

재현
----
env/Scripts/python.exe db/code/source/build_master_inventory.py
"""
from __future__ import annotations

import csv
from pathlib import Path
from collections import defaultdict

# 저장소 루트 = 본 스크립트 기준 3단계 위.
ROOT = Path(__file__).resolve().parents[3]
INV = ROOT / "db" / "data" / "_inventory"

# 입력 인벤토리 CSV 경로 모음.
SRC_DIM = INV / "01_sheet_dimensions.csv"
SRC_CLS = INV / "02_sheet_classification.csv"
SRC_CDID = INV / "07_cdid_and_first_data_rows.csv"
SRC_TIME = INV / "08_time_period_formats.csv"
SRC_UNIT = INV / "09_units.csv"
SRC_BOUND = INV / "11_subtable_boundaries.csv"
SRC_MISS = INV / "12_missing_markers.csv"

OUT_CSV = INV / "15_master_inventory.csv"


def load_csv_by_sheet(path: Path) -> dict[str, dict[str, str]]:
    """sheet 컬럼을 키로 하는 dict 형태 CSV 로드(시트당 단일 행 가정)."""
    out: dict[str, dict[str, str]] = {}
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            out[row["sheet"]] = row
    return out


def aggregate_missing(path: Path) -> dict[str, dict[str, str]]:
    """결측 인벤토리(시트당 N행)를 시트당 1행으로 집계.

    - markers: 등장 마커 종류 세미콜론 구분(예: "x")
    - missing_total: 누적 셀 수
    - missing_subtables: 결측이 등장한 부표 번호 세미콜론 구분
    """
    counter: dict[str, dict[str, object]] = defaultdict(
        lambda: {"markers": set(), "total": 0, "subs": set()}
    )
    if not path.exists():
        return {}
    with path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sn = row["sheet"]
            counter[sn]["markers"].add(row["marker"])
            counter[sn]["total"] += int(row["count"])
            counter[sn]["subs"].add(row["sub_table"])
    out: dict[str, dict[str, str]] = {}
    for sn, info in counter.items():
        out[sn] = {
            "missing_markers": ";".join(sorted(info["markers"])),
            "missing_total": str(info["total"]),
            "missing_subtables": ";".join(sorted(info["subs"], key=int)),
        }
    return out


def main() -> None:
    """마스터 인벤토리 CSV 생성.

    절차
    -----
    1) 8개 입력 인벤토리 CSV(01·02·05·07·08·09·11·12) 중 단순 join 대상인
       6개(01·02·07·08·09·11)를 (sheet) 키로 dict 로드한다.
    2) 결측 인벤토리(12)는 시트당 다중 행(부표 단위) 구조이므로 별도
       집계 함수로 시트당 1행으로 압축한다.
    3) Phase 2.1 ETL 가독성을 우선해 22개 컬럼을 재정렬한 뒤
       LEFT JOIN(좌측=01의 시트 순서) 결과를 CSV로 기록한다.

    값 가공·치환·계산은 일절 수행하지 않으며, 결측 인벤토리에 행이 없는
    시트(메타·결측 0인 시트)에 한해 missing_total 컬럼을 빈 문자열이 아닌
    "0"으로 명시 표기한다(원본 의미 보존: "결측 셀이 0건"). 이 표기는
    원본 데이터 셀 값을 바꾸는 것이 아니라 인벤토리 차원에서의 카운트 결과다.
    """
    dim = load_csv_by_sheet(SRC_DIM)
    cls = load_csv_by_sheet(SRC_CLS)
    cdid = load_csv_by_sheet(SRC_CDID)
    tfmt = load_csv_by_sheet(SRC_TIME)
    unit = load_csv_by_sheet(SRC_UNIT)
    bound = load_csv_by_sheet(SRC_BOUND)
    miss = aggregate_missing(SRC_MISS)

    # 시트 순서는 01_sheet_dimensions.csv 순서를 그대로 따름(원본 xlsx 시트 순서).
    sheets = list(dim.keys())

    # 출력 컬럼 순서 — Phase 2.1 ETL이 가장 자주 lookup하는 순서로 배치.
    fields = [
        "sheet",
        "classification_ko",
        "classification_code",
        "table_code",
        "n_rows",
        "n_cols",
        "first_cdid_row",
        "first_data_row",
        "all_cdid_rows",
        "n_subtables",
        "blank_row_positions",
        "time_format",
        "annual_first",
        "annual_last",
        "quarter_first",
        "quarter_last",
        "unit_normalized",
        "scale_factor",
        "subtable_split_required",
        "missing_markers",
        "missing_total",
        "missing_subtables",
    ]

    INV.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for sn in sheets:
            d = dim.get(sn, {})
            c = cls.get(sn, {})
            cd = cdid.get(sn, {})
            tf = tfmt.get(sn, {})
            u = unit.get(sn, {})
            b = bound.get(sn, {})
            m = miss.get(sn, {})
            row = {
                "sheet": sn,
                "classification_ko": c.get("classification_ko", ""),
                "classification_code": c.get("classification_code", ""),
                "table_code": c.get("table_code", ""),
                "n_rows": d.get("n_rows", ""),
                "n_cols": d.get("n_cols", ""),
                "first_cdid_row": cd.get("first_cdid_row", ""),
                "first_data_row": cd.get("first_data_row", ""),
                "all_cdid_rows": cd.get("all_cdid_rows", ""),
                "n_subtables": cd.get("n_subtables", ""),
                "blank_row_positions": b.get("blank_row_positions", ""),
                # 시점 포맷은 한 줄 압축 표현(대표 라벨)만 보존.
                "time_format": tf.get("formats_detected", ""),
                "annual_first": tf.get("annual_first", ""),
                "annual_last": tf.get("annual_last", ""),
                "quarter_first": tf.get("quarter_first", ""),
                "quarter_last": tf.get("quarter_last", ""),
                "unit_normalized": u.get("unit_normalized", ""),
                "scale_factor": u.get("scale_factor", ""),
                "subtable_split_required": u.get("subtable_split_required", ""),
                # 결측은 결측 인벤토리에 행이 없으면 0/빈 처리(메타·padding-only 시트).
                "missing_markers": m.get("missing_markers", ""),
                "missing_total": m.get("missing_total", "0"),
                "missing_subtables": m.get("missing_subtables", ""),
            }
            w.writerow(row)
    print(f"OK rows={len(sheets)} cols={len(fields)} -> {OUT_CSV.name}")


if __name__ == "__main__":
    main()
