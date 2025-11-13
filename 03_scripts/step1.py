import numpy as np

# csv 파일 경로
csv_path = "../01_data/IMDB top 1000.csv"

# csv 파싱 함수 정의
# 큰 따옴표 언에 있는 쉼표와 바깥에 있는 쉼표 구분
def parse_csv_line(line):
    row = []          # 한 줄을 분리한 문자열 담을 리스트
    current = ""      # 현재 문자열 누적
    inside_quotes = False   # 큰 따옴표 안에 있는지 여부 체크
    for char in line:
        if char == '"' and not inside_quotes:   # 큰 따옴표 시작
            inside_quotes = True
        elif char == '"' and inside_quotes:     # 큰 따옴표 종료
            inside_quotes = False
        elif char == ',' and not inside_quotes: # 따옴표 밖에 쉼표
            row.append(current) # 여태 누적된 문자열 리스트 안에 담기
            current = ""        # 누적 초기화
        else:
            current += char      # 문자 누적
    row.append(current)          # 마지막 문자열 리스트 안에 담기
    return row                   # for문 밖에서 반환

# csv 파일 읽기
with open(csv_path,"r", encoding="utf-8") as f:
    lines = f.read().splitlines()  # 줄 단위 리스트 생성

# 헤더와 데이터 분리
header = parse_csv_line(lines[0]) # 파싱 헤더 추출
data_lines = lines[1:]            # 데이터 줄만 따로 저장
print(header)

# 영화 제목, 장르, 평점 컬럼 인덱스 반환
title_idx = header.index("Title")  # 1
genre_idx = header.index("Genre")  # 4
rate_idx = header.index("Rate")    # 5

# 데이터 전처리 리스트 준비
processed_data = []  # 최종 NumPy 배열로 변환할 데이터 담을 리스트

# 데이터 줄 반복 처리
for line in data_lines:
    row = parse_csv_line(line) # 파싱하여 컬럼 분리

    # row 길이가 필요한 컬럼 중 가장 큰 인덱스보다 작으면 해당 컬럼이 없다는 의미
    if len(row) <= max(title_idx, genre_idx, rate_idx):
        continue  # 이 줄은 건너 뛰고, 다음 줄을 처리하러 for문 처음으로 돌아감.

    # 컬럼 값 가져오기 및 공백 제거
    title = row[title_idx].strip()
    genre = row[genre_idx].strip()
    rate = row[rate_idx].strip()

    # 결측값 제거 : 빈 문자열이 있으면 해당 행 제외
    if title == "" or genre == "" or rate == "":
        continue

    # Title에서 Released_Year 추출
    # Title 마지막에 () 형태가 있어야만 슬라이싱
    if '(' in title and title[-1] == ')':
        released_year = title[title.rfind('(')+1 : title.rfind(')')]
    else:
        continue #연도가 없으면 건너뛰기

    # Rate와 Released_Year 타입 변환 후 리스트에 추가
    try:
        processed_data.append([title, genre, float(rate), int(released_year)])
    except ValueError:
        # 변환 불가한 값이 있으면 건너뛰기
        continue

# NumPy 배열로 변환
# dtype=object 사용 : 문자열 + 숫자가 혼합된 배열
data_array = np.array(processed_data, dtype=object)

# 결과 확인
print("NumPy 배열 형태의 데이터 출력: ", data_array)
print("\n데이터 크기(shape) 확인: ", data_array.shape)

# NumPy 배열 바이너리 파일로 저장
np.save("../04_outputs/data_array.npy", data_array)

