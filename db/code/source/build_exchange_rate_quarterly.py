"""환율 4 시리즈 분기 평균 산출 스크립트 (단계 4 §4.3.1).

입력 (모두 `db/data/_external/exchange_rates/` 하위):
- `XUDLUSS_daily.csv` — BoE GBP/USD spot (daily, GBP→USD)
- `XUDLERS_daily.csv` — BoE GBP/EUR spot (daily, GBP→EUR)
- `XUDLBK67_daily.csv` — BoE Sterling ERI (daily, Jan 2005 = 100)
- `eurostat_ert_eff_ic_m_UK.tsv` — Eurostat REER for UK (monthly, REER_IC42_CPI, 2015 = 100,
  BIS RB.M.GB 가 본 환경에서 직접 다운로드 차단되어 채택한 대용 시리즈)

산출 위치:
- `report/data/exchange_rates_quarterly_2006q1_2025q4.csv` — 80 행 wide form
  (time, gbp_usd, gbp_eur, sterling_eri, eurostat_reer_ic42)

산출 방법:
- BoE 일별 → 분기 내 모든 영업일 산술 평균(방법 B 변형: 일별 직접 산출).
  09_external_sources.md §2 권고 방법 A(월 working-day 평균 → 분기 단순 평균)는 BoE
  월별 시계열을 별도 다운로드해야 하므로 본 스크립트는 일별 산술 평균만 수행하며
  방법 A 와 결과 차이가 0.05% 미만이라는 안내(§2-2)를 동일하게 인용한다.
- Eurostat REER (월별) → 분기 내 3 개월 단순 평균(방법 A 그대로).

데이터 값 불변 원칙(`db/data/CLAUDE.md`)에 따라 원본 raw csv·tsv 는 그대로 두고,
분기 평균(파생 통계)은 `report/data/` 영역으로만 산출한다.
"""
from __future__ import annotations
import csv
import os
from collections import defaultdict
from datetime import datetime
from statistics import mean

ROOT = "C:/Projects/SKKU.England"
EXT = f"{ROOT}/db/data/_external/exchange_rates"
OUT = f"{ROOT}/report/data/exchange_rates_quarterly_2006q1_2025q4.csv"


def parse_boe_daily(path: str) -> list[tuple[datetime, float]]:
    """BoE IADB 일별 CSV 파싱.

    형식: ``DATE,<CODE>`` 헤더 + ``DD MMM YYYY,<value>`` 데이터행.

    Args:
        path: BoE IADB 다운로드 CSV 의 절대 경로.

    Returns:
        ``(datetime, float)`` 튜플의 리스트(영업일 순). 결측·헤더 행은
        조용히 건너뛴다(BoE 일별 자료에는 결측 행이 0건이므로 실질적으로
        모든 영업일이 그대로 보존된다).
    """
    rows: list[tuple[datetime, float]] = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # 첫 행은 헤더(`DATE,<CODE>`) 이므로 건너뜀
        for row in reader:
            # 빈 행·헤더 잔재·중간 빈 칸 방어 — 원본 셀 값을 변경하지 않고 단순 스킵
            if len(row) < 2 or not row[0].strip() or not row[1].strip():
                continue
            d = datetime.strptime(row[0].strip(), "%d %b %Y")
            try:
                v = float(row[1].strip())
            except ValueError:
                # 숫자로 파싱되지 않는 셀은 결측으로 간주하고 건너뛴다
                continue
            rows.append((d, v))
    return rows


def to_quarter(d: datetime) -> str:
    """``datetime`` → ``YYYYQn`` 분기 라벨 변환.

    1~3월=Q1, 4~6월=Q2, 7~9월=Q3, 10~12월=Q4 의 ONS·Eurostat 표준 분기 정의를
    따른다. 입력 ``d`` 는 본 저장소의 영업일 시계열 범위(2006-01-03 ~
    2025-12-31)를 가정한다.
    """
    q = (d.month - 1) // 3 + 1
    return f"{d.year}Q{q}"


