"""
Phase 4.3 §1·§2·§3·§4 — ECOS 스타일 RDB 사용자 조회 예시 ETL.

build_ecos_db.py로 적재된 sqlite3 DB(`db/data/_db/ecos_uk_bop.sqlite`)에서
ECOS Open API의 4 주요 서비스에 대응하는 호출 예시를 한국어 출력으로 보여준다.

호출 예시
1. 통계항목 코드(ITEM_CODE1=CDID) 단일 조회 — ECOS 통계 자료 검색 서비스 대응
2. 분야·키워드(한국어/원문) 통계표 검색 — ECOS 통계표 목록 서비스 대응
3. 통계표 단위 항목 트리 조회(부모-자식·레벨·가중치) — ECOS 통계 항목 목록 서비스 대응
4. 선택 계열 CSV 내보내기 — 사용자 지정 위치로 1 CSV = 1 평면 표 산출

원칙
- 표준 라이브러리(sqlite3·csv) 사용 — 외부 의존성 없음.
- 모든 출력 한국어. CDID·STAT_CODE·CSV 경로는 영문 그대로.
- CSV 내보내기는 `db/data/_export/<요청>.csv` 기본 경로 (요청 시 변경 가능).

실행
    env/Scripts/python.exe db/code/source/query_examples.py
"""
from __future__ import annotations

import csv
import sqlite3
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

DB_DIR = Path(__file__).resolve().parents[2]
DB_FILE = DB_DIR / "data" / "_db" / "ecos_uk_bop.sqlite"
EXPORT_DIR = DB_DIR / "data" / "_export"


def example_1_item_lookup(conn: sqlite3.Connection, cdid: str = "HBOP") -> None:
    """예시 1: ITEM_CODE1(CDID) 단일 조회 — ECOS 통계 자료 검색 대응.

    CDID 1개로 모든 시점의 시계열을 표 형태로 받아옴. 메타·관측치 join.
    """
    print(f"[예시 1] CDID 단일 조회 — `{cdid}` (ECOS 통계 자료 검색 서비스 대응)")
    print("-" * 60)
    cursor = conn.execute(
        """SELECT m.STAT_CODE, m.ITEM_NAME_KR, m.UNIT_NAME, m.CYCLE,
                  o.TIME, o.RAW_CELL, o.DATA_VALUE
           FROM stat_item_meta m
           JOIN observation o ON m.item_id = o.item_id
           WHERE m.ITEM_CODE1 = ?
           ORDER BY m.STAT_CODE, o.TIME
           LIMIT 8""",
        (cdid,),
    )
    rows = list(cursor)
    if not rows:
        print(f"  (CDID {cdid} 미등록 — term_dict_seed.csv 또는 본 시범 CDID 추천 노트 참조)")
        return
    print(f"  STAT_CODE / 한국어 명칭 / 단위 / 주기 / 시점 / raw / value (상위 8행)")
    for stat_code, name_kr, unit, cycle, time, raw, value in rows:
        value_str = f"{value:>12,.1f}" if value is not None else "       NULL"
        print(f"  {stat_code:30s} {name_kr:30s} {unit:14s} {cycle} {time:8s} {raw:>10s} {value_str}")


def example_2_stat_table_search(conn: sqlite3.Connection, keyword: str = "경상수지") -> None:
    """예시 2: 분야·키워드 통계표 검색 — ECOS 통계표 목록 서비스 대응.

    한국어 또는 영문 키워드로 STAT_NAME / FIELD_SUB / KOREAN_DESCRIPTION에서 검색.
    """
    print(f"\n[예시 2] 통계표 검색 — 키워드 `{keyword}` (ECOS 통계표 목록 서비스 대응)")
    print("-" * 60)
    pattern = f"%{keyword}%"
    cursor = conn.execute(
        """SELECT STAT_CODE, STAT_NAME, FIELD_SUB, CYCLE, START_TIME, END_TIME
           FROM stat_table_meta
           WHERE STAT_NAME LIKE ? OR FIELD_SUB LIKE ? OR KOREAN_DESCRIPTION LIKE ?
                 OR STAT_NAME_EN LIKE ?
           ORDER BY STAT_CODE
           LIMIT 10""",
        (pattern, pattern, pattern, pattern),
    )
    print(f"  STAT_CODE / STAT_NAME / FIELD_SUB / 주기 / 시계열 범위 (상위 10건)")
    for stat_code, name, field_sub, cycle, start, end in cursor:
        print(f"  {stat_code:30s} {name:35s} {field_sub:25s} {cycle} {start} ~ {end}")


