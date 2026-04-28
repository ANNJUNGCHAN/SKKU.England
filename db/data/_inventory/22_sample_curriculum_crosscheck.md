# 통합 long-form CSV 표본 5+1건 강의 자료 교차 점검 (Phase 2.2 §2.4 검증)

본 문서는 db/CHECKLIST.md §2.4 세 번째 항목(통합 CSV의 표본 5건을 추출해 강의 자료의 BoP 정의와 일치하는지 교차 점검)의 산출물이다. 1차 근거는 db/data/balanceofpayments2025q4_long.csv (74,006행 × 14컬럼)와 background/BoP.pptx (31 슬라이드) + background/note/02_bop_components.md, 06_financial_account_categories.md, 07_glossary.md, 13_cdid_dictionary.csv, 14_slide_28_29_analysis.md 이다.

## 1. 요지

- 강의 자료의 BoP 5대 핵심 변수(경상수지 합계 / 상품수지 / 서비스수지 / 1차소득 잔액 / 금융계정 합계)에 대응하는 통합 CSV의 표본 5건을 2025 Q4 시점으로 추출, 5건 모두 STAT_NAME·CDID·sub_table·data_value가 강의 정의와 정합(✓).
- 강의 슬라이드 14의 항등식 CA = trade balance + balance on services + net primary income + net secondary income 을 통합 CSV Table_B sub3 값으로 검증한 결과 −65,496 + 53,335 + (−2,674) + (−3,557) = −18,392 으로 정확히 일치(HBOP 셀과 잔차 0).
- Table_J sub_table=3(Net Transactions) 부호 prefix 처리 표본(-MU7M Net direct investment) 1건도 추가 검증, sign_prefix=true 컬럼이 item_code1 앞에 - 를 붙여 보존되며 BPM6 자산·부채 증감 기준 부호 규약(슬라이드 8)과 정합. 5분류 합계 항등식 (−MU7M)+(−HHZD)+(−ZPNN)+(−HHYR)+(−LTCV) = −HBNT 도 정확히 일치(−9,371).
- §2.4 §3 통과: 통합 CSV는 강의 자료의 한국어 BoP 개념·항등식·부호 규약과 1:1 정합. ONS 영문 라벨과 강의 한국어 라벨 사이 용어 차이(예: Primary Income vs 본원소득) 외에는 보정 사항 없음.

## 2. 표본 5+1건 추출(2025 Q4)

| # | 항목(강의) | sheet | sub_table | item_code1 | time | STAT_NAME(통합 CSV) | data_value | 강의 정의 인용(요지) | 정합 평가 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 경상수지 합계 (Current Balance) | Table_B | 3 | HBOP | 2025Q4 | 영국 경상수지 (전체, 계절조정) | −18,392 | 슬라이드 14 Current account = trade balance + balance on services + net primary income + net secondary income / 슬라이드 5 경상계정: 재화 및 용역 등 실물거래 기록 | ✓ |
| 2 | 상품수지 (Balance of Goods) | Table_E | 3 | BOKI | 2025Q4 | 영국 상품무역 (수출·수입·수지) | −65,496 | 슬라이드 5 상품수지(Trade balance): 재화의 수출입, net trade in merchandise goods / 슬라이드 21 차트 Balance of Goods | ✓ |
| 3 | 서비스수지 (Balance on Services) | Table_F | 3 | IKBD | 2025Q4 | 영국 서비스무역 (수출·수입·수지, 12분류) | +53,335 | 슬라이드 5 서비스수지(Balance on services): 서비스의 수출입. 운수, 여행, 로열티 등 포함 / 슬라이드 9 한국 BoP 표 | ✓ |
| 4 | 1차소득 잔액 (Primary Income Balance) | Table_G | 3 | HBOJ | 2025Q4 | 영국 1차소득 (본원소득: 보수·투자소득·기타) | −2,674 | 슬라이드 5 본원소득수지(Balance on investment income or primary income): 임금송금, 배당 및 이자 등 / 슬라이드 25 IIP→소득 흐름 | ✓ |
| 5 | 금융계정 합계 (Total net investment) | Table_J | 3 | -HBNT | 2025Q4 | 영국 금융계정 (계절미조정) | −9,371 | 슬라이드 14 Financial account = Net acquisition of foreign financial assets − Net incurrence of liabilities + Net financial derivatives / 슬라이드 6 5분류 | ✓ |
| 5+1 (sign_prefix) | 직접투자 순거래 (Net direct investment, Total) | Table_J | 3 | -MU7M | 2025Q4 | 영국 금융계정 (계절미조정) | −1,576 | 슬라이드 6 직접투자(direct investment): 외국기업에 자금을 투입하여 경영에 참가하기 위해 행하는 투자 / 슬라이드 8 자산·부채 증감 기준 부호 prefix | ✓ |

