# CDID 사전 (13회차)

본 문서는 db/source/balanceofpayments2025q4.xlsx 본표 17개 시트에서 추출한 ONS 4자 영숫자 코드(CDID) 마스터 사전이다. 향후 ECOS ITEM_CODE1 매핑 및 ONS Time Series API 호출의 1차 키로 사용한다.

## 추출 규칙

- CDID 후보 정규식: `^[A-Z0-9]{4}$` (대문자 영문/숫자 4자, 영문 1자 이상 포함). 예: `L87S`, `MU7L`, `N2RN`.
- 부호 반전 prefix 정규식: `^\s*-\s*[A-Z0-9]{4}\s*$`. Notes Table A note 1: 'reverse the sign of series prefixed with a minus'.
- 부표 분할: 한 행에 CDID 패턴이 ≥2 등장하는 행을 부표 시작점으로 인식. 직전 비어있지 않은 행을 컬럼 헤더로 페어링.
- 라벨 'CDID' 셀과 연도 셀(예: '1997')은 제외.

## 요약 통계

- 총 CDID 행(중복 포함): **512**
- 고유 CDID 수(중복 제외): **284**
- 부호 prefix 부착 CDID 행: **59** (고유 CDID **21** 개)
- 부호 prefix 등장 시트: **Table_A, Table_D1_3, Table_D7_9, Table_H, Table_J, Table_R1, Table_R3**
- 동일 CDID가 ≥2 시트에 등장한 사례: **95** 건
- 시트당 평균 CDID 행 수: **30.1**

## 시트별 CDID 분포

| 시트 | 부표 수 | CDID 행 | 고유 CDID | sign_prefix |
|---|---:|---:|---:|---:|
| Table_A | 3 | 31 | 31 | 6 |
| Table_B | 4 | 39 | 39 | 0 |
| Table_BX | 4 | 39 | 39 | 0 |
| Table_C | 6 | 36 | 36 | 0 |
| Table_D1_3 | 3 | 17 | 17 | 6 |
| Table_D4_6 | 3 | 13 | 13 | 0 |
| Table_D7_9 | 3 | 17 | 17 | 6 |
| Table_E | 3 | 24 | 24 | 0 |
| Table_F | 3 | 36 | 36 | 0 |
| Table_G | 3 | 29 | 28 | 0 |
| Table_H | 3 | 22 | 22 | 1 |
| Table_I | 3 | 32 | 32 | 0 |
| Table_J | 3 | 31 | 29 | 22 |
| Table_K | 3 | 29 | 28 | 0 |
| Table_R1 | 3 | 31 | 31 | 6 |
| Table_R2 | 4 | 39 | 39 | 0 |
| Table_R3 | 9 | 47 | 43 | 12 |

## 부호 prefix CDID 목록

| 시트 | 부표 | col | CDID | column_label |
|---|---:|---:|---|---|
| Table_A | 3 | 2 | MU7M | Direct investment |
| Table_A | 3 | 3 | HHZD | Portfolio investment |
| Table_A | 3 | 4 | ZPNN | Financial derivatives (net) |
| Table_A | 3 | 5 | HHYR | Other investment |
| Table_A | 3 | 6 | LTCV | Reserve assets |
| Table_A | 3 | 7 | HBNT | Net financial transactions |
| Table_D1_3 | 2 | 2 | N2SV | Financial account transactions, Direct investment |
| Table_D1_3 | 2 | 3 | HHZC | Financial account transactions, Portfolio investment |
| Table_D1_3 | 2 | 4 | ZPNN | Financial account transactions, Financial derivatives (net) |
| Table_D1_3 | 2 | 5 | XBMM | Financial account transactions, Other investment |
| Table_D1_3 | 2 | 6 | LTCV | Financial account transactions, Reserve assets |
| Table_D1_3 | 2 | 7 | HBNR | Financial account transactions, Total |
| Table_D7_9 | 2 | 2 | MU7M | Financial account transactions, Direct investment |
| Table_D7_9 | 2 | 3 | HHZD | Financial account transactions, Portfolio investment |
| Table_D7_9 | 2 | 4 | ZPNN | Financial account transactions, Financial derivatives |
| Table_D7_9 | 2 | 5 | HHYR | Financial account transactions, Other investment |
| Table_D7_9 | 2 | 6 | LTCV | Financial account transactions, Reserve assets |
| Table_D7_9 | 2 | 7 | HBNT | Financial account transactions, Net transaction |
| Table_H | 2 | 4 | FKKM | General government, Payment to EU institutions, Less abatement |
| Table_J | 1 | 2 | HJYM | Direct investment abroad, Equity capital other than reinvestment of earnings |
| Table_J | 1 | 3 | HDNY | Direct investment abroad, Reinvestment of earnings |
| Table_J | 1 | 4 | N2RN | Direct investment abroad, Debt instruments |
| Table_J | 1 | 5 | N2SV | Direct investment abroad, Total |
| Table_J | 1 | 6 | HBVI | Portfolio investment abroad, Equity and investment fund shares |
| Table_J | 1 | 7 | XBMW | Portfolio investment abroad, Debt securities |
| Table_J | 1 | 8 | HHZC | Portfolio investment abroad, Total |
| Table_J | 1 | 9 | ZPNN | Financial derivatives and employee stock options |
| Table_J | 1 | 10 | XBMM | Other investment abroad |
| Table_J | 1 | 11 | LTCV | Reserve assets |
| Table_J | 1 | 12 | HBNR | Total investment abroad |
| Table_J | 3 | 2 | HBWN | Net direct investment, Equity capital other than reinvestment of earnings |
| Table_J | 3 | 3 | HBWT | Net direct investment, Reinvestment of earnings |
| Table_J | 3 | 4 | MU7L | Net direct investment, Debt instruments |
| Table_J | 3 | 5 | MU7M | Net direct investment, Total |
| Table_J | 3 | 6 | HBWV | Net portfolio investment, Equity and investment fund shares |
| Table_J | 3 | 7 | HBWX | Net portfolio investment, Debt securities |
| Table_J | 3 | 8 | HHZD | Net portfolio investment, Total |
| Table_J | 3 | 9 | ZPNN | Financial derivatives and employee stock options |
| Table_J | 3 | 10 | HHYR | Other net investment |
| Table_J | 3 | 11 | LTCV | Reserve assets |
| Table_J | 3 | 12 | HBNT | Total net investment |
| Table_R1 | 3 | 2 | MU7M | Direct investment |
| Table_R1 | 3 | 3 | HHZD | Portfolio investment |
| Table_R1 | 3 | 4 | ZPNN | Financial derivatives (net) |
| Table_R1 | 3 | 5 | HHYR | Other investment |
| Table_R1 | 3 | 6 | LTCV | Reserve assets |
| Table_R1 | 3 | 7 | HBNT | Net financial transactions |
| Table_R3 | 2 | 2 | N2SV | Direct investment |
| Table_R3 | 2 | 3 | HHZC | Portfolio investment |
| Table_R3 | 2 | 4 | ZPNN | Financial derivatives (net) |
| Table_R3 | 2 | 5 | XBMM | Other investment |
| Table_R3 | 2 | 6 | LTCV | Reserve assets |
| Table_R3 | 2 | 7 | HBNR | Total financial account transactions |
| Table_R3 | 8 | 2 | MU7M | Direct investment |
| Table_R3 | 8 | 3 | HHZD | Portfolio investment |
| Table_R3 | 8 | 4 | ZPNN | Financial derivatives |
| Table_R3 | 8 | 5 | HHYR | Other investment |
| Table_R3 | 8 | 6 | LTCV | Reserve assets |
| Table_R3 | 8 | 7 | HBNT | Total net financial account transactions |

