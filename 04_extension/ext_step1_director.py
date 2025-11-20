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

# ==========================================================
# 시각화
# ==========================================================
top10_directors = director_sorted[:10]  # 상위 10명 선택
names = [d[0] for d in top10_directors]  # 이름 리스트
scores = [d[1] for d in top10_directors]  # 평균 평점 리스트

# 그래프 크기 설정 (가로, 세로) 단위: 인치
plt.figure(figsize=(10,6))

# 수평 막대 그래프 그리기, 리스르 뒤집기 ::-1
plt.barh(names[::-1], scores[::-1], color='skyblue')

# x축 레이블 설정
plt.xlabel("평균 평점", fontproperties=fontprop)

# y축 레이블 설정
plt.ylabel("감독 이름", fontproperties=fontprop)

# 그래프 제목 설정
plt.title("감독별 평균 평점 상위 10명", fontproperties=fontprop)

# 그래프 출력
plt.show()
