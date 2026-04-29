"""
보고서 단계 2 §1 — RDB·정형 사전 인벤토리 1회 점검 스크립트.

본 스크립트의 책임
-------------------
영국 BoP·환율 분석 보고서(`report/PLAN.md` 단계 2) 가 사용할 데이터 자산을
1회만 읽기 전용(SELECT/PRAGMA) 으로 점검해 결과를 표준 출력에 출력한다.
산출 메모는 별도로 `report/research/08_data_inventory.md` 에 사람이 정리한다.

점검 범위
---------
1) RDB 5 테이블 행 수·인덱스·외래키 — `USER_GUIDE.md` 등재값과 비교
2) 정형 사전 CSV 5 파일(`db/data/_spec/`) 의 행 수·컬럼 수
3) 보고서 핵심 변수(CA 5 + FA 6 + 보조 4 = 15종) 의 RDB 등재·시점 범위
4) 분석 윈도우 80 분기(2006Q1~2025Q4) 구간 결측 점검
5) 환율 관련 통계표·항목이 RDB 에 등재돼 있는지 키워드 검색

원칙
----
- 데이터 값은 절대 수정하지 않으며 SELECT 와 PRAGMA 만 사용한다.
- 외부 의존성을 두지 않는다(표준 라이브러리 + `env/` 의 sqlite3 만 사용).
- 모든 SQL 은 정적 문자열 또는 파라미터 바인딩(`?`) 을 사용한다.
- 본 스크립트는 `env/Scripts/python.exe` (Windows) 또는 `env/bin/python` (POSIX)
  로만 실행한다.

입력
----
- DB:   `db/data/_db/ecos_uk_bop.sqlite`
- SPEC: `db/data/_spec/{specification,statcatalog,cdid_definitions,
        missing_dict_seed,term_dict_seed}.csv`

출력
----
- 표준 출력 1회 — 외부 파일을 새로 쓰지 않는다.
"""

import csv
import sqlite3
import sys
from pathlib import Path

# Windows 콘솔의 기본 코드페이지(cp949) 환경에서도 한국어 출력이 깨지지 않도록
# 표준 출력의 인코딩을 UTF-8 로 재설정한다(reconfigure 미지원 환경은 그대로 둔다).
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# 저장소 루트와 점검 대상 경로.
# 본 파일 위치: db/code/source/inventory_check_report_step2.py
#   parents[0] = source, parents[1] = code, parents[2] = db, parents[3] = ROOT
ROOT = Path(__file__).resolve().parents[3]
DB = ROOT / "db" / "data" / "_db" / "ecos_uk_bop.sqlite"
SPEC = ROOT / "db" / "data" / "_spec"

# 보고서 핵심 변수 정의 — 튜플은 (CDID, 분류, STAT_CODE 힌트, 역할 메모) 4-튜플.
#
# - 분류: CA(경상수지) / FA(금융계정) / AUX(보조 — KA·NEO·CA-GDP·NIIP)
# - STAT_CODE 힌트: 같은 ITEM_CODE1 이 여러 통계표에 중복 등재될 가능성에 대비해
#   우선 매칭할 STAT_CODE 를 미리 지정. 일치 행이 없으면 첫 번째 행으로 폴백.
# - FA 6종은 ONS Notes 시트 11번 노트 19 의 sign_prefix 운영 규칙에 따라
#   RDB ITEM_CODE1 에 '-' 접두사가 붙은 형태(`-MU7M` 등) 로 등재돼 있다.
#   이는 CDID 자체에 대한 부호 반전이 아니라 부호 규약을 보존하기 위한 표기다.
KEY_VARS = [
    ("BOKI",  "CA",  "UK_BoP_Table_A_sub1", "상품수지(Goods)"),
    ("IKBD",  "CA",  "UK_BoP_Table_A_sub1", "서비스수지(Services)"),
    ("HBOJ",  "CA",  "UK_BoP_Table_A_sub1", "1차소득(Primary income)"),
    ("IKBP",  "CA",  "UK_BoP_Table_A_sub1", "2차소득(Secondary income)"),
    ("HBOP",  "CA",  "UK_BoP_Table_A_sub1", "경상수지 합계"),
    ("-MU7M", "FA",  "UK_BoP_Table_A_sub3", "직접투자(Direct investment, sign-flipped)"),
    ("-HHZD", "FA",  "UK_BoP_Table_A_sub3", "증권투자(Portfolio, sign-flipped)"),
    ("-ZPNN", "FA",  "UK_BoP_Table_A_sub3", "파생금융(Derivatives, sign-flipped)"),
    ("-HHYR", "FA",  "UK_BoP_Table_A_sub3", "기타투자(Other, sign-flipped)"),
    ("-LTCV", "FA",  "UK_BoP_Table_A_sub3", "준비자산(Reserve, flow, sign-flipped)"),
    ("-HBNT", "FA",  "UK_BoP_Table_A_sub3", "금융계정 합계(sign-flipped)"),
    ("FNVQ",  "AUX", "UK_BoP_Table_A_sub1", "자본수지(KA)"),
    ("HHDH",  "AUX", "UK_BoP_Table_A_sub3", "오차 및 누락(NEO)"),
    ("AA6H",  "AUX", "UK_BoP_Table_B_sub4", "CA-GDP 비율"),
    ("HBQC",  "AUX", "UK_BoP_Table_K_sub3", "NIIP(순대외자산)"),
]

