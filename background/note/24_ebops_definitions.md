# 24회차 — EBOPS 2010 12분류 한국어 정의 (서비스무역 web-search 1차 보강 라운드)

본 노트는 `db/CHECKLIST.md` Phase 3.2 §4(강의 자료에 정의가 없는 CDID에 대해 ONS Time Series 페이지·BoP 매뉴얼(IMF BPM6 등) 출처 보강 요청)의 **1차 라운드 — 서비스무역 EBOPS 2010 12분류** 보강 산출물이다. 영국 ONS BoP 2025 Q4 Statistical Bulletin Tables의 `Table_F`(서비스무역) 13개 컬럼·`Table_C`(EU/non-EU 분해 일부)·`Table_BX`(귀금속 제외 서비스 부분) CDID 중 강의 자료(`background/BoP.pptx`)에 정의가 없어 `db/data/_spec/cdid_definitions_unmapped.csv`에 ko_definition이 비어 있는 항목들의 1차 자료 정의를 정리한다.

1차 자료(IMF BPM6 §10, UN MSITS 2010, UNSD EBOPS 2010, Eurostat ITS6 metadata, ONS UK Trade Glossary, 한국은행 BPM6 보도자료) 우선 — Wikipedia·언론 기사 등 secondary는 보조.

---

## 영국 ONS 적용 함의 (12분류 종합)

### 1) 자료원 분담 (ITIS 적용 범위 vs 외부 자료원)

| 분류 | 주 자료원 | ITIS 포함 여부 |
|---|---|---|
| Manufacturing services | HMRC + ITIS | 부분 |
| Maintenance and repair | ITIS | 포함 |
| Transport | **ITIS 제외** → 자체 운송조사 + BoE + HMRC CIF/FOB | 제외 |
| Travel | **ITIS 제외** → **IPS(International Passenger Survey)** | 제외 |
| Construction | ITIS | 포함 |
| Insurance and pension | ITIS + BoE 보험감독 | 포함 |
| Financial services | **ITIS 제외** → **BoE** + ONS ABS | 제외 |
| Charges for IP | ITIS | 포함 |
| Telecom/computer/info | ITIS + 가구 소액 추계 | 포함 |
| Other business services | ITIS (핵심) | 포함 |
| Personal/cultural/recreational | ITIS + 행정자료 | 부분 |
| Government services | HMT 회계 + 외교부 | 외부 |

### 2) 영국 만성 서비스 흑자 분해 (2024년 기준)

- **총 서비스수지 흑자**: GDP 6.4% (£185.5bn) — 2023년 5.8% (£160.0bn)에서 확대
- **수출 £507.0bn / 수입 £321.5bn** (2024)
- **수출 증가 기여 1위**: Charges for IP (+£13.5bn)
- **수출 증가 기여 2위**: Other business services (+£12.7bn)
- **수출 증가 기여 3위**: Travel (+£6.6bn) — 코로나 회복
- **수출 증가 기여 4위**: Financial services (+£5.3bn)
- **세계 최대 금융서비스 흑자국**: 2024년 $127bn (미국 $64.2bn의 약 2배 — TheCityUK 추산)
- **무역 비대칭성 큰 3대 항목**: Financial services / Other business services / Telecommunications, computer & information (ONS 자체 명시)

---

## 12분류별 정리표

### 1. Manufacturing services on physical inputs owned by others (SA)

