"""
Phase 3.4 §1·§2·§3 — 데이터 명세서(specification) 생성 ETL.

cdid_definitions.csv(512행) + balanceofpayments2025q4_long.csv(74,006행)에서
CDID별 START_TIME / END_TIME을 추출하고, 노트 24~28의 시트·분류별 보강 정의를
unmapped 319건의 ko_definition에 일괄 적용한 뒤, db/CHECKLIST.md §3.4 §1의
13컬럼 명세서 사양을 충족하는 통합 명세서 CSV를 산출한다.

산출 컬럼(13개, ECOS 표준 정렬)
- STAT_CODE      통계표 코드 (예: UK_BoP_Table_J_sub1)
- STAT_NAME      한국어 통계표명
- ITEM_CODE1     1단계 항목 코드 (ONS CDID)
- ITEM_CODE2     2단계 항목 코드 (LVL1 분류)
- ITEM_CODE3     3단계 항목 코드 (LVL2 합계 라인)
- ITEM_CODE4     4단계 항목 코드 (Phase 3 위임 — 빈 값)
- ITEM_NAME_EN   원문 라벨 (영문 column_label)
- ITEM_NAME_KO   한국어 명칭
- DEFINITION     한국어 정의 (강의 직접 매핑 + 노트 24~28 보강)
- UNIT_NAME      단위 (GBP_million / GBP_billion / PCT_GDP / MIXED)
- CYCLE          주기 (A / Q)
- START_TIME     시계열 시작 시점 (YYYY 또는 YYYYQn)
- END_TIME       시계열 종료 시점
- MISSING_MEANING  결측 표기 의미 (강의 자료 + ONS Notes 메타)
- SIGN_CONVENTION  부호 규약 (BPM6 자산·부채 증감 기준 + sign_prefix 운영)
- SOURCE         출처 (강의 슬라이드 번호 + 노트 24~28 + 외부 출처 URL)

원칙
- 데이터 값(value)·결측 표기는 변경하지 않음 — 명세서는 메타 컬럼 정형화 산출물.
- 멱등 동작: 재실행 시 동일 결과.
- ko_definition은 unmapped 319건에 시트·분류별 일괄 보강 정의를 적용하되,
  노트 24~28의 §6 출처 카탈로그 + §7 8필드 표준 형식을 인용한다.
- specification.csv는 단일 평면 표(1 CSV = 1 시트) 원칙 준수.

실행
    env/Scripts/python.exe db/code/source/build_specification.py
"""
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path

# Windows cp949 콘솔에서 한국어·em dash 출력 시 UnicodeEncodeError 방지
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

DB_DIR = Path(__file__).resolve().parents[2]
SPEC_DIR = DB_DIR / "data" / "_spec"
LONG_CSV = DB_DIR / "data" / "balanceofpayments2025q4_long.csv"
CDID_CSV = SPEC_DIR / "cdid_definitions.csv"
SPEC_CSV_OUT = SPEC_DIR / "specification.csv"

