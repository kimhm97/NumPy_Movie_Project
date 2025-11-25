import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# ================================================
# 파이참 한글 시각화 설정
# ================================================
#  한글 폰트 경로 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # 맑은 고딕
fontprop = fm.FontProperties(fname=font_path, size=12)  # 폰트 속성 객체 생성

# 음수 표시 문제 방지
plt.rcParams['axes.unicode_minus'] = False

# ==========================================================
# Step3 star - 배우별 평균 평점 분석
# ==========================================================

# 데이터 로드
data_array = np.load("../03_outputs/results/data_array_extension.npy", allow_pickle=True)

# 배우별 평점 수집
star_ratings = {}
for row in data_array:
    rate = row[2]
    for star in row[5]:
        star_ratings.setdefault(star, []).append(rate)

# 배우별 평균 평점 계산
star_avg = {s: round(sum(r)/len(r),2) for s,r in star_ratings.items()}

# 평균 평점 기준 내림차순 정렬
star_sorted = sorted(star_avg.items(), key=lambda x: x[1], reverse=True)

# 상위 10명 출력
print("배우별 평균 평점 상위 10명:")
for s, avg in star_sorted[:10]:
    print(f"{s}: {avg}")

# 상위 10명
top10_stars = star_sorted[:10]
names = [s[0] for s in top10_stars][::-1]
scores = [s[1] for s in top10_stars][::-1]

# ==========================================================
# 시각화: Dot Plot
# ==========================================================

plt.figure(figsize=(10,6))

# 점 그래프
plt.scatter(scores, names, s=120, color='salmon')

# 점 옆에 값 표시
for x, y in zip(scores, names):
    plt.text(x + 0.02, y, str(x), va='center', fontproperties=fontprop, fontsize=10)

plt.xlabel("평균 평점", fontproperties=fontprop)
plt.ylabel("배우 이름", fontproperties=fontprop)
plt.title("배우별 평균 평점 상위 10명 (Dot Plot)", fontproperties=fontprop)

plt.grid(axis='x', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()