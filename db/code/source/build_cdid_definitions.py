"""Phase 3.2 CDID 정의 사전 자동 채움 스크립트.

목적
----
db/CHECKLIST.md §3.2 1·2·3번 항목을 일괄 충족하는 1차 한국어 정의 사전을 생성한다.

- 입력:
  - background/note/13_cdid_dictionary.csv (512행: sheet/sub_table/column_position/
    column_label/cdid/sign_prefix/unit/table_code/classification/notes)
  - db/data/_inventory/15_master_inventory.csv (시트 단위 메타)
- 출력:
  - db/data/_spec/cdid_definitions.csv  — 13회차 사전 + 한국어 컬럼 5종 추가
  - db/data/_spec/cdid_definitions_unmapped.csv — 자동 매핑 실패 행 별도 목록
  - db/data/_spec/cdid_definitions.md — 사람 검토용 안내

자동 매핑 정책 (21회차 §5.1 권고)
---------------------------------
1. ITEM_CODE2 = LVL1·LVL2 합성 코드 (시트·부표 단위, 자동률 100%).
2. ITEM_CODE3 = LVL3 합계 라벨 (CDID 단위 사전 매핑, 22 합계 라인).
3. column_label 영문 표제어 → 한국어 정규화 사전(EN_TO_KO_LABEL).
4. ko_name = column_label 한국어 정규화 결과 + 시트 분류 보조.
5. ko_definition = 합계 시리즈는 강의 항등식 1줄 인용, 비합계는 빈 값.
6. source = 강의 슬라이드 + 회차 노트 출처 자동 부여.

매핑 실패 사례(약 30%, 주로 SITC·EBOPS 영국 특화·EU 기관 거래)는
unmapped CSV로 분리 → Phase 3.2의 후속 background-search·web-search로 위임.

원본 보존
----------
13_cdid_dictionary.csv·15_master_inventory.csv 모두 read-only.

재현
----
env/Scripts/python.exe db/code/source/build_cdid_definitions.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC_DICT = ROOT / "background" / "note" / "13_cdid_dictionary.csv"
INV = ROOT / "db" / "data" / "_inventory" / "15_master_inventory.csv"
OUT_DIR = ROOT / "db" / "data" / "_spec"
OUT_CSV = OUT_DIR / "cdid_definitions.csv"
OUT_UNMAPPED = OUT_DIR / "cdid_definitions_unmapped.csv"

# =============================================================================
# 영문 column_label → 한국어 정규화 사전(강의 자료 + 21회차 LVL3 코드표 기반).
# 출처: 21_item_hierarchy.md §2.3 + 02_bop_components.md + 06_financial_account_categories.md.
# =============================================================================
EN_TO_KO_LABEL: dict[str, str] = {
    # CA 합계·구성
    "Current balance": "경상수지 합계",
    "Capital balance": "자본수지 합계",
    "Trade in goods": "상품무역",
    "Trade in services": "서비스무역",
    "Total trade": "상품·서비스 합계",
    "Goods balance": "상품수지",
    "Total goods": "상품수지 합계",
    "Total services": "서비스수지 합계",
    "Total goods balance": "상품수지 잔액",
    "Total services balance": "서비스수지 잔액",
    # 1차소득(PI) 구성
    "Primary income, Compensation of employees": "1차소득 - 노동소득(보수)",
    "Primary income, Investment income": "1차소득 - 투자소득",
    "Primary income, Other primary income": "1차소득 - 기타",
    "Primary income, Total": "1차소득 합계",
    "Compensation of employees": "노동소득(보수)",
    "Investment income": "투자소득",
    "Investment income, Direct investment": "투자소득 - 직접투자",
    "Investment income, Portfolio investment": "투자소득 - 증권투자",
    "Investment income, Portfolio investment, Equity": "투자소득 - 증권투자(주식)",
    "Investment income, Portfolio investment, Debt securities": "투자소득 - 증권투자(채권)",
    "Investment income, Portfolio investment, Total": "투자소득 - 증권투자 합계",
    "Investment income, Other investment": "투자소득 - 기타투자",
    "Investment income, Reserve assets": "투자소득 - 준비자산",
    "Investment income, Total": "투자소득 합계",
    "Other primary income": "기타 1차소득",
    "Primary income": "1차소득",
    # 2차소득(SI) 구성
    "Secondary income, General government": "2차소득 - 일반정부",
    "Secondary income, Central government": "2차소득 - 중앙정부",
    "Secondary income, Other sectors": "2차소득 - 기타부문",
    "Secondary income, Total": "2차소득 합계",
    "Secondary income": "2차소득",
    # KA(자본수지) 구성
    "Central government, Debt forgiveness": "중앙정부 - 채무면제",
    "Central government, Other capital transfers": "중앙정부 - 기타 자본이전",
    "Other sectors, Debt forgiveness": "기타부문 - 채무면제",
    "Other sectors, Other capital transfers": "기타부문 - 기타 자본이전",
    "Capital transfers, Total": "자본이전 합계",
    "Acquisition / disposal of non-produced non-financial assets": "비생산비금융자산 취득·처분",
    "Capital account": "자본계정",
    # FA(금융계정) 5분류
    "Direct investment": "직접투자",
    "Direct investment, Equity capital": "직접투자 - 지분자본",
    "Direct investment, Equity capital, excluding reinvestment of earnings": "직접투자 - 지분자본(재투자수익 제외)",
    "Direct investment, Reinvestment of earnings": "직접투자 - 재투자수익",
    "Direct investment, Debt instruments": "직접투자 - 부채성거래",
    "Direct investment, Total": "직접투자 합계",
    "Portfolio investment": "증권투자",
    "Portfolio investment, Equity": "증권투자 - 지분증권",
    "Portfolio investment, Equity & investment fund shares": "증권투자 - 지분·투자펀드 지분",
    "Portfolio investment, Debt securities": "증권투자 - 부채증권",
    "Portfolio investment, Total": "증권투자 합계",
    "Financial derivatives": "파생금융상품",
    "Financial derivatives (net)": "파생금융상품(순)",
    "Other investment": "기타투자",
    "Other investment, Total": "기타투자 합계",
    "Reserve assets": "준비자산",
    "Total financial account": "금융계정 합계",
    "Total net financial account transactions": "순 금융계정 거래 합계",
    "Total financial account transactions": "금융계정 거래 합계",
    # IIP(국제투자대조표) 분류
    "International investment position": "국제투자대조표",
    "Net international investment position": "순 국제투자대조표",
    "UK assets": "영국 자산(IIP 자산)",
    "UK liabilities": "영국 부채(IIP 부채)",
    "Net IIP": "순 IIP(NIIP)",
    "Investment abroad": "대외투자(자산)",
    "Investment in the UK": "대내투자(부채)",
    "Net investment": "순투자",
    # 통계 불일치
    "Net errors and omissions": "오차 및 누락(NEO)",
    # SITC(상품) 9분류
    "Food, beverages and tobacco": "식료품·음료·담배",
    "Basic materials": "기초 원자재",
    "Oil": "석유",
    "Other fuels": "기타 연료",
    "Semi-manufactured goods": "반제품",
    "Finished manufactured goods": "완제품",
    "Unspecified goods": "미분류 상품",
    "Goods excluding precious metals": "상품(귀금속 제외)",
    "Total trade in goods, excluding precious metals": "상품무역 합계(귀금속 제외)",
    # EBOPS(서비스) 12분류
    "Manufacturing services on physical inputs owned by others": "위탁가공 서비스",
    "Manufacturing & maintenance": "제조 및 유지보수",
    "Maintenance and repair services": "유지·보수 서비스",
    "Transport": "운송",
    "Travel": "여행",
    "Construction": "건설",
    "Insurance and pension services": "보험·연금 서비스",
    "Financial": "금융 서비스",
    "Financial services": "금융 서비스",
    "Charges for the use of intellectual property": "지식재산권 사용료",
    "Telecommunications, computer, and information services": "통신·컴퓨터·정보 서비스",
    "Other business services": "기타 사업 서비스",
    "Personal, cultural, and recreational services": "개인·문화·여가 서비스",
    "Government goods and services": "정부 서비스",
}

# 시트(분류 코드) → LVL1·2 한국어 분류명(자동 부여용 폴백 라벨).
SHEET_KO_FALLBACK: dict[str, str] = {
    "Table_A": "국제수지 요약",
    "Table_B": "경상수지 본표",
    "Table_BX": "경상수지 본표(귀금속 제외)",
    "Table_C": "경상수지(EU/non-EU 분해)",
    "Table_D1_3": "대외투자(자산)",
    "Table_D4_6": "대내투자(부채)",
    "Table_D7_9": "순대외투자",
    "Table_E": "상품무역",
    "Table_F": "서비스무역",
    "Table_G": "1차소득",
    "Table_H": "2차소득",
    "Table_I": "자본수지",
    "Table_J": "금융계정 거래(flow)",
    "Table_K": "국제투자대조표(stock)",
    "Table_R1": "국제수지 개정 요약",
    "Table_R2": "경상수지 개정",
    "Table_R3": "국제투자 개정",
}

# 합계 시리즈에 적용할 한국어 정의 1줄(강의 항등식 인용).
# 출처: 21회차 §5.4 + 22회차 §3 항등식 검증.
ITEM_CODE3_TOT_DEFINITION: dict[str, str] = {
    "CA.TOT": "경상수지 합계 — 강의 슬라이드 14 항등식 CA = 상품수지 + 서비스수지 + 1차소득 + 2차소득의 좌변.",
    "CA.G.G_TOT": "상품수지 합계 — 재화의 수출입 차액(강의 슬라이드 5·21).",
    "CA.S.S_TOT": "서비스수지 합계 — EBOPS 12분류 서비스 거래의 합산(강의 슬라이드 5).",
    "CA.PI.PI_TOT": "1차소득 합계 — 노동소득·투자소득·기타 1차소득 합산(강의 슬라이드 5·9).",
    "CA.PI.PI_INV_TOT": "투자소득 합계 — 직접·증권·기타·준비자산 투자에서 발생한 소득 합산(강의 슬라이드 25).",
    "CA.SI.SI_TOT": "2차소득 합계 — 정부·기타부문의 이전소득 합산(강의 슬라이드 5·14).",
    "KA.KA_TOT": "자본수지 합계 — 자본이전 + 비생산비금융자산 취득·처분(강의 슬라이드 5·7·14).",
    "FA.DI.DI_TOT": "직접투자 합계 — 외국기업 경영참가 목적 투자(강의 슬라이드 6, OECD BD4 기준).",
    "FA.PIF.PIF_TOT": "증권투자 합계 — 주식·채권 등 증권 거래(강의 슬라이드 6).",
    "FA.FD.FD_NET": "파생금융상품(순) — 강의 슬라이드 6·14의 net financial derivatives 항.",
    "FA.OI.OI_TOT": "기타투자 합계 — 대출·차입·무역신용·예금 등(강의 슬라이드 6).",
    "FA.IR.IR_TOT": "준비자산 합계 — 통화당국 보유 외환·금·SDR(강의 슬라이드 6·12).",
    "FA.FA_TOT": "금융계정 합계(broad) — 강의 슬라이드 14 식 FA = NAFA - NIL + Net derivatives.",
    "IIP.DI": "IIP 직접투자 — 분기말 잔액(강의 슬라이드 25).",
    "IIP.PIF": "IIP 증권투자 — 분기말 잔액(강의 슬라이드 25).",
    "IIP.FD": "IIP 파생금융상품 — 분기말 잔액.",
    "IIP.OI": "IIP 기타투자 — 분기말 잔액.",
    "IIP.IR": "IIP 준비자산 — 분기말 잔액.",
    "IIP.IIPA.IIPA_TOT": "IIP 자산 합계(UK External Assets) — 강의 슬라이드 25.",
    "IIP.IIPL.IIPL_TOT": "IIP 부채 합계(UK External Liabilities) — 강의 슬라이드 25.",
    "IIP.NIIP": "순 국제투자대조표 NIIP = IIPA − IIPL — 강의 슬라이드 11·24·25(NFA 정의).",
    "NEO.NEO": "오차 및 누락(NEO) — 통계 불일치 보정(강의 슬라이드 6·13·14).",
}


# 21회차 §5에서 도입한 ITEM_CODE2/3 자동 매핑 사전을 본 스크립트도 참조.
# 통합 CSV ETL과 동일 매핑을 유지하기 위해 build_unified_csv.py에서 import.
def _import_unified_mappings():
    """build_unified_csv.py의 ITEM_CODE2/3 매핑을 그대로 재사용."""
    import sys
    sys.path.insert(0, str(ROOT / "db" / "code" / "source"))
    from build_unified_csv import ITEM_CODE2_BY_SHEET_SUB, ITEM_CODE3_TOT
    return ITEM_CODE2_BY_SHEET_SUB, ITEM_CODE3_TOT


# 정규식: column_label에서 끝부분 ", Total"/"Net total" 같은 합계 표지 추출용.
TOT_RE = re.compile(r"\b(?:Total|balance|Net total)\b", re.IGNORECASE)


def normalize_label_to_ko(label: str) -> str:
    """column_label 영문 표제어를 한국어로 정규화. 매칭 실패 시 빈 값."""
    if not label:
        return ""
    s = label.strip()
    # 정확 매칭 우선.
    if s in EN_TO_KO_LABEL:
        return EN_TO_KO_LABEL[s]
    # 부분 매칭(앞부분이 정확 매칭되는 경우 — 1차소득 하위 등).
    for k, v in EN_TO_KO_LABEL.items():
        if s.startswith(k + ","):
            return v
    return ""


def main() -> None:
    """본 사전 생성 진입점."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ITEM_CODE2_MAP, ITEM_CODE3_MAP = _import_unified_mappings()

    rows: list[dict] = []
    with SRC_DICT.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    out_fields = [
        "sheet",
        "sub_table",
        "column_position",
        "column_label",
        "cdid",
        "sign_prefix",
        "unit",
        "table_code",
        "classification",
        "notes",
        "item_code1",
        "item_code2",
        "item_code3",
        "ko_name",
        "ko_definition",
        "source",
    ]

    out_rows: list[dict] = []
    unmapped: list[dict] = []
    for r in rows:
        sheet = r["sheet"]
        sub_table = r["sub_table"]
        cdid = r["cdid"]
        label = r["column_label"]
        sign = r["sign_prefix"]
        # item_code1: sign_prefix=true인 경우 `-CDID` 형태로 통합 CSV와 동일 표기.
        item_code1 = ("-" + cdid) if sign == "true" else cdid
        # item_code2: 시트·부표 단위 자동 매핑(21회차 §3.1 자동률 100%).
        item_code2 = ITEM_CODE2_MAP.get((sheet, sub_table), "")
        # item_code3: CDID 단위 합계 매핑(21회차 §5 자동률 약 70% 중 합계 우선).
        item_code3 = ITEM_CODE3_MAP.get(cdid, "")
        # 한국어 명칭: column_label 영문 정규화 + 폴백.
        ko_name = normalize_label_to_ko(label)
        if not ko_name:
            ko_name = SHEET_KO_FALLBACK.get(sheet, "")
        # 한국어 정의: ITEM_CODE3 합계 라벨에 매핑된 정의가 있으면 인용, 아니면 빈 값.
        ko_definition = ITEM_CODE3_TOT_DEFINITION.get(item_code3, "")
        # source: 강의 슬라이드·노트 자동 부여.
        if item_code3:
            source = "강의 슬라이드(21·22회차 검증) + 13회차 CDID 사전"
        elif ko_name:
            source = "13회차 CDID 사전(영문 column_label) + 21회차 LVL3 코드표"
        else:
            source = "13회차 CDID 사전(영문 column_label만)"

        out_row = {
            **r,
            "item_code1": item_code1,
            "item_code2": item_code2,
            "item_code3": item_code3,
            "ko_name": ko_name,
            "ko_definition": ko_definition,
            "source": source,
        }
        out_rows.append(out_row)
        # 매핑 실패(한국어 정의 부재) 행은 별도 인벤토리. Phase 3.2 후속 작업 위임 대상.
        # ko_name은 시트 폴백 라벨로라도 채워지므로, 진짜 누락은 ko_definition 기준으로 식별.
        if not ko_definition:
            unmapped.append(out_row)

    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        w.writeheader()
        w.writerows(out_rows)
    with OUT_UNMAPPED.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        w.writeheader()
        w.writerows(unmapped)

    # 통계.
    total = len(out_rows)
    n_ko_name = sum(1 for r in out_rows if r["ko_name"])
    n_ko_def = sum(1 for r in out_rows if r["ko_definition"])
    print(
        f"OK rows={total} ko_name={n_ko_name} ({100*n_ko_name/total:.1f}%) "
        f"ko_definition={n_ko_def} ({100*n_ko_def/total:.1f}%) "
        f"unmapped={len(unmapped)}"
    )


if __name__ == "__main__":
    main()
