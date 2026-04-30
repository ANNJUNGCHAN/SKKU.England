# 13. 단계 4 §4.4 그래프 산출 — 7 항목 일괄 결과

> 분석 기간 2006Q1~2025Q4(80 분기). 본 문서는 단계 4 정량 분석 §4.4 의 7 항목(§4.4.1
> CA 합계 라인 / §4.4.2 CA 4 세부항목 비교 라인 / §4.4.3 FA 5 세부항목 누적 막대 +
> 합계 라인 / §4.4.4 BoP 항등식 잔차 라인 / §4.4.5 환율×CA 산점도 / §4.4.6 환율×BOKI
> 이중축 라인 / §4.4.7 그래프↔source CSV 매핑 README)을 일괄 산출한 결과를 보고한다.
> 모든 그래프는 단계 4 §4.1~§4.3 산출 CSV 의 값을 **그대로** 시각화했으며, 어떠한
> 환산·반올림·치환·보간도 적용하지 않았다(`db/data/CLAUDE.md` 가공 원칙 1번 준수).

---

## §1. 그래프 6건 인덱스

| 번호 | 그래프 PNG | 데이터 source CSV (1:1 동봉) | 사양 요약 |
|---|---|---|---|
| §4.4.1 | `report/figures/fig01_ca_quarterly.png` | `report/figures/fig01_data.csv` | CA 합계(HBOP) 분기 시계열 라인 + 0선 점선 + 충격 분기 5건(2008Q4·2016Q3·2020Q2·2022Q3·2025Q4) 빨강 점·라벨 |
| §4.4.2 | `report/figures/fig02_ca_components.png` | `report/figures/fig02_data.csv` | CA 4 세부항목(BOKI·IKBD·HBOJ·IKBP) 분기 시계열 비교 라인 + 0선 + 4 색 범례 |
| §4.4.3 | `report/figures/fig03_fa_components.png` | `report/figures/fig03_data.csv` | FA 5 세부항목(-MU7M·-HHZD·-ZPNN·-HHYR·-LTCV) 부호별 누적 막대 + 합계(-HBNT) 라인 오버레이 |
| §4.4.4 | `report/figures/fig04_identity_residual.png` | `report/figures/fig04_data.csv` | BoP 항등식 잔차 라인 + 0선 + ±1σ·±2σ 점선 + 2σ 밖 분기 빨강 강조 |
| §4.4.5 | `report/figures/fig05_fx_ca_scatter.png` | `report/figures/fig05_data.csv` | 환율×CA 산점도 2×2 grid (GBP/USD·Sterling ERI × lag 0·4) + 패널별 r |
| §4.4.6 | `report/figures/fig06_fx_boki_dual_axis.png` | `report/figures/fig06_data.csv` | 상·하 2 패널 — (A) BOKI 좌축 × GBP/USD 우축, (B) BOKI 좌축 × Sterling ERI 우축 + 변곡점 4 분기 수직 점선 |

§4.4.7 — 같은 폴더의 `report/figures/README.md` 가 그래프 6 ↔ source CSV 6 매핑 + 1차
출처 + 재현 절차 표를 정리한다(본 문서 §3 과 일관).

---

## §2. 각 그래프 사양·해석 한국어 단락

### 2.1 §4.4.1 — CA 합계(HBOP) 분기 시계열 라인 차트

**사양**

- 입력: `report/data/quarterly_series_2006q1_2025q4.csv` 중 `cdid == 'HBOP'` 80 행.
- 단위: GBP million (ONS Table A 부표 1 표시 부호 그대로).
- 그래프 요소: 본 라인(짙은 청, 1.6 pt) + 0선 회색 점선 + 충격 5 분기 빨강 점(s=55,
  zorder=5) + 4 px 오프셋 라벨.
- X 축: 8 분기 간격 + 마지막 분기(2025Q4) tick.

**해석**

- 80 분기 모두 적자(HBOP < 0). 평균 약 -16.0 억 GBP/분기, 표준편차 7.3 억 GBP/분기 수준.
- **2016Q3 = -32,707 GBP million** 으로 80 분기 최대 적자(슬라이드 17·18 Brexit
  국민투표 직후 분기와 일치).