- **한국어 명칭**: 가공서비스 (한국은행 BPM6 보도자료 표기)
- **정의 (영문 발췌)**: "processing, assembly, labelling, packing, and other such processes undertaken by enterprises that do not own the physical inputs concerned" (UN MSITS 2010 / BPM6 §10.62-10.71). 가공자(processor)가 비거주 의뢰인(principal) 소유 재화를 자기 노동·자본으로 변형하고 가공수수료만 수취 — **재화 경제적 소유권은 의뢰인에게 잔존**.
- **한국어 풀이**: 거주자가 다른 경제 거주자가 소유한 물리적 투입물에 대해 가공·조립·라벨링·포장 등을 수행하고 받는 가공수수료. 재화 자체의 매매가 아니라 가공 노무의 대가만 서비스로 기록.
- **세부 항목**: 가공수수료 단일 항목. 보충정보로 가공 전·후 재화 총액(gross goods values)을 EBOPS supplementary item으로 식별 가능 (BPM6 §10.65, Box 10.1-10.2).
- **사례**: 정유, 천연가스 액화, 핵연료 재처리, 의류·자동차 조립, 광물·금속 변형
- **BPM6 위치**: §10.62-10.71 (Box 10.1, Box 10.2, Table 10.2)
- **ONS 적용**: HMRC Customs 자료(특수 통관 절차 OPP/IPP)와 ITIS 결합으로 가공수수료만 분리 추출. 영국은 화학·항공기 부품 가공 등 소규모.
- **출처**:
  - https://unstats.un.org/wiki/display/M2CG/Manufacturing+services+on+physical+inputs+owned+by+others
  - https://unstats.un.org/wiki/spaces/M2CG/pages/5309606/B.1.+Goods-related+services
  - https://unstats.un.org/unsd/classifications/Econ/Download/In%20Text/EBOPS2010_english.pdf

### 2. Maintenance and repair services n.i.e. (SB)

- **한국어 명칭**: 유지보수서비스 (한국은행 표기)
- **정의 (영문 발췌)**: "Maintenance and repair work by residents on goods that are owned by non-residents and vice versa" (UN MSITS 2010). 기록 가치 = 수리 노무의 가치만 (재화 총액 아님).
- **한국어 풀이**: 거주자가 비거주자 소유 재화를 정비·수리하는 노무, 또는 그 반대. 가동 상태 유지를 위한 정비뿐 아니라 효율·용량을 회복·확장하는 수리도 포함.
- **세부 항목**: BPM6는 단일 분류. EBOPS 2010 보충정보에서 항공기·선박·기타로 세분 가능.
- **사례**: 항공기 엔진 수리, 선박 정비
- **BPM6 위치**: §10.72-10.74
- **ONS 적용**: 영국은 항공기 정비(롤스로이스·BA Engineering) 흑자 분야. ITIS 조사로 포착.
- **출처**:
  - https://unstats.un.org/wiki/spaces/M2CG/pages/5309606/B.1.+Goods-related+services
  - https://ec.europa.eu/eurostat/cache/metadata/en/bop_its6_esms.htm

### 3. Transport (SC)

- **한국어 명칭**: 운송 (한국은행 표기)
- **정의 (영문 발췌)**: "Transport includes passenger, freight, and other transport services provided by residents of one economy to residents of another economy. … classified by mode of transport (sea, air, and other, which includes rail, road, inland waterway, pipeline, space transport, and electricity transmission). Transport also includes postal and courier services." (BPM6 §10.75)
- **한국어 풀이**: 한 경제 거주자가 다른 경제 거주자에게 제공하는 사람·화물·기타 운송 서비스. 모드별(해상/항공/기타)·기능별(여객/화물/기타)로 이중 교차 분류.
- **세부 항목**:
  - 모드: 해상(Sea), 항공(Air), 기타(Other = 철도·도로·내륙수운·공간·파이프라인·송전)
  - 기능: 여객(Passenger), 화물(Freight), 기타(Other supporting/auxiliary)
  - 우편 및 택배(Postal and courier)는 별도 sub-item
  - 국제운송 화물의 보험은 **운송**이 아니라 **보험서비스**로 분류
