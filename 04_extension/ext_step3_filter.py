import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# ================================================
# 파이참 한글 시각화 설정
# ================================================
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 경로 (맑은 고딕)
fontprop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['axes.unicode_minus'] = False  # 음수 표시 문제 방지

# ==========================================================
# 데이터 로드 및 필터링 (평점 8.0 이상, 2000년 이후 제작 영화)
# ==========================================================
data_array = np.load("../03_outputs/results/data_array_extension.npy", allow_pickle=True)

min_rate = 8.0
min_year = 2000

filtered = []
for row in data_array:
    title, rate, year = row[0], row[2], row[3]
    if rate >= min_rate and year >= min_year:
        filtered.append([title, rate, year])

filtered_array = np.array(filtered, dtype=object)

# ==========================================================
# 출력: 총 영화 수 및 상위 10개 영화 정보
# ==========================================================
print(f"총 영화 수 (평점 {min_rate} 이상 & {min_year}년 이후 제작): {len(filtered_array)}\n")
print("상위 10개 영화 (평점 높은 순):")
# 평점 기준 내림차순 정렬
top10_movies = sorted(filtered_array, key=lambda x: x[1], reverse=True)[:10]
for movie in top10_movies:
    print(f"{movie[0]} - 평점: {movie[1]}")

# ==========================================================
# Dot Plot & 히스토그램을 위한 데이터 준비
# ==========================================================
rates = filtered_array[:,1].astype(float)
years = filtered_array[:,2].astype(int)

unique_years = np.unique(years)
avg_rates = []
movie_counts = []

for y in unique_years:
    y_rates = rates[years == y]
    avg_rates.append(np.mean(y_rates))
    movie_counts.append(len(y_rates))

sizes = [c*20 for c in movie_counts]  # 점 크기 조정

# ==========================================================
# 시각화
# ==========================================================
fig, axes = plt.subplots(1, 2, figsize=(14,5))  # 서브플롯 2개

# 1) 히스토그램 - 평점 분포
axes[0].hist(rates, bins=np.arange(8, 10.1, 0.2), color='lightblue', edgecolor='black')
axes[0].set_xlabel("평점", fontproperties=fontprop)
axes[0].set_ylabel("영화 수", fontproperties=fontprop)
axes[0].set_title("평점 분포 (8.0 이상)", fontproperties=fontprop)

# 2) 연도별 평균 평점 & 영화 수 Dot Plot
axes[1].scatter(unique_years, avg_rates, s=sizes, color='salmon', alpha=0.6, edgecolor='black')
for x, y, c in zip(unique_years, avg_rates, movie_counts):
    axes[1].text(x, y + 0.02, str(c), ha='center', va='bottom', fontproperties=fontprop, fontsize=9)
axes[1].set_xlabel("제작 연도", fontproperties=fontprop)
axes[1].set_ylabel("평균 평점", fontproperties=fontprop)
axes[1].set_title("연도별 평균 평점 & 영화 수", fontproperties=fontprop)
axes[1].grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()