# 보고서 분석 윈도우 — 최근 20년 80 분기(2006Q1 ~ 2025Q4).
# `observation.TIME` 컬럼의 분기 표기 형식("YYYYQn") 과 정확히 일치시킨다.
WINDOW_TIMES = [f"{y}Q{q}" for y in range(2006, 2026) for q in (1, 2, 3, 4)]
assert len(WINDOW_TIMES) == 80, "분석 윈도우는 정확히 80 분기여야 한다"


def section(title):
    """표준 출력에 절(section) 머리 행을 출력하는 보조 함수.

    파라미터
    --------
    title : str
        절 제목(한국어).

    부작용
    ------
    표준 출력에 빈 줄과 함께 `=== {title} ===` 머리 행을 출력한다.
    """
    print(f"\n=== {title} ===")


def main():
    """단계 2 §1 점검 5 절을 순차 실행하는 진입점 함수.

    실행 흐름
    ---------
    (1) RDB 5 테이블 행 수·인덱스·외래키 점검
    (2) 정형 사전 CSV 5 파일 행 수·컬럼 수 점검
    (3) 핵심 15 변수 RDB 등재·시점 범위·관측·결측 표 출력
    (4) 80 분기 윈도우 한정 결측 점검
    (5) 환율 관련 통계표·항목 키워드 검색

    부작용
    ------
    - 표준 출력에 점검 결과를 출력한다.
    - DB 파일을 읽기 전용으로 연결한다(SELECT·PRAGMA 만 사용, COMMIT 없음).
    - 새 파일을 만들지 않으며 기존 파일도 수정하지 않는다.

    예외
    ----
    DB 또는 정형 사전 파일이 존재하지 않으면 `sqlite3` 또는 `open()` 단계에서
    표준 예외가 그대로 전파된다(별도 예외 처리는 두지 않는다 — 일어날 수 없는
    시나리오에 대한 방어 코드 금지 원칙).
    """
    print(f"DB 경로: {DB}")
    print(f"DB 존재: {DB.exists()}")
    # 본 함수 종료 시점에 sqlite3 연결을 명시적으로 close 한다(아래 conn.close()).
    # row_factory 를 sqlite3.Row 로 두어 컬럼명 키 접근(r["STAT_CODE"]) 을 활성화.
    conn = sqlite3.connect(str(DB))
    conn.row_factory = sqlite3.Row

    # ----- (1) RDB 5 테이블 -----
    # USER_GUIDE.md §1·§7 에 등재된 행 수와 비교하기 위한 1차 점검.
    # 인덱스 3개, 외래키 2개도 함께 확인하여 무결성 유지 여부를 본다.
    section("(1) RDB 5 테이블 행 수")
    table_counts = {}
    for tname in ["stat_table_meta", "stat_item_meta", "observation",
                  "missing_dict", "term_dict"]:
        n = conn.execute(f"SELECT COUNT(*) FROM {tname}").fetchone()[0]
        table_counts[tname] = n
        print(f"  {tname}: {n}")

    section("(1) 인덱스")
    # SQLite 가 자동 생성하는 내부 인덱스(`sqlite_autoindex_*`) 는 점검 대상이
    # 아니므로 `name NOT LIKE 'sqlite_%'` 로 제외한다.
    idx_rows = conn.execute(
        "SELECT name, tbl_name FROM sqlite_master WHERE type='index' "
        "AND name NOT LIKE 'sqlite_%' ORDER BY name"
    ).fetchall()
    for r in idx_rows:
        print(f"  {r['name']}  on  {r['tbl_name']}")

    section("(1) 외래키")
    # PRAGMA foreign_key_list 는 자식 테이블에서 호출해야 부모를 가리키는 FK 가
    # 반환된다. stat_table_meta 는 부모 전용이므로 점검 대상에서 제외.
    for tname in ["stat_item_meta", "observation"]:
        fks = conn.execute(f"PRAGMA foreign_key_list({tname})").fetchall()
        for fk in fks:
            print(f"  {tname}.{fk['from']} -> {fk['table']}.{fk['to']}")

    # ----- (2) 정형 사전 CSV -----
    # `db/data/_spec/` 의 시드 사전이 RDB 와 1:1 대응하는지(specification ↔
    # stat_item_meta, statcatalog ↔ stat_table_meta, missing_dict_seed ↔
    # missing_dict, term_dict_seed ↔ term_dict) 행 수·컬럼 수로 1차 확인.
    # 본문 비교는 사람이 `08_data_inventory.md` §2 표에서 정리.
    section("(2) 정형 사전 CSV 행 수·컬럼 수")
    spec_files = [
        "specification.csv",
        "statcatalog.csv",
        "cdid_definitions.csv",
        "missing_dict_seed.csv",
        "term_dict_seed.csv",
    ]
    spec_stats = {}
    for fn in spec_files:
        path = SPEC / fn
        if not path.exists():
            # 파일 누락 시 즉시 보고하고 다음 파일로 넘어간다(전체 중단 없음).
            print(f"  {fn}: NOT FOUND")
            continue
        # CSV 는 UTF-8 BOM 포함 가능성 → `utf-8-sig` 로 BOM 자동 제거.
        # 헤더 1행 + 본문 N행 가정. 빈 파일이면 header 가 빈 리스트로 들어온다.
        with open(path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.reader(f)
            header = next(reader, [])
            n_rows = sum(1 for _ in reader)
        spec_stats[fn] = (n_rows, len(header))
        print(f"  {fn}: rows={n_rows}, cols={len(header)}")

    # ----- (3) 13 + 보조 2 = 15 변수 등재 + 시점 범위 -----
    # 15 변수 각각에 대해 stat_item_meta 에서 ITEM_CODE1 일치 행을 찾고,
    # STAT_CODE 힌트로 우선 매칭한다. 매칭된 item_id 로 observation 의
    # 총 관측 행 수와 DATA_VALUE NULL 행 수를 계산해 1차 결측 신호를 얻는다.
    section("(3) 핵심 13 변수 RDB 등재·시점 범위")
    print(f"  {'CDID':<6} {'분류':<4} {'STAT_CODE':<24} {'START':<8} {'END':<8} "
          f"{'OBS':>5} {'MISS':>5}  ITEM_NAME_KR")
    var_results = []
    for cdid, role, hint, memo in KEY_VARS:
        # ITEM_CODE1 = CDID 인 행을 모두 가져온다(같은 CDID 가 여러 통계표에
        # 중복 등재된 케이스가 있을 수 있어 단일 행을 가정하지 않는다).
        rows = conn.execute(
            "SELECT m.item_id, m.STAT_CODE, m.ITEM_NAME_KR, m.UNIT_NAME, "
            "m.START_TIME, m.END_TIME "
            "FROM stat_item_meta m WHERE m.ITEM_CODE1 = ? ORDER BY m.STAT_CODE",
            (cdid,),
        ).fetchall()
        if not rows:
            # 미등재 변수는 0/0 으로 기록하고 다음 변수로 넘어간다.
            print(f"  {cdid:<6} {role:<4} {hint:<24} {'-':<8} {'-':<8} "
                  f"{0:>5} {0:>5}  NOT_FOUND ({memo})")
            var_results.append({"cdid": cdid, "role": role, "stat_hint": hint,
                                "stat_actual": None, "start": None, "end": None,
                                "n_obs": 0, "n_miss": 0, "memo": memo,
                                "item_name_kr": None, "unit": None,
                                "item_id": None})
            continue
        # STAT_CODE 힌트와 일치하는 첫 행을 우선 사용한다. 일치 행이 없으면
        # 정렬된 결과의 첫 번째 행으로 폴백(현재 데이터셋에서는 모든 변수가
        # hint 와 정확히 일치한다).
        chosen = None
        for r in rows:
            if r["STAT_CODE"] == hint:
                chosen = r
                break
        if chosen is None:
            chosen = rows[0]
        item_id = chosen["item_id"]
        # 관측 행 수(전체) 와 DATA_VALUE 가 NULL 인 결측 행 수.
        # 단계 2 §3 표의 마지막 두 컬럼(총 관측, DATA_VALUE NULL) 입력값이다.
        n_obs = conn.execute(
            "SELECT COUNT(*) FROM observation WHERE item_id = ?", (item_id,)
        ).fetchone()[0]
        n_miss = conn.execute(
            "SELECT COUNT(*) FROM observation "
            "WHERE item_id = ? AND DATA_VALUE IS NULL", (item_id,)
        ).fetchone()[0]
        print(f"  {cdid:<6} {role:<4} {chosen['STAT_CODE']:<24} "
              f"{chosen['START_TIME'] or '-':<8} {chosen['END_TIME'] or '-':<8} "
              f"{n_obs:>5} {n_miss:>5}  {chosen['ITEM_NAME_KR']}")
        var_results.append({
            "cdid": cdid, "role": role, "stat_hint": hint,
            "stat_actual": chosen["STAT_CODE"],
            "start": chosen["START_TIME"], "end": chosen["END_TIME"],
            "n_obs": n_obs, "n_miss": n_miss, "memo": memo,
            "item_name_kr": chosen["ITEM_NAME_KR"],
            "unit": chosen["UNIT_NAME"], "item_id": item_id,
        })

    # ----- (4) 80 분기 윈도우 결측 점검 -----
    # 분석 윈도우(2006Q1~2025Q4) 한정으로 결측을 다시 본다. 두 종류 결측을 모두
    # 포착한다:
    #   (a) 행은 존재하지만 DATA_VALUE 가 NULL 인 경우(원본의 'x'·'..' 등).
    #   (b) 윈도우 시점 자체가 observation 에 부재한 경우(시리즈 단축).
    # 두 결측 집합의 합집합을 결측 시점으로 보고한다.
    section("(4) 80 분기(2006Q1~2025Q4) 결측 점검")
    placeholders = ",".join(["?"] * len(WINDOW_TIMES))
    print(f"  {'CDID':<6} {'OBS_in_window':>14} {'MISS_in_window':>15}  결측시점")
    window_findings = []
    for v in var_results:
        if v["item_id"] is None:
            # 등재 자체가 없으면 윈도우 점검도 의미가 없으므로 표식만 남긴다.
            print(f"  {v['cdid']:<6} {'-':>14} {'-':>15}  ITEM_NOT_REGISTERED")
            window_findings.append({**v, "obs_win": 0, "miss_win": 0,
                                    "miss_times": []})
            continue
        # 윈도우 80 시점에 해당하는 행만 추출. RAW_CELL 은 결측 코드(원시 셀
        # 텍스트) 를 보존한 컬럼으로, 추후 결측 사전(missing_dict) 매핑에 사용.
        rows_in_win = conn.execute(
            f"SELECT TIME, RAW_CELL, DATA_VALUE FROM observation "
            f"WHERE item_id = ? AND TIME IN ({placeholders}) ORDER BY TIME",
            (v["item_id"], *WINDOW_TIMES),
        ).fetchall()
        n_in = len(rows_in_win)
        # (a) 행 존재 + 값 NULL.
        miss_times = [r["TIME"] for r in rows_in_win if r["DATA_VALUE"] is None]
        # (b) 윈도우 시점 중 행 자체가 누락된 시점.
        present = {r["TIME"] for r in rows_in_win}
        absent_times = [t for t in WINDOW_TIMES if t not in present]
        # 두 결측 유형의 합집합을 정렬해 보고.
        all_miss = sorted(set(miss_times) | set(absent_times))
        miss_label = ",".join(all_miss) if all_miss else "(없음)"
        # 표 가독성을 위해 60자 초과 시 말줄임 처리(상세는 miss_times 에 그대로 보존).
        if len(miss_label) > 60:
            miss_label = miss_label[:57] + "..."
        print(f"  {v['cdid']:<6} {n_in:>14} {len(all_miss):>15}  {miss_label}")
        window_findings.append({**v, "obs_win": n_in, "miss_win": len(all_miss),
                                "miss_times": all_miss})

    # ----- (5) 환율 관련 통계표 검색 -----
    # 두 경로로 환율 시계열의 RDB 등재 여부를 점검:
    #   1) 통계표 메타(stat_table_meta) 의 표 이름 4개 컬럼 × 9 키워드.
    #   2) 통계 항목 메타(stat_item_meta) 의 항목명 5개 컬럼 × 환율 어휘.
    # 키워드는 영문 대소문자 변형을 모두 포함해 SQLite LIKE 의 case-sensitivity
    # 차이에 따른 누락 위험을 줄였다. 한국어 '환율' 도 함께 포함.
    section("(5) 환율 시계열 RDB 등재 여부")
    fx_keywords = ["%Exchange%", "%exchange%", "%EXCHANGE%",
                   "%Sterling%", "%sterling%",
                   "%환율%", "%FX%", "%effective rate%", "%Effective%"]
    fx_hits = []
    for kw in fx_keywords:
        rows = conn.execute(
            "SELECT STAT_CODE, STAT_NAME, STAT_NAME_EN, FIELD_SUB, "
            "START_TIME, END_TIME FROM stat_table_meta "
            "WHERE STAT_NAME LIKE ? OR STAT_NAME_EN LIKE ? OR FIELD_SUB LIKE ? "
            "OR KOREAN_DESCRIPTION LIKE ?",
            (kw, kw, kw, kw),
        ).fetchall()
        for r in rows:
            fx_hits.append((kw, r["STAT_CODE"], r["STAT_NAME"],
                            r["STAT_NAME_EN"], r["FIELD_SUB"],
                            r["START_TIME"], r["END_TIME"]))
    # 항목 단위 보조 검색 — 표 이름에는 '환율' 어휘가 없어도 항목명에 들어 있을
    # 가능성을 보강한다. 어미 일치(`xchange`·`terling`·`ffective rate`) 를 사용해
    # Exchange/exchange/EXCHANGE, Sterling/sterling 변형을 1회 LIKE 로 흡수.
    item_fx = conn.execute(
        "SELECT DISTINCT m.STAT_CODE, m.ITEM_CODE1, m.ITEM_NAME_KR, "
        "m.ITEM_NAME1, m.ITEM_NAME2, m.ITEM_NAME3, m.ITEM_NAME4 "
        "FROM stat_item_meta m WHERE "
        "m.ITEM_NAME_KR LIKE '%환율%' "
        "OR m.ITEM_NAME1 LIKE '%xchange%' OR m.ITEM_NAME1 LIKE '%terling%' "
        "OR m.ITEM_NAME1 LIKE '%ffective rate%' "
        "OR m.ITEM_NAME2 LIKE '%xchange%' OR m.ITEM_NAME2 LIKE '%terling%' "
        "OR m.ITEM_NAME3 LIKE '%xchange%' OR m.ITEM_NAME3 LIKE '%terling%' "
        "OR m.ITEM_NAME4 LIKE '%xchange%' OR m.ITEM_NAME4 LIKE '%terling%'"
    ).fetchall()
    if fx_hits:
        print("  통계표 검색 결과:")
        # 같은 STAT_CODE 가 여러 키워드로 중복 hit 되는 경우를 1회만 출력.
        seen = set()
        for kw, code, name, name_en, fs, st, et in fx_hits:
            key = (code,)
            if key in seen:
                continue
            seen.add(key)
            print(f"    [{kw}] {code} | {name} | {name_en} | FIELD_SUB={fs} | "
                  f"{st}~{et}")
    else:
        print("  통계표 검색 결과: HIT 0건")
    if item_fx:
        print("  항목명 검색 결과:")
        for r in item_fx:
            names = " / ".join(filter(None, [r["ITEM_NAME1"], r["ITEM_NAME2"],
                                              r["ITEM_NAME3"], r["ITEM_NAME4"]]))
            print(f"    {r['STAT_CODE']} | {r['ITEM_CODE1']} | "
                  f"KR={r['ITEM_NAME_KR']} | EN={names}")
    else:
        print("  항목명 검색 결과: HIT 0건")

    # 두 경로 중 하나라도 hit 가 있으면 환율 시계열이 RDB 에 일부라도 등재된
    # 것으로 간주. 모두 0 이면 단계 3(`web-search`) 트리거 사유로 확정.
    fx_present = bool(fx_hits or item_fx)
    print(f"\n  환율 시계열 RDB 등재: {'YES' if fx_present else 'NO'}")
    if not fx_present:
        print("  >>> 단계 3 (web-search) 트리거 권고: BoE/BIS/OECD 1차 출처에서 "
              "GBP 명목·실효환율 시계열 확보 필요")

    # 모든 점검을 마쳤으므로 DB 연결을 닫는다(쓰기 트랜잭션이 없으므로 commit
    # 불필요). 본 스크립트는 SELECT/PRAGMA 만 호출했음을 다시 한 번 명시한다.
    conn.close()


if __name__ == "__main__":
    main()
