"""
Phase 4.2 §1·§4·§5·§6·§7 — ECOS 스타일 sqlite3 RDB 적재 + 무결성 점검 ETL.

init_ecos_db.py로 빈 스키마를 적용한 뒤, 4종 메타 CSV + 세로형 통합 CSV +
시드 사전 2종을 sqlite3 DB에 적재하고 무결성 점검 지표를 산출한다.

적재 순서
1. stat_table_meta ← `db/data/_spec/statcatalog.csv` (63 STAT_CODE × 15 컬럼)
2. stat_item_meta  ← `db/data/_spec/specification.csv` (512행 × 16 컬럼)
3. observation     ← `db/data/balanceofpayments2025q4_long.csv` (74,006행 × 14 컬럼)
4. missing_dict    ← `db/data/_spec/missing_dict_seed.csv` (6행)
5. term_dict       ← `db/data/_spec/term_dict_seed.csv` (30행)

원칙
- 외래 키 무결성 보장: 적재 순서가 stat_table → stat_item → observation으로 정렬됨.
- 멱등 동작: init_ecos_db.py가 매 실행마다 빈 DB 생성 → 본 ETL은 idempotent.
- 데이터 값 불변: long-form CSV의 raw_cell·data_value 그대로 observation에 적재.
- specification.csv의 ITEM_NAME_EN을 ITEM_NAME1에, 한국어 명칭을 ITEM_NAME_KR에 매핑.

무결성 점검 지표(§4.2 §7)
- 관측치 수 (long-form CSV 행 수 vs observation 행 수)
- 시리즈 수 (specification.csv 행 수 vs stat_item_meta 행 수)
- 결측 비율 (data_value NULL / 전체 obs)
- 시점 일관성 (stat_item_meta START/END_TIME ↔ observation TIME min/max)

실행
    env/Scripts/python.exe db/code/source/init_ecos_db.py    # 1) 스키마 초기화
    env/Scripts/python.exe db/code/source/build_ecos_db.py   # 2) 적재 + 무결성 점검
"""
from __future__ import annotations

import csv
import sqlite3
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

DB_DIR = Path(__file__).resolve().parents[2]
DB_OUT = DB_DIR / "data" / "_db" / "ecos_uk_bop.sqlite"
SPEC_DIR = DB_DIR / "data" / "_spec"
DATA_DIR = DB_DIR / "data"

STATCATALOG_CSV = SPEC_DIR / "statcatalog.csv"
SPECIFICATION_CSV = SPEC_DIR / "specification.csv"
LONG_CSV = DATA_DIR / "balanceofpayments2025q4_long.csv"
MISSING_SEED_CSV = SPEC_DIR / "missing_dict_seed.csv"
TERM_SEED_CSV = SPEC_DIR / "term_dict_seed.csv"


def load_stat_table_meta(conn: sqlite3.Connection) -> int:
    """statcatalog.csv → stat_table_meta 적재."""
    with STATCATALOG_CSV.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    insert_rows = [
        (
            r["STAT_CODE"], r["STAT_NAME"], r["ENGLISH_NAME"],
            r["FIELD_MAIN"], r["FIELD_SUB"], r["ORG_NAME"],
            r["DATA_SOURCE"], r["CYCLE"], r["START_TIME"], r["END_TIME"],
            r["SOURCE_URL"], r["PUBLISHED_DATE"], r.get("BUILD_TIME", ""),
            r["KOREAN_DESCRIPTION"],
        )
        for r in rows
    ]
    conn.executemany(
        """INSERT INTO stat_table_meta
           (STAT_CODE, STAT_NAME, STAT_NAME_EN, FIELD_MAIN, FIELD_SUB,
            ORG_NAME, DATA_SOURCE, CYCLE, START_TIME, END_TIME,
            SOURCE_URL, PUBLISHED_DATE, BUILD_TIME, KOREAN_DESCRIPTION)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        insert_rows,
    )
    return len(insert_rows)


def load_stat_item_meta(conn: sqlite3.Connection) -> dict[tuple, int]:
    """specification.csv → stat_item_meta 적재.

    Returns:
        (STAT_CODE, ITEM_CODE1, sub_table_idx) → item_id 매핑 사전.
        observation 적재 시 (sheet, sub_table, item_code1) 키로 item_id 조회.
    """
    with SPECIFICATION_CSV.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    # specification.csv는 sub_table 정보가 STAT_CODE 안에 인코딩됨
    # (UK_BoP_Table_J_sub1 패턴). 따라서 (STAT_CODE, ITEM_CODE1)이 PK 역할
    insert_rows = []
    for r in rows:
        insert_rows.append((
            r["STAT_CODE"], r["ITEM_CODE1"], r["ITEM_CODE2"], r["ITEM_CODE3"], r["ITEM_CODE4"],
            r["ITEM_NAME_EN"], "", "", "",  # ITEM_NAME1~4: EN 라벨 1만, 2~4 빈 값
            r["ITEM_NAME_KO"], r["DEFINITION"],
            "",  # P_ITEM_CODE: Phase 4.1 §4 매핑은 후속 단계 위임
            None,  # LVL: 후속 단계 위임
            None,  # WGT: BoP 통상 NULL
            r["UNIT_NAME"], r["CYCLE"], r["START_TIME"], r["END_TIME"],
            r["SIGN_CONVENTION"],
            "",  # STOCK_FLOW_TYPE: 후속 단계 위임
            r["SOURCE"],
        ))

    conn.executemany(
        """INSERT INTO stat_item_meta
           (STAT_CODE, ITEM_CODE1, ITEM_CODE2, ITEM_CODE3, ITEM_CODE4,
            ITEM_NAME1, ITEM_NAME2, ITEM_NAME3, ITEM_NAME4,
            ITEM_NAME_KR, DEFINITION_KR,
            P_ITEM_CODE, LVL, WGT,
            UNIT_NAME, CYCLE, START_TIME, END_TIME,
            SIGN_CONVENTION, STOCK_FLOW_TYPE, SOURCE)
           VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        insert_rows,
    )

    # 적재 후 item_id 조회를 위한 (STAT_CODE, ITEM_CODE1) → item_id 매핑
    cursor = conn.execute(
        "SELECT item_id, STAT_CODE, ITEM_CODE1 FROM stat_item_meta"
    )
    item_id_map: dict[tuple, int] = {}
    for item_id, stat_code, item_code1 in cursor:
        item_id_map[(stat_code, item_code1)] = item_id
    return item_id_map


