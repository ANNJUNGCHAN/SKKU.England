# 영국 ONS BoP 특화 분류·표기 규칙 웹 조사 결과 (web-search 10회차)

본 문서는 `db/CHECKLIST.md` §0.2 라인 29 항목(`[web-search]` 영국 ONS 특화 분류·세분류·표기 규칙 검색 후 background_note 업로드)의 산출물이다. `07_glossary.md`에 미정의·부분 정의로 남아 있던 항목을 영국·국제기구 1차 출처에서 보강했다.

## 요약

- 우선순위 高 5개 항목은 IMF BPM6 본문·ONS Pink Book·ONS BoP 방법론 페이지에서 모두 1차 출처로 확정(충족율 5/5).
- 우선순위 中 5개 중 EBOPS 12분류, 분기 발표 일정·개정 정책, CDID(4자 영문코드) 명세, ONS 결측 표기 가이드는 확정. Pink Book 표 식별자 `D1_3·D4_6·BX·K` 등은 부분 확정(Pink Book 챕터 1~11 구조까지만 공식 페이지에 노출, 세부 표 코드는 xlsx 본문에서만 확인 가능) — 충족율 약 4/5.
- 핵심 보강 포인트: 항등식 부호 약속은 BPM6에서 `CA + KA − FA + NEO = 0` 형태(금융계정 부호반전 후 NEO 산출), 직접투자 임계 정의는 BPM6 §6.12 "10 percent or more of the voting power" 정문(定文) 확보.
- ONS는 결측 표기로 `..` `-` 사용을 권장하지 않으며, "NA" 표현도 모호성 사유로 회피하라는 자체 콘텐츠 가이드를 보유.
- Pink Book 챕터 구조는 1.Main points → 2.Economic commentary → 3.Trade in goods → 4.Trade in services → 5.Primary income → 6.Secondary income → 7.Capital account → 8.Financial account → 9.IIP → 10·11.Geographical breakdown으로 공식 확인됨.

## 항목별 발췌 표

