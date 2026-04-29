"""
Phase 4.1 §2~§11 — ECOS 스타일 sqlite3 RDB 스키마 정의·생성 ETL.

5개 테이블(통계표 메타·통계항목 메타·관측치·결측 사전·통계 용어 사전) +
인덱스 + PK + FK + 유일성 제약을 한 번에 적용한다.
db/PLAN.md §4.1 스키마 설계 사양과 정합.

산출물
- `db/data/_db/ecos_uk_bop.sqlite` — 빈 스키마(메타·관측치 적재는 build_ecos_db.py에서 별도)

테이블 사양
1. **stat_table_meta** (통계표 메타) — Phase 3.4 §5 statcatalog.csv 기반
   - STAT_CODE TEXT PK            통계표 코드 (예: UK_BoP_Table_J_sub1)
   - STAT_NAME TEXT NOT NULL      한국어 통계표명
   - STAT_NAME_EN TEXT            원문 영문 통계표명
   - FIELD_MAIN TEXT              1차 분야 분류 (예: 국제수지)
   - FIELD_SUB TEXT               2차 분야 분류
   - ORG_NAME TEXT                작성기관 (Office for National Statistics, ONS)
   - DATA_SOURCE TEXT             자료원
   - CYCLE TEXT                   주기 (A/Q/M/D)
   - START_TIME TEXT              자료 시작 시점
   - END_TIME TEXT                자료 종료 시점
   - SOURCE_URL TEXT              출처 URL
   - PUBLISHED_DATE TEXT          발표일
   - BUILD_TIME TEXT              가공 시각 (ISO 8601)
   - KOREAN_DESCRIPTION TEXT      한국어 설명

2. **stat_item_meta** (통계항목 메타) — Phase 3.4 §1·§2·§3 specification.csv 기반
   - item_id INTEGER PK AUTOINCREMENT  자동 증가 식별자
   - STAT_CODE TEXT NOT NULL FK        통계표 외래 키 (stat_table_meta.STAT_CODE)
   - ITEM_CODE1 TEXT NOT NULL          1단계 항목 코드 (ONS CDID)
   - ITEM_CODE2 TEXT                   2단계 (LVL2 분류)
   - ITEM_CODE3 TEXT                   3단계 (LVL3 합계 식별자)
   - ITEM_CODE4 TEXT                   4단계 (Phase 3 위임, 빈 값 가능)
   - ITEM_NAME1 TEXT                   1단계 영문 라벨
   - ITEM_NAME2 TEXT                   2단계 영문 라벨
   - ITEM_NAME3 TEXT                   3단계 영문 라벨
   - ITEM_NAME4 TEXT                   4단계 영문 라벨
   - ITEM_NAME_KR TEXT                 한국어 명칭
   - DEFINITION_KR TEXT                한국어 정의
   - P_ITEM_CODE TEXT                  부모 항목 코드(P_ITEM_CODE)
   - LVL INTEGER                       계층 레벨 (1·2·3·4)
   - WGT REAL                          가중치 (BoP 통상 NULL)
   - UNIT_NAME TEXT                    단위 (GBP_million / GBP_billion / PCT_GDP)
   - CYCLE TEXT                        주기 (A·Q)
   - START_TIME TEXT                   시작 시점
   - END_TIME TEXT                     종료 시점
   - SIGN_CONVENTION TEXT              부호 규약 (BPM6 자산·부채 증감 기준 등)
   - STOCK_FLOW_TYPE TEXT              flow / stock 구분
   - SOURCE TEXT                       출처
   - UNIQUE(STAT_CODE, ITEM_CODE1, ITEM_CODE2, ITEM_CODE3, ITEM_CODE4)
                                       (통계표·ITEM_CODE1~4) 유일성 제약

3. **observation** (관측치) — Phase 2.2 long-form CSV 기반
   - item_id INTEGER NOT NULL FK       통계항목 외래 키 (stat_item_meta.item_id)
   - TIME TEXT NOT NULL                시점 (YYYY / YYYYQn / YYYYMM)
   - RAW_CELL TEXT                     원본 셀 문자열 (결측 포함)
   - DATA_VALUE REAL                   숫자 변환값 (NULL 허용)
   - PRIMARY KEY (item_id, TIME)       (통계항목·시점) 기본 키

4. **missing_dict** (결측 사전)
   - missing_code TEXT PK              결측 코드 ('x', '', '..', '[c]' 등)
   - meaning_kr TEXT NOT NULL          한국어 의미
   - meaning_en TEXT                   영문 의미
   - source TEXT                       출처

5. **term_dict** (통계 용어 사전)
   - term_id TEXT PK                   용어 식별자
   - term_kr TEXT NOT NULL             한국어 명칭
   - term_en TEXT                      영문 명칭
   - definition_kr TEXT NOT NULL       한국어 정의
   - source TEXT                       출처

인덱스 (총 3개)
- idx_item_code1       ON stat_item_meta(ITEM_CODE1)   — ONS CDID 단일 키 조회
- idx_item_meta_stat   ON stat_item_meta(STAT_CODE)    — 통계표 단위 항목 조회
- idx_obs_time         ON observation(TIME)            — 시점 단일 키 조회
- (item_id, TIME) 복합 키는 PRIMARY KEY로 자동 인덱싱(별도 CREATE INDEX 불요)

원칙
- 멱등 동작: 기존 DB 파일 있으면 백업 후 새로 생성.
- 표준 라이브러리(sqlite3) 사용 — 외부 의존성 없음.
- DB 파일은 단일 파일 — 외부 서버 없이 표준 라이브러리만으로 조회 가능.

실행
    env/Scripts/python.exe db/code/source/init_ecos_db.py
"""
from __future__ import annotations

