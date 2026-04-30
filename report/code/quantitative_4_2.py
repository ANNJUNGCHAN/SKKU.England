"""보고서 단계 4 §4.2 — 항등식 잔차 산출 스크립트.

본 스크립트는 단일 호출(`env/Scripts/python.exe report/code/quantitative_4_2.py`) 로
사용자 요청 3 항목 묶음(§4.2.1 ~ §4.2.3) 의 3 평면 CSV 를 일괄 산출한다.

표적 항등식:
    CA + KA + FA + NEO ≡ 0   (광의, 회계 항등)
ONS Table_A 표시 부호 형태:
    HBOP + FNVQ + (-HBNT) + HHDH ≈ 0
    · CA  = HBOP   (Table_A_sub1)
    · KA  = FNVQ   (Table_A_sub1)
    · FA  = -HBNT  (Table_A_sub3, 부호 반전 표시 그대로)
    · NEO = HHDH   (Table_A_sub3)

부호 규약 헤더(산출 CSV 1번째 주석/명세):
    "Table_A 표시 부호 사용. -HBNT 의 음 부호는 ONS 표시값 그대로 합산"

산출물:
  1. report/data/identity_residual_2006q1_2025q4.csv          (80 행 × 7 컬럼)
  2. report/data/identity_residual_stats_2006q1_2025q4.csv    (요약 + 80 분기)
  3. report/data/identity_shock_position_2006q1_2025q4.csv    (충격 분기 z-score 표)

데이터 소스:
  - report/data/quarterly_series_2006q1_2025q4.csv   (직전 §4.1 산출, 13 변수)
  - db/data/_db/ecos_uk_bop.sqlite                   (AA6H Table_B_sub4, % of GDP)

원본 셀 값은 절대 수정하지 않으며, 모든 가공치는 별도 산출 파일에 적재한다.
"""

from __future__ import annotations

import csv
import math
import sqlite3
import statistics
import sys
from pathlib import Path

# Windows cp949 콘솔에서 한국어·em dash 안전 출력
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ---------------------------------------------------------------------------
# 0. 경로 상수
# ---------------------------------------------------------------------------

REPO_ROOT = Path(r"C:/Projects/SKKU.England")
DB_PATH = REPO_ROOT / "db/data/_db/ecos_uk_bop.sqlite"
IN_SERIES = REPO_ROOT / "report/data/quarterly_series_2006q1_2025q4.csv"
OUT_DIR = REPO_ROOT / "report/data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_RESIDUAL = OUT_DIR / "identity_residual_2006q1_2025q4.csv"
OUT_STATS = OUT_DIR / "identity_residual_stats_2006q1_2025q4.csv"
OUT_SHOCK = OUT_DIR / "identity_shock_position_2006q1_2025q4.csv"

# ---------------------------------------------------------------------------
# 1. 항등식 4 변수 매핑
#    (보고된 CSV 의 cdid 표기 그대로 — `-HBNT` 는 sign_prefix 적용된 합계 행)
# ---------------------------------------------------------------------------

CDID_CA = "HBOP"
CDID_KA = "FNVQ"
CDID_FA = "-HBNT"  # ONS 표시 부호 그대로(음 부호 포함)
CDID_NEO = "HHDH"

# 분기 윈도우(2006Q1 ~ 2025Q4 = 80)
QUARTERS = [f"{y}Q{q}" for y in range(2006, 2026) for q in range(1, 5)]
assert len(QUARTERS) == 80

# ---------------------------------------------------------------------------
# 2. 충격 분기 5 묶음
# ---------------------------------------------------------------------------

SHOCK_GROUPS: list[tuple[str, list[str]]] = [
    ("GFC (글로벌 금융위기)", ["2008Q4", "2009Q1", "2009Q2", "2009Q3", "2009Q4", "2010Q1"]),
    ("Brexit 직후", ["2016Q3", "2016Q4"]),
    ("팬데믹 (COVID-19)", ["2020Q1", "2020Q2", "2020Q3", "2020Q4"]),
    ("Mini-budget", ["2022Q3", "2022Q4"]),
    ("귀금속 연관", ["2024Q4", "2025Q1", "2025Q2", "2025Q3", "2025Q4"]),
]

