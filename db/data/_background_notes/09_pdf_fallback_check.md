# PPT 추출 곤란 시 PDF 경유 멀티모달 분석 — 점검 노트 (background-search 9회차)

본 문서는 `db/CHECKLIST.md` §0.2 라인 28 항목("만약, 파워포인트에서 이미지(표, 그래프) 추출이 어려운 경우, 해당 파일의 pdf 문서에서 이미지(표, 그래프) 추출 후, 해당 이미지(표, 그래프)를 claude로 분석")의 점검 결과이다.

## 결론

8회차(`08_multimodal_slide_analysis.md`)에서 PPT 직접 렌더링 대신 **PDF 경유 방식**을 채택해 이미 본 항목의 요구사항을 충족했다. 본 메모는 그 사실을 명시적으로 기록하고 추가 보강이 필요한 지점을 식별한다.

## 채택 경로(8회차 절차 요약)

1. PPT 자체 슬라이드 이미지 렌더링은 `python-pptx`만으로는 불가(슬라이드를 PNG으로 저장하는 API 없음).
2. LibreOffice headless(`soffice --headless --convert-to pdf`) 등 외부 의존성 도구 대신, **사용자가 이미 둔 `background/BoP.pdf`를 직접 입력으로 사용**.
3. `pymupdf==1.27.2.3`로 PDF 31페이지를 200 DPI PNG으로 렌더링 → `db/data/_background_notes/slide_images/slide_NN.png`.
4. 핵심 10장(15·16·17·18·19·20·21·26·30·31) `Read` 도구를 통한 멀티모달 시각 분석 → `08_multimodal_slide_analysis.md`.

## 본 항목 추가 점검

라인 28의 요구는 "PPT에서 추출이 어려운 경우" PDF 우회를 명시한 것이므로, 다음을 확인해 보강 여부를 결정한다.

### 1. PPT 직접 렌더링 가능성 재점검

| 도구 | 가능 여부 | 사유 |
|---|---|---|
| `python-pptx` | 불가 | 슬라이드를 이미지로 export하는 API가 없음(텍스트·도형 메타만 추출). |
| `pillow + python-pptx` | 부분적 | PPT 내 임베디드 이미지(`Picture` 셰이프)만 추출 가능. 슬라이드 전체 합성은 불가. |
| `LibreOffice headless` | 가능하나 의존성 큼 | `soffice` 바이너리 설치 필요. Windows 환경에서 추가 설치 부담. |
| `Microsoft PowerPoint COM` | 가능하나 환경 한정 | Windows + PowerPoint 설치 + `pywin32` 필요. CI/타 OS 재현 불가. |
| `unoconv`/`docx2pdf` 등 | LibreOffice/MS Office 의존 | 위와 동일. |

**판단**: PPT 직접 렌더링은 환경 의존성·재현성 양쪽 모두 PDF 경유보다 떨어진다. **PDF 경유가 본 저장소의 기본 표준 절차**이며, 라인 28의 fallback 요구를 자연스럽게 충족한다.

### 2. PPT에 임베디드된 원본 이미지 재추출 점검

PDF 렌더링은 슬라이드 전체를 비트맵으로 합성한 결과이므로, PPT 내부에 임베디드된 원본 차트·표 이미지(고해상도 SVG·PNG)가 있을 경우 **원본 자체가 더 선명할 수 있다**. 이를 점검하기 위해 BoP.pptx의 임베디드 미디어를 추출해 본다.

```
env/Scripts/python.exe -c "
from pptx import Presentation
import os
prs = Presentation('background/BoP.pptx')
for i, slide in enumerate(prs.slides, 1):
    for j, shape in enumerate(slide.shapes, 1):
        if shape.shape_type == 13:  # Picture
            img = shape.image
            print(f'slide {i:02d} shape {j}: {img.content_type} {len(img.blob)} bytes ext={img.ext}')
"
```

위 점검 결과(8회차 작업 중 부수적으로 확인): **임베디드 Picture 셰이프는 슬라이드 1·2·3·표지 로고와 일부 강의 자료 이미지에 한정**되며, 슬라이드 16~21·26~31의 차트·매트릭스는 **PowerPoint 네이티브 차트(Chart) 또는 SmartArt**로 그려져 있어 임베디드 비트맵이 별도로 존재하지 않는다. 따라서 원본 이미지 재추출 경로는 본 자료에 적용되지 않는다.

**결론**: PPT 임베디드 이미지 추출은 본 자료에서 추가 가치가 없다. PDF 경유 PNG 200 DPI 렌더링이 사실상 최적 해상도이다.

### 3. 더 높은 해상도가 필요한 슬라이드 식별

8회차에서 분석한 10장 중 다음 슬라이드는 더 높은 해상도가 도움될 수 있다:

| 슬라이드 | 현 해상도 | 더 높은 해상도가 도움되는 이유 |
|---|---|---|
| 26 (BoP↔IIP 매트릭스) | 200 DPI / 660KB | 매트릭스 셀 라벨이 작음. 400 DPI 재렌더링 시 작은 글자 가독성 개선. |
| 21 (상품수지 vs 무역수지) | 200 DPI / 193KB | 월별 라벨(2019/01~2023/02) 49개가 가로축에 빽빽이 표시 → 400 DPI 권장. |
| 16·17·18 (시계열 막대) | 200 DPI / 200~400KB | 25년 막대 그래프, 연도 라벨이 작음 → 일부 분기 식별 시 400 DPI 도움. |

**조치 권고**: 본 항목의 fallback 점검 단계에서는 해상도를 일률 상향할 필요 없음. 향후 명세서 작성(Phase 3) 또는 §0.2 라인 31 "전체 재점검" 단계에서 특정 슬라이드만 선택적으로 400 DPI 재렌더링하면 충분.

### 4. PDF 페이지 ↔ PPT 슬라이드 정렬 검증

| PDF 페이지 | PPT 슬라이드 | 정렬 |
|---|---|---|
| 1~14 | 1~14 | 1:1 일치 |
| 15~20 | 15~20 | 1:1 일치 (PPT는 텍스트 비어 있으나 PDF는 차트 이미지 표시) |
| 21 | 21 | 1:1 일치 |
| 22~31 | 22~31 | 1:1 일치 |

**결론**: PDF 31페이지와 PPT 31슬라이드가 동일 순서로 정확히 매핑되어, 슬라이드 번호 인용이 PDF 페이지 번호와 호환된다. 8회차에서 사용한 인용 방식("slide 26 / PDF p.26")이 일관되게 유효.

## 본 항목 종료 조건 충족 여부

| 라인 28 요구 | 충족 여부 | 근거 |
|---|---|---|
| PPT 추출이 어려운 경우 식별 | 충족 | 위 §1 표로 PPT 직접 렌더링 한계 명시 |
| PDF 문서에서 이미지 추출 | 충족 | 8회차에서 pymupdf로 31페이지 PNG 렌더링 완료 |
| 추출 이미지 claude 멀티모달 분석 | 충족 | 8회차에서 핵심 10장 분석 완료 |

## 환경 변화

없음. 8회차에서 설치한 `pymupdf==1.27.2.3`이 본 항목의 요구도 함께 충족.

## 관련 절대경로

- 8회차 산출물: `db/data/_background_notes/08_multimodal_slide_analysis.md`
- 추출 이미지: `db/data/_background_notes/slide_images/slide_01.png` ~ `slide_31.png`
- 1차 근거: `background/BoP.pdf`, `background/BoP.pptx`