- **BPM6 위치**: §10.75-10.93 (특히 §10.78 화물 비용의 관세선 기준 배분)
- **ONS 적용**: ITIS에서 **제외**된 영역으로, BoE 외환자료·HMRC CIF/FOB 조정·ONS 자체 운송조사 결합. 영국은 항공·해상 운송 중간 규모 적자국. CIF→FOB 조정으로 화물운임이 상품수지와 분리.
- **출처**:
  - https://unstats.un.org/wiki/display/M2CG/B.2++Good+collection+practices+and+comparison+of+data+sources+for+transport
  - https://ec.europa.eu/eurostat/cache/metadata/en/bop_its6_esms.htm
  - https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpaymentsqmi

### 4. Travel (SD)

- **한국어 명칭**: 여행 (한국은행 표기)
- **정의 (영문 발췌)**: "covers goods and services for own use or to be given away, acquired from an economy, by non-residents during visits to that economy" (BPM6 §10.94 / UNSD EBOPS overview). **여행은 특정 상품이 아니라 비거주자가 방문 경제에서 구입하는 다양한 재화·서비스의 묶음**(transactor-based component).
- **한국어 풀이**: 비거주자가 어떤 경제를 방문하는 동안 본인 소비 또는 선물용으로 그 경제에서 취득한 재화·서비스 일체. 방문 목적과 무관하게 1년 미만 체류 비거주자의 모든 지출이 포함되며, 여행에 부수되는 국제여객운임은 **운송**으로 별도 처리.
- **세부 항목**:
  - **Business travel**(업무여행): 계절·국경 근로자 지출 + 기타 업무여행
  - **Personal travel**(개인여행): Health-related(의료 관광), Education-related(유학 학비 + 체류 중 식비·숙박·교통), Other personal
  - **교육·보건 서비스**는 비거주자가 해당 경제를 방문해 받는 경우 **여행으로 분류**(EBOPS 11.2의 교육·보건과 구분)
- **BPM6 위치**: §10.94-10.117
- **ONS 적용**: ITIS 제외 → **IPS(International Passenger Survey)가 핵심 자료원**. 영국은 관광 적자(영국인 해외 지출 > 외국인 영국 지출). 코로나 이후 회복 중. 2025Q4 기준 영국 관광 흑자 일부 회복. ONS는 2022년부터 교육 서비스 추계 방법을 별도 개선 보고서로 발표.
- **출처**:
  - https://unstats.un.org/unsd/trade/events/2016/ashgabat/presentations/Day%203%2018%20UNSD%20-%20Service%20categories%20Travel%20and%20tourism.pdf
  - https://www.ons.gov.uk/businessindustryandtrade/internationaltrade/articles/methodologicalimprovementstoukeducationservicesexports/2022-11-02
  - https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpaymentsqmi

### 5. Construction (SE)

- **한국어 명칭**: 건설 (한국은행 표기)
- **정의 (영문 발췌)**: "Construction covers the creation, management, renovation, repair or extension of fixed assets in the form of buildings, land improvements of an engineering nature and such other constructions as roads, bridges and dams" (BPM6 §10.101). 평가는 **총액(gross basis)** — 모든 투입재·노무·운영잉여 포함.
- **한국어 풀이**: 건물·토목구조물(도로·교량·댐 등) 고정자산을 건설·증·개축·수리·관리하는 서비스. 부지정리, 도장, 배관, 철거 등 부수 노무 포함. 단, 해외 별도 법인(branch institutional unit)으로 1년 이상 활동하면 직접투자로 재분류.
- **세부 항목**:
  - **Construction abroad**(해외 건설): 거주자가 해외에서 수행
  - **Construction in the compiling economy**(국내 건설): 비거주자가 국내에서 수행
- **BPM6 위치**: §10.101-10.106
- **ONS 적용**: ITIS 조사 대상. 영국 건설서비스는 소규모.
- **출처**:
  - https://unstats.un.org/wiki/display/M2CG/B.3.++Construction
  - https://ec.europa.eu/eurostat/cache/metadata/en/bop_its6_esms.htm

### 6. Insurance and pension services (SF)