def load_observation(conn: sqlite3.Connection, item_id_map: dict[tuple, int]) -> tuple[int, int]:
    """long-form CSV → observation 적재.

    long-form CSV는 stat_code가 `UK_BoP_<sheet>_sub<n>` 패턴(Table_ 미포함).
    specification.csv·statcatalog.csv는 `UK_BoP_Table_<sheet>_sub<n>` 패턴(Table_ 포함).
    long-form 키를 specification 표기로 정규화한 뒤 매칭.

    Returns:
        (적재된 행 수, 매칭 실패 행 수)
    """
    inserted = 0
    skipped = 0
    batch: list[tuple] = []
    # BATCH_SIZE: sqlite3.executemany 1회 호출당 묶을 행 수.
    # 74,006행 규모에서 메모리·트랜잭션 비용을 균형 맞추는 경험적 값.
    BATCH_SIZE = 5000
    with LONG_CSV.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            # long-form 키 정규화: UK_BoP_<sheet> → UK_BoP_Table_<sheet>
            stat_code_long = row["stat_code"]
            if stat_code_long.startswith("UK_BoP_") and not stat_code_long.startswith("UK_BoP_Table_"):
                # UK_BoP_A_sub1 → UK_BoP_Table_A_sub1
                rest = stat_code_long[len("UK_BoP_"):]
                stat_code_norm = f"UK_BoP_Table_{rest}"
            else:
                stat_code_norm = stat_code_long
            key = (stat_code_norm, row["item_code1"])
            item_id = item_id_map.get(key)
            if item_id is None:
                skipped += 1
                continue
            # data_value 파싱 (빈 값/실패 시 NULL)
            data_value: float | None = None
            raw_value = row["data_value"].strip()
            if raw_value:
                try:
                    data_value = float(raw_value)
                except ValueError:
                    data_value = None
            batch.append((item_id, row["time"], row["raw_cell"], data_value))
            if len(batch) >= BATCH_SIZE:
                conn.executemany(
                    "INSERT OR IGNORE INTO observation (item_id, TIME, RAW_CELL, DATA_VALUE) VALUES (?,?,?,?)",
                    batch,
                )
                inserted += len(batch)
                batch.clear()
    if batch:
        conn.executemany(
            "INSERT OR IGNORE INTO observation (item_id, TIME, RAW_CELL, DATA_VALUE) VALUES (?,?,?,?)",
            batch,
        )
        inserted += len(batch)
    return inserted, skipped


def load_missing_dict(conn: sqlite3.Connection) -> int:
    """missing_dict_seed.csv → missing_dict 적재."""
    with MISSING_SEED_CSV.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    insert_rows = [
        (r["missing_code"], r["meaning_kr"], r["meaning_en"], r["source"])
        for r in rows
    ]
    conn.executemany(
        "INSERT INTO missing_dict (missing_code, meaning_kr, meaning_en, source) VALUES (?,?,?,?)",
        insert_rows,
    )
    return len(insert_rows)


