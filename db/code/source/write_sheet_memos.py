"""Phase 2.3 시트별 한국어 메타 메모 작성 스크립트.

목적
----
db/CHECKLIST.md §2.3 8개 항목을 일괄 충족한다. 각 시트(20개) 단위로 한국어 메모
1건을 db/data/balanceofpayments2025q4_<table_code_lower>.md(본표 17) 또는
balanceofpayments2025q4_<sheet_lower>.md(메타 시트 3)로 출력한다. 부표 단위
가로형 CSV 63건은 시트 단위 메모 1건이 모두 책임진다.

메모 8 섹션 (CHECKLIST §2.3 충족):
1. 원본 위치 (시트명·xlsx 경로)
2. 구조 변경 절차 (생성 스크립트·재현 절차)
3. 컬럼 정의 (time_period + CDID 컬럼 N개. 표로 정리)
4. 결측 의미 (13·19회차 검증 권고 한 문장)
5. 부호 규약 (19회차 §2 권고 한 문장 + 시트 분류별 분기)
6. 부표 분리 단위 (18회차 §2 카탈로그 인용)
7. 강의 위계 매핑 (18회차 §3 매트릭스 인용)
8. 추가 항목(시트별):
   - Table_BX → 귀금속 보정 표와 본표(Table_B) 관계 (19회차 §5)
   - Table_R1·R2·R3 → 통계 개정 시트 역할 (19회차 §6)
   - 메타 시트 3개 → 시트 역할(목차·주석·요약) 한국어 안내

원본 보존
----------
db/source/* 미접근. 입력은 마스터 인벤토리(15)·ETL 로그·18·19회차 자료뿐.

재현
----
env/Scripts/python.exe db/code/source/write_sheet_memos.py
"""
from __future__ import annotations

import csv
from pathlib import Path

# 저장소 루트 = 본 스크립트 기준 3단계 위.
ROOT = Path(__file__).resolve().parents[3]
INV = ROOT / "db" / "data" / "_inventory" / "15_master_inventory.csv"
LOG = ROOT / "db" / "data" / "_etl_log" / "phase2_1_split_log.csv"
OUT_DIR = ROOT / "db" / "data"