- **2020Q2 = -8,224 GBP million** 코로나 1차 봉쇄 분기로 적자가 일시적으로 축소
  (수입 급감 효과). **2022Q3 = -2,431 GBP million** 은 80 분기 중 최저 적자(에너지
  가격 충격 + 본원소득 흑자 일시 확대).
- **2025Q4 = -18,392 GBP million** 으로 직전 분기 대비 재확대.
- 충격 5건 중 2008Q4·2016Q3·2025Q4 는 평균선 이하(악화), 2020Q2·2022Q3 은 평균선
  이상(개선) 으로 구분된다.

### 2.2 §4.4.2 — CA 4 세부항목 분기 시계열 비교 라인

**사양**

- 입력: `quarterly_series_2006q1_2025q4.csv` 중 `cdid in {BOKI, IKBD, HBOJ, IKBP}` 4×80 = 320 행.
- 색상: BOKI 빨강 / IKBD 녹색 / HBOJ 청 / IKBP 보라 (각 1.5 pt).
- 사이즈: 11×5.5 in, dpi 150, ncol=2 범례.

**해석**

- **BOKI(상품수지)**: 80 분기 모두 음수. 2006Q1 -20.9 → 2016Q3 -49.3 → 2025Q4
  -65.5 GBP billion 수준의 만성 적자 + 시간 추세 악화.
- **IKBD(서비스수지)**: 80 분기 모두 양수. 2006Q1 +11.5 → 2025Q4 +53.3 GBP billion 수준
  의 구조적 흑자 + 추세 확대(BOKI 적자 부분 상쇄).
- **HBOJ(본원소득)**: 80 분기 평균 약 -3 GBP billion. 2020Q4·2022Q3·2024Q4 등 일부
  분기에서 +10~+30 GBP billion 일시 흑자(다국적 기업 송금·환차익) 발생.
- **IKBP(이전소득)**: 80 분기 모두 음수, 평균 -3.6 GBP billion 수준. 변동성 가장 작음.
- 슬라이드 14 항등식 `CA = BOKI + IKBD + HBOJ + IKBP` 가 모든 분기에서 만족(잔차 0,
  단계 4 §4.1.4 검증 결과).

### 2.3 §4.4.3 — FA 합계(-HBNT) + 5 세부항목 누적 막대 + 합계 라인

**사양**

- 입력: `quarterly_series_2006q1_2025q4.csv` 중 `cdid in {-MU7M, -HHZD, -ZPNN, -HHYR, -LTCV, -HBNT}` 6×80 = 480 행.
- 부호 분리 누적 막대: 양수는 0 위로, 음수는 0 아래로 동일 색상 누적.
- 합계 라인: -HBNT 검정 1.6 pt zorder=10 (막대 위 오버레이).
- 사이즈: 12×5.5 in.

**해석**

- 5 세부항목의 누적 막대 합과 합계 라인(-HBNT) 이 매 분기 시각적으로 일치 — 슬라이드
  21 항등식 `-HBNT = -MU7M + -HHZD + -ZPNN + -HHYR + -LTCV` 검증.
- **증권투자(-HHZD)** 와 **기타투자(-HHYR)** 가 분기 변동성 대부분을 견인. 2008Q3
  (글로벌 금융위기 직전) 양 항목 진폭이 ±150 GBP billion 으로 80 분기 최대.
- **준비자산(-LTCV)** 는 평균 ±2 GBP billion 수준으로 누적 막대에서 거의 보이지
  않는다(영국이 변동환율제·외환보유액 적극 운용 안 함, 슬라이드 22).
- **합계 라인(-HBNT)** 80 분기 평균 -19 GBP billion (FA 음수 = 자본 순수출, slide 21
  부호 규약).

### 2.4 §4.4.4 — BoP 항등식 잔차 분기 라인 차트

**사양**

- 입력: `report/data/identity_residual_2006q1_2025q4.csv` 80 행 `residual` 컬럼.
- 잔차 정의: `CA(HBOP) + KA(FNVQ) + FA(-HBNT) + NEO(HHDH)` (단계 4 §4.2 Table A 부호
  그대로 합산).
