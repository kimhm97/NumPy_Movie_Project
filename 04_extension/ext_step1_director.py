import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# ================================================
# 파이참 한글 시각화 설정
# ================================================
font_path = "C:/Windows/Fonts/malgun.ttf"
fontprop = fm.FontProperties(fname=font_path, size=12)
plt.rcParams['axes.unicode_minus'] = False

# ==========================================================
# Director - 감독별 평균 평점 분석
# ==========================================================
data_array = np.load("../03_outputs/results/data_array_extension.npy", allow_pickle=True)

# 감독별 평점 수집
director_ratings = {}
for row in data_array:
    rate = row[2]
    for director in row[4]:
        director_ratings.setdefault(director, []).append(rate)

# 평균 평점 계산
director_avg = {d: round(sum(r)/len(r),2) for d,r in director_ratings.items()}

# 내림차순 정렬
director_sorted = sorted(director_avg.items(), key=lambda x: x[1], reverse=True)

# ==========================================================
#  출력: 상위 10명
# ==========================================================
top10 = director_sorted[:10]
print("감독별 평균 평점 상위 10명:")
for name, score in top10:
    print(f"{name} - 평균 평점: {score}")

# ==========================================================
# 시각화 준비
# ==========================================================
# 이름과 점수 리스트를 역순으로 (그래프용)
names = [item[0] for item in top10][::-1]
scores = [item[1] for item in top10][::-1]

# ==========================================================
# Bar Plot
# ==========================================================
plt.figure(figsize=(10, 6))

plt.barh(names, scores, color='lightblue', edgecolor='black')
for x, y in zip(scores, names):
    plt.text(x + 0.02, y, str(x), va='center', fontproperties=fontprop, fontsize=10)

plt.xlabel("평균 평점", fontproperties=fontprop)
plt.ylabel("감독 이름", fontproperties=fontprop)
plt.title("감독별 평균 평점 상위 10명 (Bar Plot)", fontproperties=fontprop)
plt.grid(axis='x', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()

# ==========================================================
# Dot Plot
# ==========================================================
plt.figure(figsize=(10, 6))

plt.scatter(scores, names, s=120, color='skyblue')
for x, y in zip(scores, names):
    plt.text(x + 0.02, y, str(x), va='center', fontproperties=fontprop, fontsize=10)

plt.xlabel("평균 평점", fontproperties=fontprop)
plt.ylabel("감독 이름", fontproperties=fontprop)
plt.title("감독별 평균 평점 상위 10명 (Dot Plot)", fontproperties=fontprop)
plt.grid(axis='x', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()