# -*- coding: utf-8 -*-
"""SKKU 거시경제학 보고서 단계 4 §4.4 — 그래프 6건 + 데이터 source 6 CSV 산출.

입력  : c:/Projects/SKKU.England/report/data/*.csv (단계 4 §4.1~§4.3 산출물)
출력  : c:/Projects/SKKU.England/report/figures/fig0N_*.png (PNG, dpi 150)
        c:/Projects/SKKU.England/report/figures/fig0N_data.csv (그래프 1:1 source)

원칙  : (i) matplotlib backend = 'Agg' 강제, (ii) 한국어 라벨 정상 렌더,
        (iii) 입력 CSV 값 절대 수정 금지 — 시각화·재배치만.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # GUI 없이 PNG 저장 강제

import matplotlib.pyplot as plt
from matplotlib import rcParams

# cp949 콘솔에서도 한국어 출력 깨지지 않도록 stdout UTF-8 가드
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

# ---------------------------------------------------------------------------
# 한국어 폰트 설정 — Windows 기본 한글 폰트 우선 탐색
# ---------------------------------------------------------------------------
_KR_FONT_CANDIDATES = [
    "Malgun Gothic",
    "MalgunGothic",
    "NanumGothic",
    "Nanum Gothic",
    "Noto Sans CJK KR",
    "Noto Sans KR",
    "AppleGothic",
    "Gulim",
    "Dotum",
]


def _select_korean_font() -> str:
    """설치된 폰트 중 한국어 가능 폰트 1개를 선택한다."""
    from matplotlib import font_manager

    available = {f.name for f in font_manager.fontManager.ttflist}
    for name in _KR_FONT_CANDIDATES:
        if name in available:
            return name
    return rcParams["font.family"][0] if rcParams["font.family"] else "sans-serif"


_KR_FONT = _select_korean_font()
rcParams["font.family"] = _KR_FONT
rcParams["axes.unicode_minus"] = False  # 마이너스 부호 깨짐 방지
print(f"[font] Korean font selected: {_KR_FONT}")

# ---------------------------------------------------------------------------
# 경로 상수
# ---------------------------------------------------------------------------
ROOT = Path("c:/Projects/SKKU.England/report")
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# 공통 유틸
# ---------------------------------------------------------------------------
def read_csv(path: Path) -> list[dict]:
    """단계 4 §4.1~§4.3 산출 CSV 1 건을 DictReader 로 읽어 반환한다.

    - 인코딩: UTF-8 고정(단계 4 산출물 통일 규약).
    - `#` 로 시작하는 주석 헤더(부호 규약·산출 일자 등)는 자동 건너뛴다 — 본
      함수가 데이터 행만 통과시키므로 호출 측에서 별도 필터가 불필요.
    - 반환값: 각 행이 컬럼명 → 문자열 매핑인 ``list[dict]``. 숫자 변환은
      호출 측에서 :func:`fnum` 으로 명시 수행한다(빈 셀 → NaN 보존).
    """
    rows = []
    with path.open("r", encoding="utf-8") as f:
        # 주석(`#`) 헤더 라인 건너뛰기 — DictReader 가 header 자동 인식.
        lines = [ln for ln in f if not ln.lstrip().startswith("#")]
    reader = csv.DictReader(lines)
    for r in reader:
        rows.append(r)
    return rows


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    """그래프 1 건당 동봉 source CSV 1 건을 기록한다 (재현성 보장).

    - 인코딩: UTF-8, ``newline=""`` 로 Windows 환경의 ``\r\n`` 중복 방지.
    - 부작용: ``path`` 위치에 평면 표 1 개 생성. 호출 측은 ``rows`` 의 모든
      값이 평면(스칼라) 값임을 보장해야 한다.
    - 콘솔 로그: 상대경로 + 행 수를 1 줄 출력해 멱등 재실행 시 추적성 확보.
    """
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"[csv ] {path.relative_to(ROOT)} ({len(rows)} rows)")


def fnum(x) -> float:
    """CSV 셀 문자열을 ``float`` 으로 변환한다 (빈 셀 → NaN).

    데이터 무수정 원칙 상 결측을 0 으로 치환하지 않으므로 빈 문자열은 NaN
    으로만 표현한다. 호출 측에서 NaN 행은 시각화·통계량 산출 전에 별도
    필터링 책임을 진다.
    """
    if x is None or x == "":
        return float("nan")
    return float(x)


def time_to_idx(t: str) -> int:
    """``YYYYQn`` 분기 라벨을 0-based 정수 인덱스로 변환한다.

    예: ``2006Q1 → 0``, ``2006Q2 → 1``, …, ``2025Q4 → 79``. 2006Q1 을 기준
    원점으로 두는 이유는 본 보고서 분석 기간이 2006Q1~2025Q4 (n=80) 로
    고정돼 있기 때문이다.
    """
    y, q = int(t[:4]), int(t[-1])
    return (y - 2006) * 4 + (q - 1)


def quarter_labels_every(times: list[str], step: int = 8) -> tuple[list[int], list[str]]:
    """X 축 눈금 위치·라벨을 ``step`` 분기 간격으로 생성한다.

    - 입력: 분기 라벨의 정렬된 리스트 (예: ``['2006Q1', ..., '2025Q4']``).
    - 출력: ``(ticks, labels)`` — ``ticks`` 는 정수 인덱스, ``labels`` 는
      대응되는 분기 라벨. 마지막 분기는 항상 표시되도록 강제 추가하여 가장
      최근 시점의 정보를 반드시 노출한다.
    - 기본 ``step=8`` 은 2 년 간격(분기 8 개) — 80 분기 시계열에서 11 개
      눈금이 생성되며 가독성·정보량 균형이 가장 양호하다.
    """
    idx = list(range(len(times)))
    ticks = [i for i in idx if i % step == 0]
    if (len(times) - 1) not in ticks:
        ticks.append(len(times) - 1)
    labs = [times[i] for i in ticks]
    return ticks, labs


# ---------------------------------------------------------------------------
# §4.4.1 — CA 합계(HBOP) 분기 시계열 라인 차트
# ---------------------------------------------------------------------------
def fig01_ca_quarterly() -> None:
    """§4.4.1 — CA 합계(HBOP) 80 분기 라인 + 충격 5 건 빨강 점 강조.

    - 입력: ``report/data/quarterly_series_2006q1_2025q4.csv`` 중
      ``cdid == 'HBOP'`` 의 80 행.
    - 시각화 요소: 본 라인(짙은 청, 1.6 pt) + 0 선 점선 + 충격 5 분기
      (2008Q4·2016Q3·2020Q2·2022Q3·2025Q4) 빨강 점·라벨.
    - 산출물: ``report/figures/fig01_ca_quarterly.png`` (PNG, dpi 150) +
      동봉 ``fig01_data.csv`` (80 행, ``time, ca_hbop_gbp_million,
      is_shock_quarter``).
    - 데이터 변형 금지 — 입력 CSV 의 ``data_value`` 를 그대로 시각화한다.
    """
    src = read_csv(DATA_DIR / "quarterly_series_2006q1_2025q4.csv")
    rows = sorted([r for r in src if r["cdid"] == "HBOP"], key=lambda r: r["time"])
    times = [r["time"] for r in rows]
    values = [fnum(r["data_value"]) for r in rows]

    shock_quarters = ["2008Q4", "2016Q3", "2020Q2", "2022Q3", "2025Q4"]

    fig, ax = plt.subplots(figsize=(11, 5), dpi=150)
    ax.plot(range(len(times)), values, color="#1f4e79", linewidth=1.6, label="CA (HBOP)")
    ax.axhline(0, color="#666666", linestyle=":", linewidth=1.0, label="0선")
    # 충격 분기 5건 빨강 점
    sx, sy = [], []
    for sq in shock_quarters:
        if sq in times:
            i = times.index(sq)
            sx.append(i)
            sy.append(values[i])
    ax.scatter(sx, sy, color="#c0392b", s=55, zorder=5, label="충격 분기 5건")
    for xi, yi, lab in zip(sx, sy, shock_quarters):
        ax.annotate(lab, (xi, yi), xytext=(4, 8), textcoords="offset points",
                    fontsize=8, color="#c0392b")

    ticks, labs = quarter_labels_every(times, step=8)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labs, rotation=30, ha="right")
    ax.set_xlabel("분기")
    ax.set_ylabel("CA 합계 (GBP million, ONS 표시 부호)")
    ax.set_title("§4.4.1 영국 경상수지(CA, HBOP) 분기 시계열 — 2006Q1~2025Q4 (n=80)")
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.legend(loc="lower left", fontsize=9)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig01_ca_quarterly.png", dpi=150)
    plt.close(fig)
    print(f"[png ] fig01_ca_quarterly.png")

    # data source 1:1 CSV
    out_rows = [
        {
            "time": t,
            "ca_hbop_gbp_million": v,
            "is_shock_quarter": "1" if t in shock_quarters else "0",
        }
        for t, v in zip(times, values)
    ]
    write_csv(
        FIG_DIR / "fig01_data.csv",
        out_rows,
        ["time", "ca_hbop_gbp_million", "is_shock_quarter"],
    )


# ---------------------------------------------------------------------------
# §4.4.2 — CA 4 세부항목(BOKI·IKBD·HBOJ·IKBP) 분기 시계열 비교 라인
# ---------------------------------------------------------------------------
def fig02_ca_components() -> None:
    """§4.4.2 — CA 4 세부항목(BOKI·IKBD·HBOJ·IKBP) 분기 시계열 비교 라인.

    - 입력: ``quarterly_series_2006q1_2025q4.csv`` 중 4 CDID × 80 분기
      = 320 행.
    - 색상 규약: BOKI 빨강(상품수지·만성 적자) / IKBD 녹색(서비스수지·구조적
      흑자) / HBOJ 청(본원소득) / IKBP 보라(이전소득). 색상 의미는
      `report/research/03_ca_decomposition.md` 강의 인용 카드와 일관.
    - 산출물: ``fig02_ca_components.png`` + 동봉 ``fig02_data.csv`` (80 행,
      4 항목 wide-form).
    """
    src = read_csv(DATA_DIR / "quarterly_series_2006q1_2025q4.csv")
    cdids = ["BOKI", "IKBD", "HBOJ", "IKBP"]
    labels = {
        "BOKI": "상품수지 (BOKI)",
        "IKBD": "서비스수지 (IKBD)",
        "HBOJ": "본원소득 (HBOJ)",
        "IKBP": "이전소득 (IKBP)",
    }
    colors = {
        "BOKI": "#c0392b",
        "IKBD": "#1f8a4c",
        "HBOJ": "#1f4e79",
        "IKBP": "#8e44ad",
    }
    series = {}
    times_ref = None
    for cd in cdids:
        rs = sorted([r for r in src if r["cdid"] == cd], key=lambda r: r["time"])
        ts = [r["time"] for r in rs]
        vs = [fnum(r["data_value"]) for r in rs]
        if times_ref is None:
            times_ref = ts
        series[cd] = vs

    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=150)
    x = list(range(len(times_ref)))
    for cd in cdids:
        ax.plot(x, series[cd], color=colors[cd], linewidth=1.5, label=labels[cd])
    ax.axhline(0, color="#666666", linestyle=":", linewidth=1.0, label="0선")

    ticks, labs = quarter_labels_every(times_ref, step=8)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labs, rotation=30, ha="right")
    ax.set_xlabel("분기")
    ax.set_ylabel("4 세부 수지 (GBP million)")
    ax.set_title(
        "§4.4.2 CA 4 세부항목 분기 시계열 — BOKI·IKBD·HBOJ·IKBP (2006Q1~2025Q4, n=80)"
    )
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.legend(loc="lower left", fontsize=9, ncol=2)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig02_ca_components.png", dpi=150)
    plt.close(fig)
    print(f"[png ] fig02_ca_components.png")

    out_rows = []
    for i, t in enumerate(times_ref):
        out_rows.append(
            {
                "time": t,
                "boki_goods_gbp_million": series["BOKI"][i],
                "ikbd_services_gbp_million": series["IKBD"][i],
                "hboj_primary_income_gbp_million": series["HBOJ"][i],
                "ikbp_secondary_income_gbp_million": series["IKBP"][i],
            }
        )
    write_csv(
        FIG_DIR / "fig02_data.csv",
        out_rows,
        [
            "time",
            "boki_goods_gbp_million",
            "ikbd_services_gbp_million",
            "hboj_primary_income_gbp_million",
            "ikbp_secondary_income_gbp_million",
        ],
    )


# ---------------------------------------------------------------------------
# §4.4.3 — FA 합계(-HBNT) + 5 세부항목 누적 막대 + 합계 라인
# ---------------------------------------------------------------------------
def fig03_fa_components() -> None:
    """§4.4.3 — FA 5 세부항목 부호 분리 누적 막대 + 합계(-HBNT) 라인 오버레이.

    - 입력: ``quarterly_series_2006q1_2025q4.csv`` 중 6 CDID(5 세부 + 합계)
      × 80 분기 = 480 행. 부호 반전 표시(ONS Table A 부표 3 규약: 기호 앞
      ``-`` 는 BPM6 자산-부채 부호 규약을 영국식으로 표시하기 위한 sign_prefix).
    - 시각화 규약: 양수 막대는 0 위로, 음수 막대는 0 아래로 분리 누적 — 단순
      부호 무시 누적은 합계 변동의 의미를 가린다는 슬라이드 21 해설을 반영.
    - 합계 라인은 막대 위(``zorder=10``) 에 오버레이해 항등식
      ``-HBNT = -MU7M + -HHZD + -ZPNN + -HHYR + -LTCV`` 의 시각적 검증을
      가능케 한다.
    - 산출물: ``fig03_fa_components.png`` + 동봉 ``fig03_data.csv`` (80 행,
      6 컬럼).
    """
    src = read_csv(DATA_DIR / "quarterly_series_2006q1_2025q4.csv")
    sub_cdids = ["-MU7M", "-HHZD", "-ZPNN", "-HHYR", "-LTCV"]
    total_cdid = "-HBNT"
    labels = {
        "-MU7M": "직접투자 (-MU7M)",
        "-HHZD": "증권투자 (-HHZD)",
        "-ZPNN": "파생금융상품 (-ZPNN)",
        "-HHYR": "기타투자 (-HHYR)",
        "-LTCV": "준비자산 (-LTCV)",
        "-HBNT": "FA 합계 (-HBNT)",
    }
    colors = {
        "-MU7M": "#1f4e79",
        "-HHZD": "#c0392b",
        "-ZPNN": "#f39c12",
        "-HHYR": "#1f8a4c",
        "-LTCV": "#8e44ad",
    }

    series = {}
    times_ref = None
    for cd in sub_cdids + [total_cdid]:
        rs = sorted([r for r in src if r["cdid"] == cd], key=lambda r: r["time"])
        ts = [r["time"] for r in rs]
        vs = [fnum(r["data_value"]) for r in rs]
        if times_ref is None:
            times_ref = ts
        series[cd] = vs

    fig, ax = plt.subplots(figsize=(12, 5.5), dpi=150)
    x = list(range(len(times_ref)))

    # 누적 막대: 양수/음수 분리 누적 (signed stacked bar)
    pos_bottom = [0.0] * len(times_ref)
    neg_bottom = [0.0] * len(times_ref)
    for cd in sub_cdids:
        vs = series[cd]
        # 양수·음수 분리 시각화로 양 방향 누적 가능
        pos_part = [v if v > 0 else 0.0 for v in vs]
        neg_part = [v if v < 0 else 0.0 for v in vs]
        ax.bar(x, pos_part, bottom=pos_bottom, color=colors[cd], width=0.8,
               label=labels[cd], alpha=0.85, edgecolor="none")
        ax.bar(x, neg_part, bottom=neg_bottom, color=colors[cd], width=0.8,
               alpha=0.85, edgecolor="none")
        pos_bottom = [a + b for a, b in zip(pos_bottom, pos_part)]
        neg_bottom = [a + b for a, b in zip(neg_bottom, neg_part)]

    # 합계 라인
    ax.plot(x, series[total_cdid], color="black", linewidth=1.6,
            label=labels[total_cdid], zorder=10)
    ax.axhline(0, color="#666666", linestyle=":", linewidth=0.9)

    ticks, labs = quarter_labels_every(times_ref, step=8)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labs, rotation=30, ha="right")
    ax.set_xlabel("분기")
    ax.set_ylabel("FA 5 세부항목 (GBP million, 부호 반전 표시)")
    ax.set_title(
        "§4.4.3 영국 금융계정(FA, -HBNT) 5 세부항목 누적 막대 + 합계 라인 — 2006Q1~2025Q4"
    )
    ax.grid(True, linestyle=":", alpha=0.3, axis="y")
    ax.legend(loc="upper left", fontsize=8, ncol=3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig03_fa_components.png", dpi=150)
    plt.close(fig)
    print(f"[png ] fig03_fa_components.png")

    out_rows = []
    for i, t in enumerate(times_ref):
        out_rows.append(
            {
                "time": t,
                "fa_di_minus_mu7m_gbp_million": series["-MU7M"][i],
                "fa_pi_minus_hhzd_gbp_million": series["-HHZD"][i],
                "fa_fd_minus_zpnn_gbp_million": series["-ZPNN"][i],
                "fa_oi_minus_hhyr_gbp_million": series["-HHYR"][i],
                "fa_ra_minus_ltcv_gbp_million": series["-LTCV"][i],
                "fa_total_minus_hbnt_gbp_million": series["-HBNT"][i],
            }
        )
    write_csv(
        FIG_DIR / "fig03_data.csv",
        out_rows,
        [
            "time",
            "fa_di_minus_mu7m_gbp_million",
            "fa_pi_minus_hhzd_gbp_million",
            "fa_fd_minus_zpnn_gbp_million",
            "fa_oi_minus_hhyr_gbp_million",
            "fa_ra_minus_ltcv_gbp_million",
            "fa_total_minus_hbnt_gbp_million",
        ],
    )


# ---------------------------------------------------------------------------
# §4.4.4 — BoP 항등식 잔차 분기 라인 차트 (충격 강조)
# ---------------------------------------------------------------------------
def fig04_identity_residual() -> None:
    """§4.4.4 — BoP 항등식 잔차 라인 + ±1σ·±2σ 강조선 + |z|>2 분기 빨강 점.

    - 입력: ``report/data/identity_residual_2006q1_2025q4.csv`` 80 행 중
      ``residual`` 컬럼.
    - 잔차 정의: ``CA(HBOP) + KA(FNVQ) + FA(-HBNT) + NEO(HHDH)`` (단계 4
      §4.2 산출). ONS Table A 의 표시 부호를 그대로 합산하므로 평균이 0 이
      아닐 수 있다 (NEO 의 구조적 비대칭성을 시사).
    - 통계량: 본 함수가 직접 평균·SD·표준화 z-score 를 계산해 그래프에
      반영한다. 표본 분산은 자유도 ``n-1`` (불편분산) 사용.
    - 강조 분기: ``|z| > 2`` 인 분기(데이터 실측 기준)를 모두 빨강 점으로
      표시. **사용자 사양은 2 분기였으나 실측은 3 분기** — 데이터 무수정
      원칙에 따라 임의 누락하지 않고 모두 표시. 차이는 마크다운 §2.4 에
      명시.
    - 산출물: ``fig04_identity_residual.png`` + 동봉 ``fig04_data.csv``
      (80 행, ``time, residual_gbp_million, z_score, abs_z_gt2``).
    """
    src = read_csv(DATA_DIR / "identity_residual_2006q1_2025q4.csv")
    rows = sorted(src, key=lambda r: r["time"])
    times = [r["time"] for r in rows]
    resid = [fnum(r["residual"]) for r in rows]

    # 평균·SD 계산 (n=80)
    n = len(resid)
    mean = sum(resid) / n
    var = sum((v - mean) ** 2 for v in resid) / (n - 1)
    sd = var**0.5

    z = [(v - mean) / sd for v in resid]
    over2_q = [t for t, zi in zip(times, z) if abs(zi) > 2]
    print(f"  identity residual mean={mean:.2f}, sd={sd:.2f}, |z|>2 분기={over2_q}")

    fig, ax = plt.subplots(figsize=(11, 5), dpi=150)
    x = list(range(len(times)))
    ax.plot(x, resid, color="#1f4e79", linewidth=1.6, label="잔차 (CA+KA+FA+NEO)")
    ax.axhline(0, color="#666666", linestyle="-", linewidth=0.8)
    ax.axhline(mean + sd, color="#888888", linestyle=":", linewidth=0.9,
               label=f"+1σ ({mean+sd:.0f})")
    ax.axhline(mean - sd, color="#888888", linestyle=":", linewidth=0.9,
               label=f"-1σ ({mean-sd:.0f})")
    ax.axhline(mean + 2 * sd, color="#c0392b", linestyle="--", linewidth=0.9,
               label=f"+2σ ({mean+2*sd:.0f})")
    ax.axhline(mean - 2 * sd, color="#c0392b", linestyle="--", linewidth=0.9,
               label=f"-2σ ({mean-2*sd:.0f})")

    # 2σ 밖 분기 빨강 점 강조
    sx, sy, slabs = [], [], []
    for i, t in enumerate(times):
        if abs(z[i]) > 2:
            sx.append(i)
            sy.append(resid[i])
            slabs.append(t)
    ax.scatter(sx, sy, color="#c0392b", s=70, zorder=6, label="|z|>2 분기")
    for xi, yi, lab in zip(sx, sy, slabs):
        ax.annotate(lab, (xi, yi), xytext=(5, 8), textcoords="offset points",
                    fontsize=8, color="#c0392b")

    ticks, labs = quarter_labels_every(times, step=8)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labs, rotation=30, ha="right")
    ax.set_xlabel("분기")
    ax.set_ylabel("잔차 (GBP million)")
    ax.set_title(
        f"§4.4.4 BoP 항등식 잔차 — 평균 {mean:.0f}, SD {sd:.0f} (n={n})"
    )
    ax.grid(True, linestyle=":", alpha=0.4)
    ax.legend(loc="lower left", fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig04_identity_residual.png", dpi=150)
    plt.close(fig)
    print(f"[png ] fig04_identity_residual.png")

    out_rows = []
    for i, t in enumerate(times):
        out_rows.append(
            {
                "time": t,
                "residual_gbp_million": resid[i],
                "z_score": round(z[i], 6),
                "abs_z_gt2": "1" if abs(z[i]) > 2 else "0",
            }
        )
    write_csv(
        FIG_DIR / "fig04_data.csv",
        out_rows,
        ["time", "residual_gbp_million", "z_score", "abs_z_gt2"],
    )


# ---------------------------------------------------------------------------
# §4.4.5 — 환율 vs CA 산점도 (2x2 grid: GBP/USD·ERI x lag 0/4)
# ---------------------------------------------------------------------------
def fig05_fx_ca_scatter() -> None:
    """§4.4.5 — 환율 × CA 산점도 2×2 grid (양자/실효 × lag 0/4) + 패널별 r.

    - 입력: ``quarterly_series_2006q1_2025q4.csv`` (HBOP) +
      ``exchange_rates_quarterly_2006q1_2025q4.csv`` (gbp_usd, sterling_eri).
      두 파일의 ``time`` 정렬 일치 여부를 ``assert`` 로 강제 검증.
    - 4 패널 구성: ① GBP/USD × HBOP lag 0 ② GBP/USD × HBOP lag 4
      ③ Sterling ERI × HBOP lag 0 ④ Sterling ERI × HBOP lag 4. lag 4 는
      환율(t) → CA(t+4) 4 분기 후 시차로 J-curve 검증의 시간 축을 설정.
    - 각 패널 제목에 Pearson 상관계수 ``r`` 을 ``+/- d.ddd`` 표기로 노출.
    - 산출물: ``fig05_fx_ca_scatter.png`` + 동봉 ``fig05_data.csv`` (80 + 76
      = 156 행 long-form).
    """
    fx = read_csv(DATA_DIR / "exchange_rates_quarterly_2006q1_2025q4.csv")
    fx = sorted(fx, key=lambda r: r["time"])
    fx_times = [r["time"] for r in fx]
    gbpusd = [fnum(r["gbp_usd"]) for r in fx]
    eri = [fnum(r["sterling_eri_jan2005_100"]) for r in fx]

    qs = read_csv(DATA_DIR / "quarterly_series_2006q1_2025q4.csv")
    hbop_rows = sorted([r for r in qs if r["cdid"] == "HBOP"], key=lambda r: r["time"])
    ca_times = [r["time"] for r in hbop_rows]
    ca = [fnum(r["data_value"]) for r in hbop_rows]
    assert ca_times == fx_times

    def corr(xs: list[float], ys: list[float]) -> float:
        """두 수열의 Pearson 상관계수를 산출(외부 의존 없이 표준 라이브러리만 사용).

        분모가 0(상수 수열) 이면 NaN 을 반환해 그래프 라벨에 노출되지 않게
        한다. ``numpy.corrcoef`` 와 수치 일치(소수점 6 자리 이내).
        """
        n = len(xs)
        mx, my = sum(xs) / n, sum(ys) / n
        num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
        dx = (sum((a - mx) ** 2 for a in xs)) ** 0.5
        dy = (sum((b - my) ** 2 for b in ys)) ** 0.5
        return num / (dx * dy) if dx * dy > 0 else float("nan")

    # 4 panels
    fig, axes = plt.subplots(2, 2, figsize=(11, 9), dpi=150)
    panels = [
        (axes[0][0], gbpusd, ca, 0, "GBP/USD", "lag 0", "#1f4e79"),
        (axes[0][1], gbpusd[: len(ca) - 4], ca[4:], 4, "GBP/USD", "lag 4 (FX → CA 4분기 후)", "#1f4e79"),
        (axes[1][0], eri, ca, 0, "Sterling ERI (Jan 2005=100)", "lag 0", "#1f8a4c"),
        (axes[1][1], eri[: len(ca) - 4], ca[4:], 4, "Sterling ERI", "lag 4", "#1f8a4c"),
    ]
    for ax, xv, yv, lag, xlab, taglab, col in panels:
        r = corr(xv, yv)
        ax.scatter(xv, yv, color=col, s=22, alpha=0.7, edgecolor="white", linewidth=0.4)
        ax.axhline(0, color="#888888", linestyle=":", linewidth=0.7)
        ax.set_xlabel(xlab)
        ax.set_ylabel("CA 합계 (HBOP, GBP million)")
        ax.set_title(f"{xlab} × HBOP — {taglab}, r = {r:+.3f} (n={len(xv)})")
        ax.grid(True, linestyle=":", alpha=0.4)

    fig.suptitle("§4.4.5 환율 × CA 산점도 — 양자환율(GBP/USD)·실효환율(Sterling ERI) × 시차 0·4",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(FIG_DIR / "fig05_fx_ca_scatter.png", dpi=150)
    plt.close(fig)
    print(f"[png ] fig05_fx_ca_scatter.png")

    # data source: lag 0 + lag 4 long-form
    out_rows = []
    for i, t in enumerate(fx_times):
        out_rows.append(
            {
                "time_fx": t,
                "time_ca": t,
                "lag": 0,
                "gbp_usd": gbpusd[i],
                "sterling_eri": eri[i],
                "ca_hbop_gbp_million": ca[i],
            }
        )
    for i in range(len(fx_times) - 4):
        out_rows.append(
            {
                "time_fx": fx_times[i],
                "time_ca": fx_times[i + 4],
                "lag": 4,
                "gbp_usd": gbpusd[i],
                "sterling_eri": eri[i],
                "ca_hbop_gbp_million": ca[i + 4],
            }
        )
    write_csv(
        FIG_DIR / "fig05_data.csv",
        out_rows,
        ["time_fx", "time_ca", "lag", "gbp_usd", "sterling_eri", "ca_hbop_gbp_million"],
    )


# ---------------------------------------------------------------------------
# §4.4.6 — BOKI 좌축 + GBP/USD·Sterling ERI 우축 이중축 라인
# ---------------------------------------------------------------------------
def fig06_fx_boki_dual_axis() -> None:
    """§4.4.6 — BOKI 좌축 + GBP/USD·Sterling ERI 우축 이중축 라인 (2 패널 분리).

    - 입력: ``quarterly_series_2006q1_2025q4.csv`` (BOKI) +
      ``exchange_rates_quarterly_2006q1_2025q4.csv`` (gbp_usd, sterling_eri).
    - 시각화 구조: 상·하 2 패널 (``sharex=True``). 패널 (A) BOKI × GBP/USD,
      패널 (B) BOKI × Sterling ERI. **초안의 "ERI ÷50 인위 스케일링" 안은
      값 변형 우려**(`db/data/CLAUDE.md` 가공 원칙 1 번) 로 폐기하고, 두 환율
      변수를 각자 독립 우축으로 분리해 원값 그대로 표시한다.
    - 변곡점 4 분기(2008Q4·2016Q3·2022Q3·2025Q4) 는 양 패널에서 회색 수직
      점선으로 강조. 패널 (B) 만 분기 라벨을 회전 표시(상단 텍스트로 90°
      회전, 가독성 우선).
    - 산출물: ``fig06_fx_boki_dual_axis.png`` + 동봉 ``fig06_data.csv`` (80
      행, 5 컬럼).
    """
    fx = read_csv(DATA_DIR / "exchange_rates_quarterly_2006q1_2025q4.csv")
    fx = sorted(fx, key=lambda r: r["time"])
    fx_times = [r["time"] for r in fx]
    gbpusd = [fnum(r["gbp_usd"]) for r in fx]
    eri = [fnum(r["sterling_eri_jan2005_100"]) for r in fx]

    qs = read_csv(DATA_DIR / "quarterly_series_2006q1_2025q4.csv")
    boki_rows = sorted([r for r in qs if r["cdid"] == "BOKI"], key=lambda r: r["time"])
    b_times = [r["time"] for r in boki_rows]
    boki = [fnum(r["data_value"]) for r in boki_rows]
    assert b_times == fx_times

    inflection_quarters = ["2008Q4", "2016Q3", "2022Q3", "2025Q4"]

    # 상·하 2 패널로 분리: 위 = BOKI × GBP/USD, 아래 = BOKI × Sterling ERI
    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(12, 8), dpi=150, sharex=True)
    x = list(range(len(fx_times)))

    color_l = "#c0392b"
    color_r1 = "#1f4e79"
    color_r2 = "#1f8a4c"

    # ---- 패널 A: BOKI × GBP/USD ----
    ax_a.plot(x, boki, color=color_l, linewidth=1.7, label="BOKI 상품수지 (좌축)")
    ax_a.axhline(0, color="#888888", linestyle=":", linewidth=0.7)
    ax_a.set_ylabel("BOKI (GBP million)", color=color_l)
    ax_a.tick_params(axis="y", labelcolor=color_l)
    ax_a2 = ax_a.twinx()
    ax_a2.plot(x, gbpusd, color=color_r1, linewidth=1.4,
               label="GBP/USD (우축)")
    ax_a2.set_ylabel("GBP/USD (USD per GBP)", color=color_r1)
    ax_a2.tick_params(axis="y", labelcolor=color_r1)
    for iq in inflection_quarters:
        if iq in fx_times:
            xi = fx_times.index(iq)
            ax_a.axvline(xi, color="#888888", linestyle=":", linewidth=0.9, alpha=0.7)
    h1, l1 = ax_a.get_legend_handles_labels()
    h2, l2 = ax_a2.get_legend_handles_labels()
    ax_a.legend(h1 + h2, l1 + l2, loc="lower left", fontsize=8)
    ax_a.grid(True, linestyle=":", alpha=0.3)
    ax_a.set_title("(A) BOKI 좌축 × GBP/USD 우축 — 변곡점 점선: 2008Q4·2016Q3·2022Q3·2025Q4")

    # ---- 패널 B: BOKI × Sterling ERI ----
    ax_b.plot(x, boki, color=color_l, linewidth=1.7, label="BOKI 상품수지 (좌축)")
    ax_b.axhline(0, color="#888888", linestyle=":", linewidth=0.7)
    ax_b.set_ylabel("BOKI (GBP million)", color=color_l)
    ax_b.tick_params(axis="y", labelcolor=color_l)
    ax_b2 = ax_b.twinx()
    ax_b2.plot(x, eri, color=color_r2, linewidth=1.4,
               label="Sterling ERI (우축, Jan 2005=100)")
    ax_b2.set_ylabel("Sterling ERI (Jan 2005=100)", color=color_r2)
    ax_b2.tick_params(axis="y", labelcolor=color_r2)
    for iq in inflection_quarters:
        if iq in fx_times:
            xi = fx_times.index(iq)
            ax_b.axvline(xi, color="#888888", linestyle=":", linewidth=0.9, alpha=0.7)
            ax_b.text(xi, ax_b.get_ylim()[1], iq, rotation=90, va="top",
                      ha="right", fontsize=7, color="#444444")
    h1, l1 = ax_b.get_legend_handles_labels()
    h2, l2 = ax_b2.get_legend_handles_labels()
    ax_b.legend(h1 + h2, l1 + l2, loc="lower left", fontsize=8)
    ax_b.grid(True, linestyle=":", alpha=0.3)
    ax_b.set_title("(B) BOKI 좌축 × Sterling ERI 우축")
    ax_b.set_xlabel("분기")

    ticks, labs = quarter_labels_every(fx_times, step=8)
    ax_b.set_xticks(ticks)
    ax_b.set_xticklabels(labs, rotation=30, ha="right")

    fig.suptitle("§4.4.6 BOKI 상품수지 × 환율(GBP/USD·Sterling ERI) 이중축 라인 — 2006Q1~2025Q4",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(FIG_DIR / "fig06_fx_boki_dual_axis.png", dpi=150)
    plt.close(fig)
    print(f"[png ] fig06_fx_boki_dual_axis.png")

    out_rows = []
    for i, t in enumerate(fx_times):
        out_rows.append(
            {
                "time": t,
                "boki_gbp_million": boki[i],
                "gbp_usd": gbpusd[i],
                "sterling_eri_jan2005_100": eri[i],
                "is_inflection_quarter": "1" if t in inflection_quarters else "0",
            }
        )
    write_csv(
        FIG_DIR / "fig06_data.csv",
        out_rows,
        [
            "time",
            "boki_gbp_million",
            "gbp_usd",
            "sterling_eri_jan2005_100",
            "is_inflection_quarter",
        ],
    )


# ---------------------------------------------------------------------------
# §4.4.7 — figures/README.md (그래프↔source CSV 매핑 + 출처)
# ---------------------------------------------------------------------------
def fig07_readme() -> None:
    """§4.4.7 — ``report/figures/README.md`` 신설 (그래프↔source CSV 1:1 매핑).

    - 산출 폴더 인덱스 + 1차 출처 표 + 재현 절차 + 라이선스 + 변경 이력
      5 절 구성. 본 함수가 직접 마크다운 문자열을 파일에 기록한다.
    - 외부 라이브러리 의존 없이 ``Path.write_text`` 만 사용.
    """
    md = """# `report/figures/` — 단계 4 §4.4 그래프 6건 + 데이터 source 6 CSV

