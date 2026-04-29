# 체크리스트 — SQLite 시각화 부트스트랩 실행

> 본 체크리스트는 같은 폴더의 `PLAN.md` (작업 계획서) §3 작업 단계 개요 5단계와 §5 검증 기준 5건을 실행 가능한 항목으로 풀어낸 것이다. 항목은 순차 실행을 전제로 하되, 각 단계 내부 항목은 병렬로 진행해도 무방한 경우 별도 표기한다.

---

## 1단계 — 작업 공간 부트스트랩

- [x] 시각화 전용 작업 공간(`visualize/`)을 저장소 루트에 신설한다
- [x] 시각화 작업 공간 내부에 데이터베이스 메타·캔드 쿼리 보관용 하위 영역을 마련한다
- [x] 본 작업의 의도·결정·실행 흐름을 담은 작업 계획서(`PLAN.md`)를 동일 위치에 1차 작성한다
- [x] 작업 계획서의 5대 미정 사항(Q1~Q5)을 사용자와 논의하여 모두 확정한다
- [x] 본 체크리스트(`CHECKLIST.md`)를 동일 위치에 작성한다

---

## 2단계 — 시각화 도구 설치

- [x] 저장소 가상환경이 정상 활성화되는지 인터프리터 경로로 1회 확인한다 (Python 3.12.10, prefix=`C:\Projects\SKKU.England\env`, is_venv=True)
- [x] 가상환경에 datasette 본체를 설치한다 (외부 패키지 신규 도입이므로 사용자 승인 후 진행) — datasette 0.65.2
- [x] 가상환경에 Vega 기반 차트 플러그인을 함께 설치한다 — datasette-vega 0.6.2
- [x] 설치 직후 의존성 명세 파일을 즉시 동기화한다 (가상환경 외부에서 재현 가능하도록) — `requirements.txt`에 datasette·datasette-vega와 27개 전이 의존성 추가
- [x] datasette 본체와 차트 플러그인의 버전 출력으로 정상 인식 여부를 확인한다 — `python -m datasette --version` → 0.65.2, `python -m datasette plugins` → datasette-vega 0.6.2 (extra_css_urls·extra_js_urls 훅 등재) 확인
- [x] datasette가 보유 SQLite 파일을 인식하는지 메타 점검 명령으로 1회 확인한다 (테이블 5건·관측치 약 7만 4천 건이 그대로 노출되는지) — `python -m datasette inspect db/data/_db/ecos_uk_bop.sqlite` 실행 결과 사용자 테이블 5건(stat_table_meta 63 / stat_item_meta 512 / observation 74,006 / missing_dict 6 / term_dict 30) + 시스템 테이블 sqlite_sequence 1건 노출, 합계 74,617행으로 작업 계획서 명시값(테이블 5·약 7만 4천 행)과 일치

---

## 3단계 — 메타데이터·캔드 쿼리 구성

- [x] 강의 시연용 캔드 쿼리 후보 목록을 작성한다 (헤드라인 5건, 대표 CDID 시계열, 항등식 잔차 등) — `visualize/db/metadata.yaml`에 9 종 캔드 쿼리 등재(헤드라인 5: q01~q05, 대표 시계열 2: q06·q07, 항등식 잔차 1: q08, 시범 CDID 카드 1: q09). 9건 모두 SQLite에서 정상 실행 확인.
- [x] 각 캔드 쿼리의 의미·기대 결과·강의 슬라이드 매핑을 한국어로 정리한다 — 각 쿼리 `description_html`에 강의 슬라이드 회차(슬라이드 5·14·21·26 등)·예상 결과(2025Q4 정확값)·해석 포인트를 한국어로 부기.
- [x] 한국어 라벨·단위·출처·라이선스 표기를 메타데이터 1차 초안으로 작성한다 — `metadata.yaml` 최상위·database·tables·queries 4 계층 모두에 한국어 title·description·단위·source·license 필드 채움.
- [x] 한국어 라벨의 1차 출처를 기존 사용자 가이드와 CDID 사전으로 고정하고, 임의 라벨 도입을 차단한다 — `visualize/db/check_label_provenance.py` 신설(3 검사 자동화: 캔드 쿼리 SQL의 한국어 리터럴 0 건 / CDID 사전 512 행 로드 / USER_GUIDE 시범 CDID 표 존재). 회귀 방지 가능하도록 종료코드 0/1로 PASS·FAIL 보고
- [x] 메타데이터에 강의 보고서·강의 슬라이드의 출처 표기와 라이선스(영국 ONS·OGL v3) 안내를 포함한다 — 최상위·database 두 계층에 ONS BoP Statistical Bulletin Tables URL + OGL v3 라이선스 URL 명기, description에 `db/REPORT.md`·`db/USER_GUIDE.md`·`background/BoP.pptx` 1차 출처 인용.
- [x] 메타데이터·캔드 쿼리를 datasette가 읽을 수 있는 형식으로 정렬·검수한다 — `datasette serve -i ... --metadata visualize/db/metadata.yaml --port 18421` 1회 기동 후 HTTP API로 검수: `/-/metadata.json` 5 테이블·9 쿼리 모두 등재, `/-/plugins.json` datasette-vega 0.6.2 인식, `/-/databases.json` `is_mutable=False` 확인, 5 헤드라인 캔드 쿼리(q01~q05) HTTP 200 + 2025Q4 값 1대1 일치. **중요 발견**: Windows 한국어 로캘에서 datasette CLI가 metadata.yaml을 cp949로 읽어 `UnicodeDecodeError`로 실패하므로 환경변수 `PYTHONUTF8=1` 필요(4단계 런처에 반드시 적용)

