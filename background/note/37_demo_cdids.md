# 37회차 — Phase 4.3 §5 시범 CDID 추천

본 노트는 `db/CHECKLIST.md` Phase 4.3 §5번([background-search] 조회 예시에 사용할 시범 CDID 추천 요청) 산출물. Phase 4.3 사용자 조회 인터페이스(ITEM_CODE1 단일 조회·통계표 검색·항목 트리·CSV 내보내기)에 사용할 시범 CDID 5~10개를 강의 자료 등장 빈도와 본 데이터셋 매핑 가능성을 함께 고려해 추천.

1차 근거: BoP.pptx + 노트 02·04·05·13·35 + cdid_definitions.csv + term_dict_seed.csv + statcatalog.csv.

---

## §1 강의 자료에서 가장 많이 인용되는 BoP 변수

| 표제어 | 총 등장 | 슬라이드 |
|---|---:|---|
| 경상수지 / Current account / CA | 27 | 4·5·9·10·13·14·22·23·24·30·31 |
| 금융계정 / Financial account / FA | 22 | 4·5·6·8·11·12·13·14·30 |
| 준비자산 / Reserve | 19 | 4·6·9·11·12·14·25 |
| IIP / 국제투자대조표 | 11 | 4·25 |
| 서비스 / services | 7 | 4·5·9·14 |
| 상품수지 / Trade balance | 6 | 5·9·21 |
| 대외순자산 / NFA | 6 | 11·24 |
| 본원소득 / Primary income | 5 | 5·9·14 |
| 이전소득 / Secondary income | 5 | 5·9·14 |
| 증권투자 / portfolio | 5 | 6·9·30 |
| 직접투자 / direct investment | 4 | 6·9 |
| 자본수지 / Capital account / KA | 3 | 7·9 |
| 오차 및 누락 / E&O / NEO | 3 | 6·9 |

**결론**: CA(27) > FA(22) > Reserve(19) > IIP(11). 항등식 슬라이드 14가 CA·FA·Reserve·KA·E&O 모두 등장 → 시범 동선 1번.

---

## §2 본 데이터셋 핵심 시범 CDID 10개

사용자 후보 11개 검증 결과 **KTMW는 본 데이터셋 부재** → IKBD(Table_F)·KTMS(Table_A) 정정. **HMBN은 2차소득 합계가 아니라 IIP 자산 측 투자소득 합** → IKBP(2차) / HMBP(1차) 대체.

| # | CDID | 한국어 라벨 | term_id | STAT_CODE | 슬라이드 | 강조 포인트 |
|---:|---|---|---|---|---|---|
| 1 | **HBOP** | 경상수지 합계 | CA | UK_BoP_Table_A_sub1 / B_sub3 / R1_sub1 | 5·14 | 항등식 좌변. 가장 인용 빈도 높음(27회). 단일 조회 1순위. |
| 2 | **IKBJ** | 상품·서비스 합계 | TG+SV | UK_BoP_Table_A_sub1 / B_sub3 | 5·22 | "Trade balance"="상품+서비스" 합. 슬라이드 22 `(EX−IM)` 매핑. |
| 3 | **BOKI** | 상품수지 합계 | TG | UK_BoP_Table_A_sub1 / E_sub3 | 5·9·21 | 슬라이드 21 차트 1차 데이터. SITC 5묶음 합. 본 분기 −65.5bn. |
| 4 | **IKBD** | 서비스수지 합계 | SV | UK_BoP_Table_A_sub1 / F_sub3 | 5·9·14 | EBOPS 12분류 합. 영국 강점(+53.3bn). 항목 트리 데모 시 12 하위 펼침. |
| 5 | **HMBP** | 1차소득 합계 | PI | UK_BoP_Table_A_sub2 / R1_sub2 | 5·9·14 | COE+투자소득+기타. 본 분기 −2.7bn. (HMBM은 1차소득 *투자소득* 부분) |
| 6 | **IKBP** | 2차소득 합계 | SI | UK_BoP_Table_A_sub1 / B_sub3 / H_sub3 | 5·9·14 | EU 분담금·ODA·개인이전. 본 분기 −3.6bn. |
| 7 | **HBNT** | 금융계정 순거래 합계 (broad) | FA | UK_BoP_Table_A_sub3 / J_sub3 / D7_9_sub2 | 6·8·14 | **부호 반전 운영(`sign_prefix=true`)**. 시범 조회 시 `value × −1` 데모. |
| 8 | **FNVQ** | 자본수지 합계 | KA | UK_BoP_Table_A_sub1 / I_sub3 / R1_sub1 | 5·7·14 | 슬라이드 14 단순 항등식 0 가정 항. 영국 분기 작지만 0 아님(−0.8bn). |
| 9 | **HHDH** | 오차·누락 (NEO) | NEO | UK_BoP_Table_A_sub3 / R1_sub3 | 6·13·14 | 항등식 잔차. 노트 20 |NEO| 평균 5.9bn. 본 분기 +3.5bn. |
| 10 | **HBQC** | 순 IIP (Net IIP, NFA) | NFA | UK_BoP_Table_K_sub3 / D7_9_sub1 | 11·24·25 | 분기말 stock. flow(HBNT) ↔ stock(HBQC) 대조. 단위 GBP **billion**. |
| (참고) | **LTEB** | 준비자산 잔액 (RA stock) | RA | UK_BoP_Table_K_sub1 / D1_3_sub1 / R3_sub1 | 6·12·14·25 | 슬라이드 12 "종합수지−RA=0" 검증. 6시트 중복 — 트리플 위치 데모. |

