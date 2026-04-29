"""
Phase 5.1 §1·§2·§3 — RDB 적재 무결성 + 헤드라인 5건 + 무작위 표본 검증 ETL.

build_ecos_db.py로 적재된 sqlite3 DB에서 다음 3 단계를 자동 검증한다.

§1. 원본 셀 수 ↔ observation 행 수 일치
§2. 무작위 표본 10건의 RAW_CELL ↔ long-form CSV 직접 대조
§3. 헤드라인 5건 RDB 조회 일치 검증 (db/REPORT.md §2)
   - 상품무역 (BOKI 또는 LQCT) ≈ −£65.5bn @ 2025Q4
   - 서비스무역 (IKBD)           ≈ +£53.3bn @ 2025Q4
   - 경상수지 (HBOP)             ≈ −£18.4bn @ 2025Q4
   - CA/GDP (Table_B_sub4)       ≈ −2.4% @ 2025Q4
   - 순대외자산 Net IIP (HBQC)   ≈ −£199.8bn @ 2025Q4

원칙
- 표준 라이브러리(sqlite3·csv·random)만 사용.
- 데이터 값 불변: 검증 ETL은 DB·CSV 읽기만 수행, 어떤 값도 수정하지 않음.
- 결과는 stdout 출력 + 종료 코드(0=통과, 1=실패).

실행
    env/Scripts/python.exe db/code/source/verify_phase5.py
"""
from __future__ import annotations

import csv
import random
import sqlite3
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

DB_DIR = Path(__file__).resolve().parents[2]
DB_FILE = DB_DIR / "data" / "_db" / "ecos_uk_bop.sqlite"
LONG_CSV = DB_DIR / "data" / "balanceofpayments2025q4_long.csv"

# 헤드라인 5건의 기대 정량(단위: GBP m·% of GDP, 시점 2025Q4)
# REPORT.md §2 분석 결과 기준
HEADLINES = [
    {
        "name": "상품수지 (BOKI)",
        "cdid": "BOKI",
        "stat_code_filter": "UK_BoP_Table_E_sub3",
        "time": "2025Q4",
        "expected_value": -65496,  # GBP million ≈ −£65.5bn
        "tolerance_pct": 1.0,  # 1% 오차 허용
        "unit": "GBP million",
    },
    {
        "name": "서비스수지 (IKBD)",
        "cdid": "IKBD",
        "stat_code_filter": "UK_BoP_Table_F_sub3",
        "time": "2025Q4",
        "expected_value": 53335,  # +£53.3bn
        "tolerance_pct": 1.0,
        "unit": "GBP million",
    },
    {
        "name": "경상수지 (HBOP)",
        "cdid": "HBOP",
        "stat_code_filter": "UK_BoP_Table_A_sub1",
        "time": "2025Q4",
        "expected_value": -18392,  # ≈ −£18.4bn
        "tolerance_pct": 1.0,
        "unit": "GBP million",
    },
    {
        "name": "경상수지/GDP %",
        # AA6H = Table_B_sub4 "경상수지 합계 % of GDP" 행 (D28L은 본표 합계 −1.6%, AA6H가 전체 CA total −2.4%)
        "cdid": "AA6H",
        "stat_code_filter": "UK_BoP_Table_B_sub4",
        "time": "2025Q4",
        "expected_value": -2.4,
        "tolerance_pct": 5.0,  # %GDP는 소수점 절단으로 5% 허용
        "unit": "% of GDP",
    },
    {
        "name": "순대외자산 Net IIP (HBQC)",
        "cdid": "HBQC",
        "stat_code_filter": "UK_BoP_Table_K_sub3",
        "time": "2025Q4",
        "expected_value": -199.8,  # GBP billion
        "tolerance_pct": 1.0,
        "unit": "GBP billion",
    },
]


def verify_cell_count(conn: sqlite3.Connection) -> tuple[bool, str]:
    """§1: 원본 long-form CSV 셀 수 ↔ observation 행 수 일치 검증."""
    with LONG_CSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        long_count = sum(1 for _ in reader)
    obs_count = conn.execute("SELECT COUNT(*) FROM observation").fetchone()[0]
    ok = long_count == obs_count
    msg = f"long-form CSV {long_count}행 ↔ observation {obs_count}행 → {'PASS' if ok else 'FAIL'}"
    return ok, msg


