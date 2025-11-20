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

# ==========================================================
# 시각화
# ==========================================================
top10_stars = star_sorted[:10]   # 상위 10명 배우 선택
names = [s[0] for s in top10_stars]  # 배우 이름만 추출
scores = [s[1] for s in top10_stars]  # 평균 평점만 추출

plt.figure(figsize=(10,6))
plt.barh(names[::-1], scores[::-1], color='salmon')
plt.xlabel("평균 평점", fontproperties=fontprop)
plt.ylabel("배우 이름", fontproperties=fontprop)
plt.title("배우별 평균 평점 상위 10명", fontproperties=fontprop)
plt.show()