- 정상 분포: 평균 -35,777 GBP million, SD 23,663 GBP million (n=80).
- 강조선: ±1σ 회색 점선, ±2σ 빨강 파선.
- 빨강 점: |z| > 2 분기 — 본 데이터 산출 결과 **3 분기**.

**해석 — 사용자 사양 대비 데이터 실측 차이**

- 사용자 §4.4.4 사양은 "**2σ 밖 2분기(2016Q3·2022Q4)**" 강조였으나, 본 데이터에서
  실제 |z| > 2 인 분기는 **3 분기 — 2011Q1(z = +2.179) · 2016Q3(z = -2.609) ·
  2022Q4(z = +2.232)** 였다. `db/data/CLAUDE.md` 가공 원칙 1번에 따라 데이터 값을
  임의로 누락·치환할 수 없으므로 **3 분기 모두 강조 표시했고**, 본 §에서 사용자
  사양과의 차이를 명시한다.
- 2011Q1 잔차 +15,757 = 평균(-35,777) + 2.18·SD(23,663) 조건을 만족. 2σ 임계 밖이
  맞는 분기이며, 단계 4 §4.2.3 충격 분기 식별 표(`identity_shock_position` CSV)
  에는 GFC 그룹 마지막에서 1년 떨어진 시점이라 사전 등록되지 않았을 뿐이다.
- 2016Q3 -94,925 (Brexit 직후 FA 급반등) · 2022Q4 +16,989(에너지 위기 본원소득 흑자)
  는 슬라이드 17·19 표본 충격 시기와 일치한다.
- 평균 잔차 -35,777 는 0 이 아니므로 **순오차누락(NEO) 의 구조적 비대칭성**(영국
  통계청이 분기 잠정치를 음 방향으로 추정하는 회계 관행) 을 시사한다 — 단계 4 §4.2
  결론과 일관.

### 2.5 §4.4.5 — 환율 vs CA 산점도 (2×2 grid)

**사양**

- 입력: `quarterly_series_2006q1_2025q4.csv` (HBOP) + `exchange_rates_quarterly_2006q1_2025q4.csv`
  (gbp_usd, sterling_eri_jan2005_100), 80 분기 정합 확인.
- 4 패널: ① GBP/USD × HBOP lag 0 ② GBP/USD × HBOP lag 4 ③ Sterling ERI × HBOP
  lag 0 ④ Sterling ERI × HBOP lag 4. lag 4 패널은 환율(t) → CA(t+4) 4 분기 후 시차.
- 각 패널 제목에 Pearson r 표기.

**해석**

- **GBP/USD lag 0**: r = +0.133 (n=80). 약한 양의 관계 — 파운드 강세 시점에 CA 가
  약간 덜 악화되는 패턴 (J-곡선 효과 반대 방향, 단기 가격 효과 우세).
- **GBP/USD lag 4**: r = +0.037 (n=76). 시차 4 분기 후에도 거의 무상관 — 양자환율은
  CA 의 선행 지표로 약함.
- **Sterling ERI lag 0**: r = -0.025 (n=80). 무상관 수준.
- **Sterling ERI lag 4**: r = -0.082 (n=76). 약한 음의 관계 — 무역가중 실효환율 강세
  4 분기 후 CA 다소 악화 (J-곡선 음 효과). 단계 4 §4.3.3 시차 상관 표와 일치.
- 결론: 4 패널 모두 |r| < 0.15 로 단순 산점도 수준에서는 환율 → CA 단방향 관계가
  강하지 않다. 단계 4 §4.3.4 차분 회귀 결과(가격탄력성 통계적 유의)는 산점도가 아닌
  Δlog 차분에서 비로소 나타난다.

### 2.6 §4.4.6 — BOKI 좌축 + GBP/USD·Sterling ERI 우축 이중축 라인

**사양**

- 입력: `quarterly_series_2006q1_2025q4.csv` (BOKI) + `exchange_rates_quarterly_2006q1_2025q4.csv`
  (gbp_usd, sterling_eri_jan2005_100).
