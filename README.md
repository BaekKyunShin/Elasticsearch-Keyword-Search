# Elasticsearch 기반 키워드 검색 엔진 (Elasticsearch-based Keyword Search Engine)

Python과 Elasticsearch를 활용하여 구축한 범용 키워드 검색 엔진입니다.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://elasticsearch-keyword-search-4hksmdwfnx46qcp2zdheir.streamlit.app/)

## 주요 기능

* **다중 필드 통합 검색**: 사용자가 정의한 여러 필드를 동시에 검색하여 종합적인 결과를 제공합니다.
* **한글 형태소 분석**: Elasticsearch의 **Nori** 분석기 플러그인을 적용하여, 조사가 포함된 검색어 등 한국어의 특성을 고려한 정확도 높은 검색이 가능합니다.
* **직관적인 웹 UI**: **Streamlit**을 활용하여 누구나 쉽게 사용할 수 있는 깔끔하고 반응형인 웹 인터페이스를 구현했습니다.
* **클라우드 기반 배포**: **Elastic Cloud**와 **Streamlit Community Cloud**를 이용해 24시간 안정적으로 운영되는 웹 서비스로 배포할 수 있는 아키텍처를 갖추고 있습니다.

## 나만의 데이터로 활용하기 (Customization)

이 프로젝트는 다른 데이터셋에도 쉽게 적용할 수 있도록 설계되었습니다.

1.  **데이터 준비 (`data/sample_data.csv`)**: `data` 폴더에 원하는 CSV 파일을 `sample_data.csv`라는 이름으로 준비합니다.
2.  **색인 스크립트 수정 (`src/indexer.py`)**: CSV 파일의 컬럼(열) 이름에 맞게 `mapping` 변수와 `doc` 딕셔너리 부분을 수정합니다. Nori 분석기를 사용할 필드를 지정할 수 있습니다.
3.  **검색 앱 수정 (`src/app.py`)**: `multi_match` 쿼리의 `fields` 목록과 검색 결과를 화면에 표시하는 부분을 새로운 데이터 구조에 맞게 수정합니다.

## 시스템 아키텍처

```
[사용자] <---> [Streamlit Community Cloud] <---> [Elastic Cloud]
                   (프론트엔드 & 웹서버)        (백엔드 데이터베이스)
                                                      |
                                     [Elasticsearch Index with Nori Analyzer]
```

## 기술 스택

* **Backend & Framework**: Python (`3.11+`), Elasticsearch (`8.15.0`)
* **Frontend**: Streamlit (`1.49.1`)
* **Database**: Elastic Cloud, Elasticsearch (`8.15.0`)
* **Korean Analyzer**: Nori Plugin
* **Data Handling**: Pandas (`2.3.2`)
* **Deployment & DevOps**: Streamlit Community Cloud, Docker
* **Dependency Management**: Poetry (`1.8.5`)

## 로컬 환경에서 실행하기 (Setup & Installation)

### 1. 프로젝트 클론 (Clone Repository)
```bash
git clone [https://github.com/](https://github.com/)[YOUR_GITHUB_ID]/[YOUR_REPOSITORY_NAME].git
cd [YOUR_REPOSITORY_NAME]
```

### 2. Elasticsearch (with Nori) 서버 실행
프로젝트에 포함된 `Dockerfile`을 이용해 Nori 분석기가 설치된 Elasticsearch 이미지를 빌드하고 실행합니다.
```bash
# 1. Docker 이미지 빌드
docker build -t elasticsearch-nori .

# 2. Docker 컨테이너 실행
docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" --name es-container-nori elasticsearch-nori
```

### 3. 파이썬 라이브러리 설치
Poetry를 사용해 프로젝트에 필요한 파이썬 라이브러리를 설치합니다.
```bash
poetry install
```

### 4. 데이터 색인
준비된 샘플 CSV 데이터를 로컬 Elasticsearch 서버에 색인합니다.
```bash
poetry run python src/indexer.py
```

### 5. 검색 앱 실행
Streamlit 개발 서버를 실행합니다.
```bash
poetry run streamlit run src/app.py
```
웹 브라우저에서 `http://localhost:8501` 주소로 접속하여 앱을 확인할 수 있습니다.

## License
This project is licensed under the MIT License.