## 중복 CDID (여러 시트 등장)

동일 CDID가 여러 시트에 출현하는 것은 ONS Bulletin Tables의 구조적 특성이다. 예: 경상수지 잔액(IKBJ 등)은 Table_A 요약, Table_B/BX 본표, Table_R1/R2 개정 시트에 동일 CDID로 동시 게재된다. 본 사전에서는 (sheet, sub_table, column_position) 트리플로 위치를 구분하므로 데이터 적재 시 중복은 트리플 단위로 다루면 된다.

| CDID | 등장 시트 수 | 시트 목록 |
|---|---:|---|
| FNSV | 6 | Table_A, Table_B, Table_BX, Table_H, Table_R1, Table_R2 |
| FNTC | 6 | Table_A, Table_B, Table_BX, Table_H, Table_R1, Table_R2 |
| HBOJ | 6 | Table_A, Table_B, Table_BX, Table_G, Table_R1, Table_R2 |
| HBOM | 6 | Table_A, Table_B, Table_BX, Table_G, Table_R1, Table_R2 |
| IJAJ | 6 | Table_A, Table_B, Table_BX, Table_G, Table_R1, Table_R2 |
| IKBD | 6 | Table_A, Table_B, Table_BX, Table_F, Table_R1, Table_R2 |
| IKBP | 6 | Table_A, Table_B, Table_BX, Table_H, Table_R1, Table_R2 |
| LTCV | 6 | Table_A, Table_D1_3, Table_D7_9, Table_J, Table_R1, Table_R3 |
| MT5X | 6 | Table_A, Table_B, Table_BX, Table_G, Table_R1, Table_R2 |
| ZPNN | 6 | Table_A, Table_D1_3, Table_D7_9, Table_J, Table_R1, Table_R3 |
| BOKI | 5 | Table_A, Table_B, Table_E, Table_R1, Table_R2 |
| HBNT | 5 | Table_A, Table_D7_9, Table_J, Table_R1, Table_R3 |
| HHYR | 5 | Table_A, Table_D7_9, Table_J, Table_R1, Table_R3 |
| HHZD | 5 | Table_A, Table_D7_9, Table_J, Table_R1, Table_R3 |
| MU7M | 5 | Table_A, Table_D7_9, Table_J, Table_R1, Table_R3 |
| FHDM | 4 | Table_B, Table_BX, Table_H, Table_R2 |
| FHIB | 4 | Table_B, Table_BX, Table_H, Table_R2 |
| FLUD | 4 | Table_B, Table_BX, Table_H, Table_R2 |
| FLUZ | 4 | Table_B, Table_BX, Table_H, Table_R2 |
| HBOH | 4 | Table_B, Table_BX, Table_G, Table_R2 |
| HBOI | 4 | Table_B, Table_BX, Table_G, Table_R2 |
| HBOK | 4 | Table_B, Table_BX, Table_G, Table_R2 |
| HBOL | 4 | Table_B, Table_BX, Table_G, Table_R2 |
| HBOP | 4 | Table_A, Table_B, Table_R1, Table_R2 |
| HMBM | 4 | Table_A, Table_D7_9, Table_R1, Table_R3 |
| IJAH | 4 | Table_B, Table_BX, Table_G, Table_R2 |
| IJAI | 4 | Table_B, Table_BX, Table_G, Table_R2 |
| IKBB | 4 | Table_B, Table_BX, Table_F, Table_R2 |
| IKBC | 4 | Table_B, Table_BX, Table_F, Table_R2 |
| IKBJ | 4 | Table_A, Table_B, Table_R1, Table_R2 |
| IKBN | 4 | Table_B, Table_BX, Table_H, Table_R2 |
| IKBO | 4 | Table_B, Table_BX, Table_H, Table_R2 |
| LTEB | 4 | Table_D1_3, Table_D7_9, Table_K, Table_R3 |
| MT5T | 4 | Table_B, Table_BX, Table_G, Table_R2 |
| MT5V | 4 | Table_B, Table_BX, Table_G, Table_R2 |
| BOKG | 3 | Table_B, Table_E, Table_R2 |
| BOKH | 3 | Table_B, Table_E, Table_R2 |
| CGNG | 3 | Table_D7_9, Table_K, Table_R3 |
| CGNH | 3 | Table_D7_9, Table_K, Table_R3 |
| D28K | 3 | Table_B, Table_BX, Table_R2 |
| D28M | 3 | Table_B, Table_BX, Table_R2 |
| D28N | 3 | Table_B, Table_BX, Table_R2 |
| FNVQ | 3 | Table_A, Table_I, Table_R1 |
| HBNR | 3 | Table_D1_3, Table_J, Table_R3 |
| HBNS | 3 | Table_D4_6, Table_J, Table_R3 |
| HBQA | 3 | Table_D1_3, Table_K, Table_R3 |
| HBQB | 3 | Table_D4_6, Table_K, Table_R3 |
| HBQC | 3 | Table_D7_9, Table_K, Table_R3 |
| HHCB | 3 | Table_D1_3, Table_D7_9, Table_R3 |
| HHZC | 3 | Table_D1_3, Table_J, Table_R3 |
| HHZF | 3 | Table_D4_6, Table_J, Table_R3 |
| HHZZ | 3 | Table_D1_3, Table_K, Table_R3 |
| HLXV | 3 | Table_D1_3, Table_K, Table_R3 |
| HLXW | 3 | Table_D4_6, Table_K, Table_R3 |
| HLYD | 3 | Table_D4_6, Table_K, Table_R3 |
| JX96 | 3 | Table_D1_3, Table_K, Table_R3 |
| JX97 | 3 | Table_D4_6, Table_K, Table_R3 |
| JX98 | 3 | Table_D7_9, Table_K, Table_R3 |
| MU7O | 3 | Table_D7_9, Table_K, Table_R3 |
| N2SA | 3 | Table_D4_6, Table_J, Table_R3 |
| N2SV | 3 | Table_D1_3, Table_J, Table_R3 |
| N2UG | 3 | Table_D4_6, Table_K, Table_R3 |
| N2V3 | 3 | Table_D1_3, Table_K, Table_R3 |
| XBMM | 3 | Table_D1_3, Table_J, Table_R3 |
| XBMN | 3 | Table_D4_6, Table_J, Table_R3 |
| AA6H | 2 | Table_B, Table_R2 |
| AIOP | 2 | Table_D1_3, Table_R3 |
| CGNA | 2 | Table_D7_9, Table_R3 |
| D28J | 2 | Table_B, Table_R2 |
| D28L | 2 | Table_B, Table_R2 |
| FJUQ | 2 | Table_A, Table_R1 |
| FJUR | 2 | Table_A, Table_R1 |
| FKMJ | 2 | Table_A, Table_R1 |
| HBOG | 2 | Table_A, Table_R1 |
| HBON | 2 | Table_B, Table_R2 |
| HBOO | 2 | Table_B, Table_R2 |
| HHDH | 2 | Table_A, Table_R1 |
| HLYX | 2 | Table_D1_3, Table_R3 |
| HLZC | 2 | Table_D4_6, Table_R3 |
| HLZN | 2 | Table_D4_6, Table_R3 |
| HLZX | 2 | Table_D7_9, Table_R3 |
| HMBN | 2 | Table_D1_3, Table_R3 |
| HMBO | 2 | Table_D4_6, Table_R3 |
| HMBP | 2 | Table_A, Table_R1 |
| IKBH | 2 | Table_B, Table_R2 |
| IKBI | 2 | Table_B, Table_R2 |
| KTMP | 2 | Table_A, Table_R1 |
| KTMS | 2 | Table_A, Table_R1 |
| KTMY | 2 | Table_A, Table_R1 |
| KTNF | 2 | Table_A, Table_R1 |
| LQCT | 2 | Table_A, Table_R1 |
| MT5W | 2 | Table_A, Table_R1 |
| MU7E | 2 | Table_D7_9, Table_R3 |
| N2Q4 | 2 | Table_D4_6, Table_R3 |
| N2QP | 2 | Table_D1_3, Table_R3 |

