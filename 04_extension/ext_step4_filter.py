import numpy as np

# 확장 step1에서 만든 배열 불러오기
data_array = np.load("../03_outputs/results/data_array_extension.npy", allow_pickle=True)

# 사용자 입력값
min_rate = float(input("최소 평점을 입력하세요 (예: 8.0): "))
min_year = int(input("최소 제작년도를 입력하세요 (예: 2000): "))

# 조건 필터링
filtered = []
for row in data_array:
    title = row[0]
    rate = row[2]
    year = row[3]

    # 조건 체크
    if rate >= min_rate and year >= min_year:
        filtered.append([title, rate ,year])

# NumPy 배열로 변환
filtered_array = np.array(filtered, dtype=object)

# 결과 출력
print(f"평점 {min_rate} 이상 & {min_year}년 이후 제작 영화 {len(filtered)}개 목록: ")
for movie in filtered_array:
    print(f"{movie[0]}")

