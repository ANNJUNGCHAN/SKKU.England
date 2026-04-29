"""SKKU 거시경제학 강의용 영국 BoP 시각화 런처.

본 런처는 한 번의 명령으로 datasette 0.65.2를 강의 시연 모드로 기동한다.
강의실 로컬 노트북 외부에는 노출되지 않는 안전한 구성을 강제한다.

기동 사양(`visualize/db/PLAN.md` §3 4단계 + §5 검증 기준 5건):
  - 데이터베이스: `db/data/_db/ecos_uk_bop.sqlite` 를 `-i`(immutable) 옵션으로
    읽기 전용 마운트한다. 강사 노트북에서도 데이터가 절대 수정되지 않는다.
  - 메타데이터·캔드 쿼리: `visualize/db/metadata.yaml` 을 `--metadata` 로 적용.
    9 종 캔드 쿼리(헤드라인 5 + 시계열 2 + 항등식 잔차 1 + 시범 CDID 1)와
    한국어 라벨·OGL v3 라이선스·ONS 출처 표기를 함께 노출한다.
  - 호스트: `--host 127.0.0.1` 로 로컬 루프백에 한정 바인딩한다. 강사 노트북
    외부(학내·인터넷·공용 Wi-Fi)에서는 접근 자체가 불가능하다.
  - 포트: 잘 알려진 포트(80·443·1024 미만)와 흔한 개발 포트(3000·5000·
    8000·8080·8888)를 모두 피한 18421 을 고정 사용한다. 충돌 시에는 본
    스크립트 상단 `PORT` 상수를 17000~30000 범위의 다른 값으로 바꾼다.
  - 브라우저: datasette 의 `--open` 플래그로 기동 직후 기본 브라우저가
    자동으로 열린다.

운영 주의사항(Windows 한국어 로캘):
  - Windows 한국어 로캘에서 datasette CLI 가 metadata 파일을 시스템 기본
    인코딩(cp949)으로 열어 한국어 description_html 에서 즉시 죽는다. 본
    런처는 자식 프로세스 환경변수에 `PYTHONUTF8=1` 을 강제 주입하여 해당
    문제를 차단한다. 직접 `python -m datasette ...` 으로 호출할 때도 반드시
    `PYTHONUTF8=1` 을 함께 설정해야 한다.

사용법:
    env\\Scripts\\python.exe visualize\\db\\launch.py

종료 방법:
  - 콘솔에서 Ctrl+C 1회 입력 → datasette 가 SIGINT 를 받고 정상 종료한다.
    (강의실 환경에서는 Ctrl+C 가 가장 안전한 종료 방법이다.)
  - 콘솔이 막혀 있을 경우 별도 터미널에서:
        netstat -ano -p TCP | find "18421"
        taskkill /F /PID <위에서 확인한 PID>
  - 강의실 노트북 자체를 종료해도 데이터는 immutable 마운트라 변경 없다.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


# -- 경로 상수 -------------------------------------------------------------
# 저장소 루트(`visualize/db/...` 에서 두 단계 위)
REPO_ROOT = Path(__file__).resolve().parents[2]
SQLITE_PATH = REPO_ROOT / "db" / "data" / "_db" / "ecos_uk_bop.sqlite"
METADATA_YAML = REPO_ROOT / "visualize" / "db" / "metadata.yaml"

# -- 네트워크 상수 ---------------------------------------------------------
# 로컬 루프백 한정. 외부 노출이 필요해질 경우 PLAN.md 위험 표를 다시 검토한 뒤
# 별도 안건으로만 변경한다(단순히 0.0.0.0 으로 바꾸지 말 것).
HOST = "127.0.0.1"
# 잘 알려진 포트(80·443·1024 미만)와 흔한 개발 포트(3000·5000·8000·8080·
# 8888) 를 모두 피한 비표준 포트. 충돌 시 17000~30000 범위에서 변경.
PORT = 18421


def _print_banner() -> None:
    """기동 직전·직후 사용자에게 안내할 한국어 배너 출력."""
    bar = "=" * 64
    print(bar)
    print("SKKU 거시경제학 강의용 영국 BoP 시각화 런처")
    print(bar)
    print(f"  데이터베이스 : {SQLITE_PATH.relative_to(REPO_ROOT)} (immutable, 읽기 전용)")
    print(f"  메타데이터   : {METADATA_YAML.relative_to(REPO_ROOT)} (캔드 쿼리 9 종)")
    print(f"  바인딩       : {HOST}:{PORT}  (로컬 루프백 한정 — 외부 접근 불가)")
    print(f"  접속 URL     : http://{HOST}:{PORT}/")
    print()
    print("  종료 방법    : 본 콘솔에서 Ctrl+C 1회 → datasette 가 정상 종료")
    print("                별도 터미널에서:")
    print(f"                  netstat -ano -p TCP | find \"{PORT}\"")
    print("                  taskkill /F /PID <위에서 확인한 PID>")
    print(bar)
    print()


def _build_command() -> list[str]:
    """datasette serve 호출 인자 목록을 구성."""
    return [
        sys.executable,                # 가상환경 인터프리터로 강제
        "-m", "datasette",
        "serve",
        "-i", str(SQLITE_PATH),         # immutable 마운트(읽기 전용)
        "--host", HOST,
        "--port", str(PORT),
        "--metadata", str(METADATA_YAML),
        "--open",                       # 기동 직후 기본 브라우저 자동 오픈
    ]


def _build_env() -> dict[str, str]:
    """자식 프로세스용 환경변수. PYTHONUTF8=1 강제 주입."""
    env = os.environ.copy()
    # Windows 한국어 로캘에서 datasette CLI 가 metadata.yaml 을 cp949 로 읽어
    # UnicodeDecodeError 로 즉사하는 문제 차단. 본 런처를 어떤 셸에서 호출
    # 하더라도 자식 프로세스에는 항상 UTF-8 모드가 적용된다.
    env["PYTHONUTF8"] = "1"
    return env


def main() -> int:
    """런처 진입점. datasette 자식 프로세스를 기동하고 종료 코드를 반환."""
    if not SQLITE_PATH.exists():
        print(f"[런처 오류] SQLite 파일을 찾지 못함: {SQLITE_PATH}", file=sys.stderr)
        return 2
    if not METADATA_YAML.exists():
        print(f"[런처 오류] metadata.yaml 을 찾지 못함: {METADATA_YAML}", file=sys.stderr)
        return 2

    _print_banner()

    cmd = _build_command()
    env = _build_env()

    # subprocess.run 으로 자식 프로세스를 동기 실행한다. Ctrl+C 가 들어오면
    # 부모(본 스크립트)가 KeyboardInterrupt 를 받고, 자식(datasette) 도 같은
    # 콘솔 그룹에 속해 SIGINT 를 받아 정상 종료한다.
    try:
        completed = subprocess.run(cmd, env=env)
        return completed.returncode
    except KeyboardInterrupt:
        # 강의 종료 후 강사가 Ctrl+C 로 종료한 정상 경로.
        print("\n[런처] Ctrl+C 감지 — datasette 정상 종료 절차에 진입.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
