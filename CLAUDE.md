# CLAUDE.md

이 파일은 Claude Code (claude.ai/code)가 본 저장소에서 작업할 때 참고하는 지침입니다.

## 저장소 개요

성균관대학교(SKKU) 거시경제학 수업용 저장소입니다. 영국 거시경제 통계 원본 데이터(Excel)를 수집·정리하는 단계이며, 분석 코드·노트북·빌드 시스템·테스트는 아직 없습니다.

## 디렉터리 구조

- `db/source/` — 외부 기관에서 받아온 **원본 데이터(읽기 전용)**. 파일을 직접 수정하지 않으며, 가공 결과물은 별도 경로(`db/data/`) 또는 노트북 산출물로 분리합니다.
- `db/data/` — `db/source/`의 원본을 가공한 파일들이 저장되는 공간. **데이터 값은 절대로 변경하지 않으며, 파일 구조(시트 분리, 열 이름 정리, tidy/long-form 변환 등)만 조정**합니다.
- `db/code/` — 원본 검사·가공 스크립트가 보관되는 위치. 모든 실행은 `env/` 가상환경 인터프리터로 수행하며, 스크립트는 입력(`db/source/`)과 출력(`db/data/`) 경로를 명시적으로 분리합니다.
- `db/REPORT.md` — `db/source/` 데이터를 바탕으로 생성한 분석 보고서(산출물). 원본·가공 파일이 아니므로 자유롭게 갱신·재작성합니다.
- `db/CLAUDE.md` — `db/` 영역(원본 보관·가공) 작업 지침.
- `db/data/CLAUDE.md` — 가공 산출물 작성 시 따라야 할 세부 규칙(예정).
- `background/` — 데이터 분석 시 참고할 **배경 지식 자료**(강의 자료, 보고서, 슬라이드 등). 분석·해석·명세표 작성 시 이 폴더의 파일들을 우선 참조합니다. 데이터 처리 대상이 아니므로 가공·변환하지 않습니다.
- `.claude/agents/` — 서브에이전트 정의(`web-search`, `background-search`).
- `README.md` — 한국어로 작성된 데이터 출처 목록. 새 데이터셋을 추가할 때마다 갱신합니다.
- `CLAUDE.md` — 본 파일. 작업 지침.

## 편집 금지 파일

다음 파일은 **읽기·수정·접근 모두 금지**입니다. 사용자가 직접 관리하는 작업 기록 공간입니다.

- `PROMPT.md`
- `NOTE.md`

## 현재 보유 데이터·산출물

- `db/source/balanceofpayments2025q4.xlsx` — 영국 국제수지(Balance of Payments) 2025년 4분기 자료. 출처: ONS Statistical Bulletin (https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsstatisticalbulletintables).
- `db/code/source/inspect_bop.py`, `db/code/source/extract_latest.py` — 원본 xlsx 검사·최근치 추출용 스크립트.
- `db/REPORT.md` — 위 자료를 정리한 BoP 분석 보고서(작성 중).
- `background/BoP.pptx` — 강의용 BoP 슬라이드(배경지식 1차 근거).

## 진행 중인 작업

- `db/source/` 내 xlsx 파일의 시트 구조를 파악하고, 분석에 적합한 형태(tidy/long-form 등)로 정리하기 위한 **데이터 명세표**를 준비 중입니다. 명세표에는 시트별 변수, 단위, 기간(주기), 결측 처리 방식 등이 포함될 예정입니다.

## 작업 규칙

- **언어**: 사용자 대상 문서(README, 데이터 출처 안내, 명세표 등)는 **한국어**로 유지합니다. 영어로 번역하지 마세요.
- **명명 규칙**: 신규 데이터셋은 `<항목><yyyy><기간>.<확장자>` 패턴을 따릅니다 (예: `balanceofpayments2025q4.xlsx`). 분기는 `q1`–`q4`, 월은 `m01`–`m12`, 연간은 기간 표기 생략을 기본으로 합니다.
- **출처 표기**: 외부 통계청·기관 자료는 반드시 공식 다운로드 페이지 URL과 함께 README "데이터 출처" 항목에 기록해 재현 가능성을 확보합니다.
- **원본 보존**: `db/source/` 파일은 절대 수정하지 않습니다. 정제·가공이 필요하면 새 파일/디렉터리에 산출하고, 변환 절차는 코드나 노트북으로 남깁니다.

## Python 개발 환경

- **가상환경 고정**: 모든 Python 작업은 저장소 루트의 `env/` 가상환경 안에서만 수행합니다. 시스템 Python이나 다른 가상환경(`venv`, `.venv`, conda 등)은 사용하지 않습니다.
- **패키지 설치 위치**: `pip install`을 포함한 모든 패키지·도구 설치는 `env/` 가상환경을 활성화한 상태에서 실행합니다. 전역 설치(`pip install --user`, 시스템 pip) 금지.
- **requirements.txt 동기화**: `env/`에 새 패키지를 설치할 때마다 즉시 `requirements.txt`에 버전과 함께 기록합니다(`pip freeze` 또는 수동 추가). 설치한 패키지가 `requirements.txt`에 누락된 상태로 작업을 마치지 않습니다.
- **Python 실행**: 스크립트·노트북 실행, 테스트, 린터 등 모든 Python 호출은 `env/` 가상환경의 인터프리터(`env/Scripts/python.exe` on Windows / `env/bin/python` on POSIX)를 사용합니다.