import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# ================================================
# 파이참 한글 시각화 설정
# ================================================
#  한글 폰트 경로 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 맑은 고딕
fontprop = fm.FontProperties(fname=font_path, size=12)  # 폰트 속성 객체 생성

# 2️⃣ 음수 표시 문제 방지
plt.rcParams['axes.unicode_minus'] = False

# ==========================================================
# Step4 filter - 특정 조건 충족하는 영화만 필터링
# ==========================================================

# 데이터 로드
data_array = np.load("../03_outputs/results/data_array_extension.npy", allow_pickle=True)

# 조건 필터링
min_rate = 8.0
min_year = 2000

filtered = []
for row in data_array:
    title, rate, year = row[0], row[2], row[3]
    if rate >= min_rate and year >= min_year:
        filtered.append([title, rate, year])

filtered_array = np.array(filtered, dtype=object)

# 결과 출력
print(f"평점 {min_rate} 이상 & {min_year}년 이후 제작 영화 {len(filtered)}개:")
for movie in filtered_array[:20]:  # 상위 20개만 출력
    print(f"{movie[0]})")

# ==========================================================
# 시각화
# ==========================================================
titles = [f[0] for f in filtered_array[:10]]  # 상위 10개 영화 제목
rates = [f[1] for f in filtered_array[:10]]   # 평점

plt.figure(figsize=(10,6))
plt.barh(titles[::-1], rates[::-1], color='lightgreen')
plt.xlabel("평점", fontproperties=fontprop)
plt.ylabel("영화 제목", fontproperties=fontprop)
plt.title("평점 8.0 이상 & 2000년 이후 제작 영화 상위 10", fontproperties=fontprop)
plt.show()