def verify_random_sample(conn: sqlite3.Connection, n: int = 10) -> tuple[bool, list[str]]:
    """§2: 무작위 표본 n건의 RAW_CELL ↔ long-form CSV 직접 대조."""
    rng = random.Random(42)  # 재현성 위해 시드 고정
    # long-form CSV에서 데이터 행 인덱스 무작위 추출
    with LONG_CSV.open("r", encoding="utf-8", newline="") as f:
        long_rows = list(csv.DictReader(f))
    sample_indices = rng.sample(range(len(long_rows)), n)
    messages = []
    all_ok = True
    for idx in sample_indices:
        long_row = long_rows[idx]
        # long-form CSV에는 일부 행이 'UK_BoP_<sheet>' 형태로 저장되어 있고,
        # RDB stat_item_meta.STAT_CODE는 'UK_BoP_Table_<sheet>'로 정규화되어 있어
        # 조회 키를 맞춰주기 위한 접두사 보정 (값은 변경하지 않음).
        stat_code_long = long_row["stat_code"]
        if stat_code_long.startswith("UK_BoP_") and not stat_code_long.startswith("UK_BoP_Table_"):
            rest = stat_code_long[len("UK_BoP_"):]
            stat_code_norm = f"UK_BoP_Table_{rest}"
        else:
            stat_code_norm = stat_code_long
        cdid = long_row["item_code1"]
        time = long_row["time"]
        long_raw = long_row["raw_cell"]
        # DB 조회
        cursor = conn.execute(
            """SELECT o.RAW_CELL FROM observation o
               JOIN stat_item_meta m ON o.item_id = m.item_id
               WHERE m.STAT_CODE = ? AND m.ITEM_CODE1 = ? AND o.TIME = ?""",
            (stat_code_norm, cdid, time),
        )
        result = cursor.fetchone()
        if result is None:
            messages.append(f"  [{idx}] {stat_code_norm}/{cdid}@{time}: DB 행 없음 — FAIL")
            all_ok = False
        elif result[0] != long_raw:
            messages.append(
                f"  [{idx}] {stat_code_norm}/{cdid}@{time}: long='{long_raw}' DB='{result[0]}' — FAIL"
            )
            all_ok = False
        else:
            messages.append(
                f"  [{idx}] {stat_code_norm}/{cdid}@{time}: '{long_raw}' = '{result[0]}' — PASS"
            )
    return all_ok, messages


def verify_headlines(conn: sqlite3.Connection) -> tuple[bool, list[str]]:
    """§3: 헤드라인 5건 RDB 조회 일치 검증."""
    messages = []
    all_ok = True
    for h in HEADLINES:
        if h["cdid"]:
            cursor = conn.execute(
                """SELECT o.DATA_VALUE, o.RAW_CELL FROM observation o
                   JOIN stat_item_meta m ON o.item_id = m.item_id
                   WHERE m.STAT_CODE = ? AND m.ITEM_CODE1 = ? AND o.TIME = ?""",
                (h["stat_code_filter"], h["cdid"], h["time"]),
            )
        else:
            # %GDP 등 CDID 미지정 — STAT_CODE + TIME으로 조회 (Balance 행만)
            cursor = conn.execute(
                """SELECT o.DATA_VALUE, o.RAW_CELL FROM observation o
                   JOIN stat_item_meta m ON o.item_id = m.item_id
                   WHERE m.STAT_CODE = ? AND o.TIME = ?
                     AND m.ITEM_CODE3 LIKE '%CA.TOT%'""",
                (h["stat_code_filter"], h["time"]),
            )
        result = cursor.fetchone()
        if result is None:
            messages.append(f"  {h['name']}: DB 조회 실패 (STAT_CODE={h['stat_code_filter']}, TIME={h['time']}) — FAIL")
            all_ok = False
            continue
        actual_value = result[0]
        if actual_value is None:
            messages.append(f"  {h['name']}: DATA_VALUE NULL (raw='{result[1]}') — FAIL")
            all_ok = False
            continue
        diff = abs(actual_value - h["expected_value"])
        rel = abs(diff / h["expected_value"]) * 100 if h["expected_value"] != 0 else 0
        ok = rel <= h["tolerance_pct"]
        status = "PASS" if ok else "FAIL"
        messages.append(
            f"  {h['name']}: 기대 {h['expected_value']:>12,.2f} {h['unit']:14s} / "
            f"실측 {actual_value:>12,.2f} / 차이 {diff:>10,.2f} ({rel:.2f}%) — {status}"
        )
        if not ok:
            all_ok = False
    return all_ok, messages


def main() -> None:
    print("Phase 5.1 §1·§2·§3 — RDB 무결성 + 헤드라인 + 무작위 표본 검증")
    print("=" * 60)
    if not DB_FILE.exists():
        print(f"[error] DB 파일 없음: {DB_FILE}")
        sys.exit(1)

    conn = sqlite3.connect(DB_FILE)
    overall_ok = True
    try:
        # §1
        print("[§1] 원본 셀 수 ↔ observation 행 수 일치")
        ok1, msg1 = verify_cell_count(conn)
        print(f"  {msg1}")
        overall_ok = overall_ok and ok1

        # §2
        print(f"\n[§2] 무작위 표본 10건 RAW_CELL ↔ long-form CSV 직접 대조 (seed=42)")
        ok2, msgs2 = verify_random_sample(conn, n=10)
        for m in msgs2:
            print(m)
        overall_ok = overall_ok and ok2

        # §3
        print(f"\n[§3] 헤드라인 5건 RDB 조회 일치 검증 (REPORT.md §2 기준)")
        ok3, msgs3 = verify_headlines(conn)
        for m in msgs3:
            print(m)
        overall_ok = overall_ok and ok3
    finally:
        conn.close()

    print("=" * 60)
    print(f"종합 결과: {'PASS — 모든 검증 통과' if overall_ok else 'FAIL — 일부 검증 실패'}")
    sys.exit(0 if overall_ok else 1)


if __name__ == "__main__":
    main()
