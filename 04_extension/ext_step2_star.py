import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# ================================================
# 한글 폰트 설정
# ================================================
font_path = "C:/Windows/Fonts/malgun.ttf"  # 맑은 고딕
fontprop = fm.FontProperties(fname=font_path)
plt.rcParams['font.family'] = fontprop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# ================================================
# 데이터 로드
# ================================================
data_array = np.load("../03_outputs/results/data_array_extension.npy", allow_pickle=True)

# ================================================
# 배우별 평점 수집
# ================================================
star_ratings = {}
for row in data_array:
    rate = row[2]
    for star in row[5]:
        star_ratings.setdefault(star, []).append(rate)

# ================================================
# 배우별 평균 평점 계산
# ================================================
star_avg = {s: round(sum(r)/len(r), 2) for s, r in star_ratings.items()}

# ================================================
# 정렬 및 구간 나누기
# ================================================
star_sorted = sorted(star_avg.items(), key=lambda x: x[1], reverse=True)
top10 = star_sorted[:10]
middle10 = star_sorted[len(star_sorted)//2 - 5 : len(star_sorted)//2 + 5]
bottom10 = star_sorted[-10:]
all_scores = [v for v in star_avg.values()]

# ================================================
# 콘솔 출력
# ================================================
print("\n===== 상위 10명 =====")
for n, s in top10:
    print(f"{n} - 평균 평점: {s}")

print("\n===== 중위 10명 =====")
for n, s in middle10:
    print(f"{n} - 평균 평점: {s}")

print("\n===== 하위 10명 =====")
for n, s in bottom10:
    print(f"{n} - 평균 평점: {s}")

# ================================================
# 시각화 준비 함수
# ================================================
def prepare(items):
    names = [x[0] for x in items][::-1]
    scores = [x[1] for x in items][::-1]
    return names, scores

top_names, top_scores = prepare(top10)
mid_names, mid_scores = prepare(middle10)
low_names, low_scores = prepare(bottom10)

# ================================================
# 1. 막대 그래프 (상위·중위·하위)
# ================================================
fig, axes = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle("배우별 평균 평점 - Bar Plot", fontsize=18)

axes[0].barh(top_names, top_scores, color='salmon', edgecolor='black')
for x, y in zip(top_scores, top_names):
    axes[0].text(x + 0.02, y, x, va='center')
axes[0].set_title("상위 10명 - Bar Plot")

axes[1].barh(mid_names, mid_scores, color='lightgreen', edgecolor='black')
for x, y in zip(mid_scores, mid_names):
    axes[1].text(x + 0.02, y, x, va='center')
axes[1].set_title("중위 10명 - Bar Plot")

axes[2].barh(low_names, low_scores, color='skyblue', edgecolor='black')
for x, y in zip(low_scores, low_names):
    axes[2].text(x + 0.02, y, x, va='center')
axes[2].set_title("하위 10명 - Bar Plot")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# ================================================
# 2. 도트 그래프 (상위·중위·하위)
# ================================================
fig, axes = plt.subplots(3, 1, figsize=(10, 15))
fig.suptitle("배우별 평균 평점 - Dot Plot", fontsize=18)

axes[0].scatter(top_scores, top_names, s=120, color='salmon')
for x, y in zip(top_scores, top_names):
    axes[0].text(x + 0.02, y, x, va='center')
axes[0].set_title("상위 10명 - Dot Plot")

axes[1].scatter(mid_scores, mid_names, s=120, color='lightgreen')
for x, y in zip(mid_scores, mid_names):
    axes[1].text(x + 0.02, y, x, va='center')
axes[1].set_title("중위 10명 - Dot Plot")

axes[2].scatter(low_scores, low_names, s=120, color='skyblue')
for x, y in zip(low_scores, low_names):
    axes[2].text(x + 0.02, y, x, va='center')
axes[2].set_title("하위 10명 - Dot Plot")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# ================================================
# 3. 박스 플롯 (전체 데이터)
# ================================================
plt.figure(figsize=(12, 4))
plt.boxplot(all_scores, vert=False, patch_artist=True,
            boxprops=dict(facecolor='lightgray', color='black'),
            medianprops=dict(color='red', linewidth=2),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            flierprops=dict(marker='o', color='orange', alpha=0.6))
plt.title("전체 배우 평균 평점 분포 - Box Plot")
plt.xlabel("평점")
plt.yticks([])
plt.grid(axis='x', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
