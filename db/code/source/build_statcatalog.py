"""
Phase 3.4 §5 — 전체 통계표 카탈로그(statcatalog.csv) 생성 ETL.

ECOS 통계표 목록 서비스에 대응하는 통계표 단위 메타 카탈로그를 산출한다.
specification.csv(512행, CDID 단위)와 long-form CSV(74,006행)에서 STAT_CODE
단위(예: UK_BoP_Table_J_sub1) 메타데이터를 집계하여 정형화된 통계표 카탈로그를
만든다.

산출 컬럼(15개, ECOS 통계표 목록 서비스 컬럼과 1:1 정렬)
- STAT_CODE              통계표 코드 (예: UK_BoP_Table_J_sub1)
- STAT_NAME              한국어 통계표명
- ENGLISH_NAME           영문 통계표명
- FIELD_MAIN             1차 분야 분류 (예: 국제수지)
- FIELD_SUB              2차 분야 분류 (예: 경상수지 본표)
- ORG_NAME               작성기관 (Office for National Statistics, ONS)
- DATA_SOURCE            자료원 (HMRC OTS·ITIS·IPS·BoE·BIS·EEA HMT·FCDO 등)
- CYCLE                  주기 (A / Q)
- START_TIME             자료 시작 시점
- END_TIME               자료 종료 시점
- N_ITEMS                통계항목(CDID) 수
- N_OBSERVATIONS         관측치 수 (long-form CSV 합산)
- SOURCE_URL             출처 URL (ONS BoP Statistical Bulletin Tables)
- PUBLISHED_DATE         발표일
- KOREAN_DESCRIPTION     한국어 설명

원칙
- specification.csv·long-form CSV에서 자동 집계 — 손으로 편집한 산출물 없음.
- 1 CSV = 1 평면 표 원칙 준수 (db/CLAUDE.md 가공 원칙 1·2번).
- ECOS 분야 분류 규약과 충돌 없이, 본 프로젝트 접두 `UK_BoP_*`로 분리
  (PLAN.md §0.3 분야 접두 규약 준수).
- 데이터 값 불변: 셀 값을 산식으로 변형하지 않고 단순 그룹 카운트만 수행.

STAT_CODE 키 매핑 주의
- specification.csv는 `UK_BoP_Table_<sheet>_sub<n>` 패턴(`Table_` 포함).
- long-form CSV(Phase 2 산출)는 `UK_BoP_<sheet>_sub<n>` 패턴(`Table_` 미포함).
- 본 ETL은 long-form 키를 specification 표기로 정규화한 뒤 매칭한다
  (값 자체는 변경하지 않음, 키 변환만).

실행
    env/Scripts/python.exe db/code/source/build_statcatalog.py
"""
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]

DB_DIR = Path(__file__).resolve().parents[2]
SPEC_DIR = DB_DIR / "data" / "_spec"
LONG_CSV = DB_DIR / "data" / "balanceofpayments2025q4_long.csv"
SPEC_CSV = SPEC_DIR / "specification.csv"
CATALOG_OUT = SPEC_DIR / "statcatalog.csv"