def quarterly_mean_from_daily(daily: list[tuple[datetime, float]]) -> dict[str, float]:
    """일별 시계열을 분기 단위로 묶어 산술 평균(방법 B) 산출.

    09_external_sources.md §2 에서 권고한 두 방법 중 **방법 B(일별 직접 산출)**
    을 구현한다. 분기 내 모든 영업일 값을 단순 산술 평균하며 가중치는 부여하지
    않는다(공휴일·시장 휴장일은 BoE 자료 자체에 행이 없으므로 자연스럽게 제외).

    Args:
        daily: ``parse_boe_daily`` 의 반환값(영업일 순 (날짜, 값) 리스트).

    Returns:
        ``YYYYQn`` 분기 라벨 → 분기 평균 dict. 분기 내 자료가 한 건이라도 있으면
        해당 분기 키가 포함된다(80 분기 윈도우 전 구간에서 분기당 약 63 영업일
        보유).
    """
    bucket: dict[str, list[float]] = defaultdict(list)
    for d, v in daily:
        bucket[to_quarter(d)].append(v)
    return {q: mean(vs) for q, vs in bucket.items()}


def parse_eurostat_uk_reer(path: str, exch_rt: str = "REER_IC42_CPI") -> dict[str, float]:
    """Eurostat ert_eff_ic_m TSV → 월별 dict (YYYY-MM → value)."""
    with open(path, "r", encoding="utf-8") as f:
        header = f.readline().rstrip("\n")
        # 헤더 형식:
        #   freq,exch_rt,unit,geo\TIME_PERIOD<TAB>2006-01 <TAB>2006-02 ...
        first_cell, *months = header.split("\t")
        months = [m.strip() for m in months]
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if not parts:
                continue
            key = parts[0].strip()
            # key 형식: M,<exch_rt>,<unit>,<geo>
            tags = key.split(",")
            if len(tags) < 4:
                continue
            if tags[1] != exch_rt:
                continue
            if tags[3] != "UK":
                continue
            monthly: dict[str, float] = {}
            for m, raw in zip(months, parts[1:]):
                v = raw.strip()
                if not v or v == ":":
                    continue
                # Eurostat 일부 셀 끝에 플래그 문자(' p', ' e' 등) 존재
                v_clean = v.split(" ")[0]
                try:
                    monthly[m] = float(v_clean)
                except ValueError:
                    continue
            return monthly
    return {}


def quarterly_mean_from_monthly(monthly: dict[str, float]) -> dict[str, float]:
    """월별 dict 를 분기 평균으로 환산(방법 A 그대로).

    09_external_sources.md §2 의 **방법 A**(월별 자료 → 분기 내 3개월 단순 평균)
    를 구현한다. **분기 내 3개월이 모두 갖춰진 경우에만** 평균을 산출하고,
    부분 결측 분기는 결과 dict 에서 제외한다(빈 칸으로 보고). 결측 부분
    제외 정책은 `db/data/CLAUDE.md` 가공 원칙 1번(결측 표기 보존)을 따른다.

    Args:
        monthly: ``YYYY-MM`` → 월값 dict (Eurostat REER 의 월별 시계열).

    Returns:
        ``YYYYQn`` → 분기 평균 dict. 부분 결측(분기 내 3개월 미만) 분기는 누락.
    """
    bucket: dict[str, list[float]] = defaultdict(list)
    for ym, v in monthly.items():
        y, m = ym.split("-")
        q = (int(m) - 1) // 3 + 1
        bucket[f"{y}Q{q}"].append(v)
    # 분기 내 3개월이 모두 갖춰진 경우만 평균(부분 결측 분기 제외, 임의 보간 금지)
    return {q: mean(vs) for q, vs in bucket.items() if len(vs) == 3}


def quarter_iter(start: str, end: str):
    """``YYYYQn`` 라벨 시퀀스를 ``start`` 부터 ``end`` 까지 차례로 yield.

    예) ``quarter_iter("2006Q1", "2025Q4")`` → 2006Q1·2006Q2·…·2025Q4 = 80 라벨.
    분기 라벨 정렬을 (year, quarter) 튜플 비교로 처리해 문자열 정렬 함정을 피한다.
    """
    sy, sq = int(start[:4]), int(start[5])
    ey, eq = int(end[:4]), int(end[5])
    y, q = sy, sq
    while (y, q) <= (ey, eq):
        yield f"{y}Q{q}"
        q += 1
        if q > 4:
            q = 1
            y += 1


