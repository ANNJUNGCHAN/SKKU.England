"""환율–경상수지 검증(§4.3.2 ~ §4.3.5) 분석 스크립트.

입력:
- `report/data/quarterly_series_2006q1_2025q4.csv` — 13 변수 80 분기 long-form
- `report/data/exchange_rates_quarterly_2006q1_2025q4.csv` — 환율 4 시리즈 80 분기
- `report/data/identity_residual_2006q1_2025q4.csv` — 항등식 잔차 80 분기

산출:
- `report/data/fx_correlation_2006q1_2025q4.csv` — 환율 vs CA·BOKI·AA6H 단순 상관(§4.3.2)
- `report/data/fx_lag_correlation_2006q1_2025q4.csv` — 시차 상관(§4.3.3)
- `report/data/fx_regression_2006q1_2025q4.csv` — 차분 회귀 결과(§4.3.4)
- `report/data/fx_case_study_2006q1_2025q4.csv` — 사례 분석 표(§4.3.5)

분석 대상 BOP 변수:
- HBOP — 경상수지(Current Account, GBP million)
- BOKI — 상품무역(Goods Balance, GBP million)
- AA6H — CA / GDP (% of GDP) — quarterly_series_2006q1_2025q4.csv 의 ca_gdp 컬럼

분석 대상 환율:
- gbp_usd / gbp_eur / sterling_eri / eurostat_reer_ic42

데이터 값 불변 원칙: 원자료 셀은 변경하지 않으며, 분석 산출물(상관계수·회귀계수)만 새로 작성.
"""
from __future__ import annotations
import csv
import math
import os
import sqlite3
from collections import OrderedDict
from statistics import mean, pstdev

ROOT = "C:/Projects/SKKU.England"
QSER = f"{ROOT}/report/data/quarterly_series_2006q1_2025q4.csv"
FX = f"{ROOT}/report/data/exchange_rates_quarterly_2006q1_2025q4.csv"
RDB = f"{ROOT}/db/data/_db/ecos_uk_bop.sqlite"
OUT_CORR = f"{ROOT}/report/data/fx_correlation_2006q1_2025q4.csv"
OUT_LAG = f"{ROOT}/report/data/fx_lag_correlation_2006q1_2025q4.csv"
OUT_REG = f"{ROOT}/report/data/fx_regression_2006q1_2025q4.csv"
OUT_CASE = f"{ROOT}/report/data/fx_case_study_2006q1_2025q4.csv"

FX_KEYS = [
    "gbp_usd",
    "gbp_eur",
    "sterling_eri_jan2005_100",
    "eurostat_reer_ic42_cpi_2015_100",
]
FX_LABEL = {
    "gbp_usd": "GBP/USD",
    "gbp_eur": "GBP/EUR",
    "sterling_eri_jan2005_100": "Sterling ERI (BoE)",
    "eurostat_reer_ic42_cpi_2015_100": "Eurostat REER IC42 (CPI)",
}


# ---------------------------------------------------------------------------
# 입력 로딩
# ---------------------------------------------------------------------------