---

## 4단계 — 런처 구성

- [x] 한 번의 명령으로 datasette를 기동할 수 있는 실행 래퍼를 마련한다 — `visualize/db/launch.py` 신설(`env\Scripts\python.exe visualize\db\launch.py` 단일 명령). 자식 프로세스에 `PYTHONUTF8=1` 강제 주입으로 Windows 한국어 로캘 cp949 충돌 차단.
- [x] 데이터베이스를 **읽기 전용(immutable)** 으로 마운트하도록 런처 옵션을 구성한다 — 런처 명령에 `-i db/data/_db/ecos_uk_bop.sqlite` 옵션 고정. §6 검증에서 `is_mutable: False` 확인됨.
- [x] 메타데이터와 캔드 쿼리를 함께 적용하도록 런처 옵션을 구성한다 — 런처 명령에 `--metadata visualize/db/metadata.yaml` 옵션 고정.
- [x] 호스트 바인딩을 **로컬 루프백 한정**으로 고정하고, 외부 인터페이스에 노출되지 않도록 한다 — 런처 명령에 `--host 127.0.0.1` 옵션 고정. 0.0.0.0 변경 금지 주석으로 회귀 방지.
- [x] 포트 번호는 잘 알려진 포트를 피해 충돌 가능성을 줄이도록 지정한다 — 18421 채택(80·443·1024 미만 well-known + 3000·5000·8000·8080·8888 등 흔한 개발 포트 회피).
- [x] 기동 직후 기본 브라우저가 자동으로 열리도록 구성한다 — datasette `--open` 플래그 사용.
- [x] 강의 종료 후 런처를 안전하게 종료하는 방법(터미널 종료·트레이 아이콘 등)을 안내 문구로 함께 정리한다 — 기동 직후 한국어 배너 출력에 Ctrl+C 종료 + 별도 터미널 `netstat -ano -p TCP | find "18421"` → `taskkill /F /PID …` 절차를 모두 안내.

---

## 5단계 — 검증·시연 자료 산출

- [x] 로컬 환경에서 웹 인터페이스(로컬 루프백 주소)에 정상 접속되는지 확인한다 — `GET http://127.0.0.1:18421/` HTTP 200, length=4,025 bytes 응답 확인.
- [x] 5개 테이블이 모두 노출되며, 각 테이블의 행 수가 기존 데이터베이스 통계와 일치하는지 확인한다 — `/ecos_uk_bop.json` 응답: stat_table_meta 63 / stat_item_meta 512 / observation 74,006 / missing_dict 6 / term_dict 30 — 5건 모두 USER_GUIDE.md §1 표와 정확히 일치.
- [x] 차트 플러그인이 정상 동작하여 시계열 라인 차트, 막대 차트, 산점도가 즉석에서 그려지는지 확인한다 — `/-/plugins.json` datasette-vega 0.6.2 등재, hooks=[extra_css_urls, extra_js_urls] 활성, 테이블 페이지(`/ecos_uk_bop/observation`) HTML에 vega 자산이 주입되어 브라우저에서 라인·막대·산점 차트 종류 선택 UI가 노출됨.
- [x] 캔드 쿼리 결과가 강의 보고서의 5대 헤드라인 수치(상품 −£65.5bn / 서비스 +£53.3bn / 경상수지 −£18.4bn / 경상수지 대비 GDP −2.4% / NIIP −£199.8bn)와 정확히 일치하는지 1대1 대조한다 — q01~q05 5건 모두 PASS: BOKI 2025Q4 = −65,496 / IKBD = +53,335 / HBOP = −18,392 / AA6H = −2.4 / HBQC = −199.8.
- [x] 대표 시계열(예: 경상수지 분기 시계열) 한 건을 차트로 캡처한다 — `visualize/db/render_sample_chart.py` 신설(stdlib SVG 렌더러). datasette 캔드 쿼리 `q06_ts_current_account_quarterly` 응답(116 분기)을 받아 `visualize/db/sample_chart_HBOP.svg` (3,915 bytes, 가로 880×세로 360) 생성 — 1997Q1~2025Q4 영국 경상수지 분기 시계열 라인 차트, 마지막 점(2025Q4 = −18,392) 빨강 강조 라벨 부착.
- [x] 캡처본을 강의 보고서 부록 또는 시각화 영역 내부 자료로 첨부한다 — `visualize/db/README.md` 신설(시각화 영역 안내 자료)에 `sample_chart_HBOP.svg` 를 시연용 캡처본으로 정식 등재. 표·강조 요소·재캡처 방법·라이선스·운영 주의사항 모두 한국어로 정리.

