# db/data/_external/exchange_rates/

영국 거시경제학 보고서 단계 4 §4.3 환율–경상수지 검증을 위해 외부 출처에서
다운로드한 환율 4 종 raw 시계열 보관 폴더입니다. 본 영역은 `db/source/` 와 동일하게
**원본 보존 영역**으로 취급하며, 데이터 값을 변경·치환·반올림·재계산하지 않습니다.

## 보유 파일

| 파일 | 시계열 | 출처 | 시리즈 코드 | 주기 | 단위 | 시점 범위 | 라이선스 |
|---|---|---|---|---|---|---|---|
| `XUDLUSS_daily.csv` | GBP/USD spot (Sterling into US dollar) | Bank of England — IADB | XUDLUSS | 일별(영업일) | USD per GBP, 4pm London middle market | 2006-01-03 ~ 2025-12-31 | Open Government Licence v3.0 |
| `XUDLERS_daily.csv` | GBP/EUR spot (Sterling into Euro) | Bank of England — IADB | XUDLERS | 일별(영업일) | EUR per GBP, 4pm London middle market | 2006-01-03 ~ 2025-12-31 | Open Government Licence v3.0 |
| `XUDLBK67_daily.csv` | Sterling Effective Exchange Rate Index (BoE ERI) | Bank of England — Sterling ERI | XUDLBK67 | 일별(영업일) | Index (Jan 2005 = 100) | 2006-01-03 ~ 2025-12-31 | Open Government Licence v3.0 |
| `eurostat_ert_eff_ic_m_UK.tsv` | UK 환율 효과 지수 10 시리즈(NEER·REER × 5 partner group) | Eurostat — ert_eff_ic_m | M.{NEER\|REER}_{IC42\|IC37\|EU27_2020\|EA20\|EA21}.I15.UK | 월별 | Index (2015 = 100) | 2006-01 ~ 2026-02 | © European Union, [Eurostat 사용약관](https://ec.europa.eu/eurostat/about-us/policies/copyright) |

## 다운로드 출처 URL·접근 일시·HTTP 응답

본 적재는 모두 2026-04-29(UTC) 본 저장소 환경에서 직접 HTTPS 요청으로 수행했다.

- BoE IADB CSV(3 시리즈):
  `https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=01/Jan/2006&Dateto=31/Dec/2025&SeriesCodes={CODE}&CSVF=TN&UsingCodes=Y&VPD=Y&VFD=N`
  → 200 OK, `application/csv`, 5054 행/각.
- Eurostat SDMX 2.1 dissemination API(REER 4 + NEER 4 시리즈, UK 행만 필터 후 저장):
  `https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/ert_eff_ic_m?format=tsv&geo=UK&startPeriod=2006-01`
  → 200 OK, `text/tsv`. UK 행 10개 추출 후 헤더 + 본 행만 저장.

## BIS RB.M.GB(Real Broad EER, CPI deflated, 2020 = 100) 시도 결과

09_external_sources.md §1 에서 1차 출처로 식별한 **BIS RB.M.GB** 는 본 환경에서
다음 4 endpoint 모두 직접 다운로드 실패(WinError 10060 timeout / connection reset)
했다.

| Endpoint | 결과 |
|---|---|
| `https://stats.bis.org/api/v1/data/WS_EER/M.R.B.GB?format=csv` | timeout |
| `https://data.bis.org/static/eer/eer_m_b_r_GB.csv` | timeout |
| `https://fred.stlouisfed.org/graph/fredgraph.csv?id=RBGBBIS` | timeout |
| `https://fred.stlouisfed.org/graph/fredgraph.csv?id=NBGBBIS` | timeout |

본 환경에서 외부 도메인 차단 정책이 BIS 및 FRED 도메인을 막고 있는 것으로 보인다.
보고서 단계 4 §4.3 본문은 09_external_sources.md §1 가 권고한 BIS REER 대신
**Eurostat REER_IC42_CPI(2015 = 100)** 를 broad REER 대용으로 사용한다.
두 시리즈는 (i) 모두 broad partner group(BIS 64 ↔ Eurostat 42) (ii) CPI deflator
(iii) 가중치 무역 가중 — 동일 개념의 다른 가중치·기준연도 정의이므로 **수준값(level)
은 직접 비교 불가**하지만 **변화율·상관 분석** 에는 BIS 와 동등 사용 가능하다.
보고서 단계 5 §7 한계 절에 본 대체 사실을 명시할 것.

## 가공 산출물(파생 통계)은 보관하지 않음

`db/data/_external/exchange_rates/` 는 raw 보존 영역이므로 분기 평균·상관계수 등 파생
산출물은 본 폴더에 두지 않는다. 분기 평균 4 시리즈(80 분기) 와 §4.3.2~§4.3.5 분석
결과는 다음 위치에 산출했다.

- `report/data/exchange_rates_quarterly_2006q1_2025q4.csv` — 분기 평균 4 시리즈
- `report/data/fx_correlation_2006q1_2025q4.csv`           — 단순 상관(§4.3.2)
- `report/data/fx_lag_correlation_2006q1_2025q4.csv`        — 시차 상관(§4.3.3)
- `report/data/fx_regression_2006q1_2025q4.csv`            — 차분 회귀(§4.3.4)
- `report/data/fx_case_study_2006q1_2025q4.csv`            — 사례 분석(§4.3.5)

## 재현 스크립트

- 다운로드: `db/code/source/build_exchange_rate_quarterly.py` 에서 직접 호출하지 않으며,
  본 README §"다운로드 출처 URL" 의 4 endpoint 를 그대로 호출하면 동일 raw csv 가 재생성된다.
- 분기 평균 산출: `db/code/source/build_exchange_rate_quarterly.py`
- 분석(§4.3.2~§4.3.5): `db/code/source/analyze_fx_ca.py`

모든 실행은 `env/Scripts/python.exe` 가상환경 인터프리터로 수행한다(루트 CLAUDE.md
"Python 개발 환경" 절 준수).