# 시트별 1행 부표 차원 사전(18회차 §2 카탈로그 발췌).
SUBTABLE_DIMENSIONS: dict[str, dict] = {
    "Table_A": {"axis": "CA(SA) / CA(NSA) / FA 3분할", "labels": ["A.1 CA SA", "A.2 CA NSA", "A.3 FA NSA"], "hierarchy": "CA + FA 통합 요약"},
    "Table_B": {"axis": "Cr / Dr / Bal + %GDP 4분할", "labels": ["B.1 CA Credits", "B.2 CA Debits", "B.3 CA Balances", "B.4 CA Balances %GDP"], "hierarchy": "CA 4분류 합계"},
    "Table_BX": {"axis": "Cr / Dr / Bal + %GDP 4분할 (귀금속 제외)", "labels": ["BX.1 CA Cr (excl. precious metals)", "BX.2 CA Dr (excl. precious metals)", "BX.3 CA Bal (excl. precious metals)", "BX.4 CA Bal %GDP (excl. precious metals)"], "hierarchy": "CA 4분류 (귀금속 제외)"},
    "Table_C": {"axis": "EU/non-EU × Cr/Dr/Bal 6분할", "labels": ["C.1 EU Cr", "C.2 EU Dr", "C.3 EU Bal", "C.4 non-EU Cr", "C.5 non-EU Dr", "C.6 non-EU Bal"], "hierarchy": "CA × 지리(영국 특화)"},
    "Table_D1_3": {"axis": "IIP / Flow / Income 3분할 (자산 측)", "labels": ["D.1 IIP abroad", "D.2 FA tx abroad", "D.3 Income abroad"], "hierarchy": "IIP·FA·1차소득 자산"},
    "Table_D4_6": {"axis": "IIP / Flow / Income 3분할 (부채 측)", "labels": ["D.4 IIP in UK", "D.5 FA tx in UK", "D.6 Income in UK"], "hierarchy": "IIP·FA·1차소득 부채"},
    "Table_D7_9": {"axis": "IIP / Flow / Income 3분할 (순)", "labels": ["D.7 Net IIP", "D.8 Net FA tx", "D.9 Net Income"], "hierarchy": "IIP·FA·1차소득 순"},
    "Table_E": {"axis": "Exports / Imports / Balances 3분할", "labels": ["E.1 Exports of goods", "E.2 Imports of goods", "E.3 Balances of goods"], "hierarchy": "상품수지 G"},
    "Table_F": {"axis": "Exports / Imports / Balances 3분할", "labels": ["F.1 Exports of services", "F.2 Imports of services", "F.3 Balances of services"], "hierarchy": "서비스수지 S (EBOPS 12)"},
    "Table_G": {"axis": "Cr / Dr / Bal 3분할", "labels": ["G.1 PI Credits", "G.2 PI Debits", "G.3 PI Balances"], "hierarchy": "1차소득 PI"},
    "Table_H": {"axis": "Cr / Dr / Bal 3분할", "labels": ["H.1 SI Credits", "H.2 SI Debits", "H.3 SI Balances"], "hierarchy": "2차소득 SI"},
    "Table_I": {"axis": "Cr / Dr / Bal 3분할", "labels": ["I.1 KA Credits", "I.2 KA Debits", "I.3 KA Balances"], "hierarchy": "자본수지 KA"},
    "Table_J": {"axis": "NAFA / NIL / Net 3분할", "labels": ["J.1 NAFA", "J.2 NIL", "J.3 Net Transactions"], "hierarchy": "금융계정 5분류 양면 (슬라이드 14 식 1:1 동형)"},
    "Table_K": {"axis": "Assets / Liabilities / Net 3분할 (stock)", "labels": ["K.1 UK Assets", "K.2 UK Liabilities", "K.3 Net IIP"], "hierarchy": "IIP 양면 잔액"},
    "Table_R1": {"axis": "CA(SA) / CA(NSA) / FA 3분할 (개정값)", "labels": ["R1.1 CA SA rev", "R1.2 CA NSA rev", "R1.3 FA rev"], "hierarchy": "개정 운영 정보"},
    "Table_R2": {"axis": "Cr / Dr / Bal + %GDP 4분할 (개정값)", "labels": ["R2.1 Cr rev", "R2.2 Dr rev", "R2.3 Bal rev", "R2.4 %GDP rev"], "hierarchy": "개정 운영 정보"},
    "Table_R3": {"axis": "{abroad/in UK/net} × {IIP/Flow/Income} 3×3", "labels": [f"R3.{i+1}" for i in range(9)], "hierarchy": "IIP·FA·소득 양면×3 변동"},
}

# 시트별 추가 안내(귀금속·개정·메타).
EXTRA_NOTES: dict[str, str] = {
    "Table_BX": """## 8. 귀금속(비통화용 금) 보정 표와 본표(Table_B)의 관계

본 시트(Table_BX)는 Table_B에서 귀금속(비통화용 금·플래티넘·팔라듐·은) 거래를 제외한 보조표이다. ONS xlsx Notes 시트 r14의 정의에 따르면 "Precious metals includes: Non-Monetary Gold (NMG), Platinum, Palladium and Silver." 즉 Table_B − Table_BX = 위 4종 귀금속 순거래액. 강의 슬라이드 6은 준비자산의 하위로 통화용 금(monetary gold)만 명시하며, 비통화용 금의 BoP 처리 방식은 강의 자료 미수록 영역으로 BPM6 §10·§14 본문 별도 참조 필요(19회차 §5 권고).
""",
    "Table_R1": """## 8. 통계 개정(revision) 시트의 역할

본 시트는 직전 발표 BoP Bulletin 대비 본 발표(2025 Q4)에서 변경된 값을 별도 시리즈로 기록한 운영 보조 자료이다. 강의 자료는 분기 BoP의 revision triangle·발표 시차·R1/R2/R3 활용을 직접 다루지 않으나(19회차 §6), 슬라이드 26 도식의 "비거래요인 = 가격·환율·기타조정" 분해와 인접 개념으로 해석할 수 있다. 학생용 1차 분석에서는 비교 사용 시 직전 발표 시점·개정 사유를 함께 명시하고, 본표(Table_A·B·BX 등)와 직접 합산·환산하지 않을 것.
""",
    "Table_R2": """## 8. 통계 개정(revision) 시트의 역할

본 시트는 Table_B(경상수지 본표)에 대응하는 직전 발표 대비 개정값(Cr/Dr/Bal/%GDP) 4 부표 운영 자료이다. 학생용 활용 권고는 Table_R1과 동일(19회차 §6 인용).
""",
    "Table_R3": """## 8. 통계 개정(revision) 시트의 역할

본 시트는 Table_D 계열(IIP·FA·소득) 9 부표(자산/부채/순 × IIP/Flow/Income)의 직전 발표 대비 개정 운영 자료이다. 강의 슬라이드 26의 "기타조정"(other adjustments) 항을 사후적으로 추적할 수 있는 가장 가까운 자료이며, 학생용 심화 보조로 보존 정당화 가능(19회차 §6).
""",
    "Cover_sheet": """## 본 시트 역할

본 시트는 BoP Bulletin xlsx의 목차이다. 모든 시트의 표 코드(A~K, R1~R3 등)와 한국어 명칭을 한 화면에 정리한다. 본 ETL은 Cover_sheet 내용을 본표 시트 메모(본 메모를 포함) 17건에 분산 인용하므로 별도 CSV 산출하지 않는다.
""",
    "Notes": """## 본 시트 역할

본 시트는 11개 시트(Table_A~K)의 시리즈별 footnote 본문이다. 부호 prefix 안내(note 1), Cr/Dr 정의(note 2~4), 결측 마커 정의(note 5: "Cells containing [x] represent unavailable data."), 단위 진술 등 메타 정보를 모두 담는다. 본 ETL은 Notes 본문을 본표 시트 메모 17건에 분산 인용한다(13/15/19회차 산출물 = Notes 시트 직접 인용 기록).
""",
    "Records": """## 본 시트 역할

본 시트는 BoP 주요 합계 라인(상품무역·서비스무역·1차소득·2차소득·경상수지·자본수지·금융계정·NEO)의 헤드라인 수치(GBP_billion 단위) 1쪽 요약본이다. db/REPORT.md 분석 보고서의 1차 수치 인용 출처. 본 ETL은 별도 CSV 산출하지 않으며, Records 시트 인용은 REPORT 갱신 시점에 직접 수행한다.
""",
}


