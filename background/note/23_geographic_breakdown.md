# ONS Pink Book Ch.9·10 지리분해 분류 체계 (web-search 23회차)

본 문서는 `db/CHECKLIST.md` §0.2 신규 低 3번 항목(ONS 국가별 geographical breakdown Pink Book Ch.10·11 분류 체계 — EU/non-EU 분해 시트 매핑 사전)의 산출물이다.

**챕터 번호 보정**: 사용자 메모와 10회차 매핑표의 "Ch.10·11"은 ONS 공식 데이터셋 URL과 비교 결과 **Ch.9 (Geographical breakdown of current account) + Ch.10 (Geographical breakdown of IIP)** 가 정확하다. 10회차 표 #7과 12회차 매핑표는 보정 대상.

## 요약

1. ONS Pink Book에서 지리분해는 **Ch.9 (경상수지)·Ch.10 (IIP)** 이다.
2. Pink Book 지리분해는 **약 67개 개별국 + 국제기구**, 그리고 **5개 대륙(Europe·Americas·Asia·Australasia & Oceania·Africa)** 과 **EU 집계**를 포함.
3. EU 집계는 **Brexit 이후(2020-02-01부터) EU27 기준**(영국 제외)으로 전환되었고, 과거에는 EU28(영국 포함)이었다. ONS는 시계열을 EU27로 재정의해 발표 중.
4. 본 저장소 BoP Statistical Bulletin Tables의 **Table_C(6 부표)** 는 분기 단위 EU vs non-EU 분해이며, Pink Book Ch.9의 **EU/non-EU 합계 라인**과 1:1 대응(개별국 분해는 Ch.9 데이터셋에만 존재).
5. OECD·G7·BRICS·OPEC 같은 그룹은 Pink Book Ch.9·10 표준 표에는 명시되지 않으며, EU·non-EU·대륙·개별국이 기본 축이다.

## 1. Pink Book Ch.9·10 국가·지역 그룹

| 분류 축 | 항목 | 비고 |
|---|---|---|
| 대륙 | Europe / Americas / Asia / Australasia & Oceania / Africa | Pink Book Ch.9·10 공통, IIP rate-of-return 분석에도 사용 |
| 정치·통화 집계 | EU (현 EU27) | Brexit 후 EU27 기준 |
| 개별국 (총 ~67개국) | USA, Germany, France, Netherlands, Ireland, Belgium, Luxembourg, Italy, Spain, Switzerland, Norway, Japan, China, South Korea, Australia 등 | ONS 공식 표현 "covers 67 individual countries as well as international organisations" |
| 기타 | International Organisations | EU·UN 등 비국가 거주자 카운터파트 |

OECD·G7·BRICS·OPEC 등은 Pink Book Ch.9·10 본표에서는 표준 분류로 등장하지 않으며, 필요 시 Ch.9 개별국 데이터로 사용자 측 집계가 일반적 관행.

## 2. EU/non-EU 정의 변경 (Brexit)

- **2020년 1월 31일까지**: ONS 시계열 코드 명칭에 "EU 28" 사용(예: 시계열 `L84Z` "Exports trade goods & services Non. EU 28 SA"). Table_C도 과거에 EU28 기준으로 표기.
- **2020년 2월 1일 이후**: 영국 EU 탈퇴로 EU 정의가 **EU27(영국 제외)** 로 전환.
- ONS Pink Book 2025(2025-10-31 발표) 및 분기 BoP 보도자료의 EU 합계는 **EU27** 기준이며, 시계열은 일관성을 위해 과거 구간도 EU27으로 재계산.
- 27개 EU 회원국: Belgium, Bulgaria, Czech Republic, Denmark, Germany, Estonia, Ireland, Greece, Spain, France, Croatia, Italy, Cyprus, Latvia, Lithuania, Luxembourg, Hungary, Malta, Netherlands, Austria, Poland, Portugal, Romania, Slovenia, Slovakia, Finland, Sweden.

## 3. Pink Book Ch.9 개별국 (확인 범위)

검색에서 Pink Book 본문이 명시적으로 호명한 주요국: **USA, Germany, France, Netherlands, Ireland, Belgium, Luxembourg, Italy, Spain, Switzerland, Norway, Japan, China, South Korea, Australia**. 전체 67개국 명단은 본 검색에서 텍스트로 확보하지 못했고, **xlsx 다운로드(2025년 10월 31일판)** 의 시트 헤더를 직접 열람해야 확인 가능.

## 4. 본 저장소 Table_C ↔ Pink Book Ch.9 매핑 가능성

저장소 인벤토리(12회차)에서 확인된 사실:

- Table_C: 898행 × 20열, **6 부표**, 경상수지 EU/non-EU, GBP million, 1997~2025 분기.
- 12회차 매핑표는 Table_C → "Ch.10 Geographical breakdown of CA, EU vs non-EU"로 기록되어 있으나 실제는 **Ch.9** (Ch.10은 IIP). 보정 필요.

**Table_C 6 부표 추정 매핑** (Pink Book Ch.9 표준 구조에 비추어 — 실제 시트 헤더로 확정 필요):

