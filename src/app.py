import streamlit as st
from elasticsearch import Elasticsearch

# Elasticsearch 클라이언트 객체 생성 (서버 접속)
es = Elasticsearch(
    cloud_id=st.secrets["ES_CLOUD_ID"],
    basic_auth=("elastic", st.secrets["ES_PASSWORD"])
)

INDEX_NAME = 'content'

# Streamlit 웹 앱 UI 구성
st.title("콘텐츠 검색 엔진")
st.write("고전소설에 대해 키워드 기반으로 검색합니다. 제목, 저자, 장르, 줄거리에 대한 키워드를 입력해주세요.")

# 사용자 검색어 입력
with st.form(key='search_form'):
    # 텍스트 입력과 제출 버튼을 폼 안에 배치
    search_query = st.text_input("검색어를 입력하세요:", placeholder="예: 사랑, 배신, 꿈")
    # 일반 버튼을 폼 제출 버튼으로 변경
    submit_button = st.form_submit_button(label='검색')

# '검색' 버튼 생성 및 클릭 이벤트 처리
if submit_button:
    if search_query:
        # Elasticsearch 검색 쿼리 작성
        # multi_match 쿼리로 여러 필드(title, director, genre, plot)를 동시에 검색
        body = {
            "query": {
                "multi_match": {
                    "query": search_query,
                    "fields": ["title", "author", "genre", "plot"]
                }
            }
        }

        # es.search()를 이용한 검색 실행
        results = es.search(index=INDEX_NAME, body=body)

        # 검색 결과 화면 표시
        st.write(f"'{search_query}'에 대한 검색 결과 (총 {results['hits']['total']['value']}개)")

        if results['hits']['hits']:
            for doc in results['hits']['hits']:
                st.divider() # 결과 구분을 위한 라인
                st.subheader(f"{doc['_source']['title']} (관련도 점수: {round(doc['_score'], 2)})")
                st.write(f"**저자:** {doc['_source']['author']}")
                st.write(f"**장르:** {doc['_source']['genre']}")
                st.write(doc['_source']['plot'])
        else:
            st.write("검색 결과가 없습니다.")

    else:
        st.warning("검색어를 입력해주세요.")