"""
HTML → PDF 변환 (Playwright sync API + Chromium headless)
==========================================================

목적
----
보고서 단계 5 §5.3 의 **3 순위 PDF 변환 경로**. 1 순위 LaTeX(xelatex 미설치)
와 2 순위 nbconvert webpdf(Windows asyncio Proactor 비호환,
`NotImplementedError`) 가 모두 실패한 환경에서 최종 채택된 우회 경로이다.

처리 흐름
----------
1. `nbconvert --to html --embed-images` 가 사전에 생성한
   `report/notebook/uk_bop_fx_20y.html` 을 입력으로 받는다.
2. Playwright 의 동기(sync) API 로 Chromium 인스턴스를 headless 로 띄운다.
3. `file://` URI 로 HTML 을 직접 로드한 뒤, 인쇄용(`@media print`) CSS
   적용 상태에서 A4 PDF 로 출력한다.

입력
----
- `report/notebook/uk_bop_fx_20y.html` (nbconvert HTML 중간 산출, 이미지 임베드)

출력
----
- `report/notebook/uk_bop_fx_20y.pdf` (A4·한국어 포함·그래프 6 건 임베드)

의존성
------
- Python 가상환경: `env/Scripts/python.exe`
- 패키지: `playwright` (Chromium 바이너리 필요. 최초 1회
  `playwright install chromium` 으로 다운로드)

실행
----
    c:/Projects/SKKU.England/env/Scripts/python.exe report/code/html_to_pdf.py

주의
----
- Windows 의 asyncio Proactor 이벤트 루프가 nbconvert webpdf 의 비동기
  호출과 호환되지 않아 본 우회 경로가 채택되었다. 본 스크립트는 동기
  API(`sync_playwright`) 를 사용하므로 이 문제와 무관하다.
- HTML → PDF 변환은 그래픽 렌더이므로 본문 값은 변형되지 않는다(저장소
  값 불변 원칙 준수).
"""

from pathlib import Path
import sys

from playwright.sync_api import sync_playwright

# ----------------------------------------------------------------------
# 경로 설정 — 프로젝트 루트(`SKKU.England/`) 기준 상대로 산출 위치를 잡는다.
# ----------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]  # report/code/ 두 단계 위 = 저장소 루트
HTML_PATH = ROOT / "report" / "notebook" / "uk_bop_fx_20y.html"
PDF_PATH = ROOT / "report" / "notebook" / "uk_bop_fx_20y.pdf"

# 입력 HTML 이 없으면 사전 단계(nbconvert --to html)가 누락된 것이므로 즉시 중단
if not HTML_PATH.exists():
    sys.exit(f"HTML 미존재: {HTML_PATH} — 먼저 nbconvert --to html 실행 필요")

print(f"HTML : {HTML_PATH}")
print(f"PDF  : {PDF_PATH}")

# ----------------------------------------------------------------------
# Chromium headless 로 PDF 생성
# ----------------------------------------------------------------------
with sync_playwright() as p:
    # headless Chromium 인스턴스(브라우저 UI 없이 백그라운드 실행)
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # `file://` 로컬 경로 직접 로드. `networkidle` 은 모든 리소스 로드(임베드
    # 이미지·폰트 포함) 완료 시점까지 대기하여 한국어 글꼴·그래프가 빠짐없이
    # 그려진 뒤에 PDF 캡처가 시작되도록 보장한다.
    page.goto(HTML_PATH.as_uri(), wait_until="networkidle")

    # 인쇄(@media print) 스타일을 강제 적용 — 화면용 색·여백이 아닌 인쇄용
    # 레이아웃으로 캡처하기 위함.
    page.emulate_media(media="print")

    # A4 표준 용지 + 본 보고서 권장 여백(상하 18mm·좌우 14mm).
    # `print_background=True` 로 배경색·셀 강조 등 시각 요소까지 포함.
    page.pdf(
        path=str(PDF_PATH),
        format="A4",
        margin={"top": "18mm", "bottom": "18mm", "left": "14mm", "right": "14mm"},
        print_background=True,
        prefer_css_page_size=False,  # CSS @page size 가 있어도 A4 강제
    )
    browser.close()

# 산출 확인용 한 줄 로그 (단계 5 §5.3 검증 트레이스)
print(f"PDF 생성 완료: {PDF_PATH}, 크기 {PDF_PATH.stat().st_size:,} bytes")
