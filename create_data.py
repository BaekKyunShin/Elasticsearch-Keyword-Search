import pandas as pd
import os

# 1. 샘플 데이터 정의 (딕셔너리의 리스트 형태)
data = [
    {'title': '기생충', 'director': '봉준호', 'genre': '드라마, 스릴러', 'plot': '전원백수로 살 길 막막하지만 사이는 좋은 기택(송강호) 가족. 장남 기우(최우식)에게 명문대생 친구가 연결시켜 준 고액 과외 자리는 모처럼의 고정수입을 얻을 절호의 기회다.'},
    {'title': '오징어 게임', 'director': '황동혁', 'genre': '스릴러, 서바이벌', 'plot': '456억 원의 상금이 걸린 의문의 서바이벌에 참가한 사람들이 최후의 승자가 되기 위해 목숨을 걸고 극한의 게임에 도전하는 이야기를 담은 넷플릭스 시리즈.'},
    {'title': '킹덤', 'director': '김성훈', 'genre': '사극, 좀비, 스릴러', 'plot': '죽었던 왕이 되살아나자 반역자로 몰린 왕세자가 향한 조선의 끝, 그곳에서 굶주림 끝에 괴물이 되어버린 이들의 비밀을 파헤치며 시작되는 미스터리 스릴러'},
    {'title': '범죄도시', 'director': '강윤성', 'genre': '액션, 범죄', 'plot': '2004년 서울, 하얼빈에서 넘어와 단숨에 기존 조직들을 장악하고 가장 강력한 세력인 춘식이파 보스 황사장(조재윤)까지 위협하며 도시 일대의 최강자로 급부상한 신흥범죄조직의 악랄한 보스 장첸(윤계상).'},
    {'title': '극한직업', 'director': '이병헌', 'genre': '코미디, 액션', 'plot': '해체 위기의 마약반 5인방은 범죄조직 소탕을 위해 위장창업한 마약치킨이 일약 맛집으로 입소문을 타게 되면서 벌어지는 이야기를 그린 코믹 수사극이다.'},
    {'title': '부산행', 'director': '연상호', 'genre': '좀비, 액션, 스릴러', 'plot': '정체불명의 바이러스가 전국으로 확산되고 대한민국 긴급재난경보령이 선포된 가운데, 열차에 몸을 실은 사람들은 단 하나의 안전한 도시 부산까지 살아가기 위한 치열한 사투를 벌이게 된다.'}
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

print(f"'{output_path}' 파일이 성공적으로 생성되었습니다.")