- 시각화 구조: 상·하 2 패널 (sharex). 패널 (A) BOKI 좌축 × GBP/USD 우축, 패널 (B)
  BOKI 좌축 × Sterling ERI 우축. 양자/실효 환율을 ÷50 같은 인위 스케일링 없이
  각자 독립 축으로 표시한다.
- 변곡점: 2008Q4·2016Q3·2022Q3·2025Q4 4 분기 수직 회색 점선 + 라벨.

**해석**

- (A) **GBP/USD 우축**: 2007Q3 약 2.05 → 2008Q4 1.57 → 2009Q1 1.43(GFC 파운드 급락)
  → 2014Q3 1.66 회복 → 2016Q3 1.31(Brexit) → 2022Q3 1.18(에너지 위기) → 2025Q4 1.30
  수준. BOKI 는 같은 기간 -20.9 → -65.5 GBP billion 으로 만성 악화 추세.
- (B) **Sterling ERI 우축**: GBP/USD 와 유사 패턴이나 변동폭이 작다(다자 가중 평균).
  2007Q3 105 → 2008Q4 84 → 2016Q4 78 → 2022Q3 81 → 2025Q4 78.
- 환율 변곡점(파운드 약세) 직후 BOKI 가 즉시 개선되지는 않는다 — 환율 통과 효과
  (pass-through) 는 반응 시차 4 분기 이상이며 단계 4 §4.3.5 사례 분석과 일관.
- 만성 BOKI 적자 추세는 환율보다 구조적 무역 패턴(소비재·중간재 수입 의존, 슬라이드
  6 lecture note 02 §4) 에 더 크게 좌우됨을 시사.

---

## §3. 데이터 source 1:1 매핑 표

| 그래프 | source CSV (`report/figures/`) | 1차 source (`report/data/`) | 추출 컬럼 | 행 수 | 1차 출처(원자료) |
|---|---|---|---|---|---|
| §4.4.1 fig01 | `fig01_data.csv` | `quarterly_series_2006q1_2025q4.csv` | `cdid==HBOP` → `time, data_value` | 80 | ONS Balance of Payments 2025 Q4, Table A 부표 1 (CDID=HBOP, GBP million) |
| §4.4.2 fig02 | `fig02_data.csv` | `quarterly_series_2006q1_2025q4.csv` | `cdid in {BOKI, IKBD, HBOJ, IKBP}` 4×80 | 80 | ONS BoP 2025 Q4, Table A 부표 1 |
| §4.4.3 fig03 | `fig03_data.csv` | `quarterly_series_2006q1_2025q4.csv` | `cdid in {-MU7M, -HHZD, -ZPNN, -HHYR, -LTCV, -HBNT}` 6×80 | 80 | ONS BoP 2025 Q4, Table A 부표 3 (FA 5 기능별 + 합계, 부호 반전 표시) |
| §4.4.4 fig04 | `fig04_data.csv` | `identity_residual_2006q1_2025q4.csv` | `time, residual` (+ z_score, abs_z_gt2 파생) | 80 | 단계 4 §4.2 산출물 (`CA(HBOP) + KA(FNVQ) + FA(-HBNT) + NEO(HHDH)` 잔차) |
| §4.4.5 fig05 | `fig05_data.csv` | `quarterly_series_2006q1_2025q4.csv` + `exchange_rates_quarterly_2006q1_2025q4.csv` | HBOP, gbp_usd, sterling_eri_jan2005_100 (lag 0: 80 행, lag 4: 76 행, 합 156) | 156 | ONS BoP + Bank of England IADB (XUDLUSS, XUDLBK67) |
| §4.4.6 fig06 | `fig06_data.csv` | `quarterly_series_2006q1_2025q4.csv` + `exchange_rates_quarterly_2006q1_2025q4.csv` | BOKI, gbp_usd, sterling_eri_jan2005_100 (3 컬럼) | 80 | ONS BoP Table A 부표 1 + Bank of England IADB |

### 3.1 출처 인용(보고서 §1·§2 등재 형식)

- **ONS Balance of Payments 2025 Q4** — Office for National Statistics, *Balance of
  Payments: statistical bulletin tables*, balanceofpayments2025q4.xlsx, Table A 부표
  1·3, https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsstatisticalbulletintables,
  Open Government Licence v3.0.