## 시트별 CDID 표 (전수)


### Table_A (table_code=A, unit=GBP million)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | BOKI |  | Trade in goods |
| 1 | 3 | IKBD |  | Trade in services |
| 1 | 4 | IKBJ |  | Total trade |
| 1 | 5 | IJAJ |  | Primary income, Compensation of employees |
| 1 | 6 | HBOM |  | Primary income, Investment income |
| 1 | 7 | MT5X |  | Primary income, Other primary income |
| 1 | 8 | HBOJ |  | Primary income, Total |
| 1 | 9 | FNSV |  | Secondary income, General government |
| 1 | 10 | FNTC |  | Secondary income, Other sectors |
| 1 | 11 | IKBP |  | Secondary income, Total |
| 1 | 12 | HBOP |  | Current balance |
| 1 | 13 | FNVQ |  | Capital balance |
| 2 | 2 | LQCT |  | Trade in goods |
| 2 | 3 | KTMS |  | Trade in services |
| 2 | 4 | KTMY |  | Total trade |
| 2 | 5 | KTMP |  | Primary income, Compensation of employees |
| 2 | 6 | HMBM |  | Primary income, Investment income |
| 2 | 7 | MT5W |  | Primary income, Other primary income |
| 2 | 8 | HMBP |  | Primary income, Total |
| 2 | 9 | FJUQ |  | Secondary income, General government |
| 2 | 10 | FJUR |  | Secondary income, Other sectors |
| 2 | 11 | KTNF |  | Secondary income, Total |
| 2 | 12 | HBOG |  | Current balance |
| 2 | 13 | FKMJ |  | Capital balance |
| 3 | 2 | MU7M | - | Direct investment |
| 3 | 3 | HHZD | - | Portfolio investment |
| 3 | 4 | ZPNN | - | Financial derivatives (net) |
| 3 | 5 | HHYR | - | Other investment |
| 3 | 6 | LTCV | - | Reserve assets |
| 3 | 7 | HBNT | - | Net financial transactions |
| 3 | 8 | HHDH |  | Net errors and omissions [note 2] |

### Table_B (table_code=B, unit=GBP million (1-3) / % of GDP (4))

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | BOKG |  | Exports of goods |
| 1 | 3 | IKBB |  | Exports of services |
| 1 | 4 | IKBH |  | Total exports |
| 1 | 5 | IJAH |  | Primary income, Compensation of employees |
| 1 | 6 | HBOK |  | Primary income, Investment income |
| 1 | 7 | MT5T |  | Primary income, Other primary income |
| 1 | 8 | HBOH |  | Primary income, Total |
| 1 | 9 | FHDM |  | Secondary income, Central government |
| 1 | 10 | FHIB |  | Secondary income, Other sectors |
| 1 | 11 | IKBN |  | Secondary income, Total |
| 1 | 12 | HBON |  | Total credits |
| 2 | 2 | BOKH |  | Imports of goods |
| 2 | 3 | IKBC |  | Imports of services |
| 2 | 4 | IKBI |  | Total imports |
| 2 | 5 | IJAI |  | Primary income, Compensation of employees |
| 2 | 6 | HBOL |  | Primary income, Investment income |
| 2 | 7 | MT5V |  | Primary income, Other primary income |
| 2 | 8 | HBOI |  | Primary income, Total |
| 2 | 9 | FLUD |  | Secondary income, Central government |
| 2 | 10 | FLUZ |  | Secondary income, Other sectors |
| 2 | 11 | IKBO |  | Secondary income, Total |
| 2 | 12 | HBOO |  | Total debits |
| 3 | 2 | BOKI |  | Trade in goods |
| 3 | 3 | IKBD |  | Trade in services |
| 3 | 4 | IKBJ |  | Trade total |
| 3 | 5 | IJAJ |  | Primary income, Compensation of employees |
| 3 | 6 | HBOM |  | Primary income, Investment income |
| 3 | 7 | MT5X |  | Primary income, Other primary income |
| 3 | 8 | HBOJ |  | Primary income, Total |
| 3 | 9 | FNSV |  | Secondary income, Central government |
| 3 | 10 | FNTC |  | Secondary income, Other sectors |
| 3 | 11 | IKBP |  | Secondary income,  Total |
| 3 | 12 | HBOP |  | Current balance |
| 4 | 2 | D28J |  | Trade in goods |
| 4 | 3 | D28K |  | Trade in services |
| 4 | 4 | D28L |  | Trade, Total |
| 4 | 5 | D28M |  | Primary income,  Total |
| 4 | 6 | D28N |  | Secondary income, Total |
| 4 | 7 | AA6H |  | Current balance |

