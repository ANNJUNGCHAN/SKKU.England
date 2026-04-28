# Records — 한국어 메타 메모

본 메모는 ONS BoP Bulletin 2025 Q4 xlsx의 `Records` 시트(분류: **메타·주석**)를 Phase 2.1 ETL로 가공한 부표 CSV들의 한국어 메타 안내이다.

## 1. 원본 위치

- 원본 파일: `db/source/balanceofpayments2025q4.xlsx` (read-only)
- 시트명: `Records`
- 시트 차원: 35 행 × 5 열
- ONS 표 코드: `(none)`
- 출처 URL: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsstatisticalbulletintables

## 2. 구조 변경 절차 (재현 가능)

- 메타 시트는 별도 CSV로 산출하지 않는다(`db/code/source/split_subtables.py`가 `meta_notes` 분류를 자동 분기).
- 시트 본문 인용이 필요한 경우 본 메모 §8(시트 역할 안내)에 기재한다.

## 본 시트 역할

본 시트는 BoP 주요 합계 라인(상품무역·서비스무역·1차소득·2차소득·경상수지·자본수지·금융계정·NEO)의 헤드라인 수치(GBP_billion 단위) 1쪽 요약본이다. db/REPORT.md 분석 보고서의 1차 수치 인용 출처. 본 ETL은 별도 CSV 산출하지 않으며, Records 시트 인용은 REPORT 갱신 시점에 직접 수행한다.

## 생성 절차·관련 자료

- 가공 스크립트: `db/code/source/split_subtables.py` (시트 단위 가로형 CSV 분리)
- 메모 생성 스크립트: `db/code/source/write_sheet_memos.py`
- 마스터 인벤토리: `db/data/_inventory/15_master_inventory.csv`
- ETL 로그: `db/data/_etl_log/phase2_1_split_log.csv`
- 부호·결측·귀금속·개정 권고: `db/data/_inventory/19_signs_gold_revisions.md`
- 부표 ↔ 강의 위계 정합성: `db/data/_inventory/18_subtable_curriculum_alignment.md`
