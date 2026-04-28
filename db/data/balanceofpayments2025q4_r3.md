# Table_R3 — 한국어 메타 메모

본 메모는 ONS BoP Bulletin 2025 Q4 xlsx의 `Table_R3` 시트(분류: **직전 발표 대비 개정**)를 Phase 2.1 ETL로 가공한 부표 CSV들의 한국어 메타 안내이다.

## 1. 원본 위치

- 원본 파일: `db/source/balanceofpayments2025q4.xlsx` (read-only)
- 시트명: `Table_R3`
- 시트 차원: 1327 행 × 7 열
- ONS 표 코드: `R3`
- 출처 URL: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsstatisticalbulletintables

## 2. 구조 변경 절차 (재현 가능)

1. 마스터 인벤토리 1행(`db/data/_inventory/15_master_inventory.csv`)을 lookup해 `all_cdid_rows`·`blank_row_positions`·`unit_normalized` 메타를 결정.
2. 부표 분리 — CDID 행이 곧 부표 헤더, 다음 빈 행 직전이 부표 종료. 부표마다 별도 가로형 CSV 1개 출력.
3. 첫 컬럼 = 시점(`time_period`)을 ECOS TIME 규약(`YYYY` 또는 `YYYYQn`)으로 정규화.
4. 둘째 컬럼부터 = ONS CDID 4자 코드를 ASCII 소문자로 정규화. sign_prefix(`-`) 행은 `_neg_<cdid>`로 컬럼명 부착.
5. 셀 값은 원문 보존(숫자는 자릿수 변경 없음, 결측 마커 `x`·빈 셀은 그대로 문자열로 저장).
6. 재현: `env/Scripts/python.exe db/code/source/split_subtables.py`

## 3. 컬럼 정의

| 컬럼 | 의미 | 비고 |
|---|---|---|
| `time_period` | ECOS TIME 규약(`YYYY` 또는 `YYYYQn`) | 첫 컬럼 고정 |
| `<cdid>` | ONS CDID 4자 코드(소문자) | ECOS ITEM_CODE1 대응 |
| `_neg_<cdid>` | sign_prefix가 부착된 CDID(다운로드 시 부호 반전 필요) | Notes note 1 인용 |

## 4. 단위·주기·시점

- 단위: `GBP_billion` (scale_factor: `1e9`)
- 주기(CYCLE): A·Q (연간 + 분기 적층)
- 연간 시점 범위: 1997 ~ 2024
- 분기 시점 범위: 1997 Q1 ~ 2025 Q3

## 5. 결측 의미

본 시트의 빈 셀(`empty`)은 데이터 영역 외 padding이며 결측이 아니다(15회차 검증). `x`·`..`·`-` 마커는 본 시트에 등장하지 않는다.

근거: `db/data/_inventory/13_missing_meaning_validation.md`, `19_signs_gold_revisions.md` §3.

## 6. 부호 규약

본 시트는 직전 발표 대비 개정값을 기록한 운영 보조 자료이다. 부호 규약은 대응 본표(Table_A·B·BX·D·R3는 D 계열)의 BPM6 기준을 그대로 계승한다(19회차 §4).

근거: `db/data/_inventory/06_sign_convention_validation.md`, `19_signs_gold_revisions.md` §2·§4.

## 7. 부표 분리 단위 + 강의 위계 매핑

- 부표 차원: **{abroad/in UK/net} × {IIP/Flow/Income} 3×3**
- 시트 단위 BoP 위계: **IIP·FA·소득 양면×3 변동**

| 부표 # | 영문 라벨 | 출력 CSV |
|---:|---|---|
| 1 | R3.1 | `balanceofpayments2025q4_r3_sub1.csv` |
| 2 | R3.2 | `balanceofpayments2025q4_r3_sub2.csv` |
| 3 | R3.3 | `balanceofpayments2025q4_r3_sub3.csv` |
| 4 | R3.4 | `balanceofpayments2025q4_r3_sub4.csv` |
| 5 | R3.5 | `balanceofpayments2025q4_r3_sub5.csv` |
| 6 | R3.6 | `balanceofpayments2025q4_r3_sub6.csv` |
| 7 | R3.7 | `balanceofpayments2025q4_r3_sub7.csv` |
| 8 | R3.8 | `balanceofpayments2025q4_r3_sub8.csv` |
| 9 | R3.9 | `balanceofpayments2025q4_r3_sub9.csv` |

근거: `db/data/_inventory/18_subtable_curriculum_alignment.md` §2·§3.

## 8. 통계 개정(revision) 시트의 역할

본 시트는 Table_D 계열(IIP·FA·소득) 9 부표(자산/부채/순 × IIP/Flow/Income)의 직전 발표 대비 개정 운영 자료이다. 강의 슬라이드 26의 "기타조정"(other adjustments) 항을 사후적으로 추적할 수 있는 가장 가까운 자료이며, 학생용 심화 보조로 보존 정당화 가능(19회차 §6).

## 생성 절차·관련 자료

- 가공 스크립트: `db/code/source/split_subtables.py` (시트 단위 가로형 CSV 분리)
- 메모 생성 스크립트: `db/code/source/write_sheet_memos.py`
- 마스터 인벤토리: `db/data/_inventory/15_master_inventory.csv`
- ETL 로그: `db/data/_etl_log/phase2_1_split_log.csv`
- 부호·결측·귀금속·개정 권고: `db/data/_inventory/19_signs_gold_revisions.md`
- 부표 ↔ 강의 위계 정합성: `db/data/_inventory/18_subtable_curriculum_alignment.md`