## 3. 강의 정의와의 정합성 분석 (5건)

### #1 경상수지 합계 — Table_B sub3 / HBOP

통합 CSV의 STAT_NAME은 영국 경상수지 (전체, 계절조정) 이며, 강의 슬라이드 5 경상계정(Current account): 재화 및 용역 등 실물거래 기록 과 슬라이드 14의 항등식 Current account = trade balance + balance on services + net primary income + net secondary income 에서 좌변 합계와 직접 대응한다. ONS의 column_label은 Current balance 로, 강의 한국어 경상수지의 영문 표기와 일치. 더욱이 Table_B sub3의 4개 구성요소(BOKI, IKBD, HBOJ, IKBP)를 합산하면 정확히 HBOP(−18,392)가 산출되어 슬라이드 14 항등식이 1차 근거에서 즉시 검증된다.

다만 강의 슬라이드 5는 경상계정을 상품수지·서비스수지·본원소득수지·이전소득수지의 4개 하위로 분류하는 반면, ONS Table_B 컬럼 라벨은 Trade in goods / Trade in services / Primary income, Total / Secondary income, Total 로 다르게 표기된다. 항목 의미는 동일하나 한국어 강의 라벨과 영문 ONS 라벨 간 자동 매칭이 어려우므로 명세서/REPORT 작성 시 양쪽 라벨을 병기하는 것이 권장된다(STAT_NAME이 한국어로 보존되어 있으므로 매칭 보정은 최소).

### #2 상품수지 — Table_E sub3 / BOKI

통합 CSV의 STAT_NAME 영국 상품무역 (수출·수입·수지) 은 강의 슬라이드 5의 상품수지(Trade balance): 재화의 수출입, net trade in merchandise goods 정의와 정합한다. column_label Total goods balance 도 merchandise goods 의 잔액 개념과 일치. CDID BOKI는 Table_A sub1, Table_B sub3, Table_E sub3에서 동일하게 등장(통합 CSV 검색 결과)하여 ONS가 상품수지 단일 시리즈를 표 내내 일관되게 사용함을 확인. 강의 슬라이드 21의 Balance of Goods 시리즈가 본 CDID에 해당.

용어 차이 한 가지: 강의는 상품수지(Balance of goods) = 무역수지(Balance of Trade)로 슬라이드 5에서 동의어처럼 표기하나, 슬라이드 21 차트는 두 시리즈를 별도로 그린다(note/02_bop_components.md §빠진 부분 참조). ONS는 Table_E에서 Balance of Goods 만 다루며, Balance of Trade(상품+서비스 합산)는 별도 표(Table_B sub3 합계나 별도 IKBJ Trade total 시리즈)로 관리. 통합 CSV의 STAT_NAME 상품무역 은 상품수지에 한정된다는 점을 학생에게 명시할 필요.

### #3 서비스수지 — Table_F sub3 / IKBD

STAT_NAME 영국 서비스무역 (수출·수입·수지, 12분류) 은 강의 슬라이드 5 서비스수지(Balance on services): 서비스의 수출입. 운수, 여행, 로열티 등 포함 과 직접 대응. ONS Table_F sub3는 Manufacturing/Transport/Travel/Construction/Insurance/Financial/IP/Telecom/Other business/Personal/Government 등 12개 EBOPS 카테고리로 세분되어 강의의 운수·여행·로열티 등보다 풍부하다. CDID IKBD는 Table_A sub1·Table_B sub3·Table_F sub3에서 일관 사용. 2025 Q4 값 +53,335(GBP million)는 영국이 만성적으로 서비스수지 흑자국임을 재확인하는 수치로, 슬라이드 9의 한국 사례(서비스수지 −34,472)와 부호가 정반대인 점은 영국 BoP 구조 특수성으로 보고서에 부연할 가치가 있다.

용어 차이: 강의는 서비스수지 한 단어, ONS column_label은 Total services balance. STAT_NAME에 12분류 가 명시되어 EBOPS 세분류 정보가 보존된 점은 명세서 작성에 유리.

### #4 1차소득 잔액 — Table_G sub3 / HBOJ

STAT_NAME 영국 1차소득 (본원소득: 보수·투자소득·기타) 은 강의 슬라이드 5 본원소득수지(Balance on investment income or primary income): 임금송금, 배당 및 이자 등 과 의미상 정합한다. ONS는 Table_G sub3에서 Compensation of employees(IJAJ) + Investment income(HBOM) + Other primary income(MT5X) 등 3개 하위로 세분(강의의 보수·투자소득·기타 와 1:1 매핑). 강의 슬라이드 25 BoP는 flow, IIP는 stock 의 연결고리도 CDID HBOJ(투자소득 잔액)와 IIP의 자산·부채 잔액에 대응하는 흐름 측면에서 확인 가능.