def load_term_dict(conn: sqlite3.Connection) -> int:
    """term_dict_seed.csv → term_dict 적재."""
    with TERM_SEED_CSV.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    insert_rows = [
        (r["term_id"], r["term_kr"], r["term_en"], r["definition_kr"], r["source"])
        for r in rows
    ]
    conn.executemany(
        "INSERT INTO term_dict (term_id, term_kr, term_en, definition_kr, source) VALUES (?,?,?,?,?)",
        insert_rows,
    )
    return len(insert_rows)


def integrity_check(conn: sqlite3.Connection) -> dict[str, object]:
    """무결성 점검 지표 산출.

    - 관측치 수 / 시리즈 수
    - 결측 비율 (DATA_VALUE NULL / total)
    - 시점 일관성 (item별 START/END_TIME ↔ observation TIME min/max)
    """
    n_table = conn.execute("SELECT COUNT(*) FROM stat_table_meta").fetchone()[0]
    n_item = conn.execute("SELECT COUNT(*) FROM stat_item_meta").fetchone()[0]
    n_obs = conn.execute("SELECT COUNT(*) FROM observation").fetchone()[0]
    n_obs_null = conn.execute(
        "SELECT COUNT(*) FROM observation WHERE DATA_VALUE IS NULL"
    ).fetchone()[0]
    missing_ratio = n_obs_null / n_obs if n_obs else 0
    n_missing = conn.execute("SELECT COUNT(*) FROM missing_dict").fetchone()[0]
    n_term = conn.execute("SELECT COUNT(*) FROM term_dict").fetchone()[0]

    # 시점 일관성 점검: stat_item_meta START_TIME/END_TIME과
    # observation에서의 실제 min/max를 (item_id 단위로) 비교.
    # WHERE o.DATA_VALUE IS NOT NULL: 결측(`x` 등) 셀의 TIME은
    #   "관측이 존재한 첫 시점"의 정의에서 제외하기 위해 필터.
    #   이로써 specification.csv의 START_TIME(실측치 첫 등장 시점)과
    #   observation의 min(TIME) 비교가 동일 정의 위에서 이뤄진다.
    cursor = conn.execute(
        """SELECT m.item_id, m.START_TIME, m.END_TIME,
                  MIN(o.TIME) as obs_min, MAX(o.TIME) as obs_max
           FROM stat_item_meta m
           LEFT JOIN observation o ON m.item_id = o.item_id
           WHERE o.DATA_VALUE IS NOT NULL
           GROUP BY m.item_id"""
    )
    inconsistent = 0
    for item_id, start_time, end_time, obs_min, obs_max in cursor:
        if start_time != obs_min or end_time != obs_max:
            inconsistent += 1

    return {
        "n_table": n_table,
        "n_item": n_item,
        "n_obs": n_obs,
        "n_obs_null": n_obs_null,
        "missing_ratio_pct": round(missing_ratio * 100, 4),
        "n_missing_dict": n_missing,
        "n_term_dict": n_term,
        "inconsistent_time_items": inconsistent,
    }


def main() -> None:
    print("Phase 4.2 §1·§4·§5·§6·§7 — sqlite3 RDB 적재 + 무결성 점검")
    print("=" * 60)
    if not DB_OUT.exists():
        print(f"[error] DB 파일 없음: {DB_OUT}")
        print("        먼저 init_ecos_db.py를 실행하여 빈 스키마를 생성하세요.")
        sys.exit(1)

    conn = sqlite3.connect(DB_OUT)
    try:
        conn.execute("PRAGMA foreign_keys = ON")

        # 1) 통계표 메타
        n1 = load_stat_table_meta(conn)
        print(f"[1/5] stat_table_meta: {n1}행 적재")

        # 2) 통계항목 메타
        item_id_map = load_stat_item_meta(conn)
        print(f"[2/5] stat_item_meta: {len(item_id_map)}행 적재")

        # 3) 관측치
        n_obs, n_skip = load_observation(conn, item_id_map)
        print(f"[3/5] observation: {n_obs}행 적재 (매칭 실패 skip {n_skip}행)")

        # 4) 결측 사전
        n_missing = load_missing_dict(conn)
        print(f"[4/5] missing_dict: {n_missing}행 적재")

        # 5) 통계 용어 사전
        n_term = load_term_dict(conn)
        print(f"[5/5] term_dict: {n_term}행 적재")

        conn.commit()

        # 무결성 점검
        print("=" * 60)
        print("[무결성 점검 지표]")
        result = integrity_check(conn)
        for k, v in result.items():
            print(f"  {k}: {v}")
    finally:
        conn.close()
    print("=" * 60)
    print("완료.")


if __name__ == "__main__":
    main()
