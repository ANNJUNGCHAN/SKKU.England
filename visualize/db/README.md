# SKKU 거시경제학 강의용 영국 BoP 시각화 (datasette)

본 영역은 영국 국제수지(Balance of Payments) RDB(`db/data/_db/ecos_uk_bop.sqlite`)
를 datasette 0.65.2 + datasette-vega 0.6.2 로 강의실 로컬에서 시연하기 위한
시각화 부트스트랩 산출물 모음이다. 데이터 자체는 본 영역에 사본을 두지 않으며,
원본 RDB 를 immutable 모드로만 마운트한다.

## 구성

| 파일 | 용도 |
|---|---|
| `PLAN.md` | 본 영역의 작업 계획서(설계 결정·위험 표·검증 기준 5건). |
| `CHECKLIST.md` | 작업 단계별 실행 체크리스트(5 단계 25 항목 + 검증 기준 5 + 위험 점검 5). |
| `metadata.yaml` | datasette 메타데이터 — 한국어 라벨·OGL v3 라이선스·캔드 쿼리 9 종(헤드라인 5·시계열 2·항등식 잔차 1·시범 CDID 1). |
| `launch.py` | 한 번의 명령으로 datasette 를 강의 시연 모드로 기동하는 런처. |
| `check_label_provenance.py` | 한국어 라벨 출처 고정 정책(USER_GUIDE.md + CDID 사전 단일 출처) 정적 점검 스크립트. |
| `render_sample_chart.py` | 대표 시계열(`q06_ts_current_account_quarterly`) 캔드 쿼리 결과를 SVG 라인 차트로 캡처하는 도구. |
| `sample_chart_HBOP.svg` | **시연용 캡처본** — 영국 경상수지(HBOP) 1997Q1~2025Q4 분기 시계열(116 점). 가로 880×세로 360, 표준 라이브러리 SVG. |

## 빠른 시작

```bash
# 가상환경 활성화 후
env\Scripts\python.exe visualize\db\launch.py
```

기동 직후 기본 브라우저가 자동으로 `http://127.0.0.1:18421/` 를 연다. 강사
노트북 외부에는 노출되지 않는다(127.0.0.1 한정 바인딩). 종료 시 콘솔에서
Ctrl+C 1회 입력.

## 시연용 캡처본 (`sample_chart_HBOP.svg`)

`render_sample_chart.py` 가 datasette 캔드 쿼리 `q06_ts_current_account_quarterly`
를 호출해 1997Q1~2025Q4 분기 116 점을 받아 SVG 라인 차트로 캡처한 결과다.
강의 보고서 부록·강의 슬라이드 부속 자료·시각화 영역 안내 자료 어느 위치에든
재사용 가능하다.

차트 강조 요소:
- 0 선(점선) — 흑자/적자 경계.
- 마지막 점(2025Q4) 빨강 강조 + 정확값 라벨(`-18,392`) — 강의 보고서
  헤드라인 −£18.4bn 에 해당.

원본 데이터를 다른 시점에 다시 캡처하려면 런처를 켠 상태에서 본 도구를
다시 실행한다(가상환경 인터프리터로):

```bash
env\Scripts\python.exe visualize\db\render_sample_chart.py
```

## 라이선스·출처

- 데이터 출처: 영국 통계청(ONS), *Balance of Payments Statistical Bulletin
  Tables* (분기 발표).
  https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsstatisticalbulletintables
- 라이선스: Open Government Licence v3.0 (OGL v3).
  https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/

## 운영 주의사항

Windows 한국어 로캘에서는 datasette CLI 가 metadata.yaml 을 시스템 기본
인코딩(cp949) 으로 읽어 한국어 description_html 에서 즉시 죽는다. 본 영역의
런처(`launch.py`) 는 자식 프로세스에 `PYTHONUTF8=1` 을 강제 주입하여 이
문제를 차단한다. 직접 `python -m datasette ...` 으로 호출할 때도 반드시
`PYTHONUTF8=1` 을 함께 설정해야 한다.
