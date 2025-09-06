import pandas as pd
import os

# 1. 샘플 데이터 정의 (딕셔너리의 리스트 형태)
data = [
    {'title': '위대한 개츠비', 'author': 'F. 스콧 피츠제럴드', 'genre': '소설, 비극, 모더니즘', 'plot': '1920년대 미국을 배경으로, 미스터리한 백만장자 개츠비의 무모한 사랑과 꿈, 그리고 좌절을 통해 아메리칸 드림의 허상을 그려낸 소설.'},
    {'title': '호밀밭의 파수꾼', 'author': 'J.D. 샐린저', 'genre': '성장 소설, 리얼리즘', 'plot': '퇴학당한 고등학생 홀든 콜필드가 집으로 돌아가기 전 며칠간 뉴욕을 방황하며 겪는 경험과 위선적인 세상에 대한 환멸, 순수에 대한 갈망을 독백체로 이야기한다.'},
    {'title': '이방인', 'author': '알베르 카뮈', 'genre': '철학 소설, 부조리주의', 'plot': '평범한 회사원 뫼르소가 어머니의 죽음에도 슬픔을 느끼지 않고, 우발적 살인을 저지른 후에도 사회의 기대와 관습을 거부하며 부조리한 세상과 마주하는 과정을 담담하게 그린다.'},
    {'title': '죄와 벌', 'author': '표도르 도스토옙스키', 'genre': '심리 소설, 철학 소설', 'plot': '가난한 대학생 라스콜니코프가 비범한 인간은 도덕률을 넘어설 수 있다는 초인 사상에 사로잡혀 노파를 살해하고, 이후 죄의식과 불안감 속에서 벌어지는 심리적 갈등과 구원의 과정을 다룬다.'},
    {'title': '상실의 시대', 'author': '무라카미 하루키', 'genre': '연애 소설, 성장 소설', 'plot': '1960년대 일본을 배경으로 주인공 와타나베가 두 여성, 나오코와 미도리와의 관계 속에서 겪는 사랑과 상실, 죽음과 성장의 아픔을 섬세하게 그린 소설.'},
    {'title': '멋진 신세계', 'author': '올더스 헉슬리', 'genre': '디스토피아, SF 소설', 'plot': '과학 기술로 모든 것이 통제되고 인간은 인공 생산되며, 안정을 위해 진정한 자유와 감정이 제거된 미래 세계를 통해 현대 문명을 비판하는 소설.'},
    {'title': '인간실격', 'author': '다자이 오사무', 'genre': '사소설, 자전적 소설', 'plot': '주인공 요조가 순수한 내면과 위선적인 세상 사이의 괴리감 속에서 익살꾼으로 자신을 위장하며 살아가다 결국 파멸에 이르는 과정을 그린 자전적 소설.'}
]

# 2. 데이터를 pandas DataFrame으로 변환
df = pd.DataFrame(data)

# 3. 데이터를 저장할 경로 설정
output_dir = 'data'
output_filename = 'sample_data.csv'
output_path = os.path.join(output_dir, output_filename)

# 4. 'data' 디렉터리가 없으면 생성
os.makedirs(output_dir, exist_ok=True)

# 5. DataFrame을 CSV 파일로 저장
# index=False: DataFrame의 인덱스를 파일에 포함하지 않음
# encoding='utf-8-sig': Excel 등에서 한글이 깨지지 않도록 하기 위함
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"'{output_path}' 파일이 성공적으로 생성되었습니다. ")