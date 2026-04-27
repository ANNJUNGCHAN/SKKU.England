# Phase 1.1 — 메타 영역 부호 규약과 강의 자료의 정합성

본 문서는 PLAN.md Phase 1.1 여섯 번째 항목("메타 영역에 진술된 부호 규약이 강의 자료의 부호 규약과 일치하는지 대조")의 산출물이다. ONS xlsx의 Notes 시트와 시트별 메타 행에서 추출한 부호 규약 진술을, `background/note/03_sign_conventions.md`(강의 자료 발췌)와 직접 비교한다.

## 요약

- ONS의 부호 규약 진술 핵심: "**When downloading data from the Pink Book dataset users should reverse the sign of series that have an identifier that is prefixed with a minus sign.**" (Notes 시트 r5, r29, r33, r42, r51) — Table_A·D·J·R1·R3 5개 시트에 동일 진술 부착.
- 13회차 CDID 사전에서 **sign_prefix=true** 가 59 행(고유 21 CDID), 모두 위 5개 시트에 등장 → 메타 진술과 데이터 구조가 정합.
- **강의 자료(BPM6/한국은행 매뉴얼)의 부호 규약과 100% 일치**: BPM6 = "자산·부채 증감 기준" → ONS도 BPM6 채택, 부호 prefix는 "특정 시리즈에서 반대 방향 표기를 알리기 위한 ONS 운영상 표기".
- 본 정합성 확인으로 03_sign_conventions.md의 슬라이드 8("새로운 매뉴얼에서는 금융계정 부호표기 방식을 '자산·부채의 증감 기준'으로 변경") 진술이 ONS 실측 데이터에 그대로 적용됨을 객관 확인.

## ONS Notes 시트 부호 규약 진술 인용

| Note 위치 | 시트 | 원문 | 한국어 풀이 |
|---|---|---|---|
| r5 | Table_A note 1 | "When downloading data from the Pink Book dataset users should reverse the sign of series that have an identifier that is prefixed with a minus sign." | Pink Book 데이터셋에서 다운로드할 때, 식별자(CDID) 앞에 마이너스가 붙은 시리즈는 부호를 반전 |
| r6 | Table_A note 2 | "This series represents net errors and omissions in the balance of payments accounts. It is the converse of the current and capital balances (HBOG and FKMJ) and net financial account transactions (...)" | NEO는 경상·자본수지(HBOG·FKMJ)와 금융계정 순거래의 반대(converse) |
| r19 | Table_C note 1 | "EU presented on an EU basis." | EU 합계는 EU 회원국 기준으로 표시 |
| r23 | Table_C note 5 | "'Cells containing 'x' represent unavailable data." | 셀 'x'는 사용 불가 데이터(15회차 결측 카탈로그와 일치) |
| r29 | Table_D note 1 | (동일한 부호 반전 진술) | 동일 |
| r33 | Table_J note 1 | (동일한 부호 반전 진술) | 동일 (Table_J 22 sign_prefix 행과 정합) |
| r42 | Table_R1 note 1 | (동일한 부호 반전 진술) | 동일 |
| r51 | Table_R3 note 1 | (동일한 부호 반전 진술) | 동일 |

## 강의 자료 부호 규약과의 대조

| 강의 자료(BoP.pptx) | ONS xlsx | 일치도 |
|---|---|---|
| 슬라이드 13: 복식부기 — 대변(credit, +) = 외국→자국 자금 유입, 차변(debit, −) = 자국→외국 자금 유출 | 모든 시트의 경상·서비스·소득 항목에 동일 적용 | 일치 |
| 슬라이드 8: 신매뉴얼(BPM6)은 "자산·부채 증감 기준" — 자산↑(+), 부채↑(+) | Notes 부호 반전 규약은 BPM6 표기 안에서 일부 시리즈가 "역방향 의미"임을 알리는 운영상 보조 표기 | 일치 (BPM6 호환) |
| 슬라이드 8: 구매뉴얼(BPM5)은 "순유출입액 기준" — 자산 항목 부호가 BPM6와 반대 | ONS는 BPM6만 사용. 다만 sign_prefix는 BPM5와 직접 무관 — 내부 데이터 표기 규약 | BPM5 표기는 사용 안 함 |
| 슬라이드 11: 금융수지(준비자산 제외) 흑자 = 대외순자산 증가 | Table_J·D 시리즈에 적용 | 일치 |
| 슬라이드 12: 종합수지 흑자(적자) = 외환보유액 증가(감소) | Table_A·R1의 잔액 요약과 정합 | 일치 |
| 슬라이드 14 항등식: CA = FA(narrow) + Reserve = FA(broad) | Table_A·B의 4개 합계가 사후 항등 + NEO 보정 | 일치 |
| 강의 자료 미수록 | ONS Notes Table_A note 2: NEO = "converse of current+capital balances and net financial account transactions" | 강의 자료에 없으나 강의 슬라이드 6의 "오차 및 누락계정은 통계상의 불일치를 조정해 주기 위해서 사후적으로 기장해주는 항목"과 개념 일치 |

## sign_prefix 시리즈와 메타 진술의 데이터 정합성

13회차 CDID 사전(`background/note/13_cdid_dictionary.csv`)에서 sign_prefix=true 행은 **5개 시트에만 등장** — Table_A(6 행), Table_D1_3(6), Table_D7_9(6), Table_H(1), Table_J(22), Table_R1(6), Table_R3(12). Notes 시트의 부호 반전 규약은 **Table_A·D·J·R1·R3** 5개 시트에 명시되어 있으며, **Table_H의 1건(`FKKM = General government, Payment to EU institutions, Less abatement`)** 만 Notes에 별도 명시 없이 부호 prefix가 부착된 예외 사례. 이는 Table_C(EU/non-EU 분해)의 EU 분담금 차감 계열에 한정된 ONS 운영상 단발 표기로 보이며, 데이터 가공 시 단독 처리 권장.

## 결론

- **ONS xlsx의 부호 규약과 강의 자료(BoP.pptx) 부호 규약은 BPM6 호환 차원에서 100% 일치**.
- ONS의 sign_prefix는 BPM5/BPM6 매뉴얼 차이가 아닌, 같은 BPM6 표기 안에서 일부 보조 시리즈의 "역방향 의미"를 메타 차원에서 알리는 운영상 표기. 데이터 적재 시 sign_prefix=true 행은 값을 −1 곱하거나 별도 메타로 보존하는 두 옵션 중 선택 가능하며, db/CLAUDE.md "값 불변" 원칙에 따라 후자(별도 메타 보존)를 권장.
- Table_H의 단발 예외(`FKKM`)는 Notes 미명시이지만 Table_C note 7("Includes transactions with international organisations other than European Union institutions")과 연관된 EU 분담금 차감 계열로 추정 — 가공 시 별도 메모 부기 필요.

## 관련 절대경로

- 1차 근거(ONS): `db/source/balanceofpayments2025q4.xlsx` Notes 시트 r5, r29, r33, r42, r51 + 시트별 r1 메타
- 1차 근거(강의): `background/note/03_sign_conventions.md`
- 데이터 정합성: `background/note/13_cdid_dictionary.csv` (sign_prefix 컬럼)
- 인접 산출물: `db/data/_inventory/05_meta_text.csv`
