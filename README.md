# SKKU.Macroeconomics

성균관대학교(SKKU) 거시경제학 수업용 저장소. 영국 거시경제 통계 원본 데이터를 수집·정리하고, 강의 자료를 바탕으로 분석 보고서를 정리합니다.

작업 지침은 `CLAUDE.md`(루트)와 하위 `db/CLAUDE.md`, `db/data/CLAUDE.md`를 참고하세요.

## 디렉터리

- `db/source/` — 외부 기관에서 받아온 원본 데이터(읽기 전용).
- `db/data/` — 원본을 구조만 바꾼 가공본.
- `db/code/` — 검사·가공 스크립트 (`env/` 가상환경에서 실행).
- `db/REPORT.md` — BoP 분석 보고서(작성 중).
- `background/` — 강의 자료 등 배경지식 자료. 인덱스: `background/INDEX.md`.

## 데이터 출처

- `balanceofpayments2025q4` — 영국 국제수지(Balance of Payments) 2025년 4분기 자료. 출처: ONS Statistical Bulletin (https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsstatisticalbulletintables)

## 산출물

- `db/REPORT.md` — `db/source/` 자료를 정리한 BoP 분석 보고서.

## Python 환경

- 모든 Python 작업은 저장소 루트의 `env/` 가상환경에서 수행합니다.
- 패키지는 설치 즉시 `requirements.txt`에 동기화합니다.