# ---------------------------------------------------------------------------
# 3. 입력 로드 — long-form CSV → time × cdid dict
# ---------------------------------------------------------------------------


def load_quarterly_series() -> dict[str, dict[str, float]]:
    """report/data/quarterly_series_2006q1_2025q4.csv 를 (cdid → time → value) 로 적재."""
    out: dict[str, dict[str, float]] = {}
    with IN_SERIES.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cdid = row["cdid"]
            time = row["time"]
            try:
                val = float(row["data_value"])
            except (TypeError, ValueError):
                val = float("nan")
            out.setdefault(cdid, {})[time] = val
    return out


def load_aa6h_share() -> dict[str, float]:
    """RDB 에서 AA6H (Table_B_sub4, % of GDP) 분기 시계열 적재."""
    conn = sqlite3.connect(str(DB_PATH))
    try:
        rows = conn.execute(
            """
            SELECT o.TIME, o.DATA_VALUE
            FROM stat_item_meta m JOIN observation o ON m.item_id = o.item_id
            WHERE m.ITEM_CODE1 = 'AA6H' AND m.STAT_CODE = 'UK_BoP_Table_B_sub4'
            """
        ).fetchall()
    finally:
        conn.close()
    out: dict[str, float] = {}
    for time, val in rows:
        if val is not None and time in QUARTERS:
            out[time] = float(val)
    return out


# ---------------------------------------------------------------------------
# 4. §4.2.1 — 분기별 항등식 잔차 표
# ---------------------------------------------------------------------------


def build_residual_table(series: dict[str, dict[str, float]]) -> list[dict]:
    """80 분기에 대해 CA·KA·FA·NEO·잔차·잔차_부호 산출."""
    out: list[dict] = []
    for t in QUARTERS:
        ca = series[CDID_CA][t]
        ka = series[CDID_KA][t]
        fa = series[CDID_FA][t]  # 이미 -HBNT 부호 반전된 표시값
        neo = series[CDID_NEO][t]
        residual = ca + ka + fa + neo
        if residual > 0:
            sign = "+"
        elif residual < 0:
            sign = "-"
        else:
            sign = "0"
        out.append(
            {
                "time": t,
                "CA_HBOP": ca,
                "KA_FNVQ": ka,
                "FA_minusHBNT": fa,
                "NEO_HHDH": neo,
                "residual": residual,
                "residual_sign": sign,
            }
        )
    return out


def write_residual_csv(rows: list[dict]) -> None:
    """§4.2.1 분기별 잔차 표를 평면 CSV 로 적재한다.

    1·2 번째 행에 부호 규약 헤더 주석(`# ` 시작)을 박아 후속 단위(시각화·회귀)
    재현 시 부호 해석을 강제할 수 있도록 한다. 데이터 행은 80 분기 = 80 행으로
    `time, CA_HBOP, KA_FNVQ, FA_minusHBNT, NEO_HHDH, residual, residual_sign`
    의 7 컬럼 평면 표 형태이다.

    Args:
        rows: `build_residual_table` 가 산출한 80 분기 잔차 row 묶음.

    Side Effects:
        `OUT_RESIDUAL` 경로(`report/data/identity_residual_2006q1_2025q4.csv`)에
        UTF-8 인코딩으로 파일을 새로 쓴다(기존 파일 덮어쓰기, 멱등 재실행 가능).
    """
    with OUT_RESIDUAL.open("w", encoding="utf-8", newline="") as f:
        # 부호 규약 헤더(주석 2 행)
        f.write(
            "# 항등식: CA + KA + FA + NEO == 0 (광의, 회계 항등) "
            "/ Table_A 표시 부호 사용. -HBNT 의 음 부호는 ONS 표시값 그대로 합산\n"
        )
        f.write(
            "# 단위: GBP million / 변수: CA=HBOP(Table_A_sub1), KA=FNVQ(Table_A_sub1), "
            "FA=-HBNT(Table_A_sub3 부호 반전 표시), NEO=HHDH(Table_A_sub3)\n"
        )
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "time",
                "CA_HBOP",
                "KA_FNVQ",
                "FA_minusHBNT",
                "NEO_HHDH",
                "residual",
                "residual_sign",
            ],
        )
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