# 시트별 한국어 STAT_NAME / 영문 NAME / 분야 분류 / 자료원 매핑.
# 1차 분야: "국제수지" 통일. 2차 분야는 강의 슬라이드 5·6·7 분류 + ONS 시트 코드 결합.
SHEET_META: dict[str, dict[str, str]] = {
    "Table_A": {
        "ko_name": "영국 국제수지 잔액 요약",
        "en_name": "UK Balance of Payments — Summary of balances (net transactions)",
        "field_sub": "국제수지 잔액 요약",
        "data_source": "ONS BoP Statistical Bulletin Tables",
        "ko_desc": "경상·자본·금융·E&O 4개 잔액 컬럼군의 분기·연간 요약 (강의 슬라이드 13·14 항등식 직접 매핑)",
    },
    "Table_B": {
        "ko_name": "영국 경상수지 본표(SA)",
        "en_name": "UK Current account, seasonally adjusted",
        "field_sub": "경상수지 본표",
        "data_source": "ONS Annual Survey + ITIS + IPS + HMRC OTS",
        "ko_desc": "경상수지 4 부표(Credits / Debits / Balances / %GDP), 강의 슬라이드 5·14 `CA = G + S + PI + SI`",
    },
    "Table_BX": {
        "ko_name": "영국 경상수지(귀금속 제외)",
        "en_name": "UK Current account excluding precious metals (BoP basis), seasonally adjusted",
        "field_sub": "경상수지 보조표 (귀금속 제외)",
        "data_source": "ONS BoP Statistical Bulletin Tables (2020 Q3~ 신설)",
        "ko_desc": "Table_B와 동일 4 부표 구조이나 비통화용 금(SITC 9) + 은·백금·팔라듐 bullion 차감",
    },
    "Table_C": {
        "ko_name": "영국 경상수지 (EU/non-EU)",
        "en_name": "UK Current account — EU and non-EU geographical breakdown",
        "field_sub": "경상수지 지리분해 (EU/non-EU)",
        "data_source": "ONS Pink Book Ch.9 + HMRC + ITIS",
        "ko_desc": "Table_B 4 하위 + 합계를 EU vs non-EU로 분해, Brexit(2020-02-01) 후 EU27 기준 재계산",
    },
    "Table_D1_3": {
        "ko_name": "영국 IIP·금융계정·투자소득 — 자산",
        "en_name": "UK IIP, Financial Account, Investment Income — Assets (Investment abroad)",
        "field_sub": "IIP+FA+투자소득 — 자산 측",
        "data_source": "ONS AIFDI/AOFDI + BoE + BIS",
        "ko_desc": "BPM6 §6 FA 5분류 + §11 1차소득 cross-link, 자산 측 통합표",
    },
    "Table_D4_6": {
        "ko_name": "영국 IIP·금융계정·투자소득 — 부채",
        "en_name": "UK IIP, Financial Account, Investment Income — Liabilities (Investment in the UK)",
        "field_sub": "IIP+FA+투자소득 — 부채 측",
        "data_source": "ONS AIFDI/AOFDI + BoE + BIS",
        "ko_desc": "BPM6 §6 FA 5분류 + §11 1차소득 cross-link, 부채 측 통합표",
    },
    "Table_D7_9": {
        "ko_name": "영국 IIP·금융계정·투자소득 — 순",
        "en_name": "UK IIP, Financial Account, Investment Income — Net",
        "field_sub": "IIP+FA+투자소득 — 순(Net)",
        "data_source": "ONS AIFDI/AOFDI + BoE + BIS",
        "ko_desc": "Net = 자산 − 부채, sign_prefix 운영(부호 반전 필요)",
    },
    "Table_E": {
        "ko_name": "영국 상품무역",
        "en_name": "UK Trade in goods",
        "field_sub": "상품무역",
        "data_source": "HMRC Overseas Trade Statistics (OTS)",
        "ko_desc": "3 부표(Exports/Imports/Balance), SITC Rev.4 5묶음 + BPM6 §10 General merchandise",
    },
    "Table_F": {
        "ko_name": "영국 서비스무역",
        "en_name": "UK Trade in services",
        "field_sub": "서비스무역",
        "data_source": "ONS ITIS + IPS + BoE + 행정자료",
        "ko_desc": "EBOPS 2010 12분류 SA~SL (가공·유지보수·운송·여행·건설·보험·금융·IP·통신컴퓨터·기타비즈니스·개인문화·정부)",
    },
    "Table_G": {
        "ko_name": "영국 1차소득(본원소득)",
        "en_name": "UK Primary income",
        "field_sub": "1차소득(본원소득)",
        "data_source": "ONS Annual Survey + BoE + HMRC + 대사관 조사",
        "ko_desc": "BPM6 §11/§13: COE + 투자소득 3분해(직접·증권·기타) + 준비자산수익 + 기타",
    },
    "Table_H": {
        "ko_name": "영국 2차소득(이전소득)",
        "en_name": "UK Secondary income",
        "field_sub": "2차소득(이전소득)",
        "data_source": "HM Treasury + FCDO ODA + DWP·HMRC 행정자료",
        "ko_desc": "BPM6 §12/§14: 일반정부(EU·UN·ODA) + 기타 부문(개인이전·workers' remittances 메모·보험)",
    },
    "Table_I": {
        "ko_name": "영국 자본수지",
        "en_name": "UK Capital account",
        "field_sub": "자본수지",
        "data_source": "ONS Pink Book Ch.7 + EU 정산 + 외교공관 부지 거래",
        "ko_desc": "BPM6 §13/§15: 자본이전(채무면제·자본 보조금·이민·일회성) + NPNFA(토지·지하자원·마케팅·프랜차이즈·영업권). very small.",
    },
    "Table_J": {
        "ko_name": "영국 금융계정(NSA)",
        "en_name": "UK Financial account, not seasonally adjusted",
        "field_sub": "금융계정(NSA)",
        "data_source": "ONS AIFDI/AOFDI + BoE + BIS Locational Banking",
        "ko_desc": "BPM6 §6 FA 5분류(직접투자·증권·파생·기타·준비자산), 부표1·3 sign_prefix 운영",
    },
    "Table_K": {
        "ko_name": "영국 국제투자대조표(분기말)",
        "en_name": "UK International investment position, end-of-period",
        "field_sub": "국제투자대조표(IIP)",
        "data_source": "ONS Pink Book Ch.10 + EEA(HMT) + BoE",
        "ko_desc": "Net IIP = 자산 − 부채 = NFA, 단위 GBP **billion** (다른 시트 GBP million과 다름)",
    },
    "Table_R1": {
        "ko_name": "영국 개정 요약(잔액)",
        "en_name": "UK Revisions summary — balances",
        "field_sub": "개정 — 잔액 요약",
        "data_source": "ONS National Accounts Revisions Policy",
        "ko_desc": "직전 분기 발표 대비 잔액 개정 요약, 8 chapter",
    },
    "Table_R2": {
        "ko_name": "영국 경상수지 개정",
        "en_name": "UK Current account revisions",
        "field_sub": "개정 — 경상수지",
        "data_source": "ONS National Accounts Revisions Policy",
        "ko_desc": "4 부표(Credits/Debits/Balances/%GDP) 개정",
    },
    "Table_R3": {
        "ko_name": "영국 국제투자 개정",
        "en_name": "UK International investment revisions",
        "field_sub": "개정 — 국제투자",
        "data_source": "ONS National Accounts Revisions Policy",
        "ko_desc": "9 부표(IIP·FA·Income × Asset/Liability/Net) 개정, 단위 GBP billion",
    },
}

