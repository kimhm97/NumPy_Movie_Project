import numpy as np

# csv 파일 경로
csv_path = "../01_data/IMDB top 1000.csv"

# csv 파일 읽기
with open(csv_path,"r", encoding="utf-8") as f:
    lines = f.read().splitlines()  # 파일 전체 -> 줄 단위 리스트

# 헤더 확인
header = lines[0].split(',')
print(header)  # 0번째 컬럼은 빈 문자열

# 데이터 분리
data_lines = lines[1:]  # 실제 데이터

# 영화 제목, 장르, 평점 컬럼 인덱스 반환
title_idx = header.index("Title")  # 1
genre_idx = header.index("Genre")  # 4
rate_idx = header.index("Rate")    # 5

# 데이터 전처리
processed_data = []  # 전처리 후 데이터 담을 리스트

for line in data_lines:    # csv 헤더 제외한 모든 줄 전처리 하기
    row = line.split(",")  # 쉼표 기준 분리, 큰 따옴표 안에 있는 쉼표는 문자열 그대로 가져옴

    # 필요한 컬럼이 없는 행은 건너뛰기
    if len(row) <= max(title_idx, genre_idx, rate_idx):
        continue