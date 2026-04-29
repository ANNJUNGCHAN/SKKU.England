"""대표 시계열 차트 캡처 — 강의 시연 첨부용 SVG 산출 스크립트.

PLAN.md §3 5단계 §5("대표 시계열(예: 경상수지 분기 시계열) 한 건을 차트로
캡처한다") 의 산출물 산출 도구. datasette UI 의 datasette-vega 차트와 동일한
원본 데이터(`q06_ts_current_account_quarterly` 캔드 쿼리, HBOP 1997Q1–2025Q4
116 분기) 를 가지고 표준 라이브러리만으로 SVG 라인 차트를 그린다.

이 스크립트는 datasette 가 기동된 상태에서 캔드 쿼리 JSON 응답을 받아 SVG
파일 한 건(`visualize/db/sample_chart_HBOP.svg`) 을 생성한다. 외부 의존성은
이미 가상환경에 설치된 `httpx` 만 사용하며 별도 시각화 라이브러리(matplotlib·
pandas 등) 는 신규 도입하지 않는다.

실행 방법(런처가 18421 포트에서 기동 중인 상태에서):
    env\\Scripts\\python.exe visualize\\db\\render_sample_chart.py

산출물:
    visualize/db/sample_chart_HBOP.svg  (라인 차트, 가로 880 × 세로 360)
"""
from __future__ import annotations

import sys
from pathlib import Path
from xml.sax.saxutils import escape

import httpx


# 저장소 루트(`visualize/db/...` 두 단계 위)
REPO_ROOT = Path(__file__).resolve().parents[2]
DATASETTE_BASE = "http://127.0.0.1:18421"
CANNED_QUERY = "q06_ts_current_account_quarterly"
OUTPUT_SVG = REPO_ROOT / "visualize" / "db" / "sample_chart_HBOP.svg"

# SVG 캔버스 치수(픽셀 단위, 강의 슬라이드 16:9 부록에 그대로 끼워 넣을 수
# 있도록 가로 약 880px·세로 약 360px 로 잡는다).
WIDTH = 880
HEIGHT = 360
PAD_LEFT = 70   # Y 축 라벨 공간
PAD_RIGHT = 24
PAD_TOP = 36    # 제목 공간
PAD_BOTTOM = 56  # X 축 라벨 공간


def _fetch_series() -> list[tuple[str, float]]:
    """datasette 캔드 쿼리에서 (시점, 값) 리스트 추출.

    캔드 쿼리 q06 은 이미 ``TIME LIKE '%Q%'`` 필터로 분기 행만 반환하므로,
    별도 후처리 없이 그대로 차트 데이터로 쓴다.
    """
    url = f"{DATASETTE_BASE}/ecos_uk_bop/{CANNED_QUERY}.json?_shape=array"
    resp = httpx.get(url, timeout=10.0)
    resp.raise_for_status()
    rows = resp.json()
    series: list[tuple[str, float]] = []
    for row in rows:
        time = row["시점"]
        value = row["경상수지_GBP_million"]
        if value is None:
            continue
        series.append((time, float(value)))
    return series


def _scale(values: list[float], lo_pad: float = 0.06, hi_pad: float = 0.06) -> tuple[float, float]:
    """축 범위 산출(상하단에 약간의 여유를 둔다)."""
    lo = min(values)
    hi = max(values)
    span = hi - lo if hi > lo else 1.0
    return lo - span * lo_pad, hi + span * hi_pad


def _format_int(v: float) -> str:
    """천 단위 콤마 + 부호 유지(예: -18,392)."""
    return f"{int(round(v)):,}"