import shutil
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

DB_DIR = Path(__file__).resolve().parents[2]
DB_OUT = DB_DIR / "data" / "_db" / "ecos_uk_bop.sqlite"


# 5 테이블 DDL
SCHEMA_DDL = [
    # 1. 통계표 메타
    """
    CREATE TABLE stat_table_meta (
        STAT_CODE          TEXT PRIMARY KEY,
        STAT_NAME          TEXT NOT NULL,
        STAT_NAME_EN       TEXT,
        FIELD_MAIN         TEXT,
        FIELD_SUB          TEXT,
        ORG_NAME           TEXT,
        DATA_SOURCE        TEXT,
        CYCLE              TEXT,
        START_TIME         TEXT,
        END_TIME           TEXT,
        SOURCE_URL         TEXT,
        PUBLISHED_DATE     TEXT,
        BUILD_TIME         TEXT,
        KOREAN_DESCRIPTION TEXT
    )
    """,
    # 2. 통계항목 메타 — (STAT_CODE, ITEM_CODE1~4) 유일성 제약
    """
    CREATE TABLE stat_item_meta (
        item_id            INTEGER PRIMARY KEY AUTOINCREMENT,
        STAT_CODE          TEXT NOT NULL,
        ITEM_CODE1         TEXT NOT NULL,
        ITEM_CODE2         TEXT,
        ITEM_CODE3         TEXT,
        ITEM_CODE4         TEXT,
        ITEM_NAME1         TEXT,
        ITEM_NAME2         TEXT,
        ITEM_NAME3         TEXT,
        ITEM_NAME4         TEXT,
        ITEM_NAME_KR       TEXT,
        DEFINITION_KR      TEXT,
        P_ITEM_CODE        TEXT,
        LVL                INTEGER,
        WGT                REAL,
        UNIT_NAME          TEXT,
        CYCLE              TEXT,
        START_TIME         TEXT,
        END_TIME           TEXT,
        SIGN_CONVENTION    TEXT,
        STOCK_FLOW_TYPE    TEXT,
        SOURCE             TEXT,
        FOREIGN KEY (STAT_CODE) REFERENCES stat_table_meta(STAT_CODE),
        UNIQUE (STAT_CODE, ITEM_CODE1, ITEM_CODE2, ITEM_CODE3, ITEM_CODE4)
    )
    """,
    # 3. 관측치 — (item_id, TIME) 기본 키
    """
    CREATE TABLE observation (
        item_id            INTEGER NOT NULL,
        TIME               TEXT NOT NULL,
        RAW_CELL           TEXT,
        DATA_VALUE         REAL,
        PRIMARY KEY (item_id, TIME),
        FOREIGN KEY (item_id) REFERENCES stat_item_meta(item_id)
    )
    """,
    # 4. 결측 사전
    """
    CREATE TABLE missing_dict (
        missing_code       TEXT PRIMARY KEY,
        meaning_kr         TEXT NOT NULL,
        meaning_en         TEXT,
        source             TEXT
    )
    """,
    # 5. 통계 용어 사전
    """
    CREATE TABLE term_dict (
        term_id            TEXT PRIMARY KEY,
        term_kr            TEXT NOT NULL,
        term_en            TEXT,
        definition_kr      TEXT NOT NULL,
        source             TEXT
    )
    """,
]