# Phase 3.2 §4 web-search 보강 노트의 시트·분류별 정의 사전.
# 각 시트의 unmapped CDID에 일괄 적용될 한국어 정의 토큰.
# (강의 슬라이드 직접 매핑된 행은 변경하지 않음 — 강의 자료 우선 원칙)
SHEET_DEFINITION_TEMPLATE: dict[str, str] = {
    "Table_A": (
        "영국 국제수지 잔액 요약 시트의 한 항목 — 강의 슬라이드 13(복식부기 항등성) + "
        "슬라이드 14(`CA = FA(broad)` 단순화 항등식) 근거. 잔액(net transactions) 표기. "
        "본 항목의 BPM6 표준 정의는 background/note/24~28 분류별 보강 참조."
    ),
    "Table_B": (
        "경상수지 본표(SA)의 한 항목 — 강의 슬라이드 5·14 `CA = G + S + PI + SI` 항등식 "
        "성분 또는 부표 분해(Credits/Debits/Balances/%GDP). 표준 정의: "
        "background/note/24(EBOPS 12분류 서비스) + 26(SITC 상품·BPM6 §10)."
    ),
    "Table_BX": (
        "경상수지(귀금속 제외) 보조표의 한 항목 — Table_B와 동일 4 부표 구조이나 "
        "비통화용 금(non-monetary gold) 거래분 차감. 표준 정의: "
        "background/note/26(SITC + BPM6 §10.13~§10.16 비통화용 금 정의)."
    ),
    "Table_C": (
        "경상수지(EU/non-EU 분해) 보조표의 한 항목 — Table_B 4 하위 + 합계를 거래 "
        "상대방 국가군(EU vs non-EU)으로 분해. Brexit(2020-02-01) 후 EU27 기준 재계산. "
        "표준 정의: background/note/24·26 + 23(지리적 분해)."
    ),
    "Table_D1_3": (
        "IIP·금융계정·투자소득 통합표 — 자산 측(Investment abroad)의 한 항목. "
        "BPM6 §6 FA 5분류 + §11 1차소득 cross-link. 표준 정의: "
        "background/note/25(FA 5분류 BPM6/BD5) + 27(1차소득 BPM6 §11)."
    ),
    "Table_D4_6": (
        "IIP·금융계정·투자소득 통합표 — 부채 측(Investment in the UK)의 한 항목. "
        "BPM6 §6 FA 5분류 + §11 1차소득 cross-link. 표준 정의: "
        "background/note/25 + 27."
    ),
    "Table_D7_9": (
        "IIP·금융계정·투자소득 통합표 — 순(Net = NAFA − NIL)의 한 항목. "
        "BPM6 §6 FA 5분류 + §11 1차소득 cross-link. 표준 정의: "
        "background/note/25 + 27."
    ),
    "Table_E": (
        "상품무역 시트(Trade in goods, 3 부표 Exports/Imports/Balance)의 한 항목 — "
        "강의 슬라이드 5 `재화의 수출입, net trade in merchandise goods`. SITC Rev.4 "
        "5묶음(0+1·2+4·3·5+6·7+8·9) + BPM6 §10 General merchandise 분류. "
        "표준 정의: background/note/26."
    ),
    "Table_F": (
        "서비스무역 시트의 한 항목 — 강의 슬라이드 5 `서비스의 수출입(운수·여행·로열티 "
        "등)`. EBOPS 2010 12분류(SA~SL — 가공·유지보수·운송·여행·건설·보험연금·금융·"
        "IP사용료·통신컴퓨터·기타비즈니스·개인문화·정부). 표준 정의: "
        "background/note/24."
    ),
    "Table_G": (
        "1차소득(본원소득) 시트의 한 항목 — 강의 슬라이드 5·6 `임금송금·배당·이자 등, "
        "대가성 소득의 순액`. BPM6 §11/§13: COE + 투자소득 3분해(직접투자·증권투자·"
        "기타투자) + 준비자산수익 + 기타. 표준 정의: background/note/27 §2."
    ),
    "Table_H": (
        "2차소득(이전소득) 시트의 한 항목 — 강의 슬라이드 5 `아무런 대가 없이 제공되는 "
        "원조·국제기구출연금 등`. BPM6 §12/§14: 일반정부(EU 분담금·UN·ODA) + 기타 "
        "부문(개인이전·workers' remittances 메모항목·보험료·기타). 표준 정의: "
        "background/note/27 §3."
    ),
    "Table_I": (
        "자본계정(Capital Account, very small) 시트의 한 항목 — 강의 슬라이드 5·7. "
        "BPM6 §13/§15: 자본이전(채무면제·자본 보조금·이민·일회성·기타) + NPNFA(토지·"
        "지하자원·마케팅·프랜차이즈·영업권). 표준 정의: background/note/27 §1."
    ),
    "Table_J": (
        "금융계정(NSA) 시트의 한 항목 — 강의 슬라이드 6·8·11·14 `자산·부채 소유권 변동`. "
        "BPM6 §6 FA 5분류(직접투자·증권투자·금융파생·기타투자·준비자산). sign_prefix "
        "운영 규칙으로 부호 반전 필요(부표1·3 + D1_3·D7_9 유량). 표준 정의: "
        "background/note/25."
    ),
    "Table_K": (
        "국제투자대조표(IIP, 분기말) 시트의 한 항목 — 강의 슬라이드 11·14·24·25 "
        "`Net IIP = 자산 − 부채 = NFA`. 단위 GBP **billion**(다른 시트 GBP million과 다름). "
        "표준 정의: background/note/25(BPM6 §6 + Reserve Assets EEA/HMT)."
    ),
    "Table_R1": (
        "직전 발표 대비 개정 — 잔액 요약 시트의 한 항목. 개정액 = 현재 발표값 − 직전 발표값 "
        "(+ 상향 / − 하향). 강의 자료 미수록 — 표준 정의: background/note/28(ONS National "
        "Accounts Revisions Policy + 분기 t+1/t+2/t+annual 일정)."
    ),
    "Table_R2": (
        "직전 발표 대비 개정 — 경상수지 4 부표(Credits/Debits/Balances/%GDP) 시트의 한 항목. "
        "강의 자료 미수록 — 표준 정의: background/note/28."
    ),
    "Table_R3": (
        "직전 발표 대비 개정 — 국제투자 9 부표(IIP·FA·Income × Asset/Liability/Net) 시트의 "
        "한 항목. 단위 GBP **billion**(R1·R2와 다름). 강의 자료 미수록 — "
        "표준 정의: background/note/28."
    ),
}