본 폴더는 SKKU 거시경제학 보고서 단계 4 §4.4 그래프 산출물 7 항목을 모은다.

## 1. 인덱스 (그래프 6건)

| 번호 | 그래프 PNG | 주제 | 데이터 source CSV (1:1 동봉) |
|---|---|---|---|
| §4.4.1 | `fig01_ca_quarterly.png` | CA 합계(HBOP) 분기 시계열 + 충격 5건 | `fig01_data.csv` |
| §4.4.2 | `fig02_ca_components.png` | CA 4 세부항목(BOKI·IKBD·HBOJ·IKBP) 비교 라인 | `fig02_data.csv` |
| §4.4.3 | `fig03_fa_components.png` | FA 합계(-HBNT) + 5 세부항목 누적 막대 | `fig03_data.csv` |
| §4.4.4 | `fig04_identity_residual.png` | BoP 항등식 잔차 + ±1σ·±2σ + 2σ 밖 분기 강조 | `fig04_data.csv` |
| §4.4.5 | `fig05_fx_ca_scatter.png` | 환율 × CA 산점도 (GBP/USD·ERI × lag 0·4, 2×2 grid) | `fig05_data.csv` |
| §4.4.6 | `fig06_fx_boki_dual_axis.png` | BOKI 좌축 + GBP/USD·Sterling ERI 우축 이중축 라인 | `fig06_data.csv` |

