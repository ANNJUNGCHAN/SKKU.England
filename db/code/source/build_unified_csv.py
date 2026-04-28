"""Phase 2.2 세로형 통합 CSV (long-form) 생성 스크립트.

목적
----
db/CHECKLIST.md §2.2 컬럼 사양 14 컬럼 + ECOS 표준 필드 정렬을 충족하는
단일 평면 long-form CSV를 생성한다.

- 입력: 63개 부표 가로형 CSV (`db/data/balanceofpayments2025q4_*_sub*.csv`)
       + 마스터 인벤토리 (`db/data/_inventory/15_master_inventory.csv`)
       + 한국어 STAT_NAME 매핑 (`db/data/_inventory/20_korean_statname.md` — 별도 작성)
       + ITEM_CODE2~3 자동 매핑 규칙 (`db/data/_inventory/21_item_hierarchy.md` — 별도 작성)
- 출력: `db/data/balanceofpayments2025q4_long.csv` (단일 평면 표)

컬럼 사양 (PLAN.md §2.2)
------------------------
| 순서 | 컬럼 | ECOS 대응 | 설명 |
|---:|---|---|---|
| 1 | stat_code | STAT_CODE | UK_BoP_<table_code>_sub<n> 패턴 |
| 2 | stat_name | STAT_NAME | 한국어 통계표명 (시트 + 부표 단위) |
| 3 | sheet | — | 원본 시트명(부표 추적용) |
| 4 | sub_table | — | 부표 식별자(1, 2, ...) |
| 5 | item_code1 | ITEM_CODE1 | ONS CDID 4자 코드(원문 그대로 보존, sign_prefix `-` 포함) |
| 6 | item_code2 | ITEM_CODE2 | LVL 2 분류 코드(자동 매핑 가능 부분만 채움) |
| 7 | item_code3 | ITEM_CODE3 | LVL 3 분류 코드(자동 매핑 가능 부분만 채움) |
| 8 | item_code4 | ITEM_CODE4 | LVL 4 분류 코드(Phase 3.2에서 본격 작성, 본 단계는 빈 값) |
| 9 | item_name | ITEM_NAME | 부표 머리글 영문 라벨(보존) |
| 10 | unit_name | UNIT_NAME | 단위 정규화 라벨(GBP_million / GBP_billion / pct_of_GDP) |
| 11 | cycle | CYCLE | A(연간) / Q(분기) |
| 12 | time | TIME | YYYY 또는 YYYYQn |
| 13 | raw_cell | — | 부표 CSV의 원본 셀 문자열 그대로 |
| 14 | data_value | DATA_VALUE | 숫자 파싱 가능한 경우만, 그 외 빈 값 |

ECOS 매핑 메모
--------------
- sign_prefix(`-`)가 붙은 CDID는 BPM5↔BPM6 부호 규약 차이를 ETL 단계에서
  명시적으로 보존하기 위한 시그널이다(22회차 §4 단정). 본 통합 CSV의
  item_code1은 가로형 CSV에 `_neg_<cdid>` 컬럼명으로 보존된 부호 prefix를
  그대로 옮겨 `-CDID` 형태로 저장한다(예: `-MU7M`, `-HBNT`).
  실측 결과: 21 unique CDID × 8,519행에 `-` prefix가 부착됨.
- 결측은 raw_cell에 원문(`x` 또는 빈 문자열) 그대로, data_value는 빈 값.

검증 결과(22회차 표본 점검 §3·§4, 2025Q4 기준)
------------------------------------------------
- CA 항등식: BOKI + IKBD + HBOJ + IKBP = HBOP (잔차 0)
- FA 항등식: −MU7M + −HHZD + −ZPNN + −HHYR + −LTCV = −HBNT (잔차 0)
- NIIP 항등식: HBQA − HBQB = HBQC (잔차 0, 부동소수 오차 제외)
- 7튜플 키(stat_code, sub_table, item_code1, item_code2, item_code3,
  item_code4, time) 유일성 점검: 74,006 unique = 74,006 total.

원본 보존
----------
입력은 모두 부표 CSV(가로형) + 인벤토리. db/source/* 미접근.

재현
----
env/Scripts/python.exe db/code/source/build_unified_csv.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

# 저장소 루트.
ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "db" / "data"
INV = DATA_DIR / "_inventory" / "15_master_inventory.csv"
LOG = DATA_DIR / "_etl_log" / "phase2_1_split_log.csv"
OUT_CSV = DATA_DIR / "balanceofpayments2025q4_long.csv"

# 시점 정규식 — `time_period` 컬럼 분류용.
TIME_RE = re.compile(r"^(\d{4})(?:Q([1-4]))?$")
# 숫자 파싱 정규식.
NUM_RE = re.compile(r"^[+-]?[\d,]+(\.\d+)?$")


def parse_time(time_str: str) -> tuple[str, str]:
    """time_period 문자열을 (cycle, time) 튜플로 정규화.

    - "1997" → ("A", "1997")
    - "1997Q1" → ("Q", "1997Q1")
    - 기타: ("", time_str) — 비정형 라벨 보존.
    """
    m = TIME_RE.match(time_str)
    if not m:
        return ("", time_str)
    if m.group(2):
        return ("Q", time_str)
    return ("A", time_str)


def parse_data_value(raw: str) -> str:
    """원본 셀 문자열에서 숫자 파싱 가능 시 표준 표기, 아니면 빈 값."""
    s = raw.strip()
    if s == "":
        return ""
    if NUM_RE.match(s):
        # 원본 자릿수 보존(쉼표 포함 가능). 분석 시 float 변환은 사용자에 위임.
        return s.replace(",", "")
    return ""


def load_master(path: Path) -> dict[str, dict]:
    """마스터 인벤토리를 시트 키로 dict 화."""
    with path.open(encoding="utf-8") as f:
        return {row["sheet"]: row for row in csv.DictReader(f)}


def load_log(path: Path) -> list[dict]:
    """ETL 로그 로드(63 부표 메타)."""
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_stat_code(table_code: str, sub_table: str) -> str:
    """STAT_CODE 네임스페이스: `UK_BoP_<table_code>_sub<n>` 패턴.

    PLAN.md §0.3 분야 접두 규약(영국 국제수지군)에 따라 `UK_BoP_` 접두 사용.
    """
    safe_table = table_code.replace(".", "_").upper()
    return f"UK_BoP_{safe_table}_sub{sub_table}"


# =============================================================================
# 21회차 background-search 권고 — ITEM_CODE2 자동 매핑 규칙
# 출처: db/data/_inventory/21_item_hierarchy.md §3.1·§5.
# (sheet, sub_table) 키로 LVL1.LVL2 합성 코드를 자동 부여한다. 자동률 100%.
# Table_J·D·R3 등 시트 내 컬럼 위치별로 LVL2가 다른 경우는 ITEM_CODE3 단계에서
# 추가 분기되며, 본 ITEM_CODE2는 시트·부표 수준의 1차 분류에 한정한다.
# =============================================================================
ITEM_CODE2_BY_SHEET_SUB: dict[tuple[str, str], str] = {
    # Table_A: 부표1=CA SA, 부표2=CA NSA, 부표3=FA NSA + NEO
    ("Table_A", "1"): "CA",
    ("Table_A", "2"): "CA",
    ("Table_A", "3"): "FA",
    # Table_B/BX/C/R2: 모두 CA(경상수지 본표). 부표 차원은 LVL3에서 분기.
    ("Table_B", "1"): "CA", ("Table_B", "2"): "CA", ("Table_B", "3"): "CA", ("Table_B", "4"): "CA",
    ("Table_BX", "1"): "CA", ("Table_BX", "2"): "CA", ("Table_BX", "3"): "CA", ("Table_BX", "4"): "CA",
    ("Table_C", "1"): "CA", ("Table_C", "2"): "CA", ("Table_C", "3"): "CA",
    ("Table_C", "4"): "CA", ("Table_C", "5"): "CA", ("Table_C", "6"): "CA",
    ("Table_R2", "1"): "CA", ("Table_R2", "2"): "CA", ("Table_R2", "3"): "CA", ("Table_R2", "4"): "CA",
    # Table_D 시리즈: 부표1=IIP(stock), 부표2=FA(flow), 부표3=CA.PI(income).
    # SIDE는 시트별로 다름(D1.3=Asset, D4.6=Liab, D7.9=Net) — LVL4 SIDE 메타로 별도 처리.
    ("Table_D1_3", "1"): "IIP", ("Table_D1_3", "2"): "FA", ("Table_D1_3", "3"): "CA",
    ("Table_D4_6", "1"): "IIP", ("Table_D4_6", "2"): "FA", ("Table_D4_6", "3"): "CA",
    ("Table_D7_9", "1"): "IIP", ("Table_D7_9", "2"): "FA", ("Table_D7_9", "3"): "CA",
    # Table_E: 상품수지 G; Table_F: 서비스수지 S; Table_G: 1차소득 PI; Table_H: 2차소득 SI.
    ("Table_E", "1"): "CA.G", ("Table_E", "2"): "CA.G", ("Table_E", "3"): "CA.G",
    ("Table_F", "1"): "CA.S", ("Table_F", "2"): "CA.S", ("Table_F", "3"): "CA.S",
    ("Table_G", "1"): "CA.PI", ("Table_G", "2"): "CA.PI", ("Table_G", "3"): "CA.PI",
    ("Table_H", "1"): "CA.SI", ("Table_H", "2"): "CA.SI", ("Table_H", "3"): "CA.SI",
    # Table_I: 자본수지 KA.
    ("Table_I", "1"): "KA", ("Table_I", "2"): "KA", ("Table_I", "3"): "KA",
    # Table_J: 금융계정 FA(flow). 컬럼 위치별 5분류는 LVL3에서 분기.
    ("Table_J", "1"): "FA", ("Table_J", "2"): "FA", ("Table_J", "3"): "FA",
    # Table_K: IIP stock (5분류 모두). 컬럼 위치별 분기는 LVL3.
    ("Table_K", "1"): "IIP", ("Table_K", "2"): "IIP", ("Table_K", "3"): "IIP",
    # Table_R1: Table_A 패턴(부표1=CA SA, 2=CA NSA, 3=FA).
    ("Table_R1", "1"): "CA", ("Table_R1", "2"): "CA", ("Table_R1", "3"): "FA",
    # Table_R3: 9 부표(abroad/in UK/net) × (IIP/Flow/Income) — Table_D 패턴 결합.
    ("Table_R3", "1"): "IIP", ("Table_R3", "2"): "FA", ("Table_R3", "3"): "CA",
    ("Table_R3", "4"): "IIP", ("Table_R3", "5"): "FA", ("Table_R3", "6"): "CA",
    ("Table_R3", "7"): "IIP", ("Table_R3", "8"): "FA", ("Table_R3", "9"): "CA",
}

# CDID(부호 prefix 제거 후 4자 대문자) → LVL3 합계 라벨 매핑.
# 21회차 §2.3·§5.4의 핵심 항등식(CA·FA·IIP·NEO·NIIP) 검증을 자동 수행 가능하도록
# 합계 시리즈만 우선 매핑한다. 비합계 행은 LVL3을 빈 값으로 두며, Phase 3.2에서
# column_label 정규식 매칭으로 보강한다.
ITEM_CODE3_TOT: dict[str, str] = {
    # CA 합계: HBOP(CA balance), HBOG/FKMJ(NEO 보정 합계), BOKI/IKBJ(상품·서비스 합계 라인).
    "HBOP": "CA.TOT", "HBOG": "CA.TOT", "FKMJ": "CA.TOT",
    # 상품수지 합계: BOKG(Cr), BOKH(Dr), BOKI(Bal).
    "BOKG": "CA.G.G_TOT", "BOKH": "CA.G.G_TOT", "BOKI": "CA.G.G_TOT",
    # 서비스수지 합계: IKBB/IKBC/IKBD.
    "IKBB": "CA.S.S_TOT", "IKBC": "CA.S.S_TOT", "IKBD": "CA.S.S_TOT",
    # 1차소득 합계: HBOH/HBOI/HBOJ; 투자소득 합계 HBOK/HBOL/HBOM.
    "HBOH": "CA.PI.PI_TOT", "HBOI": "CA.PI.PI_TOT", "HBOJ": "CA.PI.PI_TOT",
    "HBOK": "CA.PI.PI_INV_TOT", "HBOL": "CA.PI.PI_INV_TOT", "HBOM": "CA.PI.PI_INV_TOT",
    # 2차소득 합계: IKBN/IKBO/IKBP.
    "IKBN": "CA.SI.SI_TOT", "IKBO": "CA.SI.SI_TOT", "IKBP": "CA.SI.SI_TOT",
    # 자본수지 합계: FHLD/FLYL/FNVQ.
    "FHLD": "KA.KA_TOT", "FLYL": "KA.KA_TOT", "FNVQ": "KA.KA_TOT",
    # 금융계정 5분류 합계 — 거래(flow): DI=N2SV/N2SA/MU7M, PIF=HHZC/HHZF/HHZD,
    #                                   FD=ZPNN, OI=XBMM/XBMN/HHYR, IR=LTCV.
    "N2SV": "FA.DI.DI_TOT", "N2SA": "FA.DI.DI_TOT", "MU7M": "FA.DI.DI_TOT",
    "HHZC": "FA.PIF.PIF_TOT", "HHZF": "FA.PIF.PIF_TOT", "HHZD": "FA.PIF.PIF_TOT",
    "ZPNN": "FA.FD.FD_NET",
    "XBMM": "FA.OI.OI_TOT", "XBMN": "FA.OI.OI_TOT", "HHYR": "FA.OI.OI_TOT",
    "LTCV": "FA.IR.IR_TOT",
    # 금융계정 합계(broad): HBNR/HBNS/HBNT.
    "HBNR": "FA.FA_TOT", "HBNS": "FA.FA_TOT", "HBNT": "FA.FA_TOT",
    # IIP 5분류 합계 — 잔액(stock): K col2-10. DI=N2V3/N2UG/MU7O, PIF=HHZZ/HLXW/CGNH,
    #                                            FD=JX96/JX97/JX98, OI=HLXV/HLYD/CGNG, IR=LTEB.
    "N2V3": "IIP.DI", "N2UG": "IIP.DI", "MU7O": "IIP.DI",
    "HHZZ": "IIP.PIF", "HLXW": "IIP.PIF", "CGNH": "IIP.PIF",
    "JX96": "IIP.FD", "JX97": "IIP.FD", "JX98": "IIP.FD",
    "HLXV": "IIP.OI", "HLYD": "IIP.OI", "CGNG": "IIP.OI",
    "LTEB": "IIP.IR",
    # IIP 합계(NIIP·IIPA·IIPL): HBQA(자산)/HBQB(부채)/HBQC(순).
    "HBQA": "IIP.IIPA.IIPA_TOT", "HBQB": "IIP.IIPL.IIPL_TOT", "HBQC": "IIP.NIIP",
    # 통계 불일치 NEO: HHDH.
    "HHDH": "NEO.NEO",
}

# 시트별 한국어 통계표명 매핑(20회차 background-search 권고).
# 출처: db/data/_inventory/20_korean_statname.md §2.
# 본 매핑은 STAT_NAME 컬럼의 1차 자동 채움값이며, ECOS 공식 명칭과의 교차 검증은
# Phase 2.2 적재 후 별도 위임 단계에서 보강한다(20회차 §5 빠진 부분 1번).
STAT_NAME_KO: dict[str, str] = {
    "Table_A": "영국 국제수지 요약 (잔액)",
    "Table_B": "영국 경상수지 (전체, 계절조정)",
    "Table_BX": "영국 경상수지 (귀금속 제외, 계절조정)",
    "Table_C": "영국 경상수지 (EU/non-EU 지리분해)",
    "Table_D1_3": "영국 대외투자 (자산: IIP·금융거래·투자소득)",
    "Table_D4_6": "영국 대내투자 (부채: IIP·금융거래·투자소득)",
    "Table_D7_9": "영국 순대외투자 (순포지션: IIP·금융거래·투자소득)",
    "Table_E": "영국 상품무역 (수출·수입·수지)",
    "Table_F": "영국 서비스무역 (수출·수입·수지, 12분류)",
    "Table_G": "영국 1차소득 (본원소득: 보수·투자소득·기타)",
    "Table_H": "영국 2차소득 (이전소득: 정부·기타부문)",
    "Table_I": "영국 자본수지 (자본이전·비생산비금융자산)",
    "Table_J": "영국 금융계정 (계절미조정)",
    "Table_K": "영국 국제투자대조표 (분기말 잔액)",
    "Table_R1": "영국 국제수지 개정 요약 (잔액)",
    "Table_R2": "영국 경상수지 개정 (계절조정)",
    "Table_R3": "영국 국제투자 개정 (IIP·금융계정·투자소득)",
}


def build_stat_name(
    sheet: str, sub_table: str, classification_ko: str, table_code: str
) -> str:
    """한국어 통계표명. 20회차 강의 매핑(STAT_NAME_KO)을 1차 룩업하고,
    매핑 미수록 시트는 분류 + 표 코드 + 부표 번호 합성형으로 폴백한다.

    부표 단위 STAT_NAME_SUB는 본 단계에서 작성하지 않으며(20회차 §5 빠진 부분 4번),
    부표 정보는 별도 sheet/sub_table 컬럼으로 보존한다.
    """
    base = STAT_NAME_KO.get(sheet)
    if base:
        return base
    return f"{classification_ko} (Table {table_code} 부표 {sub_table})"


def main() -> None:
    """본 ETL 진입점."""
    masters = load_master(INV)
    log_rows = load_log(LOG)

    out_rows: list[list] = []
    for log in log_rows:
        if not log["out_file"]:
            continue  # 메타 시트(skipped) 제외.
        sheet = log["sheet"]
        sub_table = log["sub_table"]
        master = masters[sheet]
        table_code = master["table_code"]
        classification_ko = master["classification_ko"]
        unit_name = master["unit_normalized"]

        stat_code = build_stat_code(table_code, sub_table)
        stat_name = build_stat_name(sheet, sub_table, classification_ko, table_code)

        # 부표 가로형 CSV 로드.
        sub_csv = DATA_DIR / log["out_file"]
        with sub_csv.open(encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            # header[0] = "time_period", header[1:] = cdid 컬럼명.
            cdid_columns = header[1:]
            for row in reader:
                time_period = row[0]
                cycle, time_norm = parse_time(time_period)
                for ci, cdid_col in enumerate(cdid_columns, start=1):
                    raw_cell = row[ci] if ci < len(row) else ""
                    # `_neg_xxxx` → 부호 prefix 보존(item_code1에 그대로 둠 ‐ `-CDID` 패턴).
                    if cdid_col.startswith("_neg_"):
                        cdid_pure = cdid_col[len("_neg_"):].upper()
                        item_code1 = "-" + cdid_pure
                    else:
                        cdid_pure = cdid_col.upper()
                        item_code1 = cdid_pure
                    data_value = parse_data_value(raw_cell)
                    # ITEM_CODE2: 21회차 §3.1 시트·부표 단위 자동 매핑(LVL1·LVL2 합성, 자동률 100%).
                    item_code2 = ITEM_CODE2_BY_SHEET_SUB.get((sheet, sub_table), "")
                    # ITEM_CODE3: 21회차 §5 합계 시리즈 자동 매핑(자동률 약 70% 중 합계 라인 우선).
                    # 합계가 아닌 하위 항목은 빈 값 — Phase 3.2에서 column_label 정규식 매칭으로 보강.
                    item_code3 = ITEM_CODE3_TOT.get(cdid_pure, "")
                    # ITEM_CODE4: LVL4 메타 차원 7개는 본 단계에서 빈 값(21회차 §5.1 권고).
                    # Phase 3.2 명세서 단계에서 7개 별도 메타 컬럼(SA_FLAG·SIDE 등)으로 부여 예정.
                    item_code4 = ""
                    # ITEM_NAME은 부표 헤더 영문 라벨(현 단계에서는 빈 값으로 두고 Phase 3.1에서 채움).
                    item_name = ""
                    out_rows.append(
                        [
                            stat_code,
                            stat_name,
                            sheet,
                            sub_table,
                            item_code1,
                            item_code2,
                            item_code3,
                            item_code4,
                            item_name,
                            unit_name,
                            cycle,
                            time_norm,
                            raw_cell,
                            data_value,
                        ]
                    )

    fields = [
        "stat_code",
        "stat_name",
        "sheet",
        "sub_table",
        "item_code1",
        "item_code2",
        "item_code3",
        "item_code4",
        "item_name",
        "unit_name",
        "cycle",
        "time",
        "raw_cell",
        "data_value",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(fields)
        w.writerows(out_rows)

    print(f"OK rows={len(out_rows)} cols={len(fields)} -> {OUT_CSV.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