### Table_BX (table_code=BX, unit=GBP million / % of GDP)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | FUS7 |  | Exports of goods, excl. precious metals |
| 1 | 3 | IKBB |  | Exports of services |
| 1 | 4 | FUS8 |  | Total exports, excl. precious metals |
| 1 | 5 | IJAH |  | Primary income, Compensation of employees |
| 1 | 6 | HBOK |  | Primary income, Investment income |
| 1 | 7 | MT5T |  | Primary income, Other primary income |
| 1 | 8 | HBOH |  | Primary income, Total |
| 1 | 9 | FHDM |  | Secondary income, Central government |
| 1 | 10 | FHIB |  | Secondary income, Other sectors |
| 1 | 11 | IKBN |  | Secondary income, Total |
| 1 | 12 | FUS9 |  | Total credits, excl. precious metals |
| 2 | 2 | FUT2 |  | Imports of goods, excl. precious metals |
| 2 | 3 | IKBC |  | Imports of services |
| 2 | 4 | FUT3 |  | Total imports, excl. precious metals |
| 2 | 5 | IJAI |  | Primary income, Compensation of employees |
| 2 | 6 | HBOL |  | Primary income, Investment income |
| 2 | 7 | MT5V |  | Primary income, Other primary income |
| 2 | 8 | HBOI |  | Primary income, Total |
| 2 | 9 | FLUD |  | Secondary income, Central government |
| 2 | 10 | FLUZ |  | Secondary income, Other sectors |
| 2 | 11 | IKBO |  | Secondary income, Total |
| 2 | 12 | FUT4 |  | Total debits, excl. precious metals |
| 3 | 2 | FUT5 |  | Trade in goods, excl. precious metals |
| 3 | 3 | IKBD |  | Trade in services |
| 3 | 4 | FUT6 |  | Trade total, excl. precious metals |
| 3 | 5 | IJAJ |  | Primary income, Compensation of employees |
| 3 | 6 | HBOM |  | Primary income, Investment income |
| 3 | 7 | MT5X |  | Primary income, Other primary income |
| 3 | 8 | HBOJ |  | Primary income, Total |
| 3 | 9 | FNSV |  | Secondary income, Central government |
| 3 | 10 | FNTC |  | Secondary income, Other sectors |
| 3 | 11 | IKBP |  | Secondary income, Total |
| 3 | 12 | FUT7 |  | Current balance, excl. precious metals |
| 4 | 2 | FUT8 |  | Trade in goods, excl. precious metals |
| 4 | 3 | D28K |  | Trade in services |
| 4 | 4 | FUT9 |  | Total trade, excl. precious metals |
| 4 | 5 | D28M |  | Primary income,  Total |
| 4 | 6 | D28N |  | Secondary income, Total |
| 4 | 7 | FUU2 |  | Current balance, excl. precious metals |

### Table_C (table_code=C, unit=GBP million)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | L87S |  | Exports of goods |
| 1 | 3 | L854 |  | Exports of services |
| 1 | 4 | L84Y |  | Total exports |
| 1 | 5 | L872 |  | Primary income, credits |
| 1 | 6 | L84S |  | Secondary income, credits |
| 1 | 7 | L873 |  | Total credits |
| 2 | 2 | L87U |  | Imports of goods |
| 2 | 3 | L868 |  | Imports of services |
| 2 | 4 | L864 |  | Total imports |
| 2 | 5 | L874 |  | Primary income, debits |
| 2 | 6 | L85W |  | Secondary income, debits |
| 2 | 7 | L875 |  | Total debits |
| 3 | 2 | L87Q |  | Trade in goods |
| 3 | 3 | L86M |  | Trade in services |
| 3 | 4 | L86I |  | Total trade |
| 3 | 5 | L876 |  | Primary income, balance |
| 3 | 6 | L86E |  | Secondary income, balance |
| 3 | 7 | L877 |  | Total balance |
| 4 | 2 | L87M |  | Exports of goods |
| 4 | 3 | L855 |  | Exports of services |
| 4 | 4 | L84Z |  | Total exports |
| 4 | 5 | L87D |  | Primary income, credits |
| 4 | 6 | L84T |  | Secondary income, credits |
| 4 | 7 | L87E |  | Total credits |
| 5 | 2 | L87O |  | Imports of goods |
| 5 | 3 | L869 |  | Imports of services |
| 5 | 4 | L865 |  | Total imports |
| 5 | 5 | L87F |  | Primary income, debits |
| 5 | 6 | L85X |  | Secondary income, debits |
| 5 | 7 | L87G |  | Total debits |
| 6 | 2 | L87K |  | Trade in goods |
| 6 | 3 | L86N |  | Trade in services |
| 6 | 4 | L86J |  | Total trade |
| 6 | 5 | L87H |  | Primary income, balance |
| 6 | 6 | L86F |  | Secondary income, balance |
| 6 | 7 | L87I |  | Total balance |

### Table_D1_3 (table_code=D1.3, unit=GBP billion)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | N2V3 |  | International investment position, Direct investment |
| 1 | 3 | HHZZ |  | International investment position, Portfolio investment |
| 1 | 4 | JX96 |  | International investment position, Financial derivatives |
| 1 | 5 | HLXV |  | International investment position, Other investment |
| 1 | 6 | LTEB |  | International investment position, Reserve assets |
| 1 | 7 | HBQA |  | International investment position, Total |
| 2 | 2 | N2SV | - | Financial account transactions, Direct investment |
| 2 | 3 | HHZC | - | Financial account transactions, Portfolio investment |
| 2 | 4 | ZPNN | - | Financial account transactions, Financial derivatives (net) |
| 2 | 5 | XBMM | - | Financial account transactions, Other investment |
| 2 | 6 | LTCV | - | Financial account transactions, Reserve assets |
| 2 | 7 | HBNR | - | Financial account transactions, Total |
| 3 | 2 | N2QP |  | Investment income earnings, Direct investment |
| 3 | 3 | HLYX |  | Investment income earnings, Portfolio investment |
| 3 | 4 | AIOP |  | Investment income earnings, Other investment |
| 3 | 5 | HHCB |  | Investment income earnings, Reserve assets |
| 3 | 6 | HMBN |  | Investment income earnings, Total |