---

## §3 슬라이드 14 항등식 검증용 시범 묶음

| 역할 | CDID | 부호 처리 | 시트 위치 |
|---|---|---|---|
| CA | **HBOP** | 그대로 | Table_A_sub1 col 12 |
| KA | **FNVQ** | 그대로 | Table_A_sub1 col 13 |
| FA(broad) | **HBNT** | **`× −1`(sign_prefix)** | Table_A_sub3 col 7 |
| NEO | **HHDH** | 그대로 | Table_A_sub3 col 8 |

검증식: `HBOP + FNVQ + (−1)·HBNT + HHDH ≈ 0`.

본 데이터셋(2025 Q4): HBOP=−18.4 / FNVQ=−0.8 / HBNT=Table_A 원시값×−1 / HHDH=+3.5.

4개 변수 모두 Table_A 한 시트에서 동시 조회 가능 → **단일 통계표 데모**(STAT_CODE = `UK_BoP_Table_A_sub1` ∪ `_sub3`)로 항등식 검증 일괄 실행.

---

## §4 추천 순위 (학생 학습 우선순위)

| 순위 | CDID | 이유 |
|---:|---|---|
| 1 | HBOP | 강의 1위(27회). 모든 항등식 좌변 |
| 2 | HBNT | `CA = FA(broad)` 우변. 부호 반전 데모 |
| 3 | BOKI | 슬라이드 21 차트 1차 데이터, 본 분기 헤드라인 |
| 4 | IKBD | 영국 강점. EBOPS 12 하위 펼침 |
| 5 | HHDH | NEO 잔차. 단순화 가정 한계 학습 |
| 6 | LTEB | 6시트 중복 — 트리플 위치 데모 |
| 7 | HBQC | flow(HBNT) ↔ stock(HBQC) 대조 + 단위 차이 |
| 8 | HMBP | 영국 만성 흐름 학습 |
| 9 | IKBP | EU 분담금·ODA 정책성 |
| 10 | FNVQ | 작지만 0 아님 학습 |

---

## §5 출처 카탈로그

- 강의 1차 근거: `BoP.pptx` 31장, 슬라이드 5·6·14·11·24·25·21
- 강의 보조: `note/02·04·05·13·14·08·35`
- 데이터 매핑: `db/data/_spec/cdid_definitions.csv` / `term_dict_seed.csv` / `statcatalog.csv`
- 실측 보조: `db/REPORT.md` §2·§3

---

## §6 확인 못한 부분

1. **사용자 후보 KTMW는 본 데이터셋·강의 자료에 부재** — IKBD/KTMS 대체.
2. **HMBN 라벨 정정** — 2차소득 합계가 아니라 IIP 자산 측 투자소득 합. 2차소득 시범 IKBP, 1차소득 시범 HMBP.
3. **ONS Time Series API 직접 검증 불가** — web-search 위임 권장.
4. **항목 트리 ITEM_CODE3 위계 확정** — 노트 33 권고 기반 후속 단계.