용어 차이 주의: 강의 슬라이드 5는 영문을 Balance on investment income **or** primary income 로 표기해 두 용어를 동의어로 사용한다. ONS는 Primary income 으로 일관 표기하며 Investment income은 그 하위 항목(HBOM)이다. 즉 통합 CSV의 1차소득 잔액 = HBOJ가 강의의 본원소득수지 전체에 대응하고, 투자소득만으로 좁히면 HBOM이라는 점에 유의해야 학생 혼동을 방지할 수 있다(note/07_glossary.md 1차소득수지 항목 참조).

### #5 금융계정 합계 — Table_J sub3 / -HBNT

STAT_NAME 영국 금융계정 (계절미조정) 은 강의 슬라이드 5의 금융계정(Financial account): 자산 및 부채의 소유권 변동과 관련된 거래 및 슬라이드 14의 식 Financial account = Net acquisition of foreign financial assets − Net incurrence of liabilities + Net financial derivatives 와 정합. ONS Table_J sub3는 정확히 5분류(Net direct investment / Net portfolio investment / Net financial derivatives / Other net investment / Reserve assets) + 합계(Total net investment, CDID = HBNT)로 구성되어 슬라이드 6의 5분류와 1:1 매핑된다.

핵심 검증: Table_J sub3의 5개 합계 컴포넌트(−MU7M + −HHZD + −ZPNN + −HHYR + −LTCV) = (−1,576) + (−61,488) + (−1,253) + 54,439 + 507 = −9,371 = −HBNT 로 정확히 일치. 즉 광의 금융계정 = 비준비 FA + 준비자산(슬라이드 14)이 본 CSV에서 자동 성립한다. 단, sign_prefix=true이므로 모든 항목이 - prefix와 함께 보존된 점이 특이하며, 이는 ONS 원본 표가 BPM5 순유출입 기준 을 부분적으로 유지(자본유출=−)하는 표기를 채택했고, ETL 단계에서 그 부호를 반전시키지 않고 prefix로 명시한 결과로 해석된다(상세는 §4).

용어 차이: 강의는 금융계정 한 단어, ONS는 Total net investment(net 표현). 또한 강의 5분류 한국어(직접투자·증권투자·파생금융상품·기타투자·준비자산증감)와 ONS 영문 라벨(Direct/Portfolio/Derivatives/Other/Reserve) 간 매핑은 note/06_financial_account_categories.md 에 정리되어 있어 보정 별도 불필요.

## 4. sign_prefix 처리 표본 검증 — Table_J -MU7M (Net direct investment, Total)

**1차 사실 점검**: 통합 CSV에서 sheet=Table_J, sub_table=3, item_code1=-MU7M, time=2025Q4 의 행은 STAT_NAME=영국 금융계정 (계절미조정), unit_name=GBP_million, data_value=−1,576 로 보존되어 있다. item_code1 이 MU7M 이 아니라 -MU7M(앞에 하이픈)으로 저장된 점이 핵심이며, 이는 15_master_inventory.csv 의 sign_prefix=true 플래그가 long-form 변환 시 코드 자체에 prefix로 옮겨졌음을 보여준다.

**부호 규약 정합성(슬라이드 8 vs BPM6)**: 강의 슬라이드 8은 새로운 매뉴얼에서는 금융계정 부호표기 방식을 자산·부채의 증감 기준 으로 변경, 자산 항목의 부호는 반대 방향으로 바뀜 이라고 명시한다. ONS 원본 Table_J sub3는 컬럼 헤더 위에 − 부호가 붙은 CDID(예: −MU7M)를 두어, 셀 값 자체는 BPM5(순유출입 기준)로 표기되어 있되 BPM6 부호로 읽으려면 부호를 반전해야 함을 표 차원에서 시그널링한다. ETL이 이를 item_code1 에 prefix로 보존한 결과, 분석자는 다음 두 방식 중 하나로 처리할 수 있다.

1. **prefix 무시 + 셀 값 그대로** (BPM5 부호로 해석): 강의 슬라이드 9 우측 표 이전 매뉴얼 기준 과 동일한 부호 규약. 자국 자본 유출 = 양(+).
2. **prefix 적용(셀 값 부호 반전)** (BPM6 부호로 해석): 강의 슬라이드 9 좌측 표 최근 매뉴얼 기준 과 동일. 자산 증가 = 양(+), 자본 유출 = 음(−).