### Table_D4_6 (table_code=D4.6, unit=GBP billion)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | N2UG |  | International investment position, Direct investment |
| 1 | 3 | HLXW |  | International investment position, Portfolio investment |
| 1 | 4 | JX97 |  | International investment position, Financial derivatives |
| 1 | 5 | HLYD |  | International investment position, Other investment |
| 1 | 6 | HBQB |  | International investment position, Total |
| 2 | 2 | N2SA |  | Financial account transactions, Direct investment |
| 2 | 3 | HHZF |  | Financial account transactions, Portfolio investment |
| 2 | 4 | XBMN |  | Financial account transactions, Other investment |
| 2 | 5 | HBNS |  | Financial account transactions, Total |
| 3 | 2 | N2Q4 |  | Investment income earnings, Direct investment |
| 3 | 3 | HLZC |  | Investment income earnings, Portfolio investment |
| 3 | 4 | HLZN |  | Investment income earnings, Other investment |
| 3 | 5 | HMBO |  | Investment income earnings, Total |

### Table_D7_9 (table_code=D7.9, unit=GBP billion)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | MU7O |  | International investment position, Direct investment |
| 1 | 3 | CGNH |  | International investment position, Portfolio investment |
| 1 | 4 | JX98 |  | International investment position, Financial derivatives |
| 1 | 5 | CGNG |  | International investment position, Other investment |
| 1 | 6 | LTEB |  | International investment position, Reserve assets |
| 1 | 7 | HBQC |  | International investment position, Net investment |
| 2 | 2 | MU7M | - | Financial account transactions, Direct investment |
| 2 | 3 | HHZD | - | Financial account transactions, Portfolio investment |
| 2 | 4 | ZPNN | - | Financial account transactions, Financial derivatives |
| 2 | 5 | HHYR | - | Financial account transactions, Other investment |
| 2 | 6 | LTCV | - | Financial account transactions, Reserve assets |
| 2 | 7 | HBNT | - | Financial account transactions, Net transaction |
| 3 | 2 | MU7E |  | Investment income earnings, Direct investment |
| 3 | 3 | HLZX |  | Investment income earnings, Portfolio investment |
| 3 | 4 | CGNA |  | Investment income earnings, Other investment |
| 3 | 5 | HHCB |  | Investment income earnings, Reserve assets |
| 3 | 6 | HMBM |  | Investment income earnings, Net earnings |

### Table_E (table_code=E, unit=GBP million)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | BOPL |  | Food, beverages and tobacco |
| 1 | 3 | BOPM |  | Basic materials |
| 1 | 4 | ELBL |  | Oil |
| 1 | 5 | BOQI |  | Other fuels |
| 1 | 6 | BOPO |  | Semi-manufactured goods |
| 1 | 7 | BOPP |  | Finished manufactured goods |
| 1 | 8 | BOQL |  | Unspecified goods |
| 1 | 9 | BOKG |  | Total goods exports |
| 2 | 2 | BQAR |  | Food, beverages and tobacco |
| 2 | 3 | BQAS |  | Basic materials |
| 2 | 4 | ENXO |  | Oil |
| 2 | 5 | BPBI |  | Other fuels |
| 2 | 6 | BQAU |  | Semi-manufactured goods |
| 2 | 7 | BQAV |  | Finished manufactured goods |
| 2 | 8 | BQAW |  | Unspecified goods |
| 2 | 9 | BOKH |  | Total goods imports |
| 3 | 2 | ELBE |  | Food, beverages and tobacco |
| 3 | 3 | ELBF |  | Basic materials |
| 3 | 4 | ENXQ |  | Oil |
| 3 | 5 | ENIW |  | Other fuels |
| 3 | 6 | ELBH |  | Semi-manufactured goods |
| 3 | 7 | ELBI |  | Finished manufactured goods |
| 3 | 8 | BQKX |  | Unspecified goods |
| 3 | 9 | BOKI |  | Total goods balance |

### Table_F (table_code=F, unit=GBP million)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | MTN7 |  | Manufacturing and maintenance services |
| 1 | 3 | FKOA |  | Transport |
| 1 | 4 | FAPO |  | Travel |
| 1 | 5 | FDSG |  | Construction |
| 1 | 6 | FDTF |  | Insurance and pension services |
| 1 | 7 | FDYI |  | Financial |
| 1 | 8 | FEBA |  | Intellectual property |
| 1 | 9 | FDYQ |  | Telecommunication, computer and information services |
| 1 | 10 | FEHH |  | Other business |
| 1 | 11 | FGXJ |  | Personal, cultural and recreational services |
| 1 | 12 | FGZA |  | Government |
| 1 | 13 | IKBB |  | Total services exports |
| 2 | 2 | MTN6 |  | Manufacturing and maintenance services |
| 2 | 3 | FHME |  | Transport |
| 2 | 4 | APQL |  | Travel |
| 2 | 5 | FIOU |  | Construction |
| 2 | 6 | FIPT |  | Insurance and pension services |
| 2 | 7 | FITY |  | Financial |
| 2 | 8 | FIVX |  | Intellectual property |
| 2 | 9 | FIUG |  | Telecommunication, computer and information services |
| 2 | 10 | FIWF |  | Other business |
| 2 | 11 | FLQJ |  | Personal, cultural and recreational services |
| 2 | 12 | FLSA |  | Government |
| 2 | 13 | IKBC |  | Total services imports |
| 3 | 2 | MTN8 |  | Manufacturing and maintenance services |
| 3 | 3 | FLYS |  | Transport |
| 3 | 4 | FNGY |  | Travel |
| 3 | 5 | FNJM |  | Construction |
| 3 | 6 | FNKF |  | Insurance and pension services |
| 3 | 7 | FNLQ |  | Financial |
| 3 | 8 | FNMR |  | Intellectual property |
| 3 | 9 | FNLY |  | Telecommunication, computer and information services |
| 3 | 10 | FNMZ |  | Other business |
| 3 | 11 | FNRB |  | Personal, cultural and recreational services |
| 3 | 12 | FNRU |  | Government |
| 3 | 13 | IKBD |  | Total services balance |