- **한국어 명칭**: 보험·연금서비스 (한국은행 표기)
- **정의 (영문 발췌)**: 가치산정 = "Gross premiums earned plus net investment income minus estimated claims incurred" (MSITS 2010 §14.261). 발생주의(earned premium)로 기록하고, 평년 수준 추정 claim을 사용해 재해성 변동을 평활화. 생명보험·연금은 보험계약 적립금(actuarial reserve) 순증분을 추가 차감.
- **한국어 풀이**: 직접보험·재보험·보험부수서비스·연금 및 표준화보증서비스. 명목 보험료가 아닌 **순보험료**(보험료 + 투자수익 − 추정보험금)가 서비스 가치.
- **세부 항목**:
  - **Direct insurance**: Life insurance / Freight insurance / Other direct insurance
  - **Reinsurance**(재보험)
  - **Auxiliary insurance**(보험부수 — 대리·중개·자문)
  - **Pension and standardised guarantee services**: Pension services / Standardised guarantee services
- **BPM6 위치**: §10.107-10.122
- **ONS 적용**: 영국 **Lloyd's of London·재보험허브**로 흑자 분야. ITIS 조사 + BoE 보험감독 자료. 무역 비대칭성(asymmetry)이 큰 항목.
- **출처**:
  - https://unstats.un.org/wiki/display/M2CG/B.4.++Insurance,+pension+and+financial+services
  - https://ec.europa.eu/eurostat/cache/metadata/en/bop_its6_esms.htm

### 7. Financial services (SG)

- **한국어 명칭**: 금융서비스 (한국은행 표기)
- **정의 (영문 발췌)**: "Financial services cover financial intermediation and auxiliary services, except those of insurance enterprises and pension funds" (BPM6 §10.118). FISIM(Financial Intermediation Services Indirectly Measured) — 예금·대출 마진으로 간접측정 — 은 **financial corporations**가 생산하며 **explicit charges**(명시적 수수료)와 합산해 측정.
- **한국어 풀이**: 금융중개와 부수서비스 일체 (보험·연금 제외). 명시적 수수료(중개수수료·자산관리비·자문)와 FISIM 합산.
- **세부 항목**:
  - **Explicitly charged and other financial services**: 자산관리, 신용카드, 투자은행, 자문 등
  - **FISIM**(간접측정 금융중개서비스)
- **BPM6 위치**: §10.118-10.136
- **ONS 적용**: **The City of London** 효과로 영국 **세계 최대 금융서비스 흑자국**. **2024년 흑자 $127bn**(미국 $64.2bn의 약 2배 — TheCityUK 추산). 자료원: ITIS **제외** + BoE 은행통계 + ONS Annual Business Survey + 자영금융기관 별도 조사. 무역 비대칭성 큰 항목.
- **출처**:
  - https://unstats.un.org/wiki/display/M2CG/B.4.++Insurance,+pension+and+financial+services
  - https://www.thecityuk.com/news/uk-retains-world-leading-financial-services-trade-surplus-and-global-hub-status/
  - https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpaymentsqmi

### 8. Charges for the use of intellectual property n.i.e. (SH)

- **한국어 명칭**: 지식재산권사용료 (한국은행 표기)
- **정의 (영문 발췌)**: 산업재산권(특허·상표·산업디자인·영업비밀) 사용 허가, 저작권(소프트웨어·문학·예술 원본) 복제·배포 권한, 프랜차이즈 권리 등 **무형자산 사용권의 대가**. 무형자산의 **소유권 양도**는 자본계정(Capital account)으로 분류되어 본 항목에서 제외.
- **한국어 풀이**: 특허·상표·저작권 등 지식재산을 사용할 권리(라이선스)에 대해 지급하는 사용료·로열티. 단, 권리 자체의 매매는 자본계정 (BPM6 §10.137-10.139).
- **세부 항목**:
  - Franchises and trademarks licensing fees
  - Licences for the use of outcomes of R&D
  - Licences to reproduce/distribute computer software
  - Licences to reproduce/distribute audiovisual products
  - Licences for other IP