| 부표 (추정) | 내용 (추정) | Pink Book Ch.9 대응 |
|---|---|---|
| Table_C 부표 1 | Trade in goods, EU vs non-EU (credits·debits·balance) | Ch.9 goods 지리분해 합계 |
| Table_C 부표 2 | Trade in services, EU vs non-EU | Ch.9 services 지리분해 합계 |
| Table_C 부표 3 | Primary income, EU vs non-EU | Ch.9 primary income 합계 |
| Table_C 부표 4 | Secondary income, EU vs non-EU | Ch.9 secondary income 합계 |
| Table_C 부표 5 | Current account total, EU vs non-EU | Ch.9 CA 총계 |
| Table_C 부표 6 | (가능성) Memo: total EU27, total non-EU, total world | Ch.9 footnote/aggregate |

분기 Table_C는 EU·non-EU 2분 축만 제공하고, **Pink Book Ch.9는 동일 항목을 67개 개별국 × 연간**으로 확장 제공하는 관계 — 따라서 분기 Table_C는 "Pink Book Ch.9 EU 합계 라인의 분기 디스어그리게이션"으로 보면 정합적.

## 5. Brexit 영향 (분류 체계 변경 요약)

- **명칭**: "EU 28" → "EU 27" (시계열 라벨 변경, 일부 CDID는 유지된 채 정의만 EU27로 재정의).
- **포함 국가**: 영국이 EU 집계에서 빠짐(2020-02-01).
- **시계열 일관성**: ONS는 과거 구간도 EU27 기준으로 재계산해 단절 없이 비교 가능하도록 처리.
- **Pink Book 2022 이후**: EU27이 표준 표기. Pink Book 2025(2025-10-31 발표)도 EU27 기준.
- **개별국 단위**에는 Brexit 영향 없음 (USA, Germany 등 변수는 그대로).

## 빠진 부분 / 추가 확인 권고

- **67개 개별국 전체 명단** — Pink Book Ch.9 xlsx(2025-10-31판, 729.5 KB) 다운로드 후 시트 헤더 직접 검사 필요.
- **Table_C 6 부표의 정확한 명칭** — 본 저장소 `db/source/balanceofpayments2025q4.xlsx`의 Table_C 시트 헤더(추정 4~7행)를 12회차 인벤토리에서 부분적으로 확인했으나 부표별 정확한 영문 명칭은 직접 추출 필요(Phase 1 시트 인벤토리 보강 단계와 자연 통합).
- **Pink Book Ch.10 (IIP) 부표 구조** — 자산/부채/순포지션, 투자유형(FDI·portfolio·other·reserves) × 국가의 교차표 구조이지만 본 검색에서 67개국 분해의 IIP별 차원 수는 텍스트로 미확인.
- **OECD/G7/BRICS 집계** — Pink Book 본표에 표준 항목으로 등장하지 않음 확인(다른 ONS 데이터셋 또는 OECD/IMF에서 직접 받아야 함).
- **EU27 재계산 시점의 ad-hoc 변경 로그** — `006656balanceofpaymentsannualgeographicaldatatables` 등 ad-hoc 페이지에서 "geographic allocation 보정" 언급되나 EU 정의 전환 시점 공식 기록은 별도 methodology 문서 확인 필요.

## 보정 권고 (선행 산출물 갱신)

- `background/note/10_ons_web_research.md` §발췌 표 #7: "10·11" → "**9·10**" 으로 챕터 번호 보정 권고(별도 단위 작업).
- `background/note/12_xlsx_sheet_inventory.md`/`csv` 매핑표: Table_C → "Ch.10" → "**Ch.9**" 보정 권고(별도 단위 작업).

## 출처

- [UK Balance of Payments, The Pink Book: 2025 (release page)](https://www.ons.gov.uk/releases/ukbalanceofpaymentsthepinkbook2025)
- [UK Balance of Payments, The Pink Book: 2025 (bulletin)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025)
- [09 Geographical breakdown of the current account, The Pink Book (dataset)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/9geographicalbreakdownofthecurrentaccountthepinkbook2016)
- [10 Geographical breakdown of the UK international investment position, The Pink Book (dataset)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/10geographicalbreakdownoftheukinternationalinvestmentpositionthepinkbook2016)
- [Pink Book Part 3 — Geographical Breakdown (2014 compendium)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/compendium/unitedkingdombalanceofpaymentsthepinkbook/2014-10-31/part3geographicalbreakdown)
- [Balance of Payments annual geographical data tables (ad-hoc)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/adhocs/006656balanceofpaymentsannualgeographicaldatatables)
- [International Investment Position: UK assets and liabilities by country, 2006–2021 (interactive)](https://www.ons.gov.uk/visualisations/dvc2188/index.html)
- [Exports trade goods & services Non. EU 28 SA (시계열 L84Z, EU28 명칭 잔존 예시)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/l84z/pnbp)
- [Balance trade goods & services EU SA (시계열 L86I)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/l86i/pnbp)
- [Bop:Total Current Account Bal EU sa £m (시계열 L877)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/timeseries/l877/pnbp)
- [Balance of payments QMI (방법론)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpayments)
- [EU 27 — Wikipedia (Brexit 후 정의 변천)](https://en.wikipedia.org/wiki/EU_27)
- [The EU27: Internal Politics and Views on Brexit — House of Commons Library](https://commonslibrary.parliament.uk/research-briefings/cbp-8362/)
- [UK Balance of Payments, The Pink Book: 2025 — GOV.UK](https://www.gov.uk/government/statistics/uk-balance-of-payments-the-pink-book-2025)