### Table_G (table_code=G, unit=GBP million)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | IJAH |  | Compensation of employees |
| 1 | 3 | MTX2 |  | Investment income, Earnings on direct investment abroad |
| 1 | 4 | CGDT |  | Investment income, Earnings on portfolio investment abroad, Equity securities |
| 1 | 5 | CGDU |  | Investment income, Earnings on portfolio investment abroad, Debt securities |
| 1 | 6 | CGDV |  | Investment income, Earnings on portfolio investment abroad, Total |
| 1 | 7 | CGDW |  | Investment income, Earnings on other investment abroad |
| 1 | 8 | HHCC |  | Investment income, Earnings on reserve assets |
| 1 | 9 | HBOK |  | Investment income, Total |
| 1 | 10 | MT5T |  | Other primary income |
| 1 | 11 | HBOH |  | Total credits |
| 2 | 2 | IJAI |  | Compensation of employees |
| 2 | 3 | MTU7 |  | Investment income, Foreign earnings on direct investment in the UK |
| 2 | 4 | HGOT |  | Investment income, Foreign earnings on portfolio investment in the UK, Equity securities |
| 2 | 5 | CGDX |  | Investment income, Foreign earnings on portfolio investment in the UK, Debt securities |
| 2 | 6 | CGDZ |  | Investment income, Foreign earnings on portfolio investment in the UK, Total |
| 2 | 7 | CGEB |  | Investment income, Earnings on other investment in the UK |
| 2 | 8 | HBOL |  | Investment income, Total |
| 2 | 9 | MT5V |  | Other primary income |
| 2 | 10 | HBOI |  | Total debits |
| 3 | 2 | IJAJ |  | Compensation of employees |
| 3 | 3 | MU7F |  | Investment income, Direct investment |
| 3 | 4 | CGEC |  | Investment income, Portfolio investment, Earnings on equity securities |
| 3 | 5 | CGED |  | Investment income, Portfolio investment, Earnings on debt securities |
| 3 | 6 | CGEE |  | Investment income, Portfolio investment, Total |
| 3 | 7 | CGFF |  | Investment income, Other investment |
| 3 | 8 | HHCC |  | Investment income, Reserve assets |
| 3 | 9 | HBOM |  | Investment income, Total |
| 3 | 10 | MT5X |  | Other primary income |
| 3 | 11 | HBOJ |  | Total balance |

### Table_H (table_code=H, unit=GBP million)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | GTTA |  | General government, receipts from EU institutions Other EU receipts |
| 1 | 3 | CGDN |  | General government, Other receipts |
| 1 | 4 | FHDM |  | General government, Total |
| 1 | 5 | H5U3 |  | Other sectors, receipts from EU institutions, Social fund |
| 1 | 6 | CGDO |  | Other sectors, Other receipts |
| 1 | 7 | FHIB |  | Other sectors, Total |
| 1 | 8 | IKBN |  | Total credits |
| 2 | 2 | MUV7 |  | General government, Payment to EU institutions, GNI own resource |
| 2 | 3 | MUV8 |  | General government, Payment to EU institutions, GNI adjustments |
| 2 | 4 | FKKM | - | General government, Payment to EU institutions, Less abatement |
| 2 | 5 | FLMT |  | General government, Payment to EU institutions, Others |
| 2 | 6 | FZJA |  | General government, Payment to EU institutions, Withdrawal agreement |
| 2 | 7 | CGDP |  | General government, Other payments |
| 2 | 8 | FLUD |  | General government, Total |
| 2 | 9 | CGDR |  | Other sectors, Payment to EU institutions |
| 2 | 10 | CGDS |  | Other sectors, Other payments |
| 2 | 11 | FLUZ |  | Other sectors, Total |
| 2 | 12 | IKBO |  | Total debits |
| 3 | 2 | FNSV |  | General government |
| 3 | 3 | FNTC |  | Other sectors |
| 3 | 4 | IKBP |  | Total balances |
| 3 | 5 | GTTB |  | Total balances, Of which EU institutions |

### Table_I (table_code=I, unit=GBP million)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | FHIV |  | Capital transfers, Central government, Debt forgiveness |
| 1 | 3 | FHJA |  | Capital transfers, Central government, Other capital transfers |
| 1 | 4 | FHIU |  | Capital transfers, Central government, Total |
| 1 | 5 | FHJD |  | Capital transfers, Other sectors, Debt forgiveness |
| 1 | 6 | GTTX |  | Capital transfers, Other sectors, EU institutions, Regional development fund |
| 1 | 7 | FHJF |  | Capital transfers, Other sectors, EU institutions, Agricultural fund for regional development |
| 1 | 8 | EBGO |  | Capital transfers, Other sectors, EU institutions, Other capital transfers |
| 1 | 9 | GTTY |  | Capital transfers, Other sectors, EU institutions, Total |
| 1 | 10 | FHJB |  | Capital transfers, Other sectors, Total |
| 1 | 11 | FHIT |  | Capital transfers, Total |
| 1 | 12 | FHJL |  | Disposal of non-produced, non-financial assets |
| 1 | 13 | FHLD |  | Total credits |
| 2 | 2 | FLWD |  | Capital transfers, Central government, Debt forgiveness |
| 2 | 3 | FLWH |  | Capital transfers, Central government, Other capital transfers (project grants) |
| 2 | 4 | FLWB |  | Capital transfers, Central government, Total |
| 2 | 5 | FLWL |  | Capital transfers, Other sectors, Debt forgiveness, Monetary financial institutions |
| 2 | 6 | HMLY |  | Capital transfers, Other sectors, Debt forgiveness, Public corporations |
| 2 | 7 | JCWM |  | Capital transfers, Other sectors, Debt forgiveness, Total |
| 2 | 8 | FLWQ |  | Capital transfers, Other sectors, Other capital transfers |
| 2 | 9 | FLWI |  | Capital transfers, Other sectors, Total |
| 2 | 10 | FLWA |  | Capital transfers Total |
| 2 | 11 | FLWT |  | Acquisitions of non-produced, non-financial assets |
| 2 | 12 | FLYL |  | Total Debits |
| 3 | 2 | FNTM |  | Capital transfers, Central government, Debt forgiveness |
| 3 | 3 | FNTN |  | Capital transfers, Central government, Other capital transfers |
| 3 | 4 | FNTL |  | Capital transfers, Central government, Total |
| 3 | 5 | FNTQ |  | Capital transfers, Other sectors, Debt forgiveness |
| 3 | 6 | FNTR |  | Capital transfers, Other sectors, Other capital transfers |
| 3 | 7 | FNTO |  | Capital transfers, Other sectors, Total |
| 3 | 8 | FNTK |  | Capital transfers, Total |
| 3 | 9 | FNTS |  | Non-produced, non-financial assets |
| 3 | 10 | FNVQ |  | Total balances |

