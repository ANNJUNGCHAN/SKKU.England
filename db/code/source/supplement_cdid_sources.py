"""
Phase 3.2 §5 — CDID 명세서 source 컬럼 보강 ETL.

Phase 3.2 §4 web-search 6 라운드(노트 24~28)에서 확보한 분류별 1차 출처를
`db/data/_spec/cdid_definitions.csv` 및 `cdid_definitions_unmapped.csv`의
source 컬럼에 시트 단위 매핑으로 추가한다.

원칙
- ko_definition이 비어 있는 unmapped CDID 행에만 source 컬럼 보강 (강의 슬라이드 직접
  매핑된 193건은 변경하지 않음 — 강의 자료 우선 원칙 유지).
- 본 ETL은 source 컬럼에 ` + background/note/<NN>(<요지>)` 토큰을 append한다.
  값(value)·정의(ko_definition)·이름(ko_name)은 변경하지 않는다.
- 멱등 동작: 이미 토큰이 들어 있으면 재추가하지 않는다.

산출물
- `db/data/_spec/cdid_definitions.csv` 갱신 (in-place, 원본 행 수·컬럼 수 불변)
- `db/data/_spec/cdid_definitions_unmapped.csv` 갱신 (동일 규칙)

실행
    env/Scripts/python.exe db/code/source/supplement_cdid_sources.py
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

# Windows cp949 콘솔에서 한국어·em dash 출력 시 UnicodeEncodeError 방지
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

# 시트 → Phase 3.2 §4 보강 노트 매핑.
# 각 값은 source 컬럼에 추가될 한국어 reference 토큰.
SHEET_NOTE_MAP: dict[str, str] = {
    "Table_A": "24·25·26·27·28(전체 잔액 요약 — 모든 분류 cross-reference)",
    "Table_B": "24·26(EBOPS 12분류 서비스 + SITC 상품·BPM6 §10 Goods)",
    "Table_BX": "26(SITC + BPM6 비통화용 금 §10.13~§10.16)",
    "Table_C": "24·26(EBOPS 서비스 + SITC 상품 EU/non-EU 분해)",
    "Table_D1_3": "25(FA 5분류 IIP+FA+투자소득 — BPM6 §6 + Appendix 4)",
    "Table_D4_6": "25(FA 5분류 IIP+FA+투자소득 — BPM6 §6 + Appendix 4)",
    "Table_D7_9": "25(FA 5분류 IIP+FA+투자소득 — BPM6 §6 + Appendix 4)",
    "Table_E": "26(SITC Rev.4 + BPM6 §10 + CIF/FOB 조정)",
    "Table_F": "24(EBOPS 2010 12분류 SA~SL)",
    "Table_G": "27(1차소득 — BPM6 §11/§13: COE + 투자소득 3분해 + 준비자산수익 + 기타)",
    "Table_H": "27(2차소득 — BPM6 §12/§14: 일반정부·기타 부문 무상이전)",
    "Table_I": "27(자본계정 — BPM6 §13/§15: 자본이전 + NPNFA)",
    "Table_J": "25(금융계정 NSA — BPM6 §6 FA 5분류 + sign_prefix 운영 규칙)",
    "Table_K": "25(IIP — BPM6 §6 + Reserve Assets EEA/HMT)",
    "Table_R1": "28(ONS National Accounts Revisions Policy — Summary balances)",
    "Table_R2": "28(ONS Revisions Policy — Current account 4 sub-tables)",
    "Table_R3": "28(ONS Revisions Policy — IIP 9 sub-tables)",
}

SPEC_DIR = Path(__file__).resolve().parents[2] / "data" / "_spec"
TARGETS = [
    SPEC_DIR / "cdid_definitions.csv",
    SPEC_DIR / "cdid_definitions_unmapped.csv",
]


def supplement_source(row: dict[str, str]) -> bool:
    """source 컬럼에 시트 매핑 토큰을 append.

    ko_definition이 비어 있는 unmapped 행에만 적용한다.
    이미 동일 토큰이 들어 있으면 재추가하지 않는다(멱등).

    Returns:
        True: 행이 갱신됨 (변경 발생)
        False: 행이 그대로 유지됨 (멱등 또는 매핑 대상 외)
    """
    # 강의 슬라이드 직접 매핑된 행은 변경하지 않음 — 강의 자료 우선 원칙 유지
    if row.get("ko_definition", "").strip():
        return False

    sheet = row.get("sheet", "")
    note_token = SHEET_NOTE_MAP.get(sheet)
    if not note_token:
        return False

    # 토큰 헤더 — source 컬럼에 추가될 prefix 식별자
    token_prefix = "background/note/"
    addition = f" + {token_prefix}{note_token}"

    # 멱등 점검: 이미 동일 토큰이 들어 있으면 skip
    current_source = row.get("source", "")
    if token_prefix in current_source:
        return False

    row["source"] = current_source + addition
    return True


def process_csv(path: Path) -> tuple[int, int]:
    """단일 CSV 파일을 in-place 갱신.

    Returns:
        (전체 행 수, 변경된 행 수)
    """
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    # 갱신 대상 행만 source 컬럼 보강
    updated = sum(1 for r in rows if supplement_source(r))

    # CSV에 다시 기록 (행 수·컬럼 수·다른 값은 그대로)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return len(rows), updated


def main() -> None:
    print("Phase 3.2 §5 — CDID source 컬럼 보강 ETL")
    print("=" * 60)
    for path in TARGETS:
        if not path.exists():
            print(f"[skip] 파일 없음: {path}")
            continue
        total, updated = process_csv(path)
        print(f"[ok] {path.name}: 전체 {total}행 / 갱신 {updated}행")
    print("=" * 60)
    print("완료.")


if __name__ == "__main__":
    main()