# 인덱스 정의
INDEX_DDL = [
    "CREATE INDEX idx_item_code1 ON stat_item_meta(ITEM_CODE1)",
    "CREATE INDEX idx_obs_time ON observation(TIME)",
    "CREATE INDEX idx_item_meta_stat ON stat_item_meta(STAT_CODE)",
]


def backup_existing_db() -> Path | None:
    """기존 DB 파일 있으면 타임스탬프 백업 후 경로 반환."""
    if not DB_OUT.exists():
        return None
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = DB_OUT.with_suffix(f".backup_{ts}.sqlite")
    shutil.copy2(DB_OUT, backup_path)
    DB_OUT.unlink()
    return backup_path


def init_schema() -> None:
    """빈 sqlite3 DB 생성 + 5 테이블 + 3 인덱스 적용."""
    DB_OUT.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_OUT)
    try:
        # 외래 키 제약 활성화 (sqlite3 기본 비활성)
        conn.execute("PRAGMA foreign_keys = ON")
        # 5 테이블 생성
        for ddl in SCHEMA_DDL:
            conn.execute(ddl)
        # 3 인덱스 생성
        for ddl in INDEX_DDL:
            conn.execute(ddl)
        conn.commit()
    finally:
        conn.close()


def verify_schema() -> dict[str, int]:
    """스키마 검증: 테이블 5개·인덱스 3개·외래키 2개·유일성 제약 1개 점검.

    Returns:
        검증 결과 딕셔너리 (key: 항목명, value: 카운트)
    """
    conn = sqlite3.connect(DB_OUT)
    try:
        # 테이블 수
        tables = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        # 인덱스 수 (autoincrement·PK 자동 인덱스 제외)
        indexes = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='index' AND name NOT LIKE 'sqlite_%' ORDER BY name"
        ).fetchall()
        # 외래키 점검
        fk_count = 0
        for table_row in tables:
            tname = table_row[0]
            fks = conn.execute(f"PRAGMA foreign_key_list({tname})").fetchall()
            fk_count += len(fks)
        return {
            "tables": len(tables),
            "table_names": [t[0] for t in tables],
            "indexes": len(indexes),
            "index_names": [i[0] for i in indexes],
            "foreign_keys": fk_count,
        }
    finally:
        conn.close()


def main() -> None:
    print("Phase 4.1 §2~§11 — ECOS 스타일 sqlite3 RDB 스키마 생성")
    print("=" * 60)
    backup = backup_existing_db()
    if backup:
        print(f"[backup] 기존 DB 백업: {backup.name}")
    init_schema()
    print(f"[init] 신규 DB 생성: {DB_OUT}")
    result = verify_schema()
    print(f"[verify] 테이블 {result['tables']}개: {result['table_names']}")
    print(f"[verify] 인덱스 {result['indexes']}개: {result['index_names']}")
    print(f"[verify] 외래키 제약 {result['foreign_keys']}개")
    print("=" * 60)
    print("완료. (적재는 build_ecos_db.py에서 별도)")


if __name__ == "__main__":
    main()