- **BPM6 위치**: §10.137-10.144
- **ONS 적용**: **2024년 영국 IP 사용료 수출 +£13.5bn 증가** — 서비스 흑자 1위 기여 항목. 제약(GSK·AstraZeneca)·미디어·게임·디자인. ITIS 조사 대상.
- **출처**:
  - https://ec.europa.eu/eurostat/statistics-explained/index.php?title=EU_international_trade_in_other_business_services
  - https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025
  - https://unstats.un.org/wiki/display/M2CG/Country+experience:+Germany:+Charges+for+the+use+of+intellectual+property

### 9. Telecommunications, computer, and information services (SI)

- **한국어 명칭**: 통신·컴퓨터·정보서비스 (한국은행 표기)
- **정의 (영문 발췌)**: "Telecommunications services cover the broadcast or transmission of sound, images, data or other information by telephone, telex, telegram, radio and television cable and broadcasting, satellite, electronic mail, facsimile services etc., including … Internet backbone services and online access services, including provision of access to the Internet" (BPM6 §10.145). "Computer services consist of hardware- and software-related services and data processing services."
- **한국어 풀이**: 통신서비스(음성·영상·데이터 송수신), 컴퓨터서비스(하드웨어·소프트웨어 관련 서비스 + 데이터 처리), 정보서비스(뉴스·기타 정보).
- **세부 항목**:
  - **Telecommunications services**: 인터넷 백본·온라인 접속 포함
  - **Computer services**: Computer software / Other computer services
  - **Information services**: News agency services / Other information services
  - **방송 컨텐츠 제작·라이선스**는 본 항목 **아님** — Personal/cultural/recreational §11.1 (audiovisual)
- **BPM6 위치**: §10.145-10.160
- **ONS 적용**: 영국 디지털·SaaS 수출 성장 항목. ITIS 조사 + 가구의 소액 거래 추계. **무역 비대칭성** 가장 큰 3대 항목 중 하나(ONS 자체 인정).
- **출처**:
  - https://unctad.org/system/files/official-document/tn_unctad_ict4d03_en.pdf
  - https://ec.europa.eu/eurostat/cache/metadata/en/bop_its6_esms.htm

### 10. Other business services (SJ)

- **한국어 명칭**: 기타사업서비스 (한국은행 표기)
- **정의 (영문 발췌)**: 다른 EBOPS 카테고리에 명시되지 않은 사업서비스 일체. 3개 하위그룹의 **이질적 집합**(heterogeneous category — Eurostat).
- **한국어 풀이**: R&D, 전문·경영자문, 기술·무역관련·기타 사업서비스를 묶은 잔여(residual) 사업서비스 분류.
- **세부 항목**:
  - **Research and development services**(연구개발서비스)
  - **Professional and management consulting services**(전문·경영컨설팅):
    - Legal, accounting, management consulting, public relations
    - Advertising, market research, public opinion polling
  - **Technical, trade-related and other business services**:
    - Architectural, engineering, scientific and other technical services
    - Waste treatment, environmental, agricultural, mining services
    - Operating leasing, trade-related services
    - Other (배전·증기·가스·인력공급·보안·사진·출판·부동산 등)
- **BPM6 위치**: §10.147, §10.149, §10.151
- **ONS 적용**: **영국 서비스 흑자 1위 절대 규모** — 2024년 IP 다음 가는 흑자 확대 기여(+£12.7bn). 영국이 미국·EU에 광범위하게 컨설팅·법무·엔지니어링 수출. ITIS 핵심 대상. **무역 비대칭성 1위 항목**(ONS 자체 인정). 2025년 UK 서비스 수입에서 가장 큰 항목(£126.5bn).
- **출처**:
  - https://ec.europa.eu/eurostat/statistics-explained/index.php?title=EU_international_trade_in_other_business_services
  - https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025
  - https://ec.europa.eu/eurostat/cache/metadata/en/bop_its6_esms.htm