# 시트별 결측 표기 의미 (노트 15 §결측 표기 카탈로그 기반)
MISSING_MEANING_DEFAULT = (
    "`x` = 비공개·미가용(unavailable, ONS Notes 11번 명시) / "
    "빈 셀 = 시리즈 시작 이전 또는 자료 없음 / "
    "GAF [c]/[x]/[z]/[low] 미사용 / legacy `..`·`-` 미사용"
)

# 시트별 부호 규약 (노트 03 + 19 + 12 sign_convention_text 컬럼 기반)
SIGN_CONVENTION_MAP: dict[str, str] = {
    "Table_A": "잔액(net) — + 흑자 / − 적자 (강의 슬라이드 10·11)",
    "Table_B": "Credits + (자국으로 자금 유입) / Debits − (자국에서 자금 유출), Balances = Cr − Dr (강의 슬라이드 13)",
    "Table_BX": "Table_B와 동일 (Cr+/Dr−, Balances = Cr − Dr)",
    "Table_C": "Table_B와 동일, EU·non-EU 분해 합산 시 부호 상쇄 가능",
    "Table_D1_3": "BPM6 자산·부채 증감 기준 — 자산 측 sign_prefix 운영(부호 반전 필요)",
    "Table_D4_6": "BPM6 자산·부채 증감 기준 — 부채 측 sign_prefix 미운영",
    "Table_D7_9": "BPM6 자산·부채 증감 기준 — 순(Net = NAFA − NIL) sign_prefix 운영",
    "Table_E": "Exports +, Imports − (절대값 게재), Balance = Ex − Im (강의 슬라이드 5)",
    "Table_F": "Exports +, Imports − (절대값 게재), Balance = Ex − Im",
    "Table_G": "Credit + / Debit −, Balance = Cr − Dr (BPM6 자산·부채 증감 기준)",
    "Table_H": "Credit + / Debit −, Balance = Cr − Dr",
    "Table_I": "Credit + / Debit −, Balance = Cr − Dr (very small — KA=0 단순화 가정 적용 가능)",
    "Table_J": (
        "BPM6 자산·부채 증감 기준 (강의 슬라이드 8) — 자산 증가 + / 부채 증가 +. "
        "음수 FA 합계 = 부채 순증 = 외국으로부터 순자본 유입(노트 03 §영국 적용 주의점). "
        "sign_prefix 부표1·3 + D1_3·D7_9 유량 운영 (부호 반전 필요)"
    ),
    "Table_K": "BPM6 자산·부채 증감 기준 — Reserve BoP/IIP 부호 비대칭(슬라이드 26)",
    "Table_R1": "Revisions = 현재 발표값 − 직전 발표값 (+ 상향 / − 하향)",
    "Table_R2": "Revisions = 현재 − 직전 (+ 상향 / − 하향)",
    "Table_R3": "Revisions = 현재 − 직전 (+ 상향 / − 하향)",
}


