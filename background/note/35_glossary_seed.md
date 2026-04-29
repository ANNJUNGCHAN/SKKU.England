# 35회차 — Phase 4.1 §10 통계 용어 사전 1차 시드

본 노트는 `db/CHECKLIST.md` Phase 4.1 §10번([background-search] 통계 용어 사전 1차 시드 한국어 정의·출처 요청) 산출물. 강의 자료(BoP.pptx 31 슬라이드) + 노트 02·03·04·05·06·07·12·13·14·19·24·25·26·27·28을 종합한 30개 용어 시드.

---

## §1 1차 시드 30개 — Phase 4 `term_dict` 테이블 시드

| term_id | term_kr | term_en | definition_kr | source |
|---|---|---|---|---|
| **BOP** | 국제수지(국제수지표) | Balance of Payments | 일정 기간 거주자–비거주자 간 모든 경제거래를 복식부기 원리로 기록한 flow 통계. 경상·자본·금융 3대 축. 사후적으로 전 계정 합 ≡ 0. | BoP.pptx slide 4-7,13; note/02; note/07 |
| **IIP** | 국제투자대조표 | International Investment Position | 특정 시점의 대외자산 잔액과 외국인의 자국 투자 잔액을 나타낸 stock 통계. ΔIIP = 거래요인(BoP FA+RA) + 비거래요인(가격·환율 재평가). | BoP.pptx slide 25; note/05 |
| **CA** | 경상수지 | Current Account | 상품·서비스·1차소득·2차소득 4 하위의 합. 흑자(+)는 생산>지출, 적자(−)는 생산<지출. | BoP.pptx slide 5,10,14; note/02; note/07 |
| **KA** | 자본수지 | Capital Account | 비생산·비금융자산(토지·지하자원·상표) 취득·처분 + 자본이전(채무면제·자본보조금·일회성). 영국 very small. | BoP.pptx slide 5,7,14; note/27 §1; note/07 |
| **FA** | 금융계정 | Financial Account | 자산·부채 소유권 변동 거래. 직접·증권·파생·기타·준비자산 5분류. 광의 FA = 비준비 FA + 준비자산. FA = NAFA − NIL + Net derivatives. | BoP.pptx slide 5,6,14; note/06; note/07 |
| **NEO** | 오차 및 누락 | Net Errors and Omissions | 통계 작성 자료원 격차·잔차 사후 조정. 강의 항등식은 NEO=0 가정. 영국 분기 |NEO| 평균 5.9bn £. | BoP.pptx slide 6,13; note/04; note/20 |
| **TG** | 상품수지 | Trade in Goods / Balance of Goods | 재화 수출입 순액. BPM6 일반상품·중계무역·비통화용 금 3분류. 양변 FOB(수입은 CIF→FOB 조정). | BoP.pptx slide 5,9,21; note/02; note/26 §2 |
| **SV** | 서비스수지 | Balance on Services | 운수·여행·로열티·금융 등 서비스 수출입 순액. EBOPS 2010 12분류(SA~SL). | BoP.pptx slide 5,9; note/02; note/24 |
| **PI** | 1차소득수지(본원소득) | Primary Income | 노동·자본 등 생산요소 제공 대가성 소득(임금·배당·이자) 순액. 구성: COE + 투자소득(직접·증권·기타·준비자산) + 기타. | BoP.pptx slide 5,9,25; note/02; note/27 §2 |
| **SI** | 2차소득수지(이전소득) | Secondary Income | 원조·국제기구출연금 등 대가 없는 무상 경상이전 순액. 일반정부(EU·UN·ODA) + 기타 부문(개인이전·workers' remittances 메모·비생명보험). | BoP.pptx slide 5,9,14; note/02; note/27 §3 |
| **DI** | 직접투자 | Direct Investment | 외국기업 경영 지배·영향력 행사 목적의 국경 간 투자. BPM6/OECD BD5 의결권 10% 임계. 하위: Equity / Reinvested earnings / Debt instruments. | BoP.pptx slide 6; note/06; note/25 §1 |
| **PINV** | 증권투자 | Portfolio Investment | 직접·준비자산에 포함되지 않는 양도 가능한 지분증권·부채증권 거래·포지션. 의결권 10% 미만, 가치증가 목적. 만기·발행자부문별 분해. | BoP.pptx slide 6; note/06; note/25 §2 |
| **DR** | 금융파생상품 | Financial Derivatives (and ESOs) | 옵션·선물·스왑 등 기초자산 위험만 거래되는 계약. 유량은 정산금 회전으로 net only(자산·부채 분리 불가); 저량은 시장가치 기준 양면. ESO 포함. | BoP.pptx slide 6,14; note/06; note/25 §3; note/19 |
| **OI** | 기타투자 | Other Investment | 직접·증권·파생·준비자산 외 잔여 금융 거래·포지션. 7 sub: Other equity / Currency-deposits / Loans / Insurance·pension / Trade credit / Other receivable·payable / SDR allocations(부채). | BoP.pptx slide 6; note/06; note/25 §4 |
| **RA** | 준비자산 | Reserve Assets | 통화당국이 BoP 조달·외환개입에 사용 가능한 외화표시 대외자산. 4구성: Monetary gold / SDRs / IMF Reserve position / Other. 자산 측만 기록. | BoP.pptx slide 6,12; note/06; note/25 §5 |
| **NFA** | 순대외자산 | Net External / Foreign Assets | 대외자산 − 대외부채. 강의는 두 차원: ① 비준비 FA 흑자 ⇒ NFA↑(slide 11), ② 통화당국 NFA로 (X−IM)=ΔNFA, NFA+DC=H(slide 24). | BoP.pptx slide 11,24; note/05; note/17 |
| **NAFA** | 자산 순취득 | Net Acquisition of Financial Assets | BPM6 부호 규약: 자산 증가 = (+). FA = NAFA − NIL + Net derivatives. ONS Table_J 부표1·D1_3 sub2가 NAFA 측. | BoP.pptx slide 8,14; note/03; note/19 |
| **NIL** | 부채 순발행 | Net Incurrence of Liabilities | BPM6 부호 규약: 부채 증가 = (+). ONS Table_J 부표2·D4_6 sub2가 NIL 측. | BoP.pptx slide 8,14; note/03; note/19 |
| **CDID** | CDID(ONS 시계열 4자리) | Code for Data Identification | ONS 시계열 4자리 영숫자 식별자(예: IKBJ, MU7M, ZPNN). ONS Time Series API 1차 키. 동일 CDID 다중 시트 등재 → (sheet, sub_table, column_position) 트리플 위치 식별. 본 데이터셋 고유 284개. | note/13 (강의 자료 미수록, ONS 표준) |
| **BPM6** | IMF 국제수지 매뉴얼 6판 | IMF BoP and IIP Manual 6th edition | IMF 2009년 발간. 금융계정 자산·부채 증감 기준(자산↑·부채↑ 모두 +), Goods for processing → 서비스 재분류, SDR 배분 부채 인식 등 BPM5 대비 핵심 변경. | BoP.pptx slide 8 ("새로운 매뉴얼"); note/03·25·27 |
| **EBOPS** | EBOPS 2010(서비스 12분류) | Extended BoP Services Classification | UN MSITS 2010·BPM6 §10 표준. 12 카테고리(SA Manufacturing / SB Maintenance / SC Transport / SD Travel / SE Construction / SF Insurance / SG Financial / SH IP charges / SI Telecom·computer·info / SJ Other business / SK Personal·cultural / SL Government). | note/24 (강의 자료 미수록, UN/IMF 표준) |
| **SITC** | SITC Rev.4 | Standard International Trade Classification, Rev.4 | UN 2006년 채택. 10개 1-digit(0 식료품 / 1 음료 / 2 비식용원재료 / 3 광물성연료 / 4 동식물유지 / 5 화학 / 6 원재료별제조품 / 7 기계·운송 / 8 기타제조 / 9 미분류). ONS Pink Book 6묶음(0+1, 2+4, 3, 5+6, 7+8, 9), 9는 비통화용 금 다수. | note/26 §1 (강의 자료 미수록, UN 표준) |
| **PM_ADJ** | 귀금속 보정(Table_BX) | Non-monetary Gold / Precious Metals Adjustment | ONS가 BoP 본표(Table_B)에서 비통화용 금·은·백금·팔라듐 bullion(SITC 9 + SITC 6 일부) 차감해 게재한 보조표. 신설 CDID: FUS7·FUS8·FUS9. NMG는 GDP 중립 처리. | note/26 §4; note/13 Table_BX (강의 자료 미수록, ONS 표준) |
| **CIF_FOB** | CIF/FOB 평가 기준 | CIF / FOB Valuation Basis | FOB(Free on Board) = 수출 관세선 가격(운임·보험 미포함), CIF(Cost-Insurance-Freight) = 수입 도착항 가격(포함). HMRC OTS는 수출 FOB·수입 CIF, BPM6 BoP는 양변 FOB → ONS는 CIF→FOB 조정 후 차감 운임·보험을 서비스(Transport·Insurance)로 재배치. | note/26 §3 (강의 자료 미수록, IMF/ONS 표준) |
| **SIGN_PREFIX** | 부호 반전 prefix | ONS Sign-reversal Prefix | ONS Notes Table A note 1: "reverse the sign of series prefixed with a minus". ` - CDID` patterns 부착 컬럼은 적재 시 부호 반전. 본 데이터셋 59행(고유 21 CDID), Table_J·R3에 집중(financial account/IIP). | note/13 §부호 prefix CDID 목록 (강의 자료 미수록, ONS 표준) |
| **EEA_UK** | EEA(영국 환평형계정) | UK Exchange Equalisation Account | 1932년 설립, HMT 명의로 BoE가 대리 운용하는 영국 공식 외환보유고 계정. 외화·금·SDR·IMF Reserve Position. 2025-10 net USD 112.4 bn(GBP 85.5 bn). 영국 BoP "Reserve Assets" 직접 연결. | note/17; note/25 §5 (강의 자료 미수록, HMT/BoE 표준) |
| **ITIS** | ITIS(국제 서비스무역 조사) | Quarterly Survey of International Trade in Services | ONS 분기 서비스무역 조사. 영국 BoP Trade in services(Table_F)·Pink Book Ch.3 핵심 자료원. 운송·여행·금융은 ITIS 제외(자체 조사·IPS·BoE 보강). | note/22; note/24 §1 자료원 분담 (강의 자료 미수록, ONS 운영) |
| **IPS** | IPS(국제여객조사) | International Passenger Survey | ONS 연속 여객 조사(연 362일). BoP Travel 항목(서비스 약 8%) 핵심 자료원. ITIS 제외 영역 — IPS가 여행 수지·관광 통계 1차 자료. | note/22; note/24 §4 (강의 자료 미수록, ONS 운영) |
| **HMRC_OTS** | HMRC OTS(영국 관세청 무역통계) | HMRC Overseas Trade Statistics | HMRC 월간 상품무역 통계. BoP Trade in goods(Table_E)·Pink Book Ch.2 사실상 전부. HS 8-digit → SITC Rev.4. 저액 거래(£873↓) SITC 931 일괄. ONS는 CIF→FOB 조정 후 BoP 반영. | note/22; note/26 §5 (강의 자료 미수록, GOV.UK 운영) |
| **PINK_BOOK** | ONS Pink Book(영국 BoP 연간) | UK Balance of Payments — The Pink Book | ONS 매년 가을(통상 10월 말, 2025년판 2025-10-31) Blue Book과 동시 발간 연간 BoP·IIP 종합 보고서. AFSS·연간 ITIS·AIFDI/AOFDI·SUT 흡수. 2025년판은 2021년 이후 전 기간 일괄 개정. | note/22; note/28 §1.3 (강의 자료 미수록, ONS 운영) |

---

## §2 출처 분류

### 강의 자료 직접 인용 — 16개

용어 BOP·IIP·CA·KA·FA·NEO·TG·SV·PI·SI·DI·PINV·DR·OI·RA·NFA — 모두 강의 슬라이드 4~25에서 정의/식 명시.

### 외부 표준(노트 24~28 보강) — 14개

NAFA·NIL: 노트 03·19 / CDID·SIGN_PREFIX: 노트 13 / BPM6: 노트 03·25·27 / EBOPS: 노트 24 / SITC: 노트 26 / PM_ADJ·CIF_FOB: 노트 26 / EEA_UK: 노트 17·25 / ITIS·IPS: 노트 22·24 / HMRC_OTS: 노트 22·26 / PINK_BOOK: 노트 22·28.

---

## §3 Phase 4 용어 사전 테이블 시드 CSV 형식

```
term_id,term_kr,term_en,definition_kr,source
BOP,"국제수지(국제수지표)","Balance of Payments","일정 기간 ...","BoP.pptx slide 4-7,13; note/02; note/07"
IIP,"국제투자대조표","International Investment Position","특정 시점의 ...","BoP.pptx slide 25; note/05"
... (이하 28행)
```

`term_id` PK, `definition_kr` 1~2문장 원칙 유지(긴 정의는 §4·§5 cross-ref로 위임).

---

## §4 출처 카탈로그

| 자료 | 사용 |
|---|---|
| `BoP.pptx` (전 31장) + slide_images | 16개 강의 직접 인용 용어 |
| `note/02·05·06·07·13·17·22·24·25·26·27·28` | 14개 외부 표준 보강 용어 |

---

## §5 확인 못한 부분 (정직 명시)

1. **term_id 표준화 충돌** — PI(1차소득) vs PINV(증권투자), DR(파생) vs FD 등 약어 충돌 가능 → Phase 4.2 ITEM_CODE 정합 검증 필요.
2. **DR vs FD** — ONS·BPM6 통상 약어 FD/FDESO. 본 시드는 DR 채택. alias 컬럼 추가 권고.
3. **RA = Reserve Assets** vs 강의 IR 표기 — cross-reference 필요.
4. **CDID·BPM6·EBOPS·SITC·CIF_FOB·SIGN_PREFIX 6 항목** — 강의 자료 미수록, 노트 외부 출처 인용. `definition_external_url` 컬럼 추가 검토.
5. **PM_ADJ term_id 표기** — 영문 약어 도입(원래 한국어 "귀금속 보정"). PK 정규화.
6. **EEA_UK term_id 충돌 회피** — European Economic Area·European Environment Agency 등 동음이의 다수 → `EEA_UK` 채택.
7. **ITIS·IPS·HMRC_OTS·PINK_BOOK 4 운영자료** — 노트별 정의 cross-validation 필요.
8. **NFA 영문 라벨** — Net External Assets vs Net Foreign Assets 노트별 차이 → Phase 4.2 표준 라벨 결정.
9. **OECD BD4·BD5 / BIS LBS·CBS / IMF SDDS Plus / EU Withdrawal Agreement** — 본 시드 30개에 미포함. Phase 4.2 자료원 카탈로그 별도 테이블 분리.
10. **시드 정의 길이** — 일부 항목(EBOPS·OI·SI·RA) 2~3문장. `definition_short`/`definition_long` 양 컬럼 도입 검토.
