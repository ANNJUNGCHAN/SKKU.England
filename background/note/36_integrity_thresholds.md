# 36회차 — Phase 4.2 §8 무결성 점검 지표 임계 기준

본 노트는 `db/CHECKLIST.md` Phase 4.2 §8번([background-search] 무결성 점검 지표의 임계 기준에 대한 통계 일반론적 가이드 자문 요청) 산출물. Phase 4 RDB 적재 후 무결성 점검 지표(관측치 수·시리즈 수·결측 비율·시점 일관성·BoP 항등식 잔차)의 임계 기준 결정. 외부 web-search 미사용, `background/` 폴더 자료 + `db/data/` 실측치 1차 근거.

---

## §1 강의 자료 임계 기준 진술 유무

### §1.1 키워드 등장 매트릭스

| 키워드 | 등장 |
|---|---|
| 임계 / 임계값 / threshold | 0회 |
| 결측 비율 / missing ratio | 0회 |
| 무결성 / integrity | 0회 |
| 시점 일관성 / consistency | 0회 |
| 50% / 30% / 5% 등 비율 임계 | 0회 |
| 품질 / quality | 0회 |
| 검증 / validation | 0회 (단 슬라이드 13의 "사후적으로 항상 일치"는 항등식 검증 개념) |
| 경고 / warning / 오류 / error | 0회 |

**결론**: 강의 자료에 무결성 점검 지표·임계 기준 일체 미수록. 본 자문은 (1) 노트 20 NEO 변동성 실측 + 노트 04 BoP 항등식 (2) 통계 일반론(ONS·GAF·BPM6)으로 도출.

---

## §2 노트 20 NEO 변동성 활용 임계 기준

### §2.1 영국 BoP 분기 NEO 절대값 (2020Q1~2025Q4, n=24)

| 지표 | 값 (£m) | 분기 GDP 대비 |
|---|---:|---:|
| 평균 (mean) | −1,503 | — |
| 표본 표준편차 (SD) | 약 6,840 | — |
| **절대값 평균 mean(\|NEO\|)** | **약 5,872** | **약 0.92%** |
| 최댓값 | +14,457 (2024Q1) | +2.05% |
| 최솟값 | −11,752 (2020Q4) | **−2.16%** |

### §2.2 BoP 항등식 잔차 임계 권고

| 임계 수준 | 잔차 \|Σ\| / 분기 GDP | 권고 처리 | 근거 |
|---|---|---|---|
| 정상 | ≤ 1.0% | 통과 (NEO 평균 수준) | 노트 20 평균 0.92% |
| 경고 | 1.0% ~ 2.5% | 로그 + 검토 | 노트 20 최대 2.16% 여유 |
| 오류 | > 2.5% | 적재 중단 + 원본 재대조 | NEO 최대치 초과 = 적재 오류 의심 |

---

## §3 일반 통계 관행 임계 기준 (참고)

### §3.1 결측 비율 경계

| 결측 비율 | 일반 권고 |
|---|---|
| < 5% | 무시 가능 수준 |
| 5% ~ 30% | 조심스러운 보간·검토 |
| 30% ~ 50% | 분석 신뢰도 의심 |
| ≥ 50% | 표준적으로 분석 부적합 |

### §3.2 시점 일관성 / §3.3 BoP 항등식 잔차

`stat_item_meta.START_TIME`/`END_TIME` ↔ `observation`의 `min/max(TIME)` 시리즈 단위 정확 일치. `CA + KA + FA + NEO ≡ 0` 절대값을 분기 GDP 대비 비율로 정규화.

---

## §4 본 데이터셋 임계 권고 (실측 기반)

### §4.1 본 데이터셋 실측 (build_ecos_db.py 1회 실행 결과)

| 지표 | 실측치 |
|---|---:|
| stat_table_meta 행 수 | 63 |
| stat_item_meta 행 수 | 512 |
| observation 행 수 | 74,006 |
| 매칭 실패 skip | 0 |
| `DATA_VALUE NULL` (결측) | 360건 |
| 결측 비율 | **0.4864%** |
| missing_dict 행 수 | 6 |
| term_dict 행 수 | 30 |
| 시점 일관성 불일치(stat_item_meta START/END_TIME ↔ observation min/max) | **0건** |

