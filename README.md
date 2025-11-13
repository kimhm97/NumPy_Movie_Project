
# 🎬 NumPy 기반 영화 평점 분석 프로젝트

**한 줄 소개:** IMDb Top 1000 영화 데이터를 활용하여 영화 평점 분석 및 데이터 처리 실습 프로젝트

---

## 📌 프로젝트 개요

* **목표:** NumPy를 활용하여 영화 데이터를 분석하고, 장르/연도별 평점 트렌드를 파악합니다.
* **사용 데이터:** [IMDB Top 1000 CSV](https://www.kaggle.com/datasets/omarhanyy/imdb-top-1000) (팀원 각자 다운로드 필요 — GitHub에 업로드 금지)
* **주요 기능:**

  1. NumPy 배열을 활용해 영화 데이터 분석
  2. 장르별/연도별 평균 평점 분석
  3. 최고 평점 영화 확인
  4. 시각화를 통해 트렌드 분석 가능
  5. 프로젝트 확장: 감독/배우별 평점 분석, 조건 필터링

---

## 👥 팀 구성 & 역할

* **김혜민 (CTO)**

  * 프로젝트 구조 설계, Step1~2 완료, GitHub 관리
  * 프로젝트 확장 기능 구현
    * 특정 감독별 평균 평점 분석
    * 특정 배우별 평균 평점 비교
    * 특정 조건 영화 필터링
  * 시각화 작업 공동 수행

* **한다예 (팀원)**

  * Step3~5 수행
    * Step3: 평점이 높은 영화 찾기
    * Step4: 장르별 평균 평점 분석
    * Step5: 연도별 평점 변화 분석 
  * 시각화 작업 공동 수행

**역할 분담 요약:**

| Step    | 담당        |
|---------| --------- |
| 1~2     | 김혜민       |
| 3~5     | 한다예       |
| 시각화     | 김혜민 + 한다예 |
| 프로젝트 확장 | 김혜민       |

---

## 📁 프로젝트 구조

```
NumPy_Movie_Project/
├── 01_data/                 
│   └── IMDB_top_1000.csv           # 원본 CSV 데이터
├── 02_scripts/              
│   ├── step1.py                    # 데이터 준비 + 전처리
│   ├── step2.py                    # 기본 데이터 탐색
│   ├── step3.py                    # 평점 높은 영화 찾기
│   ├── step4.py                    # 장르별 평균 평점 분석 
│   └── step5.py                    # 연도별 평균 평점 분석 
├── 03_outputs/              
│   ├── results/                    # Step 실행 결과 파일 
│   └── visualization/              # 시각화 결과 (PNG, PDF 등)
├── 04_extension/                   # 프로젝트 확장 분석 
├── .gitignore
├── README.md
└── requirements.txt

```

---

## 💾 데이터 관리 안내

⚠️ **중요:**

- CSV 파일(`IMDB Top 1000.csv`)은 **01_data** 폴더에 수동으로 넣어야 함.
👉 이 방식으로 관리해야 데이터 충돌이 생기지 않는다.

## 📝 Step별 진행 가이드


### Step 1: 데이터 준비

* IMDb CSV 다운로드 후, `Title`, `Genre`, `Rate` 컬럼 선택
* 결측값 제거, NumPy 배열로 변환

### Step 2: 기본 데이터 탐색

* 영화 총 개수, 평균/최고/최저 평점 계산

### Step 3: 평점이 높은 영화 찾기

* 최고 평점 영화 출력

### Step 4: 장르별 평균 평점 분석

* 모든 장르 추출 후, 장르별 평균 평점 계산
* 높은 순 정렬

### Step 5: 연도별 평점 변화 분석

* Released_Year 기준 평균 평점 계산
* 오름차순 출력

### Step 6: 결과 시각화

* Matplotlib으로 연도별 평점 트렌드 시각화
* 팀원과 함께 진행

### 프로젝트 확장 

* 특정 감독(Director)별 평균 평점 분석
* 특정 배우(Star) 별 평균 평점 비교
* 특정 조건 영화 필터링 (평점 8.0 이상 & 2000년 이후 제작)

---

## ⚙️ 협업 안내

[팀원 실행 순서]

1️⃣ git clone https://github.com/kimhm97/NumPy_Movie_Project.git

2️⃣ cd NumPy_Movie_Project

3️⃣ python -m venv .venv

4️⃣ .venv\Scripts\activate

5️⃣ pip install -r requirements.txt

6️⃣ Kaggle에서 ‘IMDB Top 1000.csv’ 다운로드 후 01_data 폴더에 저장

7️⃣ 브랜치 생성 후 분석:
    git checkout -b feature/analysis

8️⃣ 작업 완료 후:
    git add .
    git commit -m "Add visualization"
    git push origin feature/analysis

9️⃣ GitHub에서 Pull Request 생성 → Merge

---