import numpy as np

data_array = np.load("../03_outputs/results/data_array_extension.npy",allow_pickle=True)

# 배우별 평균 평점 계산
star_ratings = {}  # 배우별 평점 리스트를 담을 딕셔너리

# 각 영화 데이터를 순회하며 배우별 평점 수집
for row in data_array:
    rate = row[2]  # 해당 영화 평점
    for star in row[5]:   # row[5]에 배우 리스트가 들어 있음
        # setdefault: 배우가 키로 없으면 빈 리스트 초기화 후 append
        star_ratings.setdefault(star, []).append(rate)

# 배우별 평균 평점 계산 (소수점 21리 반올림)
star_avg = {s: round(sum(r)/len(r), 1) for s, r in star_ratings.items()}

# 평균 평점 기준 내림차순 정렬
star_avg_sort = sorted(star_avg.items(), key=lambda x: x[1], reverse=True)

# 상위 5명의 배우 출력
print("배우별 평균 평점 상위 5명:")
for s, avg in star_avg_sort[:5]:
    print(f"{s}: {avg}")