def build_time_range_index(long_csv: Path) -> dict[tuple[str, str, str], tuple[str, str]]:
    """long-form CSV에서 (sheet, sub_table, item_code1) 키별 START_TIME / END_TIME 추출.

    숫자 셀(data_value 비어있지 않음)에 한정해서 시점 범위를 산출.
    """
    print(f"[step 1/4] long-form CSV에서 시계열 시점 범위 추출 — {long_csv}")
    time_by_key: dict[tuple[str, str, str], list[str]] = defaultdict(list)
    with long_csv.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            if not row["data_value"].strip():
                continue
            key = (row["sheet"], row["sub_table"], row["item_code1"])
            time_by_key[key].append(row["time"])

    # 각 키에 대해 min·max 시점 산출
    time_range: dict[tuple[str, str, str], tuple[str, str]] = {}
    for key, times in time_by_key.items():
        # 정렬: YYYY · YYYYQn 모두 사전순 비교로 충분
        times_sorted = sorted(times)
        time_range[key] = (times_sorted[0], times_sorted[-1])
    print(f"  → {len(time_range)}개 (sheet, sub_table, item_code1) 키에서 시점 범위 추출")
    return time_range


def supplement_definition(row: dict[str, str]) -> str:
    """unmapped 행의 ko_definition을 시트별 보강 정의로 채움.

    이미 ko_definition이 있는 행은 그대로 반환.
    """
    existing = row.get("ko_definition", "").strip()
    if existing:
        return existing
    sheet = row.get("sheet", "")
    template = SHEET_DEFINITION_TEMPLATE.get(sheet)
    if not template:
        return ""
    # 시트 기반 일괄 정의 + 본 CDID의 분류·column_label을 첨부
    column_label = row.get("column_label", "").strip()
    classification = row.get("classification", "").strip()
    suffix_parts = []
    if classification:
        suffix_parts.append(f"분류: {classification}")
    if column_label:
        suffix_parts.append(f"원문 라벨: {column_label}")
    suffix = f" ({'; '.join(suffix_parts)})" if suffix_parts else ""
    return f"{template}{suffix}"


