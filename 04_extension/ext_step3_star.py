import numpy as np

data_array = np.load("../03_outputs/results/data_array_extension.npy",allow_pickle=True)

# 사용자 입력으로 특정 배우 지정
target_star = input("평균 평점을 알고 싶은 배우 이름을 입력하세요: ").strip()

# 배우별 평균 평점 계산
star_ratings = {}  # 배우별 평점 리스트를 담을 딕셔너리

# 각 영화 데이터를 순회하며 배우별 평점 수집
for row in data_array:
    rate = row[2]  # 해당 영화 평점
    for star in row[5]:   # row[5]에 배우 리스트가 들어 있음
        # setdefault: 배우가 키로 없으면 빈 리스트 초기화 후 append
        star_ratings.setdefault(star, []).append(rate)

# 특정 배우 평균 평점 계산
if target_star in star_ratings:
    avg = round(sum(star_ratings[target_star])/len(star_ratings[target_star]), 1)
    print(f"{target_star} 배우 평균 평점 : {avg}")
else:
    print(f"{target_star} 배우 정보가 데이터에 없습니다.")

