import numpy as np

# 확장 step1에서 만든 배열 불러오기
# allow_pickle = True : 배열 안에 리스트가 포함되어 있어 객체 허용 필요
data_array = np.load("../03_outputs/results/data_array_extension.npy", allow_pickle=True)

# 사용자 입력으로 특정 감독 지정
target_dire = input("평균 평점을 알고 싶은 감독 이름을 입력하세요: ").strip()

# 감독별 평균 평점
director_ratings = {}  # 감독별 평점 리스트를 담을 딕셔너리

# 각 영화 데이터를 순회하며 감독별 평점 수집
for row in data_array:
    rate = row[2]  # 해당 영화 평점
    for director in row[4]:  # row[4]에 감독 리스트가 들어 있음
        # setdefault : 감독이 키로 없으면 빈 리스트 초기화 후 append
        director_ratings.setdefault(director, []).append(rate)


# 특정 감독 평균 평점 계산
if target_dire in director_ratings:
    avg = round(sum(director_ratings[target_dire])/len(director_ratings[target_dire]),1)
    print(f"{target_dire} 감독 평균 평점 : {avg}")
else:
    print(f"{target_dire} 감독 정보가 데이터에 없습니다.")