### 11. Personal, cultural, and recreational services (SK)

- **한국어 명칭**: 개인·문화·여가서비스 (한국은행 표기)
- **정의 (영문 발췌)**: 11.1 Audiovisual + 11.2 Other personal·cultural·recreational. **§11.1**: "Audiovisual and related services relates to the production of motion pictures, radio and television programmes and musical recordings. Artistic related services includes the services provided by performing artists, authors, composers and sculptors." **§11.2**: 보건·교육·문화유산·여가·기타 개인서비스(단, 비거주자가 해당 경제에 방문해 받는 보건·교육은 **여행**으로 분류).
- **한국어 풀이**: 영화·방송·음악·예술 등 시청각·예술 서비스(11.1)와 보건·교육·문화유산·여가 등 기타 개인서비스(11.2). 거주자/비거주자 양면 — 원격으로 제공되는 경우만 포함.
- **세부 항목**:
  - **11.1 Audiovisual and related services**:
    - Audio-visual services (영화·라디오·TV·음악녹음 제작)
    - Artistic related services (공연예술·저작·작곡·조각가 서비스)
  - **11.2 Other personal, cultural and recreational services**:
    - 11.2.1 Health services (원격 의료; 의료관광은 여행)
    - 11.2.2 Education services (원격 교육; 유학은 여행)
    - 11.2.3 Heritage and recreational services (문화유산·여가)
    - 11.2.4 Other personal services (기타 개인서비스)
- **BPM6 위치**: §10.161-10.171
- **ONS 적용**: 영국 미디어·음악·예술·고등교육(원격 부분) 일부 흑자. ITIS 조사 + 별도 교육·보건 행정자료. 고등교육은 ONS가 2022년부터 별도 방법론 개선.
- **출처**:
  - https://unctad.org/en/PublicationsLibrary/tn_unctad_ict4d03_en.pdf
  - https://www.ons.gov.uk/businessindustryandtrade/internationaltrade/articles/methodologicalimprovementstoukeducationservicesexports/2022-11-02

### 12. Government goods and services n.i.e. (SL)

- **한국어 명칭**: 정부서비스 (한국은행 표기)
- **정의 (영문 발췌)**: "Services related to government functions that cannot be classified to another specific service category should be classified as government services" (UN Wiki / BPM6 §10.172). 정부 단위와 그 단위가 물리적으로 위치한 영역 사이의 거래, 그리고 enclave(대사관·영사관·군부대)·국제기구가 포함.
- **한국어 풀이**: 다른 항목으로 분류되지 않는 정부 관련 재화·서비스 거래. 대사관·영사관·군부대·국제기구의 거래, 비자수수료, 영사수수료, 외교관·공무원 해외 체류 지출 등.
- **세부 항목** (3분류 권고):
  - Embassies and consulates (대사관·영사관)
  - Military units and agencies (군부대·군기관)
  - Other government goods and services n.i.e. (기타)
- **포함**: 비자·영사 수수료, 경찰형 서비스, 기술원조(다른 항목 미해당분), 정부 면허·허가(실질 정부 행정업무 수반), 외교관·영사·군인 해외 지출, 원조 미션, 무역대표부, 국제기구 거래
- **제외**: 대사관·군부대 현지 채용 직원의 지출, 12개월 이상 체류 국제기구 직원, **자동차·선박·항공기·수렵·낚시 면허 등 자동 발급 면허 수수료**(세금으로 분류)
- **BPM6 위치**: §10.172-10.180
- **ONS 적용**: 영국은 미국·EU·UN 등에 대사관·군기관·문화원 운영. 영국 정부의 해외 지출/수입 모두 BoP에 반영. 자료원: HMT 회계 + 외교부 보고. 일반적으로 적자.
- **출처**:
  - https://unstats.un.org/wiki/spaces/M2CG/pages/5310250/B.8.+Government+goods+and+services+n.i.e.

