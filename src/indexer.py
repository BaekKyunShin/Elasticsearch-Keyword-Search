import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
import pandas as pd

# .env 파일에서 환경 변수 불러오기
load_dotenv()

# os.getenv()를 사용해 환경 변수 값 읽어오기
CLOUD_ID = os.getenv("ES_CLOUD_ID")
CLOUD_PASSWORD = os.getenv("ES_PASSWORD")

# 불러온 값으로 Elasticsearch 클라이언트 객체 생성
es = Elasticsearch(
    cloud_id=CLOUD_ID,
    basic_auth=("elastic", CLOUD_PASSWORD)
)

# 데이터를 저장할 인덱스 이름 정의
INDEX_NAME = 'k-content'

# 인덱스 매핑(스키마) 정의
mapping = {
    "properties": {
        "title": {"type": "text", "analyzer": "nori"},
        "author": {"type": "text", "analyzer": "nori"},
        "genre": {"type": "text", "analyzer": "nori"},
        "plot": {"type": "text", "analyzer": "nori"},
    }
}

# 인덱스 생성 (기존 인덱스가 있다면 삭제 후 새로 생성)
if es.indices.exists(index=INDEX_NAME):
    es.indices.delete(index=INDEX_NAME)
    print(f"인덱스 '{INDEX_NAME}'를 삭제했습니다.")

# es.indices는 인덱스들의 구조와 설정을 관리(ex. es.indices.create(), es.indices.delete(), es.indices.exists(), es.indices.put_mapping())
es.indices.create(index=INDEX_NAME, mappings=mapping)
print(f"인덱스 '{INDEX_NAME}'를 생성했습니다.")

# CSV 파일에서 데이터 읽기
try:
    df = pd.read_csv('data/sample_data.csv')

    # 데이터를 하나씩 Elasticsearch에 색인
    for i, row in df.iterrows():
        doc = {
            "title": row["title"],
            "author": row["author"],
            "genre": row["genre"],
            "plot": row["plot"]
        }
        # es.index는 하나의 문서(document)를 특정 인덱스(index)에 저장(추가 또는 수정)하는 구체적인 메서드
        es.index(index=INDEX_NAME, id=i, document=doc)
        print(f"문서 ID {i} 색인 완료: {row['title']}")

    print("\n모든 문서의 색인이 성공적으로 완료되었습니다.")

except FileNotFoundError:
    print("오류: '../data/sample_data.csv' 파일을 찾을 수 없습니다.")
    print("create_data.py를 먼저 실행하여 샘플 데이터를 생성했는지 확인하세요.")