def load_quarterly_series() -> dict[str, dict[str, float]]:
    """단계 4 §4.1 산출 ``quarterly_series_2006q1_2025q4.csv`` 적재.

    long-form(``cdid, time, data_value`` 3 컬럼) 과 wide-form(첫 컬럼 ``time``
    + 변수별 컬럼) 두 형태를 모두 자동 인식한다. §4.1 산출은 long-form 1,040
    행 형태이므로 첫 분기 본문은 long-form 분기를 통해 처리되고, wide-form
    fallback 은 후속 단위에서 형태가 바뀌어도 본 스크립트가 깨지지 않도록 하는
    안전망이다.

    Returns:
        ``cdid → time → value`` 의 2 단 dict. 결측 셀은 누락된 키로 표현하며
        ``NaN``/``0`` 으로 대체하지 않는다(`db/data/CLAUDE.md` 가공 원칙 1번).
    """
    with open(QSER, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    # 입력 csv 가 long form 인지 wide form 인지 형태 확인(첫 행의 컬럼명 검사)
    sample = rows[0]
    if "cdid" in sample and "data_value" in sample and "time" in sample:
        # long form 분기 — 단계 4 §4.1 산출 형태
        out: dict[str, dict[str, float]] = {}
        for r in rows:
            cdid = r["cdid"]
            t = r["time"]
            try:
                v = float(r["data_value"])
            except ValueError:
                # 숫자로 해석되지 않는 셀(결측 표기)은 누락 유지 — 0 치환 금지
                continue
            out.setdefault(cdid, {})[t] = v
        return out
    # wide form 대안(후속 단위에서 형태가 바뀌더라도 깨지지 않도록 fallback)
    out2: dict[str, dict[str, float]] = {}
    for r in rows:
        t = r["time"]
        for k, v in r.items():
            if k == "time":
                continue
            try:
                out2.setdefault(k, {})[t] = float(v)
            except (ValueError, TypeError):
                pass
    return out2


def load_aa6h_from_rdb() -> dict[str, float]:
    """RDB Table_B_sub4 의 AA6H(CA / GDP, %) 분기 시리즈 적재.

    SELECT-only 접근(UPDATE/DELETE/DROP 미사용). 2006~2025 윈도우의 분기 행
    (``TIME LIKE '%Q%'``) 만 가져와 dict 로 반환한다. AA6H 는 단계 4 §4.3
    단순 상관 §2.3 해석에서 CA / GDP(%) 시계열로 사용된다.

    Returns:
        ``YYYYQn → CA/GDP%`` dict. 본 자료는 80 분기 윈도우 결측 0건이므로
        실질적으로 80 키 모두 채워진다(단계 2 §3 인벤토리 점검 결과).
    """
    out: dict[str, float] = {}
    conn = sqlite3.connect(RDB)
    rows = conn.execute(
        """
        SELECT o.TIME, o.DATA_VALUE
        FROM stat_item_meta m JOIN observation o ON m.item_id=o.item_id
        WHERE m.ITEM_CODE1='AA6H' AND m.STAT_CODE='UK_BoP_Table_B_sub4'
          AND o.TIME LIKE '%Q%'
          AND CAST(SUBSTR(o.TIME,1,4) AS INTEGER) BETWEEN 2006 AND 2025
        ORDER BY o.TIME
        """
    ).fetchall()
    conn.close()
    for t, v in rows:
        if v is None:
            continue
        try:
            out[t] = float(v)
        except (ValueError, TypeError):
            continue
    return out


def load_fx() -> dict[str, dict[str, float]]:
    """``exchange_rates_quarterly_2006q1_2025q4.csv`` 의 4 환율 시리즈 적재.

    Returns:
        ``fx_key → time → value`` 의 2 단 dict. 4 환율 키는 ``FX_KEYS`` 모듈
        상수 그대로이며, 빈 셀은 누락 키로 보존한다(임의 보간 금지).
    """
    out: dict[str, dict[str, float]] = {k: {} for k in FX_KEYS}
    with open(FX, "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            t = r["time"]
            for k in FX_KEYS:
                v = r.get(k, "")
                if v == "" or v is None:
                    continue
                out[k][t] = float(v)
    return out


# ---------------------------------------------------------------------------
# 통계 헬퍼
# ---------------------------------------------------------------------------

def aligned_pair(x: dict[str, float], y: dict[str, float], times: list[str]) -> tuple[list[float], list[float]]:
    """두 시계열을 공통 시점 키로 정렬해 (xs, ys) 두 리스트로 반환.

    `times` 시점 순서를 유지하면서 ``x[t]`` 와 ``y[t]`` 가 모두 존재하는 분기만
    채집한다. Pearson·OLS 계산의 표본 정렬 단계로 사용된다.
    """
    xs, ys = [], []
    for t in times:
        if t in x and t in y:
            xs.append(x[t])
            ys.append(y[t])
    return xs, ys


def pearson(xs: list[float], ys: list[float]) -> float | None:
    """Pearson 상관계수 r 산출(외부 의존 없음, 표준 라이브러리 ``math`` 만 사용).

    표본 크기가 3 미만이거나 표본 표준편차가 0(상수 시계열)이면 ``None`` 을
    반환해 호출 측에서 안전하게 빈 셀로 출력하도록 한다. 80 분기 본문 기준
    레벨 표본은 80, QoQ 차분 표본은 79, YoY 차분 표본은 76 행이다.
    """
    n = len(xs)
    if n < 3:
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if sx == 0 or sy == 0:
        return None
    return num / (sx * sy)


def diff_qoq(series: dict[str, float], times: list[str]) -> dict[str, float]:
    """QoQ(전 분기 대비) 1차 차분: ``Δ_q x_t = x_t − x_{t−1}``.

    `times` 의 인접한 두 분기에 모두 자료가 있을 때만 차분을 산출하고, 누락된
    분기는 결과 dict 에서 빠진다(원본 결측 표기 보존).
    """
    out = {}
    for i in range(1, len(times)):
        t0, t1 = times[i - 1], times[i]
        if t0 in series and t1 in series:
            out[t1] = series[t1] - series[t0]
    return out


def diff_yoy(series: dict[str, float], times: list[str]) -> dict[str, float]:
    """YoY(전년 동분기 대비) 1차 차분: ``Δ_y x_t = x_t − x_{t−4}``.

    분기 자료 4 분기 lag 차분으로 계절성 영향을 줄이는 데 사용된다. `times`
    인덱스가 4 이상일 때만 산출하며, 누락 분기는 결과 dict 에서 빠진다.
    """
    out = {}
    for i in range(4, len(times)):
        t0, t1 = times[i - 4], times[i]
        if t0 in series and t1 in series:
            out[t1] = series[t1] - series[t0]
    return out


def log_diff_qoq(series: dict[str, float], times: list[str]) -> dict[str, float]:
    """log 차분(연속복리 변화율 근사): ``Δ ln x_t = ln(x_t / x_{t−1})``.

    분모·분자 모두 양수일 때만 산출(log 정의역 보장). §4.3.4 차분 회귀에서
    사용되며, CA·BOKI 등 음수가 등장하는 시계열은 호출 측에서 ``abs()`` 로
    절대값 변환 후 본 함수를 호출한다.
    """
    out = {}
    for i in range(1, len(times)):
        t0, t1 = times[i - 1], times[i]
        if t0 in series and t1 in series and series[t0] > 0 and series[t1] > 0:
            out[t1] = math.log(series[t1] / series[t0])
    return out


def ols(xs: list[float], ys: list[float]) -> dict[str, float] | None:
    """단순 OLS 회귀 ``y = α + β·x`` 추정.

    표준 라이브러리만으로 β̂·SE(β̂)·t(β̂)·R² 를 산출한다. 표본 4 미만이거나
    설명변수 분산이 0 이면 ``None`` 을 반환한다(호출 측에서 행 자체를 누락).
    분산 σ² = SSR / (n−2) 의 표본분산 정의를 따라 SE(β̂) = √(σ²/Σ(x−x̄)²) 로 산출.

    Returns:
        ``{n, alpha, beta, se_beta, t_beta, r2}`` 6 키 dict 또는 ``None``.
    """
    n = len(xs)
    if n < 4:
        return None
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0:
        return None
    b = sxy / sxx
    a = my - b * mx
    ssr = sum((y - (a + b * x)) ** 2 for x, y in zip(xs, ys))
    if syy == 0:
        return None
    r2 = 1 - ssr / syy
    sigma2 = ssr / (n - 2) if n > 2 else float("nan")
    se_b = math.sqrt(sigma2 / sxx) if sxx > 0 and sigma2 > 0 else float("nan")
    t_b = b / se_b if se_b and not math.isnan(se_b) else float("nan")
    return {
        "n": n,
        "alpha": a,
        "beta": b,
        "se_beta": se_b,
        "t_beta": t_b,
        "r2": r2,
    }


# ---------------------------------------------------------------------------
# §4.3.2 — 단순 상관
# ---------------------------------------------------------------------------

def section_simple_correlation(qser, fx, times) -> list[dict]:
    """§4.3.2 단순 상관계수 — 4 환율 × 3 BOP × 3 변환(레벨/QoQ/YoY).

    Pearson r 을 (i) 레벨 (ii) QoQ 차분 (iii) YoY 차분 3 가지 변환으로 각각
    산출해 12 행 = 4 환율 × 3 BOP 변수 의 평면 표를 반환한다. CA / GDP(%) 는
    RDB AA6H Table_B_sub4 시리즈를 합성 키 ``ca_gdp`` 로 등록해 사용한다.
    """
    targets = OrderedDict([
        ("HBOP", "경상수지(CA, £m, HBOP)"),
        ("BOKI", "상품수지(£m, BOKI)"),
        ("ca_gdp", "CA / GDP (%, 합성)"),
    ])
    out_rows = []
    for fxk in FX_KEYS:
        fx_series = fx[fxk]
        for var_key, var_label in targets.items():
            yser = qser.get(var_key, {})
            if not yser:
                continue
            # level
            xs, ys = aligned_pair(fx_series, yser, times)
            r_level = pearson(xs, ys)
            # qoq diff
            dx = diff_qoq(fx_series, times)
            dy = diff_qoq(yser, times)
            xs2, ys2 = aligned_pair(dx, dy, times)
            r_qoq = pearson(xs2, ys2)
            # yoy diff
            dxy = diff_yoy(fx_series, times)
            dyy = diff_yoy(yser, times)
            xs3, ys3 = aligned_pair(dxy, dyy, times)
            r_yoy = pearson(xs3, ys3)
            out_rows.append({
                "fx_series": FX_LABEL[fxk],
                "fx_key": fxk,
                "bop_series": var_label,
                "bop_key": var_key,
                "n_level": len(xs),
                "corr_level": r_level,
                "n_diff_qoq": len(xs2),
                "corr_diff_qoq": r_qoq,
                "n_diff_yoy": len(xs3),
                "corr_diff_yoy": r_yoy,
            })
    return out_rows


# ---------------------------------------------------------------------------
# §4.3.3 — 시차 상관 (J-curve)
# ---------------------------------------------------------------------------

LAGS = [0, 1, 2, 4, 8]


def section_lag_correlation(qser, fx, times) -> list[dict]:
    """§4.3.3 시차 상관 — J-curve 검증용.

    환율 QoQ 차분 ``Δ_q ER_t`` 와 BOP QoQ 차분 ``Δ_q Y_{t+lag}`` (BOP 가 ``lag``
    분기 후) 사이 Pearson r 을 산출한다. lag = 0/1/2/4/8 의 5 시차로 환율 약세
    → BOP 개선이 시차 후 부호 전환되는지 검증한다. 4 환율 × 2 BOP × 5 lag =
    40 행. 본 80 분기 윈도우에서는 4 환율 모두 lag 4 음 상관 −0.10~−0.16 만
    관찰돼 J-curve 가설은 미검출(보고서 §4.3.3 §3.3 결론).
    """
    targets = OrderedDict([
        ("HBOP", "경상수지(CA, £m, HBOP)"),
        ("BOKI", "상품수지(£m, BOKI)"),
    ])
    out_rows = []
    for fxk in FX_KEYS:
        dxq = diff_qoq(fx[fxk], times)  # 환율 차분(레벨 차분)
        for var_key, var_label in targets.items():
            yser = qser.get(var_key, {})
            if not yser:
                continue
            dyq = diff_qoq(yser, times)
            for lag in LAGS:
                # CA[t+lag] vs ER_diff[t]
                xs, ys = [], []
                for t in times:
                    if t not in dxq:
                        continue
                    # find time index
                    idx = times.index(t)
                    j = idx + lag
                    if j >= len(times):
                        continue
                    t_lead = times[j]
                    if t_lead in dyq:
                        xs.append(dxq[t])
                        ys.append(dyq[t_lead])
                r = pearson(xs, ys)
                out_rows.append({
                    "fx_series": FX_LABEL[fxk],
                    "fx_key": fxk,
                    "bop_series": var_label,
                    "bop_key": var_key,
                    "lag_quarters": lag,
                    "n": len(xs),
                    "corr_qoq_diff": r,
                })
    return out_rows


# ---------------------------------------------------------------------------
# §4.3.4 — 차분 회귀
# ---------------------------------------------------------------------------

def section_regression(qser, fx, times) -> list[dict]:
    r"""§4.3.4 차분 회귀 — Δlog ER → Δlog \|Y\| 단순 OLS.

    CA·BOKI 가 음수(적자) 시계열이라 절대값(|·|) 의 log 차분으로 변환했다.
    회귀식: ``Δlog |Y_t| = α + β · Δlog ER_t`` (n=79). 본 80 분기 윈도우에서는
    8 회귀 모두 R² < 0.01 + |t(β)| < 1 로 통계적 무의미를 확인한다(보고서 §4
    핵심 결론). 4 환율 × 2 BOP = 8 행 평면 표 반환.
    """
    out_rows = []
    targets = OrderedDict([
        ("HBOP", "|CA| (£m, HBOP)"),
        ("BOKI", "|BOKI| (£m)"),
    ])
    for fxk in FX_KEYS:
        fxser = fx[fxk]
        dxlog = log_diff_qoq(fxser, times)
        for var_key, var_label in targets.items():
            yser = qser.get(var_key, {})
            if not yser:
                continue
            abs_y = {t: abs(v) for t, v in yser.items() if v != 0}
            dylog = log_diff_qoq(abs_y, times)
            xs, ys = aligned_pair(dxlog, dylog, times)
            res = ols(xs, ys)
            if res is None:
                continue
            out_rows.append({
                "fx_series": FX_LABEL[fxk],
                "fx_key": fxk,
                "y_series": var_label,
                "y_key": var_key,
                "n": res["n"],
                "alpha": res["alpha"],
                "beta": res["beta"],
                "se_beta": res["se_beta"],
                "t_beta": res["t_beta"],
                "r2": res["r2"],
            })
    return out_rows


# ---------------------------------------------------------------------------
# §4.3.5 — 사례 분석
# ---------------------------------------------------------------------------

CASE_EVENTS = [
    # (event_label, base_quarter, note)
    ("2008Q4_GFC_Sterling_low", "2008Q4", "글로벌 금융위기 파운드 급락 직후"),
    ("2009Q1_GFC_continuation", "2009Q1", "GFC 직후 약세 연장"),
    ("2016Q3_Brexit_referendum", "2016Q3", "Brexit 국민투표 직후"),
    ("2020Q1_COVID_shock", "2020Q1", "팬데믹 충격기"),
    ("2022Q3_MiniBudget", "2022Q3", "Mini-budget 사상 최저"),
]


def section_case_study(qser, fx, times) -> list[dict]:
    """§4.3.5 사례 분석 — 5 사건 × 9 분기(k=0~8) 누적 변화 표.

    `CASE_EVENTS` 5 사건의 base 분기와 그 직후 8 분기 시점에 대해 GBP/USD ·
    Sterling ERI · BOKI · HBOP 의 누적 변화율을 산출한다. 환율은 base 대비 %
    변화, BOP 는 base 대비 GBP million 절대 차이로 계산해 부호 일관성
    (환율 약세 → BoP 개선) 을 사례별로 점검할 수 있게 한다. 본 80 분기
    윈도우에서는 5 사건 중 **Brexit 2016Q3 단 1건만** 부호 일관(8 분기 BOKI
    누적 +£6.9bn) 이 검출된다(보고서 §4.3.5 §5.6 결론).
    """
    rows = []
    usd = fx["gbp_usd"]
    eri = fx["sterling_eri_jan2005_100"]
    boki = qser.get("BOKI", {})
    hbop = qser.get("HBOP", {})
    for event_label, base_q, note in CASE_EVENTS:
        if base_q not in times:
            continue
        idx0 = times.index(base_q)
        for k in range(0, 9):  # k = 0,1,2,...,8 분기 (base 포함 9 행)
            j = idx0 + k
            if j >= len(times):
                break
            t_k = times[j]
            row = {
                "event": event_label,
                "event_note": note,
                "base_quarter": base_q,
                "k_quarters_after": k,
                "quarter": t_k,
                "gbp_usd": usd.get(t_k),
                "sterling_eri": eri.get(t_k),
                "boki_gbp_million": boki.get(t_k),
                "hbop_gbp_million": hbop.get(t_k),
            }
            # 누적 변화율 (base 대비)
            if k == 0:
                row["gbp_usd_chg_vs_base_pct"] = 0.0
                row["sterling_eri_chg_vs_base_pct"] = 0.0
                row["boki_chg_vs_base_gbpmn"] = 0.0
                row["hbop_chg_vs_base_gbpmn"] = 0.0
            else:
                u0, uk = usd.get(base_q), usd.get(t_k)
                e0, ek = eri.get(base_q), eri.get(t_k)
                b0, bk = boki.get(base_q), boki.get(t_k)
                h0, hk = hbop.get(base_q), hbop.get(t_k)
                row["gbp_usd_chg_vs_base_pct"] = (
                    100.0 * (uk - u0) / u0 if u0 and uk else None
                )
                row["sterling_eri_chg_vs_base_pct"] = (
                    100.0 * (ek - e0) / e0 if e0 and ek else None
                )
                row["boki_chg_vs_base_gbpmn"] = (
                    bk - b0 if b0 is not None and bk is not None else None
                )
                row["hbop_chg_vs_base_gbpmn"] = (
                    hk - h0 if h0 is not None and hk is not None else None
                )
            rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def fmt_corr(v):
    """상관계수 포맷터 — ``None`` 이면 빈 셀, 그 외에는 소수 4자리.

    표본 부족·상수 시계열 등으로 ``pearson`` 이 ``None`` 을 반환한 경우를
    안전하게 빈 문자열로 처리해 CSV 직렬화에서 NaN 토큰이 새지 않도록 한다.
    """
    if v is None:
        return ""
    return f"{v:.4f}"


def main() -> None:
    """§4.3.2 ~ §4.3.5 4 평면 CSV 일괄 산출 메인 절차.

    절차:
        1. quarterly_series·환율 wide·RDB AA6H 3 입력 적재(SELECT-only).
        2. 80 분기 시점 리스트(times) 를 4 환율 시계열의 합집합으로 구성.
        3. §4.3.2 단순 상관(12 행) → ``fx_correlation_…csv``.
        4. §4.3.3 시차 상관(40 행) → ``fx_lag_correlation_…csv``.
        5. §4.3.4 차분 회귀(8 행) → ``fx_regression_…csv``.
        6. §4.3.5 사례 분석(45 행) → ``fx_case_study_…csv``.

    Side Effects:
        ``OUT_CORR``·``OUT_LAG``·``OUT_REG``·``OUT_CASE`` 4 경로의 CSV 파일을
        새로 작성한다(기존 파일 덮어쓰기, 멱등 재실행 가능).
    """
    qser = load_quarterly_series()
    fx = load_fx()
    # AA6H (CA / GDP, %) 를 RDB 에서 직접 로드해 qser 에 ca_gdp 키로 등록
    qser["ca_gdp"] = load_aa6h_from_rdb()
    # 80 분기 시점 리스트
    times = sorted({t for ts in fx.values() for t in ts.keys()})

    # 사용 가능한 BOP 시리즈 진단
    print(f"BOP series keys: {sorted(qser.keys())}")
    print(f"FX series keys: {list(fx.keys())} (n_quarters per series: {[len(v) for v in fx.values()]})")
    print(f"Times: {len(times)} from {times[0]} to {times[-1]}")

    # §4.3.2 단순 상관
    rows = section_simple_correlation(qser, fx, times)
    with open(OUT_CORR, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "fx_series", "fx_key", "bop_series", "bop_key",
            "n_level", "corr_level",
            "n_diff_qoq", "corr_diff_qoq",
            "n_diff_yoy", "corr_diff_yoy",
        ])
        for r in rows:
            w.writerow([
                r["fx_series"], r["fx_key"], r["bop_series"], r["bop_key"],
                r["n_level"], fmt_corr(r["corr_level"]),
                r["n_diff_qoq"], fmt_corr(r["corr_diff_qoq"]),
                r["n_diff_yoy"], fmt_corr(r["corr_diff_yoy"]),
            ])
    print(f"saved {OUT_CORR}  rows={len(rows)}")

    # §4.3.3 시차 상관
    rows = section_lag_correlation(qser, fx, times)
    with open(OUT_LAG, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "fx_series", "fx_key", "bop_series", "bop_key",
            "lag_quarters", "n", "corr_qoq_diff",
        ])
        for r in rows:
            w.writerow([
                r["fx_series"], r["fx_key"], r["bop_series"], r["bop_key"],
                r["lag_quarters"], r["n"], fmt_corr(r["corr_qoq_diff"]),
            ])
    print(f"saved {OUT_LAG}  rows={len(rows)}")

    # §4.3.4 회귀
    rows = section_regression(qser, fx, times)
    with open(OUT_REG, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "fx_series", "fx_key", "y_series", "y_key",
            "n", "alpha", "beta", "se_beta", "t_beta", "r2",
        ])
        for r in rows:
            w.writerow([
                r["fx_series"], r["fx_key"], r["y_series"], r["y_key"],
                r["n"],
                f"{r['alpha']:.6f}",
                f"{r['beta']:.6f}",
                f"{r['se_beta']:.6f}",
                f"{r['t_beta']:.4f}",
                f"{r['r2']:.4f}",
            ])
    print(f"saved {OUT_REG}  rows={len(rows)}")

    # §4.3.5 사례 분석
    rows = section_case_study(qser, fx, times)
    with open(OUT_CASE, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "event", "event_note", "base_quarter", "k_quarters_after", "quarter",
            "gbp_usd", "sterling_eri", "boki_gbp_million", "hbop_gbp_million",
            "gbp_usd_chg_vs_base_pct", "sterling_eri_chg_vs_base_pct",
            "boki_chg_vs_base_gbpmn", "hbop_chg_vs_base_gbpmn",
        ])
        for r in rows:
            def f6(x):
                return "" if x is None else f"{x:.6f}"

            def f0(x):
                return "" if x is None else f"{x:.0f}"

            def f4(x):
                return "" if x is None else f"{x:.4f}"

            w.writerow([
                r["event"], r["event_note"], r["base_quarter"], r["k_quarters_after"], r["quarter"],
                f6(r["gbp_usd"]), f6(r["sterling_eri"]),
                f0(r["boki_gbp_million"]), f0(r["hbop_gbp_million"]),
                f4(r["gbp_usd_chg_vs_base_pct"]), f4(r["sterling_eri_chg_vs_base_pct"]),
                f0(r["boki_chg_vs_base_gbpmn"]), f0(r["hbop_chg_vs_base_gbpmn"]),
            ])
    print(f"saved {OUT_CASE}  rows={len(rows)}")


if __name__ == "__main__":
    main()