def build_specification() -> None:
    """13컬럼 명세서 CSV 생성."""
    time_range = build_time_range_index(LONG_CSV)

    print(f"[step 2/4] cdid_definitions.csv 읽기 — {CDID_CSV}")
    with CDID_CSV.open("r", encoding="utf-8", newline="") as f:
        cdid_rows = list(csv.DictReader(f))
    print(f"  → {len(cdid_rows)}행")

    print("[step 3/4] 명세서 13컬럼 매핑·산출")
    spec_fieldnames = [
        "STAT_CODE",
        "STAT_NAME",
        "ITEM_CODE1",
        "ITEM_CODE2",
        "ITEM_CODE3",
        "ITEM_CODE4",
        "ITEM_NAME_EN",
        "ITEM_NAME_KO",
        "DEFINITION",
        "UNIT_NAME",
        "CYCLE",
        "START_TIME",
        "END_TIME",
        "MISSING_MEANING",
        "SIGN_CONVENTION",
        "SOURCE",
    ]

    spec_rows: list[dict[str, str]] = []
    for row in cdid_rows:
        sheet = row["sheet"]
        sub_table = row["sub_table"]
        item_code1 = row["item_code1"]
        # STAT_CODE: PLAN.md §0.3 분야 접두 규약
        stat_code = f"UK_BoP_{sheet}_sub{sub_table}"
        # STAT_NAME: 20회차 한국어 statname 매핑 (시트 단위)
        # 본 ETL에서는 시트별 한국어 명칭만 채우고, 부표별 세분은 명세서 후속 단계로 위임
        stat_name = _stat_name_for_sheet(sheet, sub_table)
        # 한국어 정의 보강
        ko_definition = supplement_definition(row)
        # 시계열 시점 범위
        key = (sheet, sub_table, item_code1)
        start_time, end_time = time_range.get(key, ("", ""))
        # CYCLE: 시점 형식으로 추정 (Q 포함이면 분기·아니면 연간)
        cycle = "Q" if any("Q" in t for t in (start_time, end_time)) else "A"
        # MISSING_MEANING: 공통 적용
        missing_meaning = MISSING_MEANING_DEFAULT
        # SIGN_CONVENTION: 시트별
        sign_convention = SIGN_CONVENTION_MAP.get(sheet, "")
        spec_rows.append(
            {
                "STAT_CODE": stat_code,
                "STAT_NAME": stat_name,
                "ITEM_CODE1": item_code1,
                "ITEM_CODE2": row.get("item_code2", ""),
                "ITEM_CODE3": row.get("item_code3", ""),
                "ITEM_CODE4": "",  # Phase 3 위임
                "ITEM_NAME_EN": row.get("column_label", ""),
                "ITEM_NAME_KO": row.get("ko_name", ""),
                "DEFINITION": ko_definition,
                "UNIT_NAME": row.get("unit", ""),
                "CYCLE": cycle,
                "START_TIME": start_time,
                "END_TIME": end_time,
                "MISSING_MEANING": missing_meaning,
                "SIGN_CONVENTION": sign_convention,
                "SOURCE": row.get("source", ""),
            }
        )

    print(f"[step 4/4] specification.csv 기록 — {SPEC_CSV_OUT}")
    SPEC_CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with SPEC_CSV_OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=spec_fieldnames)
        writer.writeheader()
        writer.writerows(spec_rows)
    print(f"  → 명세서 {len(spec_rows)}행 × {len(spec_fieldnames)}컬럼 산출 완료")

    # 정의 채움률 검증
    filled = sum(1 for r in spec_rows if r["DEFINITION"].strip())
    print(f"  ko_definition 채움률: {filled}/{len(spec_rows)} ({filled/len(spec_rows)*100:.1f}%)")


def _stat_name_for_sheet(sheet: str, sub_table: str) -> str:
    """시트·부표별 한국어 STAT_NAME 매핑(20회차 + 23회차 정의 기반)."""
    base_map = {
        "Table_A": "영국 국제수지 잔액 요약",
        "Table_B": "영국 경상수지 본표(SA)",
        "Table_BX": "영국 경상수지(귀금속 제외)",
        "Table_C": "영국 경상수지 (EU/non-EU)",
        "Table_D1_3": "영국 IIP·금융계정·투자소득 — 자산",
        "Table_D4_6": "영국 IIP·금융계정·투자소득 — 부채",
        "Table_D7_9": "영국 IIP·금융계정·투자소득 — 순",
        "Table_E": "영국 상품무역",
        "Table_F": "영국 서비스무역",
        "Table_G": "영국 1차소득(본원소득)",
        "Table_H": "영국 2차소득(이전소득)",
        "Table_I": "영국 자본수지",
        "Table_J": "영국 금융계정(NSA)",
        "Table_K": "영국 국제투자대조표(분기말)",
        "Table_R1": "영국 개정 요약(잔액)",
        "Table_R2": "영국 경상수지 개정",
        "Table_R3": "영국 국제투자 개정",
    }
    base = base_map.get(sheet, sheet)
    return f"{base} (부표 {sub_table})"


if __name__ == "__main__":
    print("Phase 3.4 §1·§2·§3 — 데이터 명세서 생성 ETL")
    print("=" * 60)
    build_specification()
    print("=" * 60)
    print("완료.")
