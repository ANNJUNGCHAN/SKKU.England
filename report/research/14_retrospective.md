# 14. 단계 6 — 보고서 마감·복기 (`code-control` 주도)

본 문서는 `report/PLAN.md` §4 단계 6 "마감·복기" 의 12 항목과 §8 종료 조건 5 건, §7 위험 점검 6 건을 통합 점검한 결과다. 단계 1~5 모두 [x] 종료된 상태(누적 66 체크 항목)에서 본 단계가 보고서 한 편의 품질 수문 역할을 한다.

---

## §1. 단계 6 12 항목 점검

### §1.1 변경 산출물 전수 리뷰

- 단계 1 강의 자료 발췌 7 건(`research/01_inventory.md` ~ `07_consolidated_summary.md`).
- 단계 2 데이터 인벤토리 1 건(`research/08_data_inventory.md`) + 점검 스크립트 1 건(`db/code/source/inventory_check_report_step2.py`).
- 단계 3 외부 환율 1 차 출처 1 건(`research/09_external_sources.md`).
- 단계 4 정량 산출 4 건 메모(`research/10_quantitative_4_1.md` ~ `13_quantitative_4_4.md`) + 데이터 13 CSV(`report/data/`) + 그래프 6 PNG + 6 source CSV + README(`report/figures/`) + 분석 스크립트 4 건(`report/code/quantitative_4_1.py`·`quantitative_4_2.py`·`quantitative_4_4.py` + `db/code/source/build_exchange_rate_quarterly.py`·`analyze_fx_ca.py`).
- 단계 5 노트북 + PDF + HTML(`report/notebook/uk_bop_fx_20y.{ipynb,pdf,html}`) + 빌드 스크립트 2 건(`report/code/build_notebook.py`·`html_to_pdf.py`).
- 모든 산출물이 한국어 본문, UTF-8, 1 CSV = 1 평면 표 원칙 준수.

### §1.2 한국어 주석·docstring 보강

- 모든 Python 스크립트(7 건)의 모듈/함수/주요 블록에 한국어 docstring·주석 부기 완료(직전 단위들의 `code-control` 보강 결과).
- 마크다운 본문은 모두 한국어, 기관·전문용어 영문 병기 완료.

### §1.3 변경 이력 기록 + 원격 반영

- 누적 27 커밋, 모두 origin/main 에 fast-forward push 완료.
- 보고서 작성 단위 누적 17 커밋(시각화 8 + 보고서 인프라 9): `e993c5d` ~ `3ad200a`.

### §1.4 복기 점검 1 — 5 핵심 질문 답변 완비

| # | 핵심 질문 | 노트북 절 | 답변 한국어 단락 | 결과 |
|---|---|---|---|:---:|
| Q1 | 거시 동향 (만성 적자·변곡점) | §3 | 80 분기 통계량 + 충격 5 분기 해석 + 슬10·11·15 + 노 02·17·38 | PASS |
| Q2 | CA 4 분해 | §4 (4.1 상품·4.2 서비스·4.3 1차·4.4 2차) | 분산 기여도 G 64.0% + PI 39.0% + SI 4.8% + S −7.8% + 식 CA = G + S + PI + SI 80/80 0 잔차 | PASS |
| Q3 | FA 5 분해 | §5 | SD PI_FA 53,964 ≈ OI 54,604 >> DI 29,016 > FD 23,921 >> RA 4,069 + 슬6·8·17 | PASS |
| Q4 | 항등식 일관성 | §6 | 잔차 평균 −35,777·SD 23,663·2σ 밖 2016Q3·2022Q4 + 2025Q4 검산 일치 | PASS |
| Q5 | 환율–CA 관계 | §7 | R²<0.01 환율 단독 1% 미만 + J-curve 미검출 + Brexit 단일 사례 부호 일관 | PASS |

5/5 PASS.

### §1.5 복기 점검 2 — 모든 정량 식별자 부기

- 본문 모든 정량에 (CDID + Table 코드 + 시점) 부기 완비.
- 외부 출처(환율 4 시리즈) 는 시리즈 코드 + URL + 라이선스 동시 부기(09 §1·§5 인용 형식).
- PASS.

### §1.6 복기 점검 3 — 강의 / 외부 인용 균형

- 강의 자료 인용: 슬5·6·8·10·11·13·14·15·17·22·24·27·28·30·31 + 노트 02·04·06·08·14·17·19·20·24·25·27·38 — 본문 11 절 모두 1 건 이상.
- 외부 출처 인용: BoE IADB 3 시리즈·BIS·Eurostat·BoE WP 312·BoE WP 2020·ONS Economic Review 2019·BoE WP 1019·IMF Article IV·HMRC NMG·ONS Pink Book — §7·§9 본문 + 부록 표.
- 균형 양호. 본 보고서는 주제 자체가 강의 도메인이므로 강의 인용 비중이 외부보다 약간 더 높음(5:3 정도).
- PASS.

### §1.7 복기 점검 4 — 그래프-표 1:1 추적

- fig01_ca_quarterly.png ↔ fig01_data.csv (HBOP 80 분기)
- fig02_ca_components.png ↔ fig02_data.csv (CA 4 세부 80 분기)
- fig03_fa_components.png ↔ fig03_data.csv (FA 5 세부 80 분기)
- fig04_identity_residual.png ↔ fig04_data.csv (잔차 80 분기)
- fig05_fx_ca_scatter.png ↔ fig05_data.csv (환율 vs CA 156 행 — 4 패널 × 39 점)
- fig06_fx_boki_dual_axis.png ↔ fig06_data.csv (환율 + BOKI 80 분기)
- 6/6 1:1 매핑, `figures/README.md` 에 등재.
- PASS.