def example_3_item_tree(conn: sqlite3.Connection, stat_code: str = "UK_BoP_Table_A_sub1") -> None:
    """예시 3: 통계표 단위 항목 트리 조회 — ECOS 통계 항목 목록 서비스 대응.

    하나의 STAT_CODE 안에 등록된 모든 항목의 (LVL·P_ITEM_CODE·WGT) 메타 표시.
    Phase 4.1 §4 위계 매핑은 후속 단계 위임이므로 LVL·P_ITEM_CODE는 빈 값일 수 있음.
    """
    print(f"\n[예시 3] 통계표 항목 트리 — `{stat_code}` (ECOS 통계 항목 목록 서비스 대응)")
    print("-" * 60)
    cursor = conn.execute(
        """SELECT ITEM_CODE1, ITEM_CODE2, ITEM_CODE3, ITEM_NAME_KR,
                  LVL, P_ITEM_CODE, UNIT_NAME, SIGN_CONVENTION
           FROM stat_item_meta
           WHERE STAT_CODE = ?
           ORDER BY ITEM_CODE2, ITEM_CODE3, ITEM_CODE1
           LIMIT 15""",
        (stat_code,),
    )
    print(f"  CDID / ITEM_CODE2 / ITEM_CODE3 / 한국어 명칭 / LVL / P_ITEM_CODE / 단위 / 부호 규약 (상위 15행)")
    for cdid, code2, code3, name_kr, lvl, p_code, unit, sign in cursor:
        lvl_str = str(lvl) if lvl is not None else "-"
        p_str = p_code if p_code else "-"
        sign_short = (sign[:30] + "…") if sign and len(sign) > 30 else (sign or "")
        print(f"  {cdid:6s} {code2:6s} {code3:14s} {name_kr:30s} {lvl_str:3s} {p_str:6s} {unit:14s} {sign_short}")


def example_4_export_series(conn: sqlite3.Connection, cdid: str = "HBOP") -> Path:
    """예시 4: 선택 계열 CSV 내보내기 — 1 CSV = 1 평면 표.

    CDID 1개의 모든 시계열을 CSV로 내보냄. 메타 일부 컬럼 + 시점·관측치.
    """
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = EXPORT_DIR / f"export_{cdid}.csv"
    cursor = conn.execute(
        """SELECT m.STAT_CODE, m.ITEM_CODE1, m.ITEM_NAME_KR, m.UNIT_NAME, m.CYCLE,
                  o.TIME, o.RAW_CELL, o.DATA_VALUE
           FROM stat_item_meta m
           JOIN observation o ON m.item_id = o.item_id
           WHERE m.ITEM_CODE1 = ?
           ORDER BY m.STAT_CODE, o.TIME""",
        (cdid,),
    )
    rows = list(cursor)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["STAT_CODE", "ITEM_CODE1", "ITEM_NAME_KR", "UNIT_NAME", "CYCLE",
                         "TIME", "RAW_CELL", "DATA_VALUE"])
        for row in rows:
            writer.writerow([
                row[0], row[1], row[2], row[3], row[4],
                row[5], row[6],
                f"{row[7]}" if row[7] is not None else "",
            ])
    print(f"\n[예시 4] CSV 내보내기 — CDID `{cdid}`")
    print("-" * 60)
    print(f"  출력 파일: {out_path}")
    print(f"  내보낸 행 수: {len(rows)}")
    return out_path


def main() -> None:
    print("Phase 4.3 §1·§2·§3·§4 — ECOS 스타일 RDB 사용자 조회 예시")
    print("=" * 60)
    if not DB_FILE.exists():
        print(f"[error] DB 파일 없음: {DB_FILE}")
        print("        먼저 init_ecos_db.py + build_ecos_db.py를 실행하세요.")
        sys.exit(1)

    conn = sqlite3.connect(DB_FILE)
    try:
        # 시범 CDID는 강의 슬라이드 14 항등식의 핵심 변수: HBOP=경상수지, KTMS=서비스 합계 등
        # (구체 CDID는 노트 37 시범 CDID 추천 결과와 연동)
        example_1_item_lookup(conn, cdid="HBOP")
        example_2_stat_table_search(conn, keyword="경상수지")
        example_3_item_tree(conn, stat_code="UK_BoP_Table_A_sub1")
        example_4_export_series(conn, cdid="HBOP")
    finally:
        conn.close()
    print("=" * 60)
    print("완료.")


if __name__ == "__main__":
    main()
