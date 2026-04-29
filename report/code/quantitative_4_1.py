"""보고서 단계 4 §4.1 — 시계열·통계량 산출 스크립트.

본 스크립트는 단일 호출(`env/Scripts/python.exe report/code/quantitative_4_1.py`) 로
사용자 요청 5건(§4.1.1 ~ §4.1.5) 의 5 평면 CSV 를 일괄 산출한다.

산출물:
  1. report/data/quarterly_series_2006q1_2025q4.csv   (long-form 13 × 80 = 1,040 행)
  2. report/data/statistics_2006q1_2025q4.csv         (변수당 1행 통계량)
  3. report/data/trend_2006q1_2025q4.csv              (선형 트렌드)
  4. report/data/ca_decomposition_2006q1_2025q4.csv   (CA 분해 + 검증 + 분산 기여도)
  5. report/data/fa_share_2006q1_2025q4.csv           (FA 점유 비중·변동성)

데이터 소스: db/data/_db/ecos_uk_bop.sqlite (읽기 전용 SELECT).
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
OUT_DIR = REPO_ROOT / "report/data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_SERIES = OUT_DIR / "quarterly_series_2006q1_2025q4.csv"
OUT_STATS = OUT_DIR / "statistics_2006q1_2025q4.csv"
OUT_TREND = OUT_DIR / "trend_2006q1_2025q4.csv"
OUT_CA = OUT_DIR / "ca_decomposition_2006q1_2025q4.csv"
OUT_FA = OUT_DIR / "fa_share_2006q1_2025q4.csv"

# ---------------------------------------------------------------------------
# 1. 분석 대상 13 변수 (CDID, STAT_CODE, 분류, 한국어 라벨)
# ---------------------------------------------------------------------------

VARIABLES: list[tuple[str, str, str, str]] = [
    # (CDID/ITEM_CODE1, STAT_CODE, 분류, 한국어 라벨)
    ("BOKI", "UK_BoP_Table_A_sub1", "CA", "상품무역(G)"),
    ("IKBD", "UK_BoP_Table_A_sub1", "CA", "서비스무역(S)"),
    ("HBOJ", "UK_BoP_Table_A_sub1", "CA", "1차소득(PI)"),
    ("IKBP", "UK_BoP_Table_A_sub1", "CA", "2차소득(SI)"),
    ("HBOP", "UK_BoP_Table_A_sub1", "CA", "경상수지 합계(CA)"),
    ("-MU7M", "UK_BoP_Table_A_sub3", "FA", "직접투자(DI)"),
    ("-HHZD", "UK_BoP_Table_A_sub3", "FA", "증권투자(PI_FA)"),
    ("-ZPNN", "UK_BoP_Table_A_sub3", "FA", "파생금융상품(FD)"),
    ("-HHYR", "UK_BoP_Table_A_sub3", "FA", "기타투자(OI)"),
    ("-LTCV", "UK_BoP_Table_A_sub3", "FA", "준비자산(RA)"),
    ("-HBNT", "UK_BoP_Table_A_sub3", "FA", "금융계정 합계(FA)"),
    ("FNVQ", "UK_BoP_Table_A_sub1", "AUX", "자본수지(KA)"),
    ("HHDH", "UK_BoP_Table_A_sub3", "AUX", "순오차누락(NEO)"),
]

# 분기 윈도우 (2006Q1 ~ 2025Q4)
START_TIME = "2006Q1"
END_TIME = "2025Q4"


def quarter_to_index(t: str) -> int:
    """`YYYYQn` 분기 문자열을 1997Q1=0 기준 정수 정렬 키로 환산.

    파라미터
    ----------
    t : str
        `2006Q1`·`2025Q4` 등 ONS·ECOS 표준 분기 표기.

    반환값
    ------
    int
        1997Q1 을 0으로 두는 정수 인덱스. 분기 거리 계산·정렬에 사용.
    """
    yr = int(t[:4])
    q = int(t[-1])
    return (yr - 1997) * 4 + (q - 1)


def quarter_list(start: str, end: str) -> list[str]:
    """시작·종료 분기를 받아 [start, end] 폐구간 분기 문자열 리스트 생성.

    파라미터
    ----------
    start, end : str
        `YYYYQn` 형식 분기 문자열. 예: `2006Q1`, `2025Q4`.

    반환값
    ------
    list[str]
        `2006Q1`, `2006Q2`, …, `2025Q4` 와 같이 시간 순 정렬된 분기 라벨.
        본 스크립트에서는 80 분기(20년) 윈도우를 산출하기 위해 사용.
    """
    s = quarter_to_index(start)
    e = quarter_to_index(end)
    out: list[str] = []
    for idx in range(s, e + 1):
        yr = 1997 + idx // 4
        q = idx % 4 + 1
        out.append(f"{yr}Q{q}")
    return out


QUARTERS = quarter_list(START_TIME, END_TIME)
assert len(QUARTERS) == 80, f"분기 수 불일치: {len(QUARTERS)}"


# ---------------------------------------------------------------------------
# 2. RDB 에서 변수별 80 분기 시계열 적재
# ---------------------------------------------------------------------------

def load_series(conn: sqlite3.Connection) -> dict[str, dict[str, float]]:
    """{CDID: {TIME: data_value}} 구조로 13 변수 시계열을 적재.

    ITEM_CODE1·STAT_CODE 조건으로 Table_A 한정 단일 항목 보장.
    """
    series: dict[str, dict[str, float]] = {}
    for cdid, stat_code, _cls, _label in VARIABLES:
        rows = conn.execute(
            """
            SELECT o.TIME, o.DATA_VALUE
            FROM stat_item_meta m
            JOIN observation o ON m.item_id = o.item_id
            WHERE m.ITEM_CODE1 = ?
              AND m.STAT_CODE = ?
              AND o.TIME LIKE '%Q%'
              AND o.TIME >= ?
              AND o.TIME <= ?
            ORDER BY o.TIME
            """,
            (cdid, stat_code, START_TIME, END_TIME),
        ).fetchall()
        d = {t: float(v) for t, v in rows if v is not None}
        if len(d) != 80:
            raise RuntimeError(f"{cdid} 분기 행 수 비정상: {len(d)} (예상 80)")
        series[cdid] = d
    return series


def fetch_unit(conn: sqlite3.Connection, cdid: str, stat_code: str) -> str:
    """`stat_item_meta` 에서 (ITEM_CODE1, STAT_CODE) 쌍의 UNIT_NAME 단일 조회.

    Table_A 13 변수는 모두 `GBP million` 단위로 등재돼 있어야 하며,
    혹여 누락 시 빈 문자열을 반환한다(상위 호출부에서 자체 점검).
    """
    row = conn.execute(
        "SELECT UNIT_NAME FROM stat_item_meta WHERE ITEM_CODE1=? AND STAT_CODE=?",
        (cdid, stat_code),
    ).fetchone()
    return row[0] if row else ""


# ---------------------------------------------------------------------------
# 3. §4.1.1 — long-form 평면 표
# ---------------------------------------------------------------------------

def write_long_form(conn: sqlite3.Connection, series: dict[str, dict[str, float]]) -> int:
    """§4.1.1 — 13 변수 × 80 분기 long-form 평면 표를 CSV 로 산출.

    부작용
    ------
    `OUT_SERIES` 경로(`report/data/quarterly_series_2006q1_2025q4.csv`) 에
    1,040 행 + 헤더 1행을 신규 작성(덮어쓰기). 기존 파일은 멱등적으로 갱신된다.

    반환값
    ------
    int
        헤더 제외 데이터 행 수(예상치 1,040). 호출부에서 assert 로 검증.
    """
    rows_written = 0
    with OUT_SERIES.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        # 헤더: 영문 식별자 + 한국어 라벨 컬럼 분리(분석 도구 호환성 우선)
        w.writerow(["cdid", "item_name_kr", "stat_code", "time", "data_value", "unit"])
        for cdid, stat_code, _cls, label in VARIABLES:
            unit = fetch_unit(conn, cdid, stat_code)
            data = series[cdid]
            for t in QUARTERS:
                # 한 행 = 한 (변수, 분기) 관측치, 값은 RDB 원시값을 그대로 출력
                w.writerow([cdid, label, stat_code, t, data[t], unit])
                rows_written += 1
    return rows_written


# ---------------------------------------------------------------------------
# 4. §4.1.2 — 통계량 표 (평균·중앙값·SD·max·min·자기상관 lag 1·4·8)
# ---------------------------------------------------------------------------

def autocorr(values: list[float], lag: int) -> float:
    """라그-k 표본 자기상관 (분모는 분산, 평균 동일하게 사용).

    공식: r_k = sum((x_t - mean)(x_{t-k} - mean)) / sum((x_t - mean)^2)
    Box-Jenkins 표준 정의.
    """
    n = len(values)
    if lag <= 0 or lag >= n:
        return float("nan")
    mu = sum(values) / n
    denom = sum((x - mu) ** 2 for x in values)
    if denom == 0:
        return float("nan")
    num = sum((values[i] - mu) * (values[i - lag] - mu) for i in range(lag, n))
    return num / denom


def write_statistics(series: dict[str, dict[str, float]]) -> int:
    """§4.1.2 — 변수당 9 통계량(평균·중앙값·SD·max·min·자기상관 lag 1·4·8) 표 산출.

    부작용
    ------
    `OUT_STATS` 경로(`report/data/statistics_2006q1_2025q4.csv`) 에
    13 행 + 헤더 1행을 작성. 자기상관은 무차원, 그 외는 GBP million.

    반환값
    ------
    int
        데이터 행 수(예상치 13). 호출부에서 assert 로 검증.
    """
    rows = 0
    with OUT_STATS.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "cdid", "item_name_kr", "category", "n",
            "mean", "median", "stdev", "max", "min",
            "autocorr_lag1", "autocorr_lag4", "autocorr_lag8",
        ])
        for cdid, _stat, cls, label in VARIABLES:
            vals = [series[cdid][t] for t in QUARTERS]
            w.writerow([
                cdid, label, cls, len(vals),
                round(statistics.fmean(vals), 4),
                round(statistics.median(vals), 4),
                round(statistics.stdev(vals), 4),
                round(max(vals), 4),
                round(min(vals), 4),
                round(autocorr(vals, 1), 6),
                round(autocorr(vals, 4), 6),
                round(autocorr(vals, 8), 6),
            ])
            rows += 1
    return rows


# ---------------------------------------------------------------------------
# 5. §4.1.3 — 단순 선형 트렌드 (y_t = α + β·year + ε)
# ---------------------------------------------------------------------------

def linear_regression(x: list[float], y: list[float]) -> tuple[float, float, float, float]:
    """단순 OLS — α, β, t-stat(β), R^2 반환.

    표본 표준오차는 잔차분산을 (n-2) 자유도로 나눠 산출한다.
    """
    n = len(x)
    mx = sum(x) / n
    my = sum(y) / n
    sxx = sum((xi - mx) ** 2 for xi in x)
    sxy = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    syy = sum((yi - my) ** 2 for yi in y)
    if sxx == 0:
        return float("nan"), float("nan"), float("nan"), float("nan")
    beta = sxy / sxx
    alpha = my - beta * mx
    resid = [y[i] - (alpha + beta * x[i]) for i in range(n)]
    rss = sum(r * r for r in resid)
    df = n - 2
    if df <= 0 or rss == 0:
        return alpha, beta, float("nan"), 1.0 if syy == 0 else 1.0 - rss / syy
    sigma2 = rss / df
    se_beta = math.sqrt(sigma2 / sxx)
    t_beta = beta / se_beta if se_beta > 0 else float("nan")
    r2 = 1.0 - rss / syy if syy > 0 else float("nan")
    return alpha, beta, t_beta, r2


def write_trend(series: dict[str, dict[str, float]]) -> int:
    """§4.1.3 — 13 변수 단순 선형 트렌드(연도 회귀) 추정 결과 CSV 산출.

    회귀 모형: y_t = α + β · year_t + ε_t. year 는 분기를 십진수 연으로 환산
    (2006Q1 = 2006.00, 2006Q2 = 2006.25, …, 2025Q4 = 2025.75). β 는 연간 변화량
    (GBP million / year), t-stat 은 잔차분산 자유도 n-2 표준 OLS.

    부작용
    ------
    `OUT_TREND` 경로(`report/data/trend_2006q1_2025q4.csv`) 에 13 행 + 헤더.

    반환값
    ------
    int
        데이터 행 수(예상치 13).
    """
    # 회귀에 사용하는 x 는 연(年) 십진수 (예: 2006Q1 = 2006.00, 2006Q2 = 2006.25 …)
    years = [int(t[:4]) + (int(t[-1]) - 1) * 0.25 for t in QUARTERS]

    rows = 0
    with OUT_TREND.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "cdid", "item_name_kr", "category",
            "alpha", "beta_per_year", "t_stat_beta", "r_squared", "n",
        ])
        for cdid, _stat, cls, label in VARIABLES:
            vals = [series[cdid][t] for t in QUARTERS]
            alpha, beta, t_beta, r2 = linear_regression(years, vals)
            w.writerow([
                cdid, label, cls,
                round(alpha, 4), round(beta, 4), round(t_beta, 4), round(r2, 6), len(vals),
            ])
            rows += 1
    return rows


# ---------------------------------------------------------------------------
# 6. §4.1.4 — CA 분해 기여도 (G + S + PI + SI = CA 검증 + 분산 기여도)
# ---------------------------------------------------------------------------

def write_ca_decomposition(series: dict[str, dict[str, float]]) -> tuple[int, int]:
    """§4.1.4 — 분기별 G+S+PI+SI=CA 항등식 검증 + 4 항목 분산 기여도 CSV 산출.

    분산 기여도는 Cov(comp, CA) / Var(CA) 로 계산하며 4 항목 합계는 선형성에 의해
    이론적으로 1.0 이 되어야 한다(부동소수점 오차 한도 내 검증).
    잔차 임계값은 0.5 GBP million(= 50 만 파운드)으로, ONS 발표 단위(GBP million)
    의 반올림 오차 한도를 넉넉히 잡았다.

    부작용
    ------
    `OUT_CA` 경로(`report/data/ca_decomposition_2006q1_2025q4.csv`) 에 80 행 + 헤더.
    표준출력에 검증 결과(잔차 분기 수·max |잔차|, 분산 기여도) 를 출력.

    반환값
    ------
    tuple[int, int]
        (작성한 데이터 행 수, |잔차|>0.5 분기 수). 두 번째 값이 0 이면 80/80 정확 일치.
    """
    g = series["BOKI"]
    s = series["IKBD"]
    pi = series["HBOJ"]
    si = series["IKBP"]
    ca = series["HBOP"]

    # 분산 기여도: 분기별 (component - mean) * (CA - mean_CA) / Var(CA) 평균
    # = Cov(comp, CA) / Var(CA), 합치면 1 이 됨 (linearity).
    vals_ca = [ca[t] for t in QUARTERS]
    mu_ca = statistics.fmean(vals_ca)
    var_ca = sum((v - mu_ca) ** 2 for v in vals_ca)

    contrib: dict[str, float] = {}
    for key, src in (("G", g), ("S", s), ("PI", pi), ("SI", si)):
        vals_c = [src[t] for t in QUARTERS]
        mu_c = statistics.fmean(vals_c)
        cov = sum((vals_c[i] - mu_c) * (vals_ca[i] - mu_ca) for i in range(len(QUARTERS)))
        contrib[key] = cov / var_ca if var_ca > 0 else float("nan")

    contrib_sum = sum(contrib.values())

    rows_written = 0
    mismatch_count = 0
    max_abs_residual = 0.0

    with OUT_CA.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "time",
            "G_BOKI", "S_IKBD", "PI_HBOJ", "SI_IKBP",
            "CA_HBOP", "G_plus_S_plus_PI_plus_SI",
            "residual_GBP_million",
            "share_G_var", "share_S_var", "share_PI_var", "share_SI_var", "share_sum",
        ])
        for t in QUARTERS:
            sum_4 = g[t] + s[t] + pi[t] + si[t]
            resid = ca[t] - sum_4
            if abs(resid) > 0.5:  # 0.5 GBP million = 50 만 파운드 임계
                mismatch_count += 1
            if abs(resid) > max_abs_residual:
                max_abs_residual = abs(resid)
            w.writerow([
                t,
                round(g[t], 4), round(s[t], 4), round(pi[t], 4), round(si[t], 4),
                round(ca[t], 4), round(sum_4, 4),
                round(resid, 4),
                round(contrib["G"], 6), round(contrib["S"], 6),
                round(contrib["PI"], 6), round(contrib["SI"], 6),
                round(contrib_sum, 6),
            ])
            rows_written += 1

    print(f"  [CA 분해] G+S+PI+SI = CA 검증: 전체 {len(QUARTERS)} 분기 중 |잔차|>0.5 = {mismatch_count} 건, "
          f"max |residual| = {max_abs_residual:.6f} (GBP million)")
    print(f"  [CA 분해] 분산 기여도: G={contrib['G']:.4f}, S={contrib['S']:.4f}, "
          f"PI={contrib['PI']:.4f}, SI={contrib['SI']:.4f}, 합계={contrib_sum:.6f}")
    return rows_written, mismatch_count


# ---------------------------------------------------------------------------
# 7. §4.1.5 — FA 점유 비중·변동성 표
# ---------------------------------------------------------------------------

def write_fa_share(series: dict[str, dict[str, float]]) -> int:
    """FA 5 세부의 분기별 점유 비중 + 변동성 비교.

    점유 비중 두 정의를 산출:
      - share_signed: 부호 있는 점유 = component / FA_total (FA_total ≠ 0 인 경우)
      - share_abs: 절대값 기반 = |component| / sum(|components|)
    변동성: 80분기 SD.
    """
    fa_keys = ["-MU7M", "-HHZD", "-ZPNN", "-HHYR", "-LTCV"]
    label_of = {cdid: label for cdid, _, _, label in VARIABLES}

    # SD 계산
    sd_table = {k: statistics.stdev([series[k][t] for t in QUARTERS]) for k in fa_keys}
    fa_total = series["-HBNT"]

    # 1) 분기별 wide 표 (점유 비중)
    rows_written = 0
    with OUT_FA.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        # 첫 80행: 분기별 시계열 (구분 행 = "row_kind=quarterly")
        w.writerow([
            "row_kind", "time",
            "DI_MU7M", "PI_HHZD", "FD_ZPNN", "OI_HHYR", "RA_LTCV",
            "FA_total_HBNT", "abs_sum_5",
            "share_signed_DI", "share_signed_PI_FA", "share_signed_FD",
            "share_signed_OI", "share_signed_RA",
            "share_abs_DI", "share_abs_PI_FA", "share_abs_FD",
            "share_abs_OI", "share_abs_RA",
        ])
        for t in QUARTERS:
            comps = [series[k][t] for k in fa_keys]
            total = fa_total[t]
            abs_sum = sum(abs(c) for c in comps)
            # signed share: 분모가 0 에 가까우면 NaN 처리
            ss = [
                (c / total) if abs(total) > 1e-9 else float("nan")
                for c in comps
            ]
            sa = [
                (abs(c) / abs_sum) if abs_sum > 1e-9 else float("nan")
                for c in comps
            ]
            w.writerow([
                "quarterly", t,
                round(comps[0], 4), round(comps[1], 4), round(comps[2], 4),
                round(comps[3], 4), round(comps[4], 4),
                round(total, 4), round(abs_sum, 4),
                round(ss[0], 6), round(ss[1], 6), round(ss[2], 6),
                round(ss[3], 6), round(ss[4], 6),
                round(sa[0], 6), round(sa[1], 6), round(sa[2], 6),
                round(sa[3], 6), round(sa[4], 6),
            ])
            rows_written += 1

        # 마지막 3 요약 행: 항목별 SD·평균 점유(부호 있음/절대값)
        #   - row_kind=summary_stdev          → 80분기 원시값 SD (GBP million)
        #   - row_kind=summary_mean_share_signed → 80분기 share_signed 평균(NaN 제외)
        #   - row_kind=summary_mean_share_abs    → 80분기 share_abs 평균(NaN 제외)
        # wide 표 양식을 유지하기 위해 각 요약 행은 해당 metric 컬럼만 채우고
        # 무관 컬럼은 빈 문자열로 둔다(별도 long-form summary 파일은 산출하지 않는다).

        # 항목별 평균 share (signed / abs)
        avg_signed: list[float] = []
        avg_abs: list[float] = []
        for idx, k in enumerate(fa_keys):
            ss_list: list[float] = []
            sa_list: list[float] = []
            for t in QUARTERS:
                comps = [series[kk][t] for kk in fa_keys]
                total = fa_total[t]
                abs_sum = sum(abs(c) for c in comps)
                if abs(total) > 1e-9:
                    ss_list.append(comps[idx] / total)
                if abs_sum > 1e-9:
                    sa_list.append(abs(comps[idx]) / abs_sum)
            avg_signed.append(statistics.fmean(ss_list) if ss_list else float("nan"))
            avg_abs.append(statistics.fmean(sa_list) if sa_list else float("nan"))

        # SD row
        w.writerow([
            "summary_stdev", "2006Q1-2025Q4",
            round(sd_table["-MU7M"], 4), round(sd_table["-HHZD"], 4),
            round(sd_table["-ZPNN"], 4), round(sd_table["-HHYR"], 4),
            round(sd_table["-LTCV"], 4),
            "", "",  # FA_total·abs_sum
            "", "", "", "", "",  # signed share 5
            "", "", "", "", "",  # abs share 5
        ])
        rows_written += 1

        # signed share 평균 row
        w.writerow([
            "summary_mean_share_signed", "2006Q1-2025Q4",
            "", "", "", "", "",  # 원시값 5 비움
            "", "",
            round(avg_signed[0], 6), round(avg_signed[1], 6), round(avg_signed[2], 6),
            round(avg_signed[3], 6), round(avg_signed[4], 6),
            "", "", "", "", "",
        ])
        rows_written += 1

        # abs share 평균 row
        w.writerow([
            "summary_mean_share_abs", "2006Q1-2025Q4",
            "", "", "", "", "",
            "", "",
            "", "", "", "", "",
            round(avg_abs[0], 6), round(avg_abs[1], 6), round(avg_abs[2], 6),
            round(avg_abs[3], 6), round(avg_abs[4], 6),
        ])
        rows_written += 1

    print(f"  [FA 점유] SD: DI={sd_table['-MU7M']:.0f}, PI_FA={sd_table['-HHZD']:.0f}, "
          f"FD={sd_table['-ZPNN']:.0f}, OI={sd_table['-HHYR']:.0f}, RA={sd_table['-LTCV']:.0f} (GBP million)")
    print(f"  [FA 점유] 평균 |share|: DI={avg_abs[0]:.4f}, PI_FA={avg_abs[1]:.4f}, "
          f"FD={avg_abs[2]:.4f}, OI={avg_abs[3]:.4f}, RA={avg_abs[4]:.4f}")

    return rows_written


# ---------------------------------------------------------------------------
# 8. main
# ---------------------------------------------------------------------------

def main() -> None:
    """5 평면 CSV 산출 파이프라인의 진입점.

    실행 순서:
      1) RDB 연결(읽기 전용 SELECT) 및 13 변수 × 80 분기 시계열 적재
      2) §4.1.1 long-form 평면 표 산출 (1,040 행)
      3) §4.1.2 통계량 표 산출 (13 행)
      4) §4.1.3 트렌드 회귀 표 산출 (13 행)
      5) §4.1.4 CA 분해·항등식 검증 표 산출 (80 행, 잔차 0 일치 점검)
      6) §4.1.5 FA 점유·변동성 표 산출 (80 분기 + 3 요약 = 83 행)

    각 단계 종료 시 행 수를 assert 로 검증해 멱등 재실행 시에도 동일 산출이
    보장되도록 한다. RDB 는 SELECT 만 수행하며 어떠한 쓰기 동작도 하지 않는다.
    """
    if not DB_PATH.exists():
        raise SystemExit(f"RDB 미존재: {DB_PATH}")
    print(f"[입력] {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    try:
        series = load_series(conn)
        print(f"[load] 13 변수 × 80 분기 적재 완료")

        n1 = write_long_form(conn, series)
        print(f"[§4.1.1] {OUT_SERIES} — {n1} 행")
        assert n1 == 1040, f"§4.1.1 행 수 비정상: {n1}"

        n2 = write_statistics(series)
        print(f"[§4.1.2] {OUT_STATS} — {n2} 행")
        assert n2 == 13

        n3 = write_trend(series)
        print(f"[§4.1.3] {OUT_TREND} — {n3} 행")
        assert n3 == 13

        n4, mm = write_ca_decomposition(series)
        print(f"[§4.1.4] {OUT_CA} — {n4} 행 (불일치 {mm} 건)")
        assert n4 == 80

        n5 = write_fa_share(series)
        print(f"[§4.1.5] {OUT_FA} — {n5} 행 (80 분기 + 3 요약)")
        assert n5 == 83
    finally:
        conn.close()

    print("\n[완료] 5 평면 CSV 산출 종료.")


if __name__ == "__main__":
    main()
