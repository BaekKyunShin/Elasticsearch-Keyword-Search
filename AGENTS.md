# Repository Guidelines
이 문서는 Elasticsearch 기반 키워드 검색 서비스를 일관되고 유지보수 가능한 상태로 기여하기 위한 핵심 지침을 제공합니다.

## 프로젝트 구조 및 모듈 구성
- `src/indexer.py`는 `content` 인덱스를 초기화하고 Nori 분석기 매핑을 적용한 뒤 `data/sample_data.csv`의 행을 순차적으로 색인합니다.
- `src/app.py`는 Streamlit UI를 실행하며 다중 필드 검색을 수행하고 결과 카드를 정리해 보여줍니다.
- `create_data.py`는 샘플 데이터를 재생성하므로 파생된 CSV 파일은 `data/` 디렉터리에 유지합니다.
- `Dockerfile`은 Nori 플러그인이 포함된 Elasticsearch 8.15 이미지를 빌드하며, 배포 흐름은 `README.md`에 정리되어 있습니다.

## 빌드·테스트·개발 명령어
- `docker build -t elasticsearch-nori .` : Nori가 활성화된 로컬 Elasticsearch 이미지를 빌드합니다.
- `docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e "xpack.security.enabled=false" --name es-container-nori elasticsearch-nori` : 개발용 클러스터를 `localhost:9200`에서 실행합니다.
- `poetry install` : `pyproject.toml`에 정의된 Python 의존성을 동기화합니다.
- `poetry run python create_data.py` : 스키마 변경 시 `data/sample_data.csv`를 다시 생성합니다.
- `poetry run python src/indexer.py` : 최신 CSV 데이터로 `content` 인덱스를 재구축합니다.
- `poetry run streamlit run src/app.py` : UI를 `http://localhost:8501`에서 시작합니다.

## 코딩 스타일 및 네이밍 규칙
- Python 3.11을 기준으로 PEP 8 규칙과 4칸 들여쓰기를 적용하며, 저장소에서 선호하는 단일 따옴표 문자열을 유지합니다.
- 모듈·함수는 `snake_case`, Streamlit 위젯은 의미 있는 영문명, Elasticsearch 인덱스는 소문자로 명명합니다.
- 비밀 값은 `dotenv`로 로드하고 `ES_CLOUD_ID`, `ES_PASSWORD`처럼 대문자 환경 변수로 참조합니다.

## 테스트 지침
- 현재는 수동 검증이 기본입니다. 재색인 후 대표 검색어를 실행해 하이라이트와 필터가 의도대로 동작하는지 확인하세요.
- 자동화를 도입할 경우 `pytest` 사용을 권장하며, 테스트 코드는 `tests/` 아래에 두고 Elasticsearch 호출은 픽스처로 스텁 처리해 오프라인 실행을 유지합니다.
- 새로 추가한 샘플 쿼리나 픽스처는 문서화하여 팀원들이 동일하게 재현할 수 있도록 합니다.

## 커밋 및 PR 가이드라인
- `git log`에 보이는 간결한 동사형 스타일을 따르세요(예: `워크플로우 수정: curl -L 제거 및 HEAD/GET 요청 분리로 안정성 개선`). 요약 후 콜론을 사용해 세부 사항을 덧붙입니다.
- 관련 이슈를 참조하고, 색인·검색 품질에 미치는 영향과 UI/색인 변경 시 스크린샷 또는 터미널 출력도 첨부합니다.
- 제출 전 Docker와 Streamlit 명령이 로컬에서 성공하는지 확인하고, 리뷰어가 따라야 할 수동 절차를 함께 적어둡니다.

## 환경 및 보안 유의사항
- `.env`는 버전 관리에서 제외하고, 비밀 값은 안전한 채널로만 공유합니다.
- Elastic Cloud를 대상으로 작업할 경우 `src/indexer.py`의 삭제·재생성 로직이 올바른 프로젝트에만 적용되는지 실행 전에 반드시 확인하세요.