## 2. 데이터 source 1:1 매핑 + 1차 출처

| 그래프 | 1차 source (`report/data/`) | 추출 컬럼 | 1차 출처 |
|---|---|---|---|
| §4.4.1 | `quarterly_series_2006q1_2025q4.csv` (CDID=HBOP, 80 행) | `time`, `data_value` | ONS Balance of Payments 2025 Q4, Table A 부표 1 (CDID=HBOP) |
| §4.4.2 | `quarterly_series_2006q1_2025q4.csv` (CDID=BOKI/IKBD/HBOJ/IKBP, 4×80 행) | `cdid`, `time`, `data_value` | ONS BoP 2025 Q4, Table A 부표 1 |
| §4.4.3 | `quarterly_series_2006q1_2025q4.csv` (CDID=-MU7M/-HHZD/-ZPNN/-HHYR/-LTCV/-HBNT, 6×80 행) | `cdid`, `time`, `data_value` | ONS BoP 2025 Q4, Table A 부표 3 (FA 5 기능별 + 합계, 부호 반전 표시) |
| §4.4.4 | `identity_residual_2006q1_2025q4.csv` (80 행) | `time`, `residual` | 단계 4 §4.2 산출물 (CA+KA+FA+NEO 잔차) |
| §4.4.5 | `quarterly_series_2006q1_2025q4.csv` + `exchange_rates_quarterly_2006q1_2025q4.csv` | HBOP, gbp_usd, sterling_eri_jan2005_100 (2×80, lag 0+4) | ONS BoP + Bank of England IADB (XUDLUSS, XUDLBK67) |
| §4.4.6 | `quarterly_series_2006q1_2025q4.csv` + `exchange_rates_quarterly_2006q1_2025q4.csv` | BOKI, gbp_usd, sterling_eri_jan2005_100 (3×80) | ONS BoP + Bank of England IADB (XUDLUSS, XUDLBK67) |