### Table_J (table_code=J, unit=GBP million)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | HJYM | - | Direct investment abroad, Equity capital other than reinvestment of earnings |
| 1 | 3 | HDNY | - | Direct investment abroad, Reinvestment of earnings |
| 1 | 4 | N2RN | - | Direct investment abroad, Debt instruments |
| 1 | 5 | N2SV | - | Direct investment abroad, Total |
| 1 | 6 | HBVI | - | Portfolio investment abroad, Equity and investment fund shares |
| 1 | 7 | XBMW | - | Portfolio investment abroad, Debt securities |
| 1 | 8 | HHZC | - | Portfolio investment abroad, Total |
| 1 | 9 | ZPNN | - | Financial derivatives and employee stock options |
| 1 | 10 | XBMM | - | Other investment abroad |
| 1 | 11 | LTCV | - | Reserve assets |
| 1 | 12 | HBNR | - | Total investment abroad |
| 2 | 2 | HJYR |  | Direct investment in the UK, Equity capital other than reinvestment of earnings |
| 2 | 3 | CYFV |  | Direct investment in the UK, Reinvestment of earnings |
| 2 | 4 | N2R7 |  | Direct investment in the UK, Debt instruments |
| 2 | 5 | N2SA |  | Direct investment in the UK, Total |
| 2 | 6 | XBLW |  | Portfolio investment in the UK, Equity and investment fund shares |
| 2 | 7 | XBLX |  | Portfolio investment in the UK, Debt securities |
| 2 | 8 | HHZF |  | Portfolio investment in the UK, Total |
| 2 | 9 | XBMN |  | Other investment in the UK |
| 2 | 10 | HBNS |  | Total investment in the UK |
| 3 | 2 | HBWN | - | Net direct investment, Equity capital other than reinvestment of earnings |
| 3 | 3 | HBWT | - | Net direct investment, Reinvestment of earnings |
| 3 | 4 | MU7L | - | Net direct investment, Debt instruments |
| 3 | 5 | MU7M | - | Net direct investment, Total |
| 3 | 6 | HBWV | - | Net portfolio investment, Equity and investment fund shares |
| 3 | 7 | HBWX | - | Net portfolio investment, Debt securities |
| 3 | 8 | HHZD | - | Net portfolio investment, Total |
| 3 | 9 | ZPNN | - | Financial derivatives and employee stock options |
| 3 | 10 | HHYR | - | Other net investment |
| 3 | 11 | LTCV | - | Reserve assets |
| 3 | 12 | HBNT | - | Total net investment |

### Table_K (table_code=K, unit=GBP billion)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | CGMO |  | Direct investment abroad, Equity and investment fund shares |
| 1 | 3 | N2TT |  | Direct investment abroad, Debt instruments |
| 1 | 4 | N2V3 |  | Direct investment abroad, Total |
| 1 | 5 | HEPX |  | Portfolio investment abroad, Equity and investment fund shares |
| 1 | 6 | HHZX |  | Portfolio investment abroad, Debt securities |
| 1 | 7 | HHZZ |  | Portfolio investment abroad, Total |
| 1 | 8 | JX96 |  | Financial derivatives and employee stock options |
| 1 | 9 | HLXV |  | Other investment abroad |
| 1 | 10 | LTEB |  | Reserve assets |
| 1 | 11 | HBQA |  | Total UK assets |
| 2 | 2 | HBUY |  | Direct investment in the UK, Equity and investment fund shares |
| 2 | 3 | N2TD |  | Direct investment in the UK, Debt instruments |
| 2 | 4 | N2UG |  | Direct investment in the UK, Total |
| 2 | 5 | HLXX |  | Portfolio investment in the UK, Equity and investment fund shares |
| 2 | 6 | HLXY |  | Portfolio investment in the UK, Debt securities |
| 2 | 7 | HLXW |  | Portfolio investment in the UK, Total |
| 2 | 8 | JX97 |  | Financial derivatives and employee stock options |
| 2 | 9 | HLYD |  | Other investment in the UK |
| 2 | 10 | HBQB |  | Total UK liabilities |
| 3 | 2 | HBSH |  | Direct investment, Equity and investment fund shares |
| 3 | 3 | MU7N |  | Direct investment, Debt instruments |
| 3 | 4 | MU7O |  | Direct investment, Net total |
| 3 | 5 | CGNE |  | Portfolio investment, Equity and investment fund shares |
| 3 | 6 | CGNF |  | Portfolio investment, Debt securities |
| 3 | 7 | CGNH |  | Portfolio investment, Net total |
| 3 | 8 | JX98 |  | Financial derivatives and employee stock options |
| 3 | 9 | CGNG |  | Other investment |
| 3 | 10 | LTEB |  | Reserve assets |
| 3 | 11 | HBQC |  | Total net investment |

### Table_R1 (table_code=R1, unit=GBP million)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | BOKI |  | Trade in goods |
| 1 | 3 | IKBD |  | Trade in services |
| 1 | 4 | IKBJ |  | Total trade |
| 1 | 5 | IJAJ |  | Primary income, Compensation of employees |
| 1 | 6 | HBOM |  | Primary income, Investment income |
| 1 | 7 | MT5X |  | Primary income, Other primary income |
| 1 | 8 | HBOJ |  | Primary income, Total |
| 1 | 9 | FNSV |  | Secondary income, General government |
| 1 | 10 | FNTC |  | Secondary income, Other sectors |
| 1 | 11 | IKBP |  | Secondary income, Total |
| 1 | 12 | HBOP |  | Current balance |
| 1 | 13 | FNVQ |  | Capital balance |
| 2 | 2 | LQCT |  | Trade in goods |
| 2 | 3 | KTMS |  | Trade in services |
| 2 | 4 | KTMY |  | Total trade |
| 2 | 5 | KTMP |  | Primary income, Compensation of employees |
| 2 | 6 | HMBM |  | Primary income, Investment income |
| 2 | 7 | MT5W |  | Primary income, Other primary income |
| 2 | 8 | HMBP |  | Primary income, Total |
| 2 | 9 | FJUQ |  | Secondary income, General government |
| 2 | 10 | FJUR |  | Secondary income, Other sectors |
| 2 | 11 | KTNF |  | Secondary income, Total |
| 2 | 12 | HBOG |  | Current balance |
| 2 | 13 | FKMJ |  | Capital balance |
| 3 | 2 | MU7M | - | Direct investment |
| 3 | 3 | HHZD | - | Portfolio investment |
| 3 | 4 | ZPNN | - | Financial derivatives (net) |
| 3 | 5 | HHYR | - | Other investment |
| 3 | 6 | LTCV | - | Reserve assets |
| 3 | 7 | HBNT | - | Net financial transactions |
| 3 | 8 | HHDH |  | Net errors and omissions [note 2] |

