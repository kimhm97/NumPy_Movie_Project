import numpy as np

# 확장 step1에서 만든 배열 불러오기
# allow_pickle = True : 배열 안에 리스트가 포함되어 있어 객체 허용 필요
data_array = np.load("../03_outputs/results/data_array_extension.npy", allow_pickle=True)

# 감독별 평균 평점
director_ratings = {}  # 감독별 평점 리스트를 담을 딕셔너리

# 각 영화 데이터를 순회하며 감독별 평점 수집
for row in data_array:
    rate = row[2]  # 해당 영화 평점
    for director in row[4]:  # row[4]에 감독 리스트가 들어 있음
        # setdefault : 감독이 키로 없으면 빈 리스트 초기화 후 append
        director_ratings.setdefault(director, []).append(rate)


# 감독별 평균 평점 (소수점 1자리 반올림)
director_avg = {d: round(sum(r)/len(r), 1) for d, r in director_ratings.items()}

# 평균 평점 기준 내림차순 정렬
director_avg_sort = sorted(director_avg.items(), key=lambda x: x[1], reverse= True)

# 상위 5명의 감독 출력
print("감독별 평균 상위 5명")
for d, avg in director_avg_sort[:5]:
    print(f"{d}: {avg}")