def _build_svg(series: list[tuple[str, float]]) -> str:
    """series 를 SVG 문자열 한 덩어리로 직렬화."""
    times = [t for t, _ in series]
    values = [v for _, v in series]
    n = len(values)

    # 축 범위
    y_lo, y_hi = _scale(values)
    plot_w = WIDTH - PAD_LEFT - PAD_RIGHT
    plot_h = HEIGHT - PAD_TOP - PAD_BOTTOM

    def x_pos(i: int) -> float:
        # 데이터 인덱스 → 픽셀 X
        return PAD_LEFT + (i / max(n - 1, 1)) * plot_w

    def y_pos(v: float) -> float:
        # 값 → 픽셀 Y(상단이 0이므로 뒤집어 계산)
        ratio = (v - y_lo) / (y_hi - y_lo)
        return PAD_TOP + (1 - ratio) * plot_h

    # 데이터 폴리라인
    points = " ".join(f"{x_pos(i):.1f},{y_pos(values[i]):.1f}" for i in range(n))

    # Y 축 그리드 + 라벨(0 선 강조)
    grid_steps = 5
    y_lines = []
    for k in range(grid_steps + 1):
        v = y_lo + (y_hi - y_lo) * (k / grid_steps)
        y = y_pos(v)
        y_lines.append(
            f'<line x1="{PAD_LEFT}" y1="{y:.1f}" x2="{PAD_LEFT + plot_w}" y2="{y:.1f}" '
            f'stroke="#e5e5e5" stroke-width="1"/>'
            f'<text x="{PAD_LEFT - 6}" y="{y + 4:.1f}" text-anchor="end" '
            f'font-size="11" fill="#555">{_format_int(v)}</text>'
        )
    # 값 0 선(영점) 강조 — 데이터 범위 안에 0이 들어 있을 때만 그림
    if y_lo < 0 < y_hi:
        y0 = y_pos(0.0)
        y_lines.append(
            f'<line x1="{PAD_LEFT}" y1="{y0:.1f}" x2="{PAD_LEFT + plot_w}" y2="{y0:.1f}" '
            f'stroke="#999" stroke-width="1.2" stroke-dasharray="4 3"/>'
        )

    # X 축 라벨(연도 단위로 5 개만 표시)
    x_label_indices = [0]
    for k in (1, 2, 3, 4):
        x_label_indices.append(int(round(k * (n - 1) / 4)))
    x_label_indices.append(n - 1)
    seen: set[int] = set()
    x_labels = []
    for i in x_label_indices:
        if i in seen:
            continue
        seen.add(i)
        x_labels.append(
            f'<text x="{x_pos(i):.1f}" y="{HEIGHT - PAD_BOTTOM + 18}" '
            f'text-anchor="middle" font-size="11" fill="#555">{escape(times[i])}</text>'
        )

    # 마지막 분기(2025Q4) 점 + 라벨 강조 — 헤드라인 −£18.4bn 시각 강조
    last_x = x_pos(n - 1)
    last_y = y_pos(values[-1])
    last_label = f"{escape(times[-1])} · {_format_int(values[-1])}"

    # 제목 + 부제
    title = "영국 경상수지(HBOP) 분기 시계열 — 1997Q1 ~ 2025Q4"
    subtitle = (
        f"datasette 캔드 쿼리 {CANNED_QUERY} 결과를 표준 라이브러리 SVG 로 캡처 "
        f"(단위: GBP million, n = {n} 분기, 출처: ONS BoP Statistical Bulletin Tables)"
    )

    svg = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 {WIDTH} {HEIGHT}\" width=\"{WIDTH}\" height=\"{HEIGHT}\" font-family=\"Segoe UI, sans-serif\">
  <rect x=\"0\" y=\"0\" width=\"{WIDTH}\" height=\"{HEIGHT}\" fill=\"#ffffff\"/>
  <text x=\"{PAD_LEFT}\" y=\"20\" font-size=\"14\" font-weight=\"600\" fill=\"#222\">{escape(title)}</text>
  <text x=\"{PAD_LEFT}\" y=\"34\" font-size=\"11\" fill=\"#666\">{escape(subtitle)}</text>
  {''.join(y_lines)}
  <polyline points=\"{points}\" fill=\"none\" stroke=\"#1f77b4\" stroke-width=\"1.6\"/>
  <circle cx=\"{last_x:.1f}\" cy=\"{last_y:.1f}\" r=\"4\" fill=\"#d62728\" stroke=\"#fff\" stroke-width=\"1.2\"/>
  <text x=\"{last_x - 8:.1f}\" y=\"{last_y - 10:.1f}\" text-anchor=\"end\" font-size=\"11\" fill=\"#d62728\" font-weight=\"600\">{last_label}</text>
  {''.join(x_labels)}
  <line x1=\"{PAD_LEFT}\" y1=\"{HEIGHT - PAD_BOTTOM}\" x2=\"{PAD_LEFT + plot_w}\" y2=\"{HEIGHT - PAD_BOTTOM}\" stroke=\"#bbb\" stroke-width=\"1\"/>
  <line x1=\"{PAD_LEFT}\" y1=\"{PAD_TOP}\" x2=\"{PAD_LEFT}\" y2=\"{HEIGHT - PAD_BOTTOM}\" stroke=\"#bbb\" stroke-width=\"1\"/>
</svg>
"""
    return svg


def main() -> int:
    """진입점. datasette 응답을 받아 SVG 차트 1건을 저장."""
    series = _fetch_series()
    if not series:
        print("[차트 캡처 오류] 빈 시계열 — datasette 가 18421 포트에서 기동 중인지 확인.", file=sys.stderr)
        return 1
    svg = _build_svg(series)
    OUTPUT_SVG.write_text(svg, encoding="utf-8")
    print(f"[차트 캡처] 저장 완료 — {OUTPUT_SVG.relative_to(REPO_ROOT)} ({len(series)} 분기)")
    print(f"  최신: {series[-1][0]} = {series[-1][1]:,.0f} GBP million")
    return 0


if __name__ == "__main__":
    sys.exit(main())
