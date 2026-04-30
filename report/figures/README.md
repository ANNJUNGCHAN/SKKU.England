# `report/figures/` — 단계 4 §4.4 그래프 6건 + 데이터 source 6 CSV

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
c:\Projects\SKKU.England\env\Scripts\python.exe c:\Projects\SKKU.England\report\code\quantitative_4_4.py
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