ORG_NAME = "Office for National Statistics (ONS)"
FIELD_MAIN = "국제수지"
SOURCE_URL = "https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsstatisticalbulletintables"
PUBLISHED_DATE = "2026-03-31"


def main() -> None:
    """
    statcatalog.csv 생성 진입점.

    절차
        1. specification.csv를 읽어 STAT_CODE 단위로 그룹화한다(63개).
        2. long-form CSV를 순회하여 STAT_CODE별 관측치 수를 집계한다.
           specification 표기와의 명명 불일치를 흡수하기 위해 long-form 키를
           `UK_BoP_<sheet>_sub<n>` → `UK_BoP_Table_<sheet>_sub<n>`로 정규화한다.
        3. 시트별 메타(SHEET_META 17 시트)를 결합하여 15컬럼 카탈로그 행을 만든다.

    부작용
        - 파일 쓰기: db/data/_spec/statcatalog.csv (UTF-8, 1행=헤더, 64행 총).

    예외
        - SPEC_CSV / LONG_CSV가 없거나 헤더가 다르면 KeyError로 즉시 실패한다
          (선행 단계 산출물 누락을 빠르게 드러내기 위함).
    """
    print("Phase 3.4 §5 — 통계표 카탈로그 생성 ETL")
    print("=" * 60)

    # 1) specification.csv에서 STAT_CODE 단위 집계
    print(f"[step 1/3] specification.csv 읽기 — {SPEC_CSV}")
    with SPEC_CSV.open("r", encoding="utf-8", newline="") as f:
        spec_rows = list(csv.DictReader(f))
    print(f"  → {len(spec_rows)}행")

    # STAT_CODE → 그룹 메타 집계
    by_stat_code: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in spec_rows:
        by_stat_code[r["STAT_CODE"]].append(r)
    print(f"  → 고유 STAT_CODE: {len(by_stat_code)}개")

    # 2) long-form CSV에서 STAT_CODE 단위 관측치 수 집계
    #
    # 주의: long-form(Phase 2 산출)의 stat_code는 `UK_BoP_<sheet>_sub<n>` 형식이고,
    # specification.csv의 STAT_CODE는 `UK_BoP_Table_<sheet>_sub<n>` 형식이다
    # (Phase 2와 Phase 3.4 산출이 서로 다른 시점에 정해진 명명 규약).
    # 본 ETL은 specification 표기를 카탈로그의 정식 STAT_CODE로 사용하므로,
    # long-form 키를 `UK_BoP_` → `UK_BoP_Table_`로 정규화하여 일치시킨다.
    # 데이터 값은 변경하지 않고 키 표기만 매핑한다.
    print(f"[step 2/3] long-form CSV에서 관측치 수 집계 — {LONG_CSV}")
    obs_count: dict[str, int] = defaultdict(int)
    long_prefix = "UK_BoP_"
    with LONG_CSV.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            raw_key = row["stat_code"]
            # `UK_BoP_A_sub1` → `UK_BoP_Table_A_sub1`로 정규화
            if raw_key.startswith(long_prefix) and not raw_key.startswith(long_prefix + "Table_"):
                norm_key = long_prefix + "Table_" + raw_key[len(long_prefix):]
            else:
                norm_key = raw_key
            obs_count[norm_key] += 1
    matched = sum(1 for sc in by_stat_code if obs_count.get(sc, 0) > 0)
    print(f"  → 고유 long-form stat_code: {len(obs_count)}개, specification 매칭: {matched}/{len(by_stat_code)}")

    # 3) 카탈로그 행 산출
    print("[step 3/3] 카탈로그 15컬럼 매핑·산출")
    catalog_rows: list[dict[str, str]] = []
    for stat_code in sorted(by_stat_code.keys()):
        rows = by_stat_code[stat_code]
        # 시트 추출 (예: UK_BoP_Table_J_sub1 → Table_J)
        # STAT_CODE 패턴: UK_BoP_<sheet>_sub<n>
        prefix = "UK_BoP_"
        body = stat_code[len(prefix):]
        # 끝에서 _sub<n> 분리
        if "_sub" in body:
            sheet, sub = body.rsplit("_sub", 1)
        else:
            sheet, sub = body, ""
        meta = SHEET_META.get(sheet, {})
        # 시점 범위 (해당 STAT_CODE의 모든 행에서 min·max)
        starts = [r["START_TIME"] for r in rows if r.get("START_TIME")]
        ends = [r["END_TIME"] for r in rows if r.get("END_TIME")]
        start_time = min(starts) if starts else ""
        end_time = max(ends) if ends else ""
        # 주기 (시점에 Q 포함 여부)
        cycles = {r["CYCLE"] for r in rows}
        cycle = "Q" if "Q" in cycles else "A"
        ko_name_full = f"{meta.get('ko_name', sheet)} (부표 {sub})"
        en_name_full = f"{meta.get('en_name', sheet)} — sub-table {sub}"
        catalog_rows.append(
            {
                "STAT_CODE": stat_code,
                "STAT_NAME": ko_name_full,
                "ENGLISH_NAME": en_name_full,
                "FIELD_MAIN": FIELD_MAIN,
                "FIELD_SUB": meta.get("field_sub", ""),
                "ORG_NAME": ORG_NAME,
                "DATA_SOURCE": meta.get("data_source", ""),
                "CYCLE": cycle,
                "START_TIME": start_time,
                "END_TIME": end_time,
                "N_ITEMS": str(len(rows)),
                "N_OBSERVATIONS": str(obs_count.get(stat_code, 0)),
                "SOURCE_URL": SOURCE_URL,
                "PUBLISHED_DATE": PUBLISHED_DATE,
                "KOREAN_DESCRIPTION": meta.get("ko_desc", ""),
            }
        )

    fieldnames = [
        "STAT_CODE",
        "STAT_NAME",
        "ENGLISH_NAME",
        "FIELD_MAIN",
        "FIELD_SUB",
        "ORG_NAME",
        "DATA_SOURCE",
        "CYCLE",
        "START_TIME",
        "END_TIME",
        "N_ITEMS",
        "N_OBSERVATIONS",
        "SOURCE_URL",
        "PUBLISHED_DATE",
        "KOREAN_DESCRIPTION",
    ]

    CATALOG_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CATALOG_OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(catalog_rows)
    print(f"  → 카탈로그 {len(catalog_rows)}행 × {len(fieldnames)}컬럼 산출 완료")
    print(f"  → 파일: {CATALOG_OUT}")
    print("=" * 60)
    print("완료.")


if __name__ == "__main__":
    main()
