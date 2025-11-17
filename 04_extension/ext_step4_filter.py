import numpy as np

# 확장 step1에서 만든 배열 불러오기
data_array = np.load("../03_outputs/results/data_array_extension.npy", allow_pickle=True)

def filter_movies(data, min_rate=0.0, min_year=0):
    """
    특정 조건을 만족하는 영화만 필터링
    :param data: NumPy 배열, 확장 step1 데이터
    :param min_rate: 최소 평점 (float)
    :param min_year: 최소 제작 연도 (int)
    :return: 조건을 만족하는 영화 리스트 [[Title, Rate, Year, Genre],...]
    """
    filtered = []
    for row in data:
        title = row[0]
        rate = row[2]
        year = row[3]

        # 조건 체크
        if rate >= min_rate and year >= min_year:
            filtered.append([title,rate,year])

    return filtered

# 평점  8.0 이상, 2000년 이후 제작
filter_list = filter_movies(data_array, 8.0, 2000)

print(f"총 {len(filter_list)}편의 영화가 조건을 만족합니다.\n")
print(" 조건 충족 영화 상위 10편 목록")
for mov in filter_list[:10]:
    print(f"{mov[0]}")