def load_csv(path: Path) -> list[dict]:
    """CSV를 dict 리스트로 로드."""
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_memo(sheet: str, master_row: dict, log_rows: list[dict]) -> Path:
    """시트 1개에 대한 한국어 메타 메모(.md)를 생성."""
    table_code_raw = master_row["table_code"]
    classification = master_row["classification_ko"]
    classification_code = master_row["classification_code"]
    is_meta = classification_code == "meta_notes"

    if is_meta:
        out_name = f"balanceofpayments2025q4_{sheet.lower()}.md"
    else:
        table_code_lower = table_code_raw.replace(".", "_").lower()
        out_name = f"balanceofpayments2025q4_{table_code_lower}.md"
    out_path = OUT_DIR / out_name

    n_subtables = master_row["n_subtables"] or "0"
    unit = master_row["unit_normalized"] or "(메타 시트)"
    scale = master_row["scale_factor"] or "(메타 시트)"
    cycle = "A·Q (연간 + 분기 적층)" if not is_meta else "(메타 시트)"
    annual_first = master_row["annual_first"]
    annual_last = master_row["annual_last"]
    quarter_first = master_row["quarter_first"]
    quarter_last = master_row["quarter_last"]
    missing = master_row["missing_markers"] or "없음"
    missing_total = master_row["missing_total"] or "0"
    missing_subs = master_row["missing_subtables"]

    lines: list[str] = []
    lines.append(f"# {sheet} — 한국어 메타 메모")
    lines.append("")
    lines.append(
        f"본 메모는 ONS BoP Bulletin 2025 Q4 xlsx의 `{sheet}` 시트(분류: **{classification}**)를 "
        f"Phase 2.1 ETL로 가공한 부표 CSV들의 한국어 메타 안내이다."
    )
    lines.append("")

    # §1. 원본 위치
    lines.append("## 1. 원본 위치")
    lines.append("")
    lines.append(f"- 원본 파일: `db/source/balanceofpayments2025q4.xlsx` (read-only)")
    lines.append(f"- 시트명: `{sheet}`")
    lines.append(f"- 시트 차원: {master_row['n_rows']} 행 × {master_row['n_cols']} 열")
    lines.append(f"- ONS 표 코드: `{table_code_raw}`")
    lines.append("- 출처 URL: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsstatisticalbulletintables")
    lines.append("")

    # §2. 구조 변경 절차
    lines.append("## 2. 구조 변경 절차 (재현 가능)")
    lines.append("")
    if is_meta:
        lines.append("- 메타 시트는 별도 CSV로 산출하지 않는다(`db/code/source/split_subtables.py`가 `meta_notes` 분류를 자동 분기).")
        lines.append("- 시트 본문 인용이 필요한 경우 본 메모 §8(시트 역할 안내)에 기재한다.")
    else:
        lines.append("1. 마스터 인벤토리 1행(`db/data/_inventory/15_master_inventory.csv`)을 lookup해 `all_cdid_rows`·`blank_row_positions`·`unit_normalized` 메타를 결정.")
        lines.append("2. 부표 분리 — CDID 행이 곧 부표 헤더, 다음 빈 행 직전이 부표 종료. 부표마다 별도 가로형 CSV 1개 출력.")
        lines.append("3. 첫 컬럼 = 시점(`time_period`)을 ECOS TIME 규약(`YYYY` 또는 `YYYYQn`)으로 정규화.")
        lines.append("4. 둘째 컬럼부터 = ONS CDID 4자 코드를 ASCII 소문자로 정규화. sign_prefix(`-`) 행은 `_neg_<cdid>`로 컬럼명 부착.")
        lines.append("5. 셀 값은 원문 보존(숫자는 자릿수 변경 없음, 결측 마커 `x`·빈 셀은 그대로 문자열로 저장).")
        lines.append("6. 재현: `env/Scripts/python.exe db/code/source/split_subtables.py`")
    lines.append("")

    # §3. 컬럼 정의 (본표만)
    if not is_meta:
        lines.append("## 3. 컬럼 정의")
        lines.append("")
        lines.append("| 컬럼 | 의미 | 비고 |")
        lines.append("|---|---|---|")
        lines.append("| `time_period` | ECOS TIME 규약(`YYYY` 또는 `YYYYQn`) | 첫 컬럼 고정 |")
        lines.append("| `<cdid>` | ONS CDID 4자 코드(소문자) | ECOS ITEM_CODE1 대응 |")
        lines.append("| `_neg_<cdid>` | sign_prefix가 부착된 CDID(다운로드 시 부호 반전 필요) | Notes note 1 인용 |")
        lines.append("")

        # §4. 단위·주기·시점
        lines.append("## 4. 단위·주기·시점")
        lines.append("")
        lines.append(f"- 단위: `{unit}` (scale_factor: `{scale}`)")
        lines.append(f"- 주기(CYCLE): {cycle}")
        lines.append(f"- 연간 시점 범위: {annual_first} ~ {annual_last}")
        lines.append(f"- 분기 시점 범위: {quarter_first} ~ {quarter_last}")
        if master_row["subtable_split_required"] == "yes":
            lines.append("- 부표 단위로 단위 차이 — sub4(%GDP)는 단위가 다르므로 별도 처리.")
        lines.append("")

        # §5. 결측 의미 (19회차 권고 인용)
        lines.append("## 5. 결측 의미")
        lines.append("")
        if missing != "없음" and missing_total != "0":
            lines.append(
                f"본 시트의 셀 `x`는 ONS Notes 시트 note 5의 정의(\"Cells containing [x] represent unavailable data.\")에 따라 "
                f"**미가용(not available, GAF `[x]`)** 의미이며, **비공개(`[c]`)·적용 불가(`[z]`)와 단일 라벨로 통합하지 않는다**. "
                f"본 시트 결측 셀 수: **{missing_total}** (부표 {missing_subs})."
            )
            lines.append("")
            lines.append(
                "Table_C의 1997 Q1 ~ 1998 Q4 EU/non-EU 분기 분해 미가용은 ITIS 분기 조사 표본 안정화 전 + EU15 → EU27 정의 변경에 따른 "
                "소급 재계산 불가가 결합된 결과로 추정된다(13회차 §3 강의용 해석)."
            )
        else:
            lines.append(
                "본 시트의 빈 셀(`empty`)은 데이터 영역 외 padding이며 결측이 아니다(15회차 검증). "
                "`x`·`..`·`-` 마커는 본 시트에 등장하지 않는다."
            )
        lines.append("")
        lines.append("근거: `db/data/_inventory/13_missing_meaning_validation.md`, `19_signs_gold_revisions.md` §3.")
        lines.append("")

        # §6. 부호 규약 (19회차 권고 인용)
        lines.append("## 6. 부호 규약")
        lines.append("")
        if classification_code in ("capital_financial", "iip", "summary"):
            lines.append(
                "본 시트는 **BPM6 매뉴얼의 자산·부채 증감 기준**을 따른다(강의 슬라이드 8 직접 인용: "
                "\"새로운 매뉴얼에서는 금융계정 부호 표기 방식을 [자산·부채의 증감 기준]으로 변경 — 자산 증가/부채 증가 모두 (+)\"). "
                "단, ONS가 CDID 식별자 앞에 마이너스(`-`)를 부착한 시리즈는 다운로드 시 부호를 반전해야 한다(Notes note 1). "
                "본 ETL은 sign_prefix를 `_neg_<cdid>` 컬럼명에 보존해 후속 분석 시 명시적으로 식별 가능하도록 했다."
            )
        elif classification_code in ("current_main", "current_detail"):
            lines.append(
                "본 시트는 **강의 슬라이드 13의 Cr/Dr 정의**를 따른다 — 대변(credit, +) = 외국에서 자국으로 자금 유입, "
                "차변(debit, −) = 자국에서 외국으로 자금 유출. 합계 차원에서 사후 항등(전 계정 합 = 0)이 성립하나, "
                "부분합(예: 경상수지)은 흑자(+) / 적자(−) 가능."
            )
        else:
            lines.append(
                "본 시트는 직전 발표 대비 개정값을 기록한 운영 보조 자료이다. 부호 규약은 대응 본표(Table_A·B·BX·D·R3는 D 계열)의 BPM6 "
                "기준을 그대로 계승한다(19회차 §4)."
            )
        lines.append("")
        lines.append("근거: `db/data/_inventory/06_sign_convention_validation.md`, `19_signs_gold_revisions.md` §2·§4.")
        lines.append("")

        # §7. 부표 분리 단위 + 강의 위계 매핑 (18회차 인용)
        sub_meta = SUBTABLE_DIMENSIONS.get(sheet, {"axis": "(미분류)", "labels": [], "hierarchy": "(미분류)"})
        lines.append("## 7. 부표 분리 단위 + 강의 위계 매핑")
        lines.append("")
        lines.append(f"- 부표 차원: **{sub_meta['axis']}**")
        lines.append(f"- 시트 단위 BoP 위계: **{sub_meta['hierarchy']}**")
        lines.append("")
        lines.append("| 부표 # | 영문 라벨 | 출력 CSV |")
        lines.append("|---:|---|---|")
        # 출력 파일명은 ETL 로그에서 직접 가져옴(시트 키로 매칭).
        sheet_subs = [r for r in log_rows if r["sheet"] == sheet and r["out_file"]]
        for i, lbl in enumerate(sub_meta["labels"], start=1):
            csv_name = next((r["out_file"] for r in sheet_subs if r["sub_table"] == str(i)), "")
            lines.append(f"| {i} | {lbl} | `{csv_name}` |")
        lines.append("")
        lines.append("근거: `db/data/_inventory/18_subtable_curriculum_alignment.md` §2·§3.")
        lines.append("")

    # §8. 시트별 추가 안내(귀금속·개정·메타).
    extra = EXTRA_NOTES.get(sheet, "")
    if extra:
        lines.append(extra)

    # 마지막 — 생성 절차·관련 자료.
    lines.append("## 생성 절차·관련 자료")
    lines.append("")
    lines.append("- 가공 스크립트: `db/code/source/split_subtables.py` (시트 단위 가로형 CSV 분리)")
    lines.append("- 메모 생성 스크립트: `db/code/source/write_sheet_memos.py`")
    lines.append("- 마스터 인벤토리: `db/data/_inventory/15_master_inventory.csv`")
    lines.append("- ETL 로그: `db/data/_etl_log/phase2_1_split_log.csv`")
    lines.append("- 부호·결측·귀금속·개정 권고: `db/data/_inventory/19_signs_gold_revisions.md`")
    lines.append("- 부표 ↔ 강의 위계 정합성: `db/data/_inventory/18_subtable_curriculum_alignment.md`")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def main() -> None:
    """본 작성기 진입점."""
    masters = load_csv(INV)
    log_rows = load_csv(LOG)
    written: list[Path] = []
    for m in masters:
        sn = m["sheet"]
        path = write_memo(sn, m, log_rows)
        written.append(path)
    print(f"OK memos={len(written)} -> db/data/balanceofpayments2025q4_*.md")


if __name__ == "__main__":
    main()