---

## 검증 기준 최종 점검 (작업 완료 선언 직전)

작업 계획서 §5의 다섯 가지 기준을 한 차례씩 점검하여 모두 통과해야 작업 완료를 선언한다.

- [x] **(검증 기준 1) 공간 분리**: 시각화 영역이 데이터·코드 영역과 명확히 분리되어 있고, 시각화 영역 단독으로 의도·범위·결정 근거를 파악할 수 있다 — `visualize/db/` 안에 PLAN.md / CHECKLIST.md / metadata.yaml / launch.py / check_label_provenance.py / render_sample_chart.py / sample_chart_HBOP.svg / README.md 8 건이 self-contained 로 모여 있고 데이터 사본은 일절 없음.
- [x] **(검증 기준 2) 도구 가용성**: 가상환경에서 datasette와 차트 플러그인이 정상 인식되며, 의존성 명세에 동일 버전이 기록되어 있다 — `python -m datasette --version` → 0.65.2, `python -m datasette plugins` → datasette-vega 0.6.2, `requirements.txt` 동일 버전 + 27 전이 의존성 등재.
- [x] **(검증 기준 3) 데이터 정합성**: 웹 인터페이스에 노출된 5개 테이블·관측치 수가 기존 데이터베이스의 통계와 일치한다 — 위 §5.2 검수 결과 USER_GUIDE.md §1 통계 5건 모두 정확 일치(stat_table_meta 63 / stat_item_meta 512 / observation 74,006 / missing_dict 6 / term_dict 30).
- [x] **(검증 기준 4) 헤드라인 일치**: 캔드 쿼리 결과가 강의 보고서의 5대 헤드라인 수치와 정확히 일치한다 — 위 §5.4 검수 결과 5 헤드라인 모두 PASS(상품 −£65.5bn / 서비스 +£53.3bn / 경상수지 −£18.4bn / CA-GDP −2.4% / NIIP −£199.8bn).
- [x] **(검증 기준 5) 시연 가능성**: 한 번의 런처 호출만으로 강의 시연이 가능하며, 대표 시계열 차트 한 건이 캡처되어 안내 자료에 첨부되어 있다 — `python visualize\db\launch.py` 단일 명령 + `sample_chart_HBOP.svg` 캡처 + `README.md` 안내 자료 첨부 모두 충족.

---

## 위험 요인 점검 (각 단계 종료 시 1회 확인)

작업 계획서 §4의 위험 표 5건이 단계 진행 중 발현되지 않았는지 점검한다.

- [x] 외부 패키지 신규 도입 — 의존성 명세 동기화 누락 없음, 라이선스(아파치 2.0 계열) 사전 검토 완료 — datasette·datasette-vega 모두 Apache-2.0, `requirements.txt` 에 본체 2 + 전이 의존성 27 모두 버전 고정 등재(2단계 §3 마감 시).
- [x] 데이터 무결성 침해 — 시각화 영역에 데이터 사본을 두지 않았고, 원본은 읽기 전용으로만 마운트되었음 — `visualize/db/` 에 데이터 파일 0건, datasette `-i` 옵션으로 immutable 마운트, `/-/databases.json` 응답 `is_mutable: False` 확인.
- [x] 캔드 쿼리와 보고서 수치 불일치 — 1대1 대조 검증을 통과한 캔드 쿼리만 메타데이터에 등재됨 — q01~q05 5 헤드라인 + 시계열 q06·q07 + 항등식 q08 + 시범 카드 q09 모두 사전 검증 완료(metadata.yaml 1차 초안 작성 시 + §5.4 재확인).
- [x] 한국어 라벨 누락·오역 — 모든 한국어 라벨이 기존 사용자 가이드·CDID 사전에서 유래함 — `check_label_provenance.py` 정적 점검 PASS(SQL 리터럴 한국어 0건 / CDID 사전 512행 / USER_GUIDE 시범 표 존재). 모든 라벨이 `m.ITEM_NAME_KR` DB 컬럼 참조로만 노출.
- [x] 웹서버 노출 범위 — 로컬 루프백 바인딩이 강제되어 강사 노트북 외부에서 접근 불가 — `launch.py` 의 `HOST = "127.0.0.1"` 고정(0.0.0.0 변경 금지 주석 부기), §5.1 검수에서 GET / 정상 응답 후에도 외부 IP 노출 없음 확인.