-MU7M 의 셀 값 −1,576을 그대로 두면(방식 1) 영국이 2025 Q4에 직접투자 자본을 1,576 GBP million 순유입한 것으로 해석되고, 부호를 반전하면(방식 2) 영국 거주자의 해외 직접투자 자산이 1,576 GBP million 순감소한 것으로 해석된다. 어느 방식이 강의 항등식 CA = FA(broad) 와 일관된지 확인하면, 2025 Q4 CA(HBOP) = −18,392, FA(broad, -HBNT) = −9,371, E&O(HHDH)·KA(FNVQ)를 합산해 잔차가 통계불일치 범위 내인지 점검 가능. **강의 자료(슬라이드 8)와의 정합 결론**: sign_prefix는 BPM5↔BPM6 부호 규약 차이를 ETL 차원에서 명시적으로 보존한 것으로, 강의 슬라이드 8의 자산 항목 부호 반전 진술과 직접 일치. 즉 item_code1 의 - prefix는 이 셀을 BPM6로 해석하려면 부호 반전 신호로 읽으면 강의 정의와 1:1 정합한다.

**보정 권고**: REPORT.md/명세서에서 Table_J 시리즈를 사용할 때 (a) BPM5 표기 셀 값과 (b) BPM6 해석 부호 반전 값을 양쪽 컬럼으로 명기하거나, 분석 단계에서 sign_prefix=true 플래그를 자동 적용해 부호를 반전한 추가 컬럼(data_value_bpm6 등)을 만들 것. 현재 long CSV는 (a)만 보존하고 (b)는 prefix 시그널로 위임하므로, Phase 3 명세서에서 이 처리 규칙을 표준 절차로 고정해야 한다.

## 5. 결론

**§2.4 §3 통과 단정**: 통합 CSV의 5+1건 표본은 강의 자료(BoP.pptx 슬라이드 5·6·8·9·14·21·25)의 한국어 BoP 정의·항등식·부호 규약과 1:1 정합하며, 잔차 0의 항등식 검증(CA, FA 양쪽)에서도 데이터 무결성이 확인되었다. STAT_NAME에 한국어 통계표명이 보존되어 강의 자료와의 매칭이 즉시 가능하며, sub_table·item_code1·time·data_value의 모든 차원에서 강의 변수와 1:1 대응이 성립한다.

**잔여 보정 권고**:

1. (高) sign_prefix=true CDID 약 70여 개(Table_A sub3, Table_J sub1, Table_J sub3 전체 등)에 대해 BPM6 부호 적용 컬럼 추가 — 분석자가 prefix를 직접 다루지 않아도 되도록 ETL 단계에서 data_value_bpm6 보조 컬럼 도입 검토.
2. (中) Balance of Goods vs Balance of Trade 용어 차이 → 강의 슬라이드 21이 두 시리즈를 동시 표기하나 정의 텍스트가 결여 → REPORT.md 각주 또는 용어집에 명시.
3. (中) Primary Income(HBOJ) 전체와 그 하위 Investment Income(HBOM)의 강의 영문 표기 혼용 → 명세서에서 본원소득=HBOJ, 투자소득=HBOM 을 명시 분리.
4. (低) Table_F sub3의 EBOPS 12분류는 강의 자료(슬라이드 5의 운수·여행·로열티 등)보다 상세 → Phase 3 명세서에서 12분류 정의를 외부(MSITS 2010) 보강 권장(note/07_glossary.md 미정의 표제어 中급 우선순위).

## 6. 출처

- 통합 CSV: db/data/balanceofpayments2025q4_long.csv (74,006행 × 14컬럼, Phase 2.2 산출물)
- CDID 사전: background/note/13_cdid_dictionary.csv (512행)
- 강의 슬라이드: background/BoP.pptx 슬라이드 5(BoP 5대 구성), 6(FA 5분류), 8(부호 규약 변경), 9(한국 BoP 표 신·구 매뉴얼 비교), 14(항등식), 21(Balance of Goods·Trade 차트), 25(BoP↔IIP)
- 멀티모달 노트: background/slide_images/slide_05.png, slide_06.png, slide_08.png, slide_09.png, slide_14.png, slide_21.png, slide_25.png
- 강의 정의 발췌: background/note/02_bop_components.md §발췌표, background/note/03_sign_conventions.md §항목별 발췌, background/note/06_financial_account_categories.md §분류별 발췌, background/note/07_glossary.md BoP_구성/금융계정/부호규약 섹션, background/note/14_slide_28_29_analysis.md (J-curve 부수 검증)
- 통합 CSV 마스터 인벤토리: db/data/_inventory/15_master_inventory.csv (sign_prefix 플래그 출처)
- 부호 규약·금 거래 보정 분석: db/data/_inventory/19_signs_gold_revisions.md