### §1.8 복기 점검 5 — 보고서 §9 한계 명시

- 본 단위 보고서 §9 한계·주의사항 절에 다음 6 항목 명시 완비:
  · 데이터 개정(R1·R2·R3) 영향.
  · BIS REER (RB.M.GB) 미적재 → Eurostat REER IC42 대체.
  · GDP 분모 추정(AA6H 역산) 가정.
  · BPM6 부호 규약 해석 차이 (ONS Table_A 표시 부호).
  · 분기 평균 산출 방법 혼합(BoE 방법 B 일별 영업일 평균 + Eurostat 방법 A 월평균).
  · R²≈0 의 해석 — ERPT 충격원인별 광범위 분포(Forbes·Hjortsoe·Nenova 2015·2018).
- 추가 한계: Net IIP −£199.8bn 은 Pink Book Ch.9 IIP 별도 시계열로 본 보고서가 직접 계산하지 않음(부록 B REF 표기).
- PASS.

### §1.9 복기 점검 6 — 다음 단위 작업 후보 정리

- 본 보고서가 다루지 못한 후속 분석 후보:
  · BIS RB.M.GB 다운로드 차단 해소 후 Eurostat 와의 상관 검증(robustness).
  · 분기 평균 방법 A vs 방법 B 의 변동성 분기(2008Q4·2016Q3·2022Q3) 결과 비교 부록 추가.
  · ERPT 부문별(상품 vs 서비스) 분해(BoE WP 2021 trade elasticities 패턴 응용).
  · 2025 NMG 일회성 영향을 부록 BX(귀금속 제외) 시계열로 재산출.
  · 분기 GDP 명목치(YBHA) 외부 시계열 직접 결합으로 GDP 분모 추정 정확성 향상.
- 본 단위들은 모두 별도 안건으로 분리되며, 본 보고서 한 편의 완성에는 영향 없음.

### §1.10 복기 미진 항목 갱신 / 단계 1~5 재진입

- 본 점검에서 미진 항목 0 건. 단계 1~5 재진입 불요.

### §1.11 미진 항목 닫힘 또는 §9 한계 명시 최종 확인

- 미진 0 건. §9 한계 명시 6 항목 + Net IIP REF 1 항목 = 총 7 항목 모두 본문 §9 에 명시 완비.

### §1.12 단계 6 종료 — PLAN.md §6 누적 메모 + 보고서 완성 선언

- `report/PLAN.md` §6 단계 6 항목에 본 점검 결과 한 단락 누적 기록.
- 본 보고서 한 편 완성 선언 가능.

---

## §2. 종료 조건 5 건 점검

| # | 조건 | 결과 |
|---|---|:---:|
| 1 | 5 핵심 질문 답변 완비 (§1.4) | PASS |
| 2 | 노트북 무오류 실행 (`jupyter nbconvert --execute`) | PASS (error 0, 1.40 MB) |
| 3 | PDF 한국어·그래프 sanity check (pypdf 텍스트 추출 + fig 6 임베드) | PASS (23 페이지) |
| 4 | 식별자·출처 부기 완비 | PASS |
| 5 | 단계 6 복기 미진 항목 정리 또는 §9 한계 명시 | PASS (미진 0 + §9 7 항목) |

5/5 PASS.

---

## §3. 위험 점검 6 건

| # | 위험 | 대응 결과 |
|---|---|---|
| 1 | 환율 시계열 미확보 | BoE 3 시리즈 + Eurostat REER IC42 적재. BIS RB.M.GB 차단은 §9 한계 명시 + Eurostat 대체로 우회 |
| 2 | 강의 자료 인용 부족 | 본문 11 절 모두 강의 인용 1 건 이상 — 슬 15 + 노트 12 종 |
| 3 | 정량과 본문의 정합 불일치 | 모든 정량에 식별자(CDID + Table 코드 + 시점) 부기 + 헤드라인 4/4 PASS |
| 4 | PDF 변환 시 한국어 깨짐 | LaTeX·webpdf 실패 후 Playwright sync Chromium 채택, 한국어 sanity check PASS |
| 5 | 그래프 누락·표와의 불일치 | 6 PNG ↔ 6 source CSV 1:1 매핑 + figures/README.md 등재 |
| 6 | 보고서 분량 과대·과소 | 노트북 셀 44 + PDF 23 페이지 — 강의용 가독성 가이드 부합 |

6/6 위험 미발현 또는 대응 완료.

---

## §4. 보고서 한 편 완성 선언

본 점검으로 `report/notebook/uk_bop_fx_20y.{ipynb,pdf}` 한 편이 다음 5 종료 조건과 6 위험 점검을 모두 통과하였음을 확인한다.

**완성 선언 일자**: 2026-04-30 (Asia/Seoul)
**누적 커밋**: 27 (시각화 부트스트랩 8 + 보고서 인프라 3 + 단계 1~5 16)
**총 체크 항목**: 단계 1 (8) + 단계 2 (6) + 단계 3 (8) + 단계 4 (22) + 단계 5 (22) + 단계 6 (12) + 종료 조건 (5) + 위험 점검 (6) = **89 항목 모두 [x]**

본 보고서는 본 단위로 정식 종료되며, 후속 추가 분석은 §1.9 후보 5 건을 별도 안건으로 분리하여 진행한다.