- **Bank of England IADB** — Interactive Database, 시리즈 XUDLUSS(GBP/USD spot)·
  XUDLBK67(Sterling ERI, Jan 2005=100), https://www.bankofengland.co.uk/boeapps/database/,
  Open Government Licence v3.0. 분기 평균은 일별 영업일 산술 평균(09_external_sources.md
  방법 B).

### 3.2 재현 명령

```bat
c:\Projects\SKKU.England\env\Scripts\python.exe c:\Projects\SKKU.England\report\code\quantitative_4_4.py
```

- matplotlib backend = `Agg` 강제(GUI 없이 PNG 저장).
- 한국어 폰트 자동 선택: Malgun Gothic 우선 → 미설치 환경에서 NanumGothic·Noto Sans
  CJK KR·AppleGothic 후보 자동 폴백.
- `axes.unicode_minus = False` 로 마이너스 부호 깨짐 방지.
- 입력 CSV 값은 **수정·치환·반올림·환산 금지** — 시각화·재배치만 적용.
- PNG 1건당 같은 폴더의 `figXX_data.csv` 1건이 1:1 동봉되어 추적성 보장.

### 3.3 의존성 추가 안내(matplotlib 도입)

본 §4.4 7 항목 산출을 위해 가상환경(`env/`)에 **matplotlib 3.10.9** 와 그 의존
패키지(numpy 2.4.4, contourpy 1.3.3, cycler 0.12.1, fonttools 4.62.1, kiwisolver
1.5.0, packaging 26.2, pyparsing 3.3.2, python-dateutil 2.9.0, six 1.17.0) 를
2026-04-29 신규 설치하고 `c:/Projects/SKKU.England/requirements.txt` 에 즉시
동기화했다(`CLAUDE.md` Python 개발 환경 §3 준수). 향후 단계 4·5 신규 그래프 산출에서도
이 1 회 설치 결과를 그대로 활용한다.

---

## §4. 단계 4 §4.5 마감 인계

§4.4 7 항목(그래프 6 + README 1) 일괄 마감으로 단계 4 정량 분석 절은 §4.1 분기
시계열 적재 → §4.2 항등식 잔차 → §4.3 환율–CA 상관·회귀·사례 → **§4.4 그래프 산출**
4 절을 모두 완료했다. 다음 §4.5 단계 4 정량 결과 종합·단계 5 인계 작업에 다음 산출을
사용한다.

| 인계 대상 | 인계 산출물 | §4.5 활용 방향 |
|---|---|---|
| 단계 5 §1 헤드라인 | `fig01_ca_quarterly.png` + `fig01_data.csv` | CA 만성 적자·충격 분기 해설 표지용 |
| 단계 5 §2 BOKI vs IKBD 구조 분석 | `fig02_ca_components.png` | 슬라이드 6·14 강의 정의와 연결한 구조 도해 |
| 단계 5 §3 FA 변동성 | `fig03_fa_components.png` | -HHZD·-HHYR 진폭 수치 결합 |
| 단계 5 §4 항등식 한계·NEO 비대칭 | `fig04_identity_residual.png` | 평균 -35,777 + 3 분기 |z|>2 강조 |
| 단계 5 §5 환율 통과 효과 한계 | `fig05_fx_ca_scatter.png` + `fig06_fx_boki_dual_axis.png` | r·시차 + 사례 분기 정성 해설 |
| 단계 5 §7 한계 절 | 본 §2.4 사용자 사양 대비 데이터 차이(2 → 3 분기) | 항등식 잔차 정의·임계 기준 재고 |

본 문서는 단계 4 정량 분석 §4.4 의 모든 항목을 마감하며, 본 §의 PNG·CSV 12 파일은
단계 5 보고서 본문 인용 시 절대경로(`report/figures/...`) 그대로 인용한다.

---

## 5. 변경 이력

- **2026-04-29** — §4.4 7 항목 (그래프 6 PNG + 6 CSV + 1 README) 일괄 작성. matplotlib
  3.10.9 가상환경 신규 설치 + `requirements.txt` 동기화. fig04 강조 분기는 사용자 사양
  2 분기 대비 데이터 실측 3 분기로 산출(§2.4 명시).
