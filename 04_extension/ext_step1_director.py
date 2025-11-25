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
# Step2 Director - 감독별 평균 평점 분석
# ==========================================================

# 데이터 로드
data_array = np.load("../03_outputs/results/data_array_extension.npy", allow_pickle=True)

# 감독별 평균 평점 계산
director_ratings = {}
for row in data_array:
    rate = row[2]
    for director in row[4]:
        director_ratings.setdefault(director, []).append(rate)

# 평균 평점 계산
director_avg = {d: round(sum(r)/len(r),2) for d,r in director_ratings.items()}

# 내림차순 정렬
director_sorted = sorted(director_avg.items(), key=lambda x: x[1], reverse=True)

# 상위 10명 출력
print("감독별 평균 평점 상위 10명:")
for d, avg in director_sorted[:10]:
    print(f"{d}: {avg}")


# 상위 10명
top10 = director_sorted[:10]

# 이름과 점수 리스트를 역순으로 (높은 점수가 아래 오지 않도록 보기 좋게)
names = [item[0] for item in top10][::-1]
scores = [item[1] for item in top10][::-1]

# ==========================================================
# 시각화: Dot Plot
# ==========================================================

plt.figure(figsize=(10, 6))

# 점 그래프
plt.scatter(scores, names, s=120, color='skyblue')

# 값 텍스트 표시
for x, y in zip(scores, names):
    plt.text(x + 0.02, y, str(x), va='center', fontproperties=fontprop, fontsize=10)

plt.xlabel("평균 평점", fontproperties=fontprop)
plt.ylabel("감독 이름", fontproperties=fontprop)
plt.title("감독별 평균 평점 상위 10명 (Dot Plot)", fontproperties=fontprop)

plt.grid(axis='x', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()