---

## 출처 카탈로그 (1차 출처 우선)

### IMF (BPM6) — 본문 PDF 직접 접근은 403 차단되나 §10 단락 번호는 Eurostat·UN Wiki 인용으로 확정

- IMF BPM6 매뉴얼 본문 PDF Chapter 10 Services (403 차단): https://www.imf.org/external/pubs/ft/bop/2014/pdf/BPM6_12F.pdf
- IMF BPM6 BoP Manual landing page: https://www.imf.org/external/pubs/ft/bop/2007/bopman6.htm

### UN Statistics Division — MSITS 2010

- UNSD EBOPS 2010 매뉴얼 PDF: https://unstats.un.org/unsd/classifications/Econ/Download/In%20Text/EBOPS2010_english.pdf
- UNSD MSITS 2010 매뉴얼 본문 PDF: https://unstats.un.org/unsd/publication/seriesm/seriesm_86rev1e.pdf
- UN MSITS 2010 Compilers Guide Wiki Home: https://unstats.un.org/wiki/display/M2CG/MSITS+2010+Compilers+Guide+Home
- UN Wiki — B.1 Goods-related services: https://unstats.un.org/wiki/spaces/M2CG/pages/5309606/B.1.+Goods-related+services
- UN Wiki — Manufacturing services on physical inputs owned by others: https://unstats.un.org/wiki/display/M2CG/Manufacturing+services+on+physical+inputs+owned+by+others
- UN Wiki — B.2 Transport (data sources): https://unstats.un.org/wiki/display/M2CG/B.2++Good+collection+practices+and+comparison+of+data+sources+for+transport
- UN Wiki — B.3 Construction: https://unstats.un.org/wiki/display/M2CG/B.3.++Construction
- UN Wiki — B.4 Insurance, pension and financial services: https://unstats.un.org/wiki/display/M2CG/B.4.++Insurance,+pension+and+financial+services
- UN Wiki — B.8 Government goods and services n.i.e.: https://unstats.un.org/wiki/spaces/M2CG/pages/5310250/B.8.+Government+goods+and+services+n.i.e.

### Eurostat

- Eurostat ITS6 metadata (BPM6 service categories SA-SL): https://ec.europa.eu/eurostat/cache/metadata/en/bop_its6_esms.htm
- Eurostat — EU international trade in other business services: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=EU_international_trade_in_other_business_services

### ONS (영국)

- ONS BoP QMI: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/balanceofpaymentsqmi
- ONS UK Trade Glossary PDF: https://www.ons.gov.uk/file?uri=%2Feconomy%2Fnationalaccounts%2Fbalanceofpayments%2Fmethodologies%2Fuktrade%2Ftradeglossarytcm77422528.pdf
- ONS International Trade in Services QMI: https://www.ons.gov.uk/businessindustryandtrade/internationaltrade/methodologies/internationaltradeinservicesqmi
- ONS International Trade in Services (ITIS) methodology: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/methodologies/internationaltradeinservicesitis
- ONS UK Pink Book 2025 bulletin: https://www.ons.gov.uk/economy/nationalaccounts/balanceofpayments/bulletins/unitedkingdombalanceofpaymentsthepinkbook/2025
- ONS Methodological improvements to UK education services exports (2022): https://www.ons.gov.uk/businessindustryandtrade/internationaltrade/articles/methodologicalimprovementstoukeducationservicesexports/2022-11-02

### 한국은행 (한국어 명칭 출처)

- 한국은행 BPM6 시행 관련 보도자료/설명자료 (KIF 보존본): https://vwserver.kif.re.kr/html/KM/132992924831864691_%EA%B5%AD%EC%A0%9C%EC%88%98%EC%A7%80%ED%86%B5%EA%B3%84%EA%B0%9C%EC%9A%94.hwp.files/Sections1.html
- 한국은행 ECOS: https://ecos.bok.or.kr/

### 추가 참고

