"""한국어 라벨 출처 고정 정책 정적 점검 스크립트.

정책(`visualize/db/PLAN.md` §2 + `db/USER_GUIDE.md` 1차 출처):
- 한국어 라벨의 단일 진실 원천(SSoT)은 두 곳뿐이다.
  (1) `db/data/_spec/cdid_definitions.csv` (CDID 사전, ITEM_NAME_KR 컬럼)
  (2) `db/USER_GUIDE.md` 4절 시범 CDID 표
- `visualize/db/metadata.yaml`의 캔드 쿼리 SQL은 한국어 라벨을 절대로
  문자열 리터럴로 박지 않는다. 라벨은 DB 컬럼 참조(`m.ITEM_NAME_KR`,
  `m.UNIT_NAME` 등)로만 노출된다.
- 이 스크립트는 위 두 가지를 회귀 방지용으로 1회 정적 점검한다.

실행 방법:
    env\\Scripts\\python.exe visualize\\db\\check_label_provenance.py

종료 코드:
- 0: 정책 충족(SQL 리터럴에 한국어 라벨 없음 + cdid_definitions.csv 사전 로드 가능)
- 1: 정책 위반(한국어 라벨이 SQL 문자열에 박혀 있거나 사전 로드 실패)
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import yaml

# Windows 기본 콘솔 인코딩(cp949)에서 한국어·em dash(—) 출력 시
# UnicodeEncodeError가 발생하므로, 표준 출력/에러를 UTF-8로 재구성한다.
# 이 스크립트의 출력은 사람이 읽는 진단 메시지뿐이며, 종료 코드만이
# 회귀 점검의 실질 결과이므로 표시 인코딩 변경은 부작용이 없다.
for _stream_name in ("stdout", "stderr"):
    _stream = getattr(sys, _stream_name, None)
    _reconfigure = getattr(_stream, "reconfigure", None)
    if callable(_reconfigure):
        try:
            _reconfigure(encoding="utf-8")
        except Exception:
            # 일부 비표준 환경(IDE 캡처 스트림 등)에서는 재구성이 불가할 수
            # 있으나, 그 경우 상위 환경이 이미 UTF-8을 처리할 가능성이 높다.
            pass


# 저장소 루트(`visualize/db/...`에서 두 단계 위)
REPO_ROOT = Path(__file__).resolve().parents[2]
METADATA_YAML = REPO_ROOT / "visualize" / "db" / "metadata.yaml"
CDID_DEFINITIONS = REPO_ROOT / "db" / "data" / "_spec" / "cdid_definitions.csv"
USER_GUIDE = REPO_ROOT / "db" / "USER_GUIDE.md"

# 한국어(가–힣) 문자 1자라도 포함하는지 검사하는 정규식
HANGUL_RE = re.compile(r"[가-힣]")
# SQL 안의 작은따옴표·큰따옴표로 묶인 문자열 리터럴 매칭
SINGLE_QUOTED = re.compile(r"'([^']*)'")
DOUBLE_QUOTED = re.compile(r'"([^"]*)"')


def load_canned_queries() -> dict[str, str]:
    """metadata.yaml에서 캔드 쿼리 9 종의 (이름→SQL) 매핑을 추출."""
    with METADATA_YAML.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return {
        name: q["sql"]
        for name, q in data["databases"]["ecos_uk_bop"]["queries"].items()
    }


def find_hangul_literals(sql: str) -> list[str]:
    """SQL 문자열 안에서 한국어 문자가 들어간 따옴표 리터럴만 모아 반환."""
    hits: list[str] = []
    for pattern in (SINGLE_QUOTED, DOUBLE_QUOTED):
        for match in pattern.finditer(sql):
            literal = match.group(1)
            if HANGUL_RE.search(literal):
                hits.append(literal)
    return hits


def assert_cdid_dictionary_loadable() -> int:
    """CDID 사전(cdid_definitions.csv)이 로드 가능한지 확인.

    실제 라벨 일치성까지는 검증하지 않는다(metadata.yaml은 SQL JOIN으로
    DB 컬럼을 참조하므로, DB 자체가 사전을 단일 출처로 적재된 시점에서
    라벨 일치성이 자동 보장됨).
    """
    if not CDID_DEFINITIONS.exists():
        print(f"FAIL: CDID 사전 파일 없음 — {CDID_DEFINITIONS}")
        return 1
    with CDID_DEFINITIONS.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        print(f"FAIL: CDID 사전이 비어 있음 — {CDID_DEFINITIONS}")
        return 1
    print(f"PASS: CDID 사전 로드 — {len(rows)} 행, 출처 {CDID_DEFINITIONS.relative_to(REPO_ROOT)}")
    return 0


def assert_user_guide_present() -> int:
    """USER_GUIDE.md 존재 확인. 시범 CDID 9 종 표가 정상 위치에 있는지 키워드로 검사."""
    if not USER_GUIDE.exists():
        print(f"FAIL: USER_GUIDE 없음 — {USER_GUIDE}")
        return 1
    text = USER_GUIDE.read_text(encoding="utf-8")
    # 시범 CDID 표의 9 종 라벨 중 핵심 3종이 모두 등장하는지만 확인.
    required = ["HBOP", "IKBD", "LTEB"]
    missing = [k for k in required if k not in text]
    if missing:
        print(f"FAIL: USER_GUIDE에서 시범 CDID 누락 — {missing}")
        return 1
    print(f"PASS: USER_GUIDE 시범 CDID 표 확인 — {USER_GUIDE.relative_to(REPO_ROOT)}")
    return 0


def main() -> int:
    """정책 점검 진입점. 위반 1건이라도 발견되면 종료 코드 1."""
    print("[정책 점검] 한국어 라벨 출처 고정")
    print(f"  - metadata.yaml = {METADATA_YAML.relative_to(REPO_ROOT)}")
    print(f"  - 1차 출처(1)  = {CDID_DEFINITIONS.relative_to(REPO_ROOT)}")
    print(f"  - 1차 출처(2)  = {USER_GUIDE.relative_to(REPO_ROOT)}")
    print()

    failures = 0

    # (1) 캔드 쿼리 SQL에 한국어 문자열 리터럴이 박혀 있는지
    queries = load_canned_queries()
    print(f"[검사 1] 캔드 쿼리 {len(queries)} 종 SQL 안에 한국어 리터럴이 박혀 있는지")
    violations: list[tuple[str, str]] = []
    for name, sql in queries.items():
        for literal in find_hangul_literals(sql):
            violations.append((name, literal))
    if violations:
        failures += 1
        print(f"  FAIL: {len(violations)} 건 위반 — 한국어 라벨이 SQL 문자열에 직접 박혀 있음")
        for name, literal in violations:
            print(f"    · {name}: {literal!r}")
    else:
        print("  PASS: SQL 리터럴 안 한국어 0 건 — 모든 라벨이 DB 컬럼 참조로만 노출")

    # (2) 1차 출처(CDID 사전) 로드 가능
    print()
    print("[검사 2] CDID 사전(cdid_definitions.csv) 로드 가능 여부")
    failures += assert_cdid_dictionary_loadable()

    # (3) 1차 출처(USER_GUIDE) 시범 CDID 표 존재
    print()
    print("[검사 3] USER_GUIDE.md 시범 CDID 표 존재 여부")
    failures += assert_user_guide_present()

    print()
    print("=" * 60)
    if failures:
        print(f"전체 결과: FAIL ({failures} 건)")
        return 1
    print("전체 결과: PASS — 한국어 라벨 출처 고정 정책 충족")
    return 0


if __name__ == "__main__":
    sys.exit(main())
