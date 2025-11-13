import numpy as np

# NumPy 배열 불러오기
data_array = np.load("../03_outputs/results/data_array.npy", allow_pickle=True)

# 총 영화 개수
total_movies = data_array.shape[0]  # NumPy 배열 행 수 = 영화 개수
print("총 영화 개수:", total_movies)

# 평점 (Rate) 관련 통계
# 평점은 배열의 3번째 컬럼 (인덱스 2)
ratings = data_array[:, 2]  # 평점 컬럼 추출
ave_rat = np.mean(ratings)  # 평균
max_rat = np.max(ratings)   # 최고
min_rat = np.min(ratings)   # 최저

print(f"평균 평점: {ave_rat:.1f}\n최고 평점: {max_rat}\n최저 평점: {min_rat}")
