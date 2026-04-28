# Table_BX — 한국어 메타 메모

본 메모는 ONS BoP Bulletin 2025 Q4 xlsx의 `Table_BX` 시트(분류: **경상수지 본표**)를 Phase 2.1 ETL로 가공한 부표 CSV들의 한국어 메타 안내이다.

## 1. 원본 위치

- 원본 파일: `db/source/balanceofpayments2025q4.xlsx` (read-only)
- 시트명: `Table_BX`
- 시트 차원: 600 행 × 12 열
- ONS 표 코드: `BX`
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

- 단위: `MIXED (3×GBP_million + 1×pct_of_GDP)` (scale_factor: `mixed`)
- 주기(CYCLE): A·Q (연간 + 분기 적층)
- 연간 시점 범위: 1997 ~ 2025
- 분기 시점 범위: 1997 Q1 ~ 2025 Q4
- 부표 단위로 단위 차이 — sub4(%GDP)는 단위가 다르므로 별도 처리.

## 5. 결측 의미

본 시트의 빈 셀(`empty`)은 데이터 영역 외 padding이며 결측이 아니다(15회차 검증). `x`·`..`·`-` 마커는 본 시트에 등장하지 않는다.

근거: `db/data/_inventory/13_missing_meaning_validation.md`, `19_signs_gold_revisions.md` §3.

## 6. 부호 규약

본 시트는 **강의 슬라이드 13의 Cr/Dr 정의**를 따른다 — 대변(credit, +) = 외국에서 자국으로 자금 유입, 차변(debit, −) = 자국에서 외국으로 자금 유출. 합계 차원에서 사후 항등(전 계정 합 = 0)이 성립하나, 부분합(예: 경상수지)은 흑자(+) / 적자(−) 가능.

근거: `db/data/_inventory/06_sign_convention_validation.md`, `19_signs_gold_revisions.md` §2·§4.

## 7. 부표 분리 단위 + 강의 위계 매핑

- 부표 차원: **Cr / Dr / Bal + %GDP 4분할 (귀금속 제외)**
- 시트 단위 BoP 위계: **CA 4분류 (귀금속 제외)**

| 부표 # | 영문 라벨 | 출력 CSV |
|---:|---|---|
| 1 | BX.1 CA Cr (excl. precious metals) | `balanceofpayments2025q4_bx_sub1.csv` |
| 2 | BX.2 CA Dr (excl. precious metals) | `balanceofpayments2025q4_bx_sub2.csv` |
| 3 | BX.3 CA Bal (excl. precious metals) | `balanceofpayments2025q4_bx_sub3.csv` |
| 4 | BX.4 CA Bal %GDP (excl. precious metals) | `balanceofpayments2025q4_bx_sub4.csv` |

근거: `db/data/_inventory/18_subtable_curriculum_alignment.md` §2·§3.

## 8. 귀금속(비통화용 금) 보정 표와 본표(Table_B)의 관계

본 시트(Table_BX)는 Table_B에서 귀금속(비통화용 금·플래티넘·팔라듐·은) 거래를 제외한 보조표이다. ONS xlsx Notes 시트 r14의 정의에 따르면 "Precious metals includes: Non-Monetary Gold (NMG), Platinum, Palladium and Silver." 즉 Table_B − Table_BX = 위 4종 귀금속 순거래액. 강의 슬라이드 6은 준비자산의 하위로 통화용 금(monetary gold)만 명시하며, 비통화용 금의 BoP 처리 방식은 강의 자료 미수록 영역으로 BPM6 §10·§14 본문 별도 참조 필요(19회차 §5 권고).

## 생성 절차·관련 자료

- 가공 스크립트: `db/code/source/split_subtables.py` (시트 단위 가로형 CSV 분리)
- 메모 생성 스크립트: `db/code/source/write_sheet_memos.py`
- 마스터 인벤토리: `db/data/_inventory/15_master_inventory.csv`
- ETL 로그: `db/data/_etl_log/phase2_1_split_log.csv`
- 부호·결측·귀금속·개정 권고: `db/data/_inventory/19_signs_gold_revisions.md`
- 부표 ↔ 강의 위계 정합성: `db/data/_inventory/18_subtable_curriculum_alignment.md`