# ---------------------------------------------------------------------------
# 5. §4.2.2 — 잔차 통계량 + |잔차|/GDP 비율
# ---------------------------------------------------------------------------


def build_residual_stats(
    residual_rows: list[dict], series: dict[str, dict[str, float]], aa6h: dict[str, float]
) -> tuple[dict, list[dict]]:
    """잔차 평균·SD·|잔차| 평균 + 분기별 |잔차|/GDP (%)."""
    residuals = [r["residual"] for r in residual_rows]
    abs_residuals = [abs(x) for x in residuals]
    n = len(residuals)
    mean_r = statistics.fmean(residuals)
    sd_r = statistics.stdev(residuals) if n > 1 else float("nan")
    mean_abs = statistics.fmean(abs_residuals)

    # GDP 추정: GDP_estimated[t] = HBOP[t] / (AA6H[t] / 100)
    quarter_rows: list[dict] = []
    ratios: list[float] = []
    for r in residual_rows:
        t = r["time"]
        ca = series[CDID_CA][t]
        share = aa6h.get(t)
        if share is None or share == 0:
            gdp_est = float("nan")
            ratio = float("nan")
        else:
            gdp_est = ca / (share / 100.0)
            ratio = abs(r["residual"]) / gdp_est * 100.0 if gdp_est else float("nan")
            ratios.append(ratio)
        quarter_rows.append(
            {
                "time": t,
                "residual": r["residual"],
                "abs_residual": abs(r["residual"]),
                "CA_HBOP": ca,
                "AA6H_pct_GDP": share if share is not None else "",
                "GDP_estimated": gdp_est,
                "abs_residual_over_GDP_pct": ratio,
            }
        )

    summary = {
        "n_quarters": n,
        "mean_residual": mean_r,
        "sd_residual": sd_r,
        "mean_abs_residual": mean_abs,
        "mean_abs_resid_over_GDP_pct": statistics.fmean(ratios) if ratios else float("nan"),
        "max_abs_resid_over_GDP_pct": max(ratios) if ratios else float("nan"),
        "min_abs_resid_over_GDP_pct": min(ratios) if ratios else float("nan"),
        "median_abs_resid_over_GDP_pct": statistics.median(ratios) if ratios else float("nan"),
    }
    return summary, quarter_rows