### Table_R2 (table_code=R2, unit=GBP million / % of GDP)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | BOKG |  | Exports of goods |
| 1 | 3 | IKBB |  | Exports of services |
| 1 | 4 | IKBH |  | Total exports |
| 1 | 5 | IJAH |  | Primary income, Compensation of employees |
| 1 | 6 | HBOK |  | Primary income, Investment income |
| 1 | 7 | MT5T |  | Primary income, Other primary income |
| 1 | 8 | HBOH |  | Primary income, Total |
| 1 | 9 | FHDM |  | Secondary income, Central government |
| 1 | 10 | FHIB |  | Secondary income, Other sectors |
| 1 | 11 | IKBN |  | Secondary income, Total |
| 1 | 12 | HBON |  | Total credits |
| 2 | 2 | BOKH |  | Imports of goods |
| 2 | 3 | IKBC |  | Imports of services |
| 2 | 4 | IKBI |  | Total imports |
| 2 | 5 | IJAI |  | Primary income, Compensation of employees |
| 2 | 6 | HBOL |  | Primary income, Investment income |
| 2 | 7 | MT5V |  | Primary income, Other primary income |
| 2 | 8 | HBOI |  | Primary income, Total |
| 2 | 9 | FLUD |  | Secondary income, Central government |
| 2 | 10 | FLUZ |  | Secondary income, Other sectors |
| 2 | 11 | IKBO |  | Secondary income, Total |
| 2 | 12 | HBOO |  | Total debits |
| 3 | 2 | BOKI |  | Trade in goods |
| 3 | 3 | IKBD |  | Trade in services |
| 3 | 4 | IKBJ |  | Total trade |
| 3 | 5 | IJAJ |  | Primary income, Compensation of employees |
| 3 | 6 | HBOM |  | Primary income, Investment income |
| 3 | 7 | MT5X |  | Primary income, Other primary income |
| 3 | 8 | HBOJ |  | Primary income, Total |
| 3 | 9 | FNSV |  | Secondary income, Central government |
| 3 | 10 | FNTC |  | Secondary income, Other sectors |
| 3 | 11 | IKBP |  | Secondary income, Total |
| 3 | 12 | HBOP |  | Total balance |
| 4 | 2 | D28J |  | Trade in goods |
| 4 | 3 | D28K |  | Trade in services |
| 4 | 4 | D28L |  | Total trade |
| 4 | 5 | D28M |  | Primary income,  Total |
| 4 | 6 | D28N |  | Secondary income, Total |
| 4 | 7 | AA6H |  | Current balance |

### Table_R3 (table_code=R3, unit=GBP billion)

| 부표 | col | CDID | sign | column_label |
|---:|---:|---|:---:|---|
| 1 | 2 | N2V3 |  | Direct investment |
| 1 | 3 | HHZZ |  | Portfolio investment |
| 1 | 4 | JX96 |  | Financial derivatives |
| 1 | 5 | HLXV |  | Other investment |
| 1 | 6 | LTEB |  | Reserve assets |
| 1 | 7 | HBQA |  | Total international investment position |
| 2 | 2 | N2SV | - | Direct investment |
| 2 | 3 | HHZC | - | Portfolio investment |
| 2 | 4 | ZPNN | - | Financial derivatives (net) |
| 2 | 5 | XBMM | - | Other investment |
| 2 | 6 | LTCV | - | Reserve assets |
| 2 | 7 | HBNR | - | Total financial account transactions |
| 3 | 2 | N2QP |  | Direct investment |
| 3 | 3 | HLYX |  | Portfolio investment |
| 3 | 4 | AIOP |  | Other investment |
| 3 | 5 | HHCB |  | Reserve assets |
| 3 | 6 | HMBN |  | Total investment income earnings |
| 4 | 2 | N2UG |  | Direct investment |
| 4 | 3 | HLXW |  | Portfolio investment |
| 4 | 4 | JX97 |  | Financial derivatives |
| 4 | 5 | HLYD |  | Other investment |
| 4 | 6 | HBQB |  | Total international investment position |
| 5 | 2 | N2SA |  | Direct investment |
| 5 | 3 | HHZF |  | Portfolio investment |
| 5 | 4 | XBMN |  | Other investment |
| 5 | 5 | HBNS |  | Total financial account transactions |
| 6 | 2 | N2Q4 |  | Direct investment |
| 6 | 3 | HLZC |  | Portfolio investment |
| 6 | 4 | HLZN |  | Other investment |
| 6 | 5 | HMBO |  | Total investment income |
| 7 | 2 | MU7O |  | Direct investment |
| 7 | 3 | CGNH |  | Portfolio investment |
| 7 | 4 | JX98 |  | Financial derivatives |
| 7 | 5 | CGNG |  | Other investment |
| 7 | 6 | LTEB |  | Reserve assets |
| 7 | 7 | HBQC |  | Total net international investment position |
| 8 | 2 | MU7M | - | Direct investment |
| 8 | 3 | HHZD | - | Portfolio investment |
| 8 | 4 | ZPNN | - | Financial derivatives |
| 8 | 5 | HHYR | - | Other investment |
| 8 | 6 | LTCV | - | Reserve assets |
| 8 | 7 | HBNT | - | Total net financial account transactions |
| 9 | 2 | MU7E |  | Direct investment |
| 9 | 3 | HLZX |  | Portfolio investment |
| 9 | 4 | CGNA |  | Other investment |
| 9 | 5 | HHCB |  | Reserve assets |
| 9 | 6 | HMBM |  | Total net investment income earnings |

## 후속 작업 권고

1. **Phase 2.2 통합 CSV의 ITEM_CODE1 자동 채움**: 본 사전의 (sheet, sub_table, column_position) 트리플을 long-form 변환 파이프라인의 left-join 키로 사용하면, 데이터 셀마다 CDID를 부착할 수 있다. ECOS ITEM_CODE1 = CDID 직결 가능 (수작업 매핑 0건).
2. **부호 반전 자동화**: sign_prefix=true 행 59건(고유 21 CDID)은 적재 시 값에 -1 을 곱해 정규화하거나, 부호 보존 컬럼을 별도 유지. Table_J(22행)와 Table_R3(12행)이 압도적이며 모두 financial account/IIP revision 영역.
3. **ONS Time Series API 검증 표본**: 무작위 5~10개 CDID에 대해 https://api.ons.gov.uk/timeseries/{cdid}/dataset/PN2/data 호출 후 xlsx 값과 대조. PN2(Pink Book) 데이터셋이 본 Bulletin Tables와 동일 시계열 ID 체계를 공유.
4. **중복 CDID 처리 규약 명시**: 95개 CDID가 2개 이상 시트에 출현. (a) 본표(Table_B/C/E~K) → 정본, (b) Table_A → 요약 사본, (c) Table_R1/R2/R3 → revision 사본. 적재 시 origin 컬럼을 부여해 source-of-truth를 명시 권고.
5. **Table_J 부호 prefix 22행 검증**: Notes Table A note 1 외에 Table_J 자체 헤더(2~5행)에 부호 규약 보강 텍스트가 있는지 12회차 인벤토리 메모에 추가 권고.

## 출처·재현

- 입력: db/source/balanceofpayments2025q4.xlsx (read-only)
- 인벤토리: background/note/12_xlsx_sheet_inventory.csv
- 코드: db/code/source/extract_cdid.py (env/, openpyxl 3.1.5)
- 실행: `env/Scripts/python.exe db/code/source/extract_cdid.py` → CSV+MD 동시 갱신
