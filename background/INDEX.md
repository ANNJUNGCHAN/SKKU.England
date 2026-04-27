# background/ 인덱스

본 폴더는 SKKU 거시경제학 수업의 **배경지식 자료**를 보관합니다. `background-search` 서브에이전트가 1차 근거로 삼는 위치이며, 외부 일반 지식보다 본 폴더의 자료를 우선 참조합니다.

상위 규칙은 루트 `CLAUDE.md`를 우선 따릅니다. 본 폴더 자체는 데이터 가공 대상이 아니므로 파일을 수정·삭제·이동하지 않습니다.

## 자료 목록

| 파일 | 형식 | 주제 | 비고 |
| --- | --- | --- | --- |
| `BoP.pptx` | PowerPoint | 국제수지(Balance of Payments) 강의 슬라이드 | `python-pptx`로 텍스트 추출 |
| `BoP.pdf` | PDF | BoP.pptx의 PDF 본 | `pypdf`/`pymupdf`로 추출 |
| `slide_images/slide_NN.png` | PNG | BoP.pdf 31페이지를 200 DPI로 렌더링한 시각 자료 | 멀티모달 분석 입력 |
| `note/01_inventory.md` ~ `18_iip_revaluation_decomp.md` | Markdown | `background-search`·`web-search`로 작성한 한국어 발췌·정리 노트 (18건) | Phase 3 명세서 작성의 1차 근거 |
| `note/12_xlsx_sheet_inventory.csv`, `13_cdid_dictionary.csv`, `15_units.csv`, `15_missing.csv`, `17_boe_reserve_assets.csv`, `18_iip_revaluation_decomp.csv` | CSV | 노트 부속 정형 데이터(시트 인벤토리·CDID 사전·단위·결측·BoE/HMT/ONS/IMF 출처 카탈로그·IIP 4분해 출처) | 1 CSV = 1 평면 표 원칙 |

> 새 자료를 추가할 때마다 위 표를 갱신합니다. 폴더 구조를 분류별로 나누는 경우 폴더 단위 주제도 같이 표기합니다.

## 인용 표기 규칙

- 본 폴더 자료를 인용할 때는 `background/<파일명>` 경로와 함께 **슬라이드 번호** 또는 **페이지/섹션**을 명시합니다.
  - 예: `background/BoP.pptx` 슬라이드 7
- 핵심 인용은 원문(또는 그 한국어 번역)을 짧게 발췌해 함께 보여줍니다.
- 자료가 일반 통계 정의와 다를 경우, 본 폴더의 표기를 따르고 차이를 짧게 부연합니다.

## 추가 절차

1. 새 자료를 `background/`에 복사합니다(가급적 원본 형식 그대로).
2. 본 `INDEX.md`의 자료 목록 표에 한 줄을 추가합니다.
3. 텍스트 추출이 필요한 형식(`.pptx`, `.pdf`, `.docx`)이면 `background-search` 에이전트가 `env/`에 적절한 라이브러리를 사용해 추출합니다(필요 시 `requirements.txt`도 함께 갱신).

## 금지 사항

- `background/` 자료의 수정·삭제·이동
- 본 폴더에 가공된 파생 산출물 저장 (산출물은 `db/data/` 또는 `db/REPORT.md`로)
- 출처 불명 자료 추가