def write_residual_stats_csv(summary: dict, quarter_rows: list[dict]) -> None:
    """§4.2.2 잔차 통계량 + |잔차|/GDP 비율 표를 평면 CSV 로 적재한다.

    파일 안에 두 SECTION 을 직렬로 배치한다:
      - SECTION 1: `metric, value` 2 컬럼 형식의 요약 메트릭 8 행.
      - SECTION 2: `time, residual, abs_residual, CA_HBOP, AA6H_pct_GDP,
        GDP_estimated, abs_residual_over_GDP_pct` 7 컬럼의 분기별 80 행.

    각 SECTION 직전에 한국어 식별 주석 1 행을 박아 다운스트림 파서가
    blank-line / `# [SECTION ...]` 패턴으로 두 표를 분리할 수 있게 한다.

    Args:
        summary: `build_residual_stats` 의 첫 반환값(요약 dict, 8 키).
        quarter_rows: 같은 함수의 두 번째 반환값(분기별 80 row 묶음).

    Side Effects:
        `OUT_STATS` 경로(`report/data/identity_residual_stats_2006q1_2025q4.csv`)
        에 UTF-8 인코딩으로 파일을 새로 쓴다(기존 파일 덮어쓰기, 멱등 재실행 가능).
    """
    with OUT_STATS.open("w", encoding="utf-8", newline="") as f:
        f.write(
            "# §4.2.2 잔차 통계량 + |잔차|/GDP 비율 / 분모 GDP는 HBOP/(AA6H/100) 역산 "
            "/ AA6H = Table_B_sub4 'CA % of GDP'\n"
        )
        f.write("# 부호 규약: CA + KA + FA + NEO == 0 (FA = -HBNT, ONS 표시 부호 그대로)\n")

        # 1. 요약 메트릭 (key, value 두 컬럼)
        f.write("\n# [SECTION 1] 요약 메트릭 (단위: GBP million / % of GDP)\n")
        writer1 = csv.writer(f)
        writer1.writerow(["metric", "value"])
        for k, v in summary.items():
            if isinstance(v, float):
                writer1.writerow([k, f"{v:.6f}"])
            else:
                writer1.writerow([k, v])

        # 2. 분기별 표
        f.write("\n# [SECTION 2] 분기별 |잔차|/GDP 비율 (80 행)\n")
        writer2 = csv.DictWriter(
            f,
            fieldnames=[
                "time",
                "residual",
                "abs_residual",
                "CA_HBOP",
                "AA6H_pct_GDP",
                "GDP_estimated",
                "abs_residual_over_GDP_pct",
            ],
        )
        writer2.writeheader()
        for r in quarter_rows:
            writer2.writerow(
                {
                    "time": r["time"],
                    "residual": f"{r['residual']:.4f}",
                    "abs_residual": f"{r['abs_residual']:.4f}",
                    "CA_HBOP": f"{r['CA_HBOP']:.4f}",
                    "AA6H_pct_GDP": r["AA6H_pct_GDP"],
                    "GDP_estimated": (
                        f"{r['GDP_estimated']:.4f}"
                        if isinstance(r["GDP_estimated"], float) and not math.isnan(r["GDP_estimated"])
                        else ""
                    ),
                    "abs_residual_over_GDP_pct": (
                        f"{r['abs_residual_over_GDP_pct']:.6f}"
                        if isinstance(r["abs_residual_over_GDP_pct"], float)
                        and not math.isnan(r["abs_residual_over_GDP_pct"])
                        else ""
                    ),
                }
            )


# ---------------------------------------------------------------------------
# 6. §4.2.3 — 충격 분기 잔차 정상 분포 대비 위치
# ---------------------------------------------------------------------------


def normal_cdf(x: float) -> float:
    """표준정규 누적분포함수 Φ(x).

    `math.erf` 의 항등식 `Φ(x) = 0.5 · (1 + erf(x / √2))` 을 사용해 외부 의존
    없이(즉 `scipy.stats.norm.cdf` 도입 없이) 표준정규 CDF 를 계산한다.

    Args:
        x: z-score(표준정규로 환산된 값).

    Returns:
        Φ(x) ∈ [0, 1] — 잔차가 정상분포라면 기대되는 이론 백분위(소수).
        호출 측에서 ×100 으로 곱해 % 단위로 환산한다.
    """
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def empirical_percentile(value: float, sorted_values: list[float]) -> float:
    """표본 분포 내 누적 백분위(0~100, %).

    SciPy `percentileofscore(..., kind='mean')` 과 동일 정의를 표준 라이브러리만
    으로 구현. 동률(value 와 같은 표본)은 `(less + leq) / 2` 즉 평균 순위로
    처리해 좌·우 편향 없이 백분위를 추정한다.

    Args:
        value: 백분위를 산출할 대상 값(잔차 £m).
        sorted_values: 정렬 여부와 무관하게 사용 가능한 표본(80 분기 잔차).
            함수 내부에서 정렬 가정 없이 less/leq 카운트만 수행한다.

    Returns:
        0~100 사이 누적 백분위(%). 표본이 비어 있으면 NaN 반환.
    """
    n = len(sorted_values)
    if n == 0:
        return float("nan")
    # value 보다 엄격히 작은 표본 수와, 작거나 같은 표본 수의 평균을 순위로 사용
    less = sum(1 for v in sorted_values if v < value)
    leq = sum(1 for v in sorted_values if v <= value)
    rank = (less + leq) / 2.0
    return rank / n * 100.0