## 3. 재현 절차

```bat
c:\\Projects\\SKKU.England\\env\\Scripts\\python.exe c:\\Projects\\SKKU.England\\report\\code\\quantitative_4_4.py
```

- matplotlib backend = `Agg` 강제(GUI 없이 PNG 저장).
- 한국어 라벨은 `Malgun Gothic` 우선 → 미설치 시 NanumGothic·Noto Sans CJK KR 후보 자동 선택.
- 입력 CSV 값은 **수정·치환·반올림·환산 금지** — 시각화 시 그대로 사용.
- 모든 PNG 1건당 같은 폴더의 `figXX_data.csv` 1건이 1:1 동봉되어 추적성 보장.

## 4. 라이선스·주의

- ONS 자료: Open Government Licence v3.0
- Bank of England IADB(XUDLUSS, XUDLERS, XUDLBK67): Open Government Licence v3.0
- Eurostat REER: © European Union, Eurostat copyright

분기 평균 산출 방법(BoE 일별 → 분기 영업일 산술 평균, Eurostat 월 → 3 개월 단순 평균)은
`report/data/exchange_rates_quarterly_2006q1_2025q4.md` 참조.

## 5. 변경 이력

- 2026-04-29 — 7 항목 (그래프 6 + README 1) 최초 작성. 단계 4 §4.4 마감.
"""
    out = FIG_DIR / "README.md"
    out.write_text(md, encoding="utf-8")
    print(f"[md  ] {out.relative_to(ROOT)}")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> None:
    """7 항목(그래프 6 + README 1) 을 순서대로 멱등 산출하는 진입점.

    - 본 스크립트는 외부 상태에 의존하지 않으며 ``report/data/`` 입력만
      읽는다. 동일 입력에서 동일 출력이 보장되므로 임의 횟수 재실행이
      가능하다(이전 산출물은 같은 경로에 덮어쓴다).
    - 호출 순서는 §4.4.1 → §4.4.7 보고서 절 순서와 동일.
    """
    print("=" * 72)
    print(" SKKU 거시경제학 보고서 단계 4 §4.4 — 그래프 6 + README 1 산출")
    print("=" * 72)
    fig01_ca_quarterly()
    fig02_ca_components()
    fig03_fa_components()
    fig04_identity_residual()
    fig05_fx_ca_scatter()
    fig06_fx_boki_dual_axis()
    fig07_readme()
    print("=" * 72)
    print(" done")


if __name__ == "__main__":
    main()