| # | 항목 | 정의 (영문 발췌 + 한국어 풀이) | 출처 URL | 07_glossary 매핑 |
|---|---|---|---|---|
| 1 | **BoP 항등식·부호** | "The sum of the current and capital account balances is equal to the balance of the financial account." (ONS) / "Under BPM6, **net errors and omissions are calculated as the balance on the financial account minus the sum of the balances on the current and capital accounts**" → 즉 `CA + KA − FA + NEO = 0` (FA는 자산순취득 기준 양수). | [ONS Summary of BoP](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpayments), [Eurostat BPM6 metadata](https://ec.europa.eu/eurostat/cache/metadata/en/bop_6_esms.htm) | "경상수지", "자본수지", "금융계정", "오차 및 누락" 표제어의 항등식 박스 |
| 2 | **FDI 10% 임계** | BPM6 §6.12: "immediate direct investment relationships arise when a direct investor directly owns equity that entitles it to **10 percent or more of the voting power** in the direct investment enterprise." 10~50% 보유 시 associate(연관기업), 50% 초과 시 subsidiary. | [IMF DITT D.10 가이드](https://www.imf.org/-/media/files/data/statistics/bpm6/ditt/d10-defining-the-boundaries-of-direct-investment.pdf), [BOPCOM 04/31](https://www.imf.org/external/pubs/ft/bop/2004/04-31.pdf) | "직접투자(Direct Investment)" 표제어 — 10% 임계, associate/subsidiary 구분 추가 |
| 3 | **거주자/비거주자** | "A resident institutional unit … has a **centre of (predominant) economic interest** in the economic territory of a country." 운용 기준은 **"actual or intended location for one year or more"**. ONS는 동일 BPM6/SNA 정의를 따름. | [Eurostat Glossary: Resident institutional unit](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Resident_institutional_unit), [IMF BPM Ch.4](https://www.imf.org/external/np/sta/bop/pdf/chap4.pdf) | "거주자(Resident)" 표제어 — "1년 이상" 기준·"중심적 경제이익" 명시 |
| 4 | **분개 예시** | 이중기입(Double-entry): "every transaction is represented by two entries with equal values but opposite signs, a debit (−) and a credit (+)." 상품수출 예: 경상계정 Goods **credit (+)**, 금융계정 외환자산 증가 **debit/asset acquisition (+)**. (러시아→폴란드 자동차 수출 예시) | [BIS IFC Bulletin 52](https://www.bis.org/ifc/publ/ifcb52_07.pdf), [BoJ BPM6 설명](https://www.boj.or.jp/en/statistics/outline/exp/exbpsm6.htm) | "분개(Journal Entry)" 신설 또는 "이중기입" 박스 추가 |
| 5 | **Trade in goods vs Trade balance** | ONS UK Trade: "Trade in goods reports … general merchandise, goods for processing, repairs on goods, goods procured in port and non-monetary gold." Total trade balance = goods + services. 예: 2025Q4 total trade deficit 2.2bn = goods deficit 55.5bn − services surplus 53.3bn. | [ONS UK Trade Glossary PDF](https://www.ons.gov.uk/file?uri=%2Feconomy%2Fnationalaccounts%2Fbalanceofpayments%2Fmethodologies%2Fuktrade%2Ftradeglossarytcm77422528.pdf), [ONS UK Trade bulletin](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/uktrade/february2025) | "상품수지" vs "총무역수지" 표제어 분리 |
| 6 | **CDID 체계** | "the **four-character variable code**, which ONS refers to as the variable's CDID" — 영문 4자(예: **MGSX** 실업률, **IKBK** 수출, **YBHA** GDP, **ABMX** GNI). 시계열 URL은 `…/timeseries/{cdid}/…` 형식. | [ONS Time Series Tool](https://www.ons.gov.uk/timeseriestool), [UK Data Explorer CDID Tips](https://ukdataexplorer.com/onsdatatips.html) | "CDID" 표제어 — "4자 영문 식별자" 명세, 예시 CDID 추가 |
| 7 | **Pink Book 표 식별자** | 공식 챕터 구조: 01 Main points · 02 Economic commentary · **03 Trade in goods** · **04 Trade in services** · **05 Primary income** · **06 Secondary income** · **07 Capital account** · **08 Financial account** · **09 IIP** · **10 Geographical breakdown of current account** · **11 Geographical breakdown of IIP**. 본문 표 코드(D1.3, K, BX 등)는 ONS 페이지에서 공개되지 않음 — xlsx 시트명 직접 매핑 필요. | [ONS Pink Book 2015 compendium](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/compendium/unitedkingdombalanceofpaymentsthepinkbook/2015-10-30), [Pink Book dataset](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/pinkbook) | "Pink Book 챕터 구조" 박스로 정리 |
| 8 | **EBOPS 2010 (12 main categories)** | UN MSITS 2010: ① Manufacturing services on physical inputs owned by others ② Maintenance & repair n.i.e. ③ Transport ④ Travel ⑤ Construction ⑥ Insurance & pension ⑦ Financial ⑧ Charges for use of intellectual property n.i.e. ⑨ Telecommunications, computer & information ⑩ Other business ⑪ Personal, cultural & recreational ⑫ Government goods & services n.i.e. | [UNSD EBOPS 2010 PDF](https://unstats.un.org/unsd/classifications/Econ/Download/In%20Text/EBOPS2010_english.pdf), [UNSD EBOPS overview](https://unstats.un.org/unsd/trade/events/2016/ashgabat/presentations/Day%203%2014%20UNSD%20-%20EBOPS.pdf) | "서비스무역(Trade in services)" 표제어에 12분류 표 부착 |
| 9 | **ONS 결측 표기** | ONS Service Manual: `..`, `-` 사용 비권장 → Government Analysis Function의 표 기호 가이드를 따르고 **대괄호 표기**[ ] 사용 권고. "NA"는 의미가 모호(Not Available/Not Applicable)하므로 회피. 결측 사유는 별도 열 또는 표지(cover sheet)에 기재. | [ONS Service Manual: Datasets](https://service-manual.ons.gov.uk/content/content-types/datasets) | "결측 처리(Missing data convention)" 표제어 신설 |
| 10 | **분기 발표·개정 정책** | "We publish quarterly figures **three months after the end of the reference period**." BoP는 분기 GDP/국민계정과 동시 발표. 12개월 전 일정 사전공개. 개정은 National Accounts Revisions Policy(2024-05 갱신, 2025-06 추가 갱신)에 따라 수행되며, 직전 분기 외 시계열은 두 번째 릴리스 시 일괄 갱신. | [ONS BoP QMI](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpaymentsqmi), [National Accounts Revisions Policy](https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/revisions/revisionspoliciesforeconomicstatistics/nationalaccountsrevisionspolicyupdateddecember2017), [BoP revision triangles](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsrevisiontriangles) | "발표 일정·개정 정책" 박스 추가 |

## 추가 발견 (예상 못 한 ONS 특화 규칙)

1. **BPM5→BPM6 부호 전환 주의**: Net errors and omissions(NEO) 계산식이 BPM5(`CA+KA+FA`의 부호 반전)에서 BPM6(`FA−(CA+KA)`)로 바뀜. 동일 영국 시계열을 BPM5 기반 옛 자료와 비교할 때 NEO 부호가 뒤바뀌어 보일 수 있음.
2. **Pink Book ≠ BoP Statistical Bulletin**: 본 저장소에 있는 `balanceofpayments2025q4.xlsx`는 **분기 통계 불러틴 표**이지 Pink Book(연간)이 아님. 두 출처는 동일 항등식을 따르되 표 번호 체계와 시점이 다름.
3. **데이터 소스 다중 출처**: BoP 작성에는 HMRC Overseas Trade Statistics, ITIS(International Trade in Services Survey), IPS(International Passenger Survey), FDI Survey, BIS 국제은행통계가 결합됨 — 시계열 간 개정 사유 추적 시 이 점이 중요.
4. **CDID는 시계열 단위로 부여**, 표/시트 단위가 아님. 동일한 "수출" 개념이라도 명목·실질·계절조정 여부에 따라 별도 CDID가 부여되므로 매핑표 작성 시 주의.
5. **Government Analysis Function** 표기 가이드가 ONS 데이터셋 표준임 — 향후 `db/data/`에서 결측을 Excel 셀에 남길 때 `[c]`(confidential), `[low]`(반올림 0), `[x]`(불가용) 등 대괄호 코드 사용을 검토할 가치.

## 빠진 부분 / 확인 못한 항목

- **Pink Book 본문의 세부 표 코드(D1.3, D4.6, D7.9, K, A, B, BX, C, R1~R3 등)**: ONS 공개 웹페이지에서는 챕터(1~11)까지만 노출되고, 표 단위 코드는 xlsx 파일 시트명에만 존재. 사용자 명세에 등장한 식별자는 Pink Book이 아닌 **BoP 분기 Statistical Bulletin Tables**(저장소 보유 파일)의 시트 코드로 추정되며, 공식 코드북·메타데이터 페이지는 발견되지 않음 → **xlsx 시트명을 직접 추출해 매핑하는 후속 작업**이 필요(Phase 1).
- **OECD BD4 4판** 본문은 IMF/OECD 사이트에서 PDF 직접 접근이 차단(403). 10% 임계 정의는 BPM6와 동일하다는 사실은 BPM6 가이던스 노트로 교차확인되나, BD4 고유의 추가 기준(Special Purpose Entities, FATS 등)은 미확보 — 후속 회차에서 OECD iLibrary 또는 OECD.Stat 메타데이터 페이지 접근 권장.
- **표준 분개 예시(상품수출 시 차변·대변 양식)**: BIS·BoJ 자료로 개념은 확정했으나, ONS 자체 교재에 수록된 예시는 발견되지 않음 → `background/BoP.pptx` 강의 슬라이드의 분개 예시와 교차검증 필요.

## 후속 권고

1. `db/source/balanceofpayments2025q4.xlsx`의 시트명 전체 목록을 추출해 본 결과의 Pink Book 챕터 구조와 매핑하여 표 식별자 사전을 별도 작성(Phase 1과 자연스럽게 연결).
2. `07_glossary.md`에 위 항목들을 표제어별로 반영하되, 항등식·FDI 10%·거주자 1년 기준·EBOPS 12분류·CDID 4자 코드·결측 표기 권고·개정 정책 12개월 사전공개를 정량 사실로 명시.
3. BPM5↔BPM6 부호 전환 주의사항을 별도 박스로 강조(특히 NEO 부호 반전).

## 출처 목록

- [ONS Summary of the balance of payments (methodology)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpayments)
- [ONS Balance of payments QMI](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpaymentsqmi)
- [ONS Pink Book 2015 compendium (chapter list)](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/compendium/unitedkingdombalanceofpaymentsthepinkbook/2015-10-30)
- [ONS Pink Book dataset landing](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/pinkbook)
- [ONS Balance of payments time series & revision triangles](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/datasets/balanceofpaymentsrevisiontriangles)
- [ONS National Accounts Revisions Policy (updated 2024-05 / 2025-06)](https://www.ons.gov.uk/methodology/methodologytopicsandstatisticalconcepts/revisions/revisionspoliciesforeconomicstatistics/nationalaccountsrevisionspolicyupdateddecember2017)
- [ONS UK Trade Glossary PDF](https://www.ons.gov.uk/file?uri=%2Feconomy%2Fnationalaccounts%2Fbalanceofpayments%2Fmethodologies%2Fuktrade%2Ftradeglossarytcm77422528.pdf)
- [ONS UK Trade bulletin Feb 2025](https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/uktrade/february2025)
- [ONS Time Series Explorer (CDID tool)](https://www.ons.gov.uk/timeseriestool)
- [ONS Service Manual — Datasets (missing data conventions)](https://service-manual.ons.gov.uk/content/content-types/datasets)
- [UK Data Explorer — Finding ONS data / CDID tips](https://ukdataexplorer.com/onsdatatips.html)
- [IMF DITT Guidance Note D.10 (FDI boundaries, 10% rule)](https://www.imf.org/-/media/files/data/statistics/bpm6/ditt/d10-defining-the-boundaries-of-direct-investment.pdf)
- [IMF BOPCOM-04/31 — Direct Investment 10% Threshold](https://www.imf.org/external/pubs/ft/bop/2004/04-31.pdf)
- [IMF BPM6 Appendix 4 — FDI](https://www.imf.org/external/pubs/ft/bop/2014/pdf/BPM6_A4F.pdf)
- [IMF BPM6 Chapter 4 — Economic Territory, Units, Sectors, Residence](https://www.imf.org/external/np/sta/bop/pdf/chap4.pdf)
- [IMF BPM6 FAQ on Sign Convention (BPM5→BPM6 NEO change)](https://www.imf.org/external/pubs/ft/bop/2007/bpm6faq.pdf)
- [Eurostat BPM6 metadata (identity formula, NEO calculation)](https://ec.europa.eu/eurostat/cache/metadata/en/bop_6_esms.htm)
- [Eurostat Glossary — Resident institutional unit](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Resident_institutional_unit)
- [BIS IFC Bulletin 52 — Double-entry bookkeeping in BoP](https://www.bis.org/ifc/publ/ifcb52_07.pdf)
- [Bank of Japan — BPM6 explanation (journal entry example)](https://www.boj.or.jp/en/statistics/outline/exp/exbpsm6.htm)
- [UNSD — EBOPS 2010 official PDF](https://unstats.un.org/unsd/classifications/Econ/Download/In%20Text/EBOPS2010_english.pdf)
- [UNSD — EBOPS 2010 overview presentation](https://unstats.un.org/unsd/trade/events/2016/ashgabat/presentations/Day%203%2014%20UNSD%20-%20EBOPS.pdf)