def build_shock_table(
    residual_rows: list[dict],
    summary: dict,
    quarter_rows: list[dict],
) -> list[dict]:
    """충격 분기별 잔차 z-score, 백분위, |잔차|/GDP."""
    residuals_by_time = {r["time"]: r["residual"] for r in residual_rows}
    ratio_by_time = {r["time"]: r["abs_residual_over_GDP_pct"] for r in quarter_rows}
    sorted_residuals = sorted(residuals_by_time.values())
    mean_r = summary["mean_residual"]
    sd_r = summary["sd_residual"]

    rows: list[dict] = []
    for group_label, quarters in SHOCK_GROUPS:
        for q in quarters:
            res = residuals_by_time[q]
            z = (res - mean_r) / sd_r if sd_r and not math.isnan(sd_r) else float("nan")
            pct = empirical_percentile(res, sorted_residuals)
            theoretical = normal_cdf(z) * 100.0 if not math.isnan(z) else float("nan")
            ratio = ratio_by_time.get(q, float("nan"))
            # |z| > 2 (정상 분포 외) / |z| > 1 (1σ 외) 라벨
            if math.isnan(z):
                band = ""
            elif abs(z) > 2:
                band = "outside_2sd"
            elif abs(z) > 1:
                band = "outside_1sd"
            else:
                band = "inside_1sd"
            rows.append(
                {
                    "shock_group": group_label,
                    "time": q,
                    "residual": res,
                    "z_score": z,
                    "empirical_percentile_pct": pct,
                    "theoretical_normal_cdf_pct": theoretical,
                    "abs_residual_over_GDP_pct": ratio,
                    "sd_band": band,
                }
            )
    return rows


def write_shock_csv(rows: list[dict], summary: dict) -> None:
    """§4.2.3 충격 분기 z-score 표를 평면 CSV 로 적재한다.

    부호 규약·정상분포(평균·SD·n) 메타정보를 1~3행 주석으로 박은 뒤,
    `shock_group, time, residual, z_score, empirical_percentile_pct,
    theoretical_normal_cdf_pct, abs_residual_over_GDP_pct, sd_band` 8 컬럼의
    평면 표를 적재한다. 부동소수 포맷은 잔차는 4자리, z·이론백분위는 6자리,
    경험 백분위는 4자리로 일관 적용해 시각화 단계에서의 추가 가공을 단순화.

    Args:
        rows: `build_shock_table` 가 산출한 충격 분기 19개 row 묶음.
        summary: `build_residual_stats` 의 첫 반환값(요약 메트릭).
            mean·SD·n_quarters 를 헤더 주석에 박는 데에만 사용한다.

    Side Effects:
        `OUT_SHOCK` 경로(`report/data/identity_shock_position_2006q1_2025q4.csv`)
        에 UTF-8 인코딩으로 파일을 새로 쓴다(기존 파일 덮어쓰기, 멱등 재실행 가능).
    """
    with OUT_SHOCK.open("w", encoding="utf-8", newline="") as f:
        f.write(
            "# §4.2.3 충격 분기 잔차 정상 분포 대비 위치 / 정상 분포 = 80 분기 잔차 평균·SD\n"
        )
        f.write(
            f"# 정상분포: mean = {summary['mean_residual']:.4f} GBP million, "
            f"SD = {summary['sd_residual']:.4f} GBP million (n = {summary['n_quarters']})\n"
        )
        f.write(
            "# 부호 규약: CA + KA + FA + NEO == 0 (FA = -HBNT, ONS 표시 부호 그대로)\n"
        )
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "shock_group",
                "time",
                "residual",
                "z_score",
                "empirical_percentile_pct",
                "theoretical_normal_cdf_pct",
                "abs_residual_over_GDP_pct",
                "sd_band",
            ],
        )
        writer.writeheader()
        for r in rows:
            writer.writerow(
                {
                    "shock_group": r["shock_group"],
                    "time": r["time"],
                    "residual": f"{r['residual']:.4f}",
                    "z_score": (
                        f"{r['z_score']:.6f}"
                        if isinstance(r["z_score"], float) and not math.isnan(r["z_score"])
                        else ""
                    ),
                    "empirical_percentile_pct": (
                        f"{r['empirical_percentile_pct']:.4f}"
                        if isinstance(r["empirical_percentile_pct"], float)
                        and not math.isnan(r["empirical_percentile_pct"])
                        else ""
                    ),
                    "theoretical_normal_cdf_pct": (
                        f"{r['theoretical_normal_cdf_pct']:.4f}"
                        if isinstance(r["theoretical_normal_cdf_pct"], float)
                        and not math.isnan(r["theoretical_normal_cdf_pct"])
                        else ""
                    ),
                    "abs_residual_over_GDP_pct": (
                        f"{r['abs_residual_over_GDP_pct']:.6f}"
                        if isinstance(r["abs_residual_over_GDP_pct"], float)
                        and not math.isnan(r["abs_residual_over_GDP_pct"])
                        else ""
                    ),
                    "sd_band": r["sd_band"],
                }
            )