def main() -> None:
    """4 raw 시계열 → 분기 wide CSV 산출 메인 절차.

    절차:
        1. BoE 3 일별 CSV(USD/EUR/ERI) 와 Eurostat 월별 TSV 를 각각 파싱.
        2. BoE 시리즈는 방법 B(일별 산술 평균), Eurostat REER 은 방법 A
           (월 → 분기 단순 평균) 로 분기 평균 산출.
        3. 2006Q1~2025Q4 80 분기 라벨을 순회하며 4 컬럼 wide CSV 1개를 작성.
        4. 콘솔에 산출 행 수·완전 적재 행 수·시작/종료 분기 표본을 출력해
           멱등 재실행 시 대조할 수 있게 한다.

    Side Effects:
        ``OUT`` 경로(``report/data/exchange_rates_quarterly_2006q1_2025q4.csv``)
        를 새로 작성한다(기존 파일 덮어쓰기, 멱등 재실행 가능).
    """
    usd_daily = parse_boe_daily(f"{EXT}/XUDLUSS_daily.csv")
    eur_daily = parse_boe_daily(f"{EXT}/XUDLERS_daily.csv")
    eri_daily = parse_boe_daily(f"{EXT}/XUDLBK67_daily.csv")
    reer_monthly = parse_eurostat_uk_reer(
        f"{EXT}/eurostat_ert_eff_ic_m_UK.tsv", "REER_IC42_CPI"
    )

    usd_q = quarterly_mean_from_daily(usd_daily)
    eur_q = quarterly_mean_from_daily(eur_daily)
    eri_q = quarterly_mean_from_daily(eri_daily)
    reer_q = quarterly_mean_from_monthly(reer_monthly)

    quarters = list(quarter_iter("2006Q1", "2025Q4"))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        # 헤더 — 컬럼 의미·단위는 동반 메모(`exchange_rates_quarterly_2006q1_2025q4.md`)
        # 의 "컬럼" 표를 참조. 결측은 빈 셀로 두며 임의로 0/NA 치환하지 않는다.
        w.writerow([
            "time",
            "gbp_usd",
            "gbp_eur",
            "sterling_eri_jan2005_100",
            "eurostat_reer_ic42_cpi_2015_100",
        ])
        for q in quarters:
            # 분기별 4 시리즈 평균 적재. 분기에 자료가 없으면 빈 문자열 셀.
            # `q in usd_q` 분기 가드가 먼저 평가되므로 `:.6f` 포맷이 빈 문자열에
            # 적용될 가능성은 없다(가독성 보강을 위한 인라인 주석).
            w.writerow([
                q,
                f"{usd_q[q]:.6f}" if q in usd_q else "",
                f"{eur_q[q]:.6f}" if q in eur_q else "",
                f"{eri_q[q]:.6f}" if q in eri_q else "",
                f"{reer_q[q]:.6f}" if q in reer_q else "",
            ])

    n_full = sum(
        1
        for q in quarters
        if q in usd_q and q in eur_q and q in eri_q and q in reer_q
    )
    print(f"saved {OUT}  rows={len(quarters)} full_rows={n_full}")
    print(f"  usd_q={len(usd_q)}  eur_q={len(eur_q)}  eri_q={len(eri_q)}  reer_q={len(reer_q)}")
    print(f"  sample 2006Q1: usd={usd_q.get('2006Q1')} eur={eur_q.get('2006Q1')} "
          f"eri={eri_q.get('2006Q1')} reer={reer_q.get('2006Q1')}")
    print(f"  sample 2025Q4: usd={usd_q.get('2025Q4')} eur={eur_q.get('2025Q4')} "
          f"eri={eri_q.get('2025Q4')} reer={reer_q.get('2025Q4')}")


if __name__ == "__main__":
    main()
