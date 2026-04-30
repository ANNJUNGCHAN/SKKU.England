# exchange_rates_quarterly_2006q1_2025q4.csv

영국 거시경제학 보고서 단계 4 §4.3.1 산출물. 환율 4 시리즈의 2006Q1~2025Q4 분기 평균
시계열 80 행 wide form.

## 컬럼

| 컬럼 | 시계열 | 단위 | 산출 방법 | 1차 출처 |
|---|---|---|---|---|
| `time` | 분기 라벨 | YYYYQn | — | — |
| `gbp_usd` | GBP/USD spot 분기 평균 | USD per GBP | 일별 4pm London middle market 의 분기 내 영업일 산술 평균 | BoE IADB **XUDLUSS** |
| `gbp_eur` | GBP/EUR spot 분기 평균 | EUR per GBP | 일별 4pm London middle market 의 분기 내 영업일 산술 평균 | BoE IADB **XUDLERS** |
| `sterling_eri_jan2005_100` | Sterling ERI 분기 평균 | Index, Jan 2005 = 100 | 일별 ERI 의 분기 내 영업일 산술 평균 | BoE **XUDLBK67** (Sterling ERI) |
| `eurostat_reer_ic42_cpi_2015_100` | UK Real EER (CPI deflated, 42 industrial partners) 분기 평균 | Index, 2015 = 100 | 월별 데이터의 분기 내 3 개월 단순 평균(방법 A) | Eurostat **ert_eff_ic_m**, M.REER_IC42_CPI.I15.UK |

## 분기 평균 산출 방법

- BoE 3 시리즈(USD/EUR/ERI) 는 일별 영업일 자료가 본 환경에서 정상 다운로드되어
  09_external_sources.md §2 의 **방법 B**(일별 산술 평균) 로 분기 평균을 산출했다.
  방법 A(월 working-day 평균 → 분기 단순 평균) 와의 차이는 §2-2 안내대로 0.05% 미만이
  일반적이며, 2008Q4·2016Q3·2022Q3 등 변동성 분기에서는 0.2%p 이상 벌어질 수 있다.
- Eurostat REER 은 월별 자료만 발표되므로 **방법 A** 그대로 분기 내 3개월 단순 평균을
  취했다.
- BoE 일별 데이터에는 결측이 없으며(2006-01-03 ~ 2025-12-31, 5053 영업일 + 헤더),
  본 시점 윈도우에 분기당 평균 약 63 영업일이 모두 포함된다.

## BIS RB.M.GB 대체 안내

09_external_sources.md §1 표 4번 1차 출처로 식별한 **BIS RB.M.GB**(Real Broad EER, CPI
deflated, 2020 = 100) 는 본 환경에서 BIS data API(`stats.bis.org`, `data.bis.org`)
및 FRED 미러(`fred.stlouisfed.org/RBGBBIS`) 모두 timeout 으로 직접 다운로드에 실패했다
(자세한 시도 로그: `db/data/_external/exchange_rates/README.md`).

본 산출물은 BIS REER 대용으로 **Eurostat REER_IC42_CPI(2015 = 100)** 를 채택한다.
두 시리즈 모두 broad partner group(64 vs 42) + CPI deflator + 무역 가중 평균
이라는 동일 개념을 공유하지만 **기준연도와 가중치 정의가 달라 수준값(level)은 직접
비교가 불가**하다. 본 보고서에서는 (i) 변화율·차분, (ii) 분기 간 상관·회귀 분석에만
사용하며 보고서 단계 5 §7 한계 절에 본 대체 사실을 명시한다.

## 결측

- 본 산출물은 80 분기 모두 4 컬럼 전부 적재 완료(full_rows=80).
- 향후 갱신 시 일부 분기 월별 자료가 미발표일 경우 분기 평균을 빈 칸으로 두며
  `0`/`NA` 로 임의 치환하지 않는다(`db/data/CLAUDE.md` 가공 원칙 1번).

## 재현 스크립트

`db/code/source/build_exchange_rate_quarterly.py` (env/Scripts/python.exe 로 실행).
입력은 `db/data/_external/exchange_rates/` 의 raw csv·tsv 파일이며, 본 산출물 외에는
어떤 파일도 수정하지 않는다.

## 출처 인용 형식 (보고서 §1·§2 등재)

```text
GBP/USD spot, 분기 평균 — Bank of England, IADB 시리즈 XUDLUSS(일별 4pm 미들레이트),
  https://www.bankofengland.co.uk/boeapps/database/, 영업일 갱신,
  라이선스: Open Government Licence v3.0. 분기 평균은 일별 영업일 산술 평균(방법 B).
GBP/EUR spot, 분기 평균 — Bank of England, IADB 시리즈 XUDLERS, 동.
Sterling NEER (Sterling ERI), 분기 평균 — Bank of England, IADB 시리즈 XUDLBK67
  (Jan 2005 = 100), https://www.bankofengland.co.uk/statistics/sterling-exchange-rate-index,
  라이선스: Open Government Licence v3.0.
Sterling REER, 분기 평균 — Eurostat, ert_eff_ic_m, REER_IC42_CPI(2015 = 100, broad
  42 industrial partners), https://ec.europa.eu/eurostat/databrowser/view/ert_eff_ic_m,
  © European Union, Eurostat copyright. BIS RB.M.GB 직접 다운로드 차단으로 대체 채택.
```