# ---------------------------------------------------------------------------
# 7. main + 콘솔 검증 출력
# ---------------------------------------------------------------------------


def main() -> None:
    series = load_quarterly_series()
    for cdid in (CDID_CA, CDID_KA, CDID_FA, CDID_NEO):
        if cdid not in series or len(series[cdid]) != 80:
            raise RuntimeError(
                f"입력 시계열 누락: {cdid} (분기 수={len(series.get(cdid, {}))}); 80 필요"
            )
    aa6h = load_aa6h_share()
    missing_aa6h = [t for t in QUARTERS if t not in aa6h]
    print(f"[load] AA6H 분기 적재: {len(aa6h)}/80, 누락: {len(missing_aa6h)}")
    if missing_aa6h:
        print(f"       missing: {missing_aa6h[:8]}{'...' if len(missing_aa6h) > 8 else ''}")

    # §4.2.1
    residual_rows = build_residual_table(series)
    write_residual_csv(residual_rows)
    print(f"[§4.2.1] 산출 완료: {OUT_RESIDUAL.name} ({len(residual_rows)} 행)")

    # 헤드라인 검산 — 2025Q4
    q4 = next(r for r in residual_rows if r["time"] == "2025Q4")
    print(
        f"  · 2025Q4 검산: CA={q4['CA_HBOP']:+.0f}, KA={q4['KA_FNVQ']:+.0f}, "
        f"FA={q4['FA_minusHBNT']:+.0f}, NEO={q4['NEO_HHDH']:+.0f} "
        f"=> 잔차={q4['residual']:+.0f} (예상 -25,111 ≈ 노트 38 §2.3 -25.2bn)"
    )

    sign_count = {"+": 0, "-": 0, "0": 0}
    for r in residual_rows:
        sign_count[r["residual_sign"]] += 1
    print(f"  · 부호 분포 (n=80): + {sign_count['+']} / - {sign_count['-']} / 0 {sign_count['0']}")

    # §4.2.2
    summary, quarter_rows = build_residual_stats(residual_rows, series, aa6h)
    write_residual_stats_csv(summary, quarter_rows)
    print(f"[§4.2.2] 산출 완료: {OUT_STATS.name} (요약 {len(summary)} + 분기 {len(quarter_rows)})")
    print(
        f"  · mean_residual={summary['mean_residual']:.2f}, "
        f"sd_residual={summary['sd_residual']:.2f}, "
        f"mean_abs_residual={summary['mean_abs_residual']:.2f}"
    )
    print(
        f"  · |잔차|/GDP 평균={summary['mean_abs_resid_over_GDP_pct']:.4f}%, "
        f"max={summary['max_abs_resid_over_GDP_pct']:.4f}%, "
        f"median={summary['median_abs_resid_over_GDP_pct']:.4f}%"
    )

    # §4.2.3
    shock_rows = build_shock_table(residual_rows, summary, quarter_rows)
    write_shock_csv(shock_rows, summary)
    print(f"[§4.2.3] 산출 완료: {OUT_SHOCK.name} ({len(shock_rows)} 충격 분기 행)")
    band_count = {"inside_1sd": 0, "outside_1sd": 0, "outside_2sd": 0}
    for r in shock_rows:
        if r["sd_band"] in band_count:
            band_count[r["sd_band"]] += 1
    print(
        f"  · 충격 분기 SD 분포: 1σ 안 {band_count['inside_1sd']} / "
        f"1σ 밖 {band_count['outside_1sd']} / 2σ 밖 {band_count['outside_2sd']}"
    )


if __name__ == "__main__":
    main()