- TheCityUK — UK financial services trade surplus 2024: https://www.thecityuk.com/news/uk-retains-world-leading-financial-services-trade-surplus-and-global-hub-status/
- BEA US International Services Definitions: https://www.bea.gov/international/international-services-definition
- WTO Measuring Trade in Services Training Module: https://www.wto.org/english/res_e/statis_e/services_training_pres_e.pdf
- UNCTAD — ICT services and ICT-enabled services: https://unctad.org/system/files/official-document/tn_unctad_ict4d03_en.pdf
- OECD-WTO Balanced Trade in Services (BaTIS) methodology: https://www.oecd.org/content/dam/oecd/en/data/methods/OECD-WTO-Balanced-Trade-in-Services-database-methodology-BPM6.pdf

---

## 확인 못한 부분

1. **IMF BPM6 본문 PDF 직접 인용**: IMF 서버가 PDF 직접 접근을 403으로 차단. §10.62-10.180 단락별 **원문 인용**은 본 라운드에서 IMF 1차 페이지로 직접 검증하지 못했으나, 단락 번호 자체는 UN MSITS Compilers Guide Wiki·Eurostat 메타데이터·UNSD 발표자료에서 일관되게 확인되어 **단락 번호 자체는 신뢰 가능**.
2. **한국은행 「국제수지통계의 이해」 PDF 직접 다운로드**: 한국은행 fileDown.do URL이 직접 페치에서 빈 응답. 12분류의 한국어 표기 중 **"가공서비스, 운송, 여행, 건설"**은 KIF 보존본·KDI 자료로 확인되었으나, 나머지 8개("유지보수서비스", "보험·연금서비스", "금융서비스", "지식재산권사용료", "통신·컴퓨터·정보서비스", "기타사업서비스", "개인·문화·여가서비스", "정부서비스")는 한국은행 BPM6 시행 보도자료 통상 표기 관행으로 추정. 한국은행 ECOS 표제어 100% 일치는 후속 라운드에서 보강 필요.
3. **xlsx 시트 CDID와 EBOPS 12분류 직접 매핑**: 본 라운드는 EBOPS 12분류 정의·세부 항목·BPM6 §10 위치까지만. CDID 매핑은 후속 단계의 Phase 3.4 명세서 작성 시 적용.

---

## Phase 3.2 §4 활용 가이드

본 노트의 12분류 정의는 `db/data/_spec/cdid_definitions_unmapped.csv` 중 다음 시트의 ko_definition 컬럼 보강에 적용:

| 시트 | unmapped CDID 수 | 본 노트 적용 분류 |
|---|---|---|
| Table_F | 33 | EBOPS 2010 12분류(SA-SL) 모두 |
| Table_C | 36 (일부) | EBOPS 12분류 중 EU/non-EU 분해된 항목 |
| Table_BX | 27 (일부) | 서비스 부문 항목(귀금속 제외 시 영향 없음) |
| Table_B | 23 (일부) | 서비스 합계 라인 |
| Table_R2 | 23 (일부) | 서비스 개정 |
| Table_E | 21 | 본 라운드 적용 외(SITC 5분류는 별도 라운드) |

후속 라운드 계획:
- 라운드 2: FA 5분류(직접투자·증권투자·파생·기타투자·준비자산) — Table_J 15 + D1_3 5 + D4_6 4 + D7_9 5 + Table_K 12 = 41건
- 라운드 3: SITC 5분류·상품무역 세부 — Table_E 21 + Table_BX 27 + Table_B 23 일부
- 라운드 4: 자본계정 세부(채무면제·이민·비생산비금융자산) — Table_I 29
- 라운드 5: 1차·2차소득 세부(직접투자수익·이자·근로자보수·EU 분담금 등) — Table_G 23 + Table_H 19
- 라운드 6: 개정 시트 메타(R1 15 + R2 23 + R3 14)
- 라운드 7: Table_A 합계 라인 15
