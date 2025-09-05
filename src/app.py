import streamlit as st
from elasticsearch import Elasticsearch

# Elasticsearch 클라이언트 객체 생성 (서버 접속)
es = Elasticsearch(
    cloud_id=st.secrets["ES_CLOUD_ID"],
    basic_auth=("elastic", st.secrets["ES_PASSWORD"])
)

INDEX_NAME = 'k-content'

# Streamlit 웹 앱의 UI 구성
st.title("🎬 K-콘텐츠 검색 엔진")
st.write("영화나 드라마의 줄거리(plot)를 기반으로 검색합니다.")

# 1. 사용자로부터 검색어 입력받기
search_query = st.text_input("검색어를 입력하세요:", placeholder="예: 생존을 위한 치열한 사투")

# 2. '검색' 버튼 생성 및 클릭 이벤트 처리
if st.button("검색"):
    if search_query:
        # 3. Elasticsearch에 보낼 검색 쿼리(Query) 작성
        # multi_match 쿼리로 여러 필드(title, director, genre, plot)를 동시에 검색
        body = {
            "query": {
                "multi_match": {
                    "query": search_query,
                    "fields": ["title", "director", "genre", "plot"]
                }
            }
        }

        # 4. es.search()를 이용해 검색 실행
        results = es.search(index=INDEX_NAME, body=body)

        # 5. 검색 결과 화면에 표시
        st.write(f"'{search_query}'에 대한 검색 결과 (총 {results['hits']['total']['value']}개)")

        if results['hits']['hits']:
            for doc in results['hits']['hits']:
                st.divider() # 결과 구분을 위한 라인
                st.subheader(f"{doc['_source']['title']} (평점: {round(doc['_score'], 2)})")
                st.write(f"**감독:** {doc['_source']['director']}")
                st.write(f"**장르:** {doc['_source']['genre']}")
                st.write(doc['_source']['plot'])
        else:
            st.write("검색 결과가 없습니다.")

    else:
        st.warning("검색어를 입력해주세요.")