### §4.2 임계 권고 표

| 지표 | 정상 | 경고 | 오류 | 비고 |
|---|---|---|---|---|
| 관측치 수 | long-form CSV 74,006 ± 0% | 차이 > 0% | 차이 > 0.1% | 적재는 정확 일치 표준 |
| 시리즈 수 | specification.csv 512 ± 0% | 차이 ≥ 1행 | 차이 ≥ 1행 | 메타-관측치 1:1 |
| 전체 결측 비율 | ≤ 1% | 1% ~ 5% | > 10% | 본 xlsx 0.49% — 매우 낮음 |
| 시리즈 단위 결측 비율 | ≤ 5% | 5% ~ 30% | > 50% | Table_C 1997-1998 36 시리즈 5% 초과 — 메타 note 컬럼에 사유 기재 후 통과 |
| START_TIME 일관성 | 일치 100% | 불일치 ≤ 36건(알려진 사유) | 불일치 > 36건 | 본 build_ecos_db.py 실행 결과 0건(`x` 마커 포함 정의로 통일 — §4.3) |
| END_TIME 일관성 | 일치 100% | 불일치 ≥ 1건 | 불일치 ≥ 1건 | 본 데이터셋 0건 |
| BoP 항등식 잔차 \|H BoP\| / 분기 GDP | ≤ 1.0% | 1.0% ~ 2.5% | > 2.5% | 노트 20 NEO 분포 기반 (§2.2) |

### §4.3 START_TIME 정의 운영 결정

build_ecos_db.py의 integrity_check 결과 **시점 일관성 불일치 0건** — `x` 마커 포함을 첫 시점으로 통일하는 옵션이 자연스럽게 적용됨. spec의 START_TIME = `x` 행 포함 첫 시점이 관측치 min(TIME)과 일치.

### §4.4 BoP 항등식 잔차 점검 (Phase 5 회귀 검증 연계)

`CHECKLIST.md` §5.1 헤드라인 수치 재계산·`db/REPORT.md` 분석을 활용. 분기별 `CA + KA + FA + NEO` 합산값을 RDB 조회로 산출, 분기 GDP로 정규화.

---

## §5 출처 카탈로그

| 자료 | 본 노트 사용 |
|---|---|
| BoP.pptx (전 31장) | §1.1 임계 키워드 0회 |
| `note/04_identities.md` | §2.2 항등식 |
| `note/20_neo_volatility.md` | §2.1·§2.2 NEO 분포 |
| `note/15_units_and_missing.md` | §4.1 결측 카탈로그 |
| `note/30_specification_review.md` | §4.1 specification.csv 512행 |
| `note/32_metadata_model.md` | §1.1 강의 미수록 매트릭스 |
| `note/34_missing_dictionary.md` | §3.1·§4.3 결측 사전 시드 |
| `db/data/balanceofpayments2025q4_long.csv` | §4.1 74,006행 / 360 결측 |
| `db/data/_spec/specification.csv` | §4.1 512행 |
| `db/data/_db/ecos_uk_bop.sqlite` (build_ecos_db.py 실행) | §4.1 무결성 점검 실측 |

---

## §6 확인하지 못한 부분 (정직 명시)

1. **ECOS 적재 후 검증 지표 표준** — 한국은행 ECOS Open API의 무결성 점검 응답 스키마는 본 폴더 자료로 확인 불가. 외부 web-search 위임 권고.
2. **SDMX/GSBPM 운영 검증 단계** — UNECE GSBPM Phase 7~8 + ESS QAF Quality Indicators 본문은 본 폴더 미수록.
3. **결측 비율 30·50·80% 경계 출처 PDF** — Schafer 1999·Bennett 2001·Little & Rubin 본문 PDF 미보강.
4. **분기 명목 GDP 시계열 부재** — §4.2 BoP 항등식 잔차 정규화 분모(분기 명목 GDP)는 `db/source/`에 미보유. GDP 시계열 별도 다운로드 필요.
5. **`x` 360건의 1997-1998 미공개 사유** — ONS 상세 사유 미확보. 메타 note 컬럼 기재로 운영.
