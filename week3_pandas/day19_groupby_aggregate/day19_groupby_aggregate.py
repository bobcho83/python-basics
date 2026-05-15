# 오늘 배운 것: 그룹화와 집계 (Groupby & Aggregate)
# 같은 종류끼리 묶어서 원하는 통계를 한 번에 뽑아내는 법

# 개념 정리
# groupby()    : 특정 열 기준으로 데이터를 그룹으로 묶기
# sum/mean/count/max/min/std : 그룹별 집계 함수
# agg()        : 여러 집계 함수를 한 번에 적용 (리스트·딕셔너리·이름 지정)
# filter()     : 그룹 단위 조건 필터링 (lambda 활용)
# transform()  : 그룹 통계를 원본 DataFrame 크기로 되돌려 붙이기
# 다중 그룹화  : groupby(['열1', '열2']) — 2가지 이상 기준으로 계층 집계

import pandas as pd

# ===== 초급 =====
# 핵심: groupby() 기본 구조 + 집계 함수 (sum / mean / count) + agg() 한 번에 집계

df = pd.DataFrame({
    'product': ['노트북', '마우스', '노트북', '마우스', '키보드'],
    'sales'  : [100, 50, 150, 60, 80],
    'date'   : ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03']
})

# groupby() — 제품별로 그룹 객체 생성
grouped = df.groupby('product')

# for 루프로 각 그룹 확인
for name, group in grouped:
    print(f"\n=== {name} ===")
    print(group)

# 단일 집계 함수
print("\n[제품별 매출 합계]")
print(df.groupby('product')['sales'].sum())

print("\n[제품별 평균 매출]")
print(df.groupby('product')['sales'].mean())

print("\n[제품별 데이터 개수]")
print(df.groupby('product')['sales'].count())

# agg() — 리스트로 여러 함수 동시 적용
print("\n[sum·mean·count 한 번에]")
result = df.groupby('product')['sales'].agg(['sum', 'mean', 'count'])
print(result)

# ===== 중급 =====
# 핵심: agg() 딕셔너리·이름 커스터마이징 + filter() 그룹 필터링 + isin() 활용

# agg() 딕셔너리 — 컬럼마다 다른 함수 적용
print("\n[컬럼별 다른 함수 적용 (딕셔너리)]")
result = df.groupby('product').agg({
    'sales': ['sum', 'mean', 'count'],
    'date' : 'count'
})
print(result)

# agg() 이름 커스터마이징 — 결과 열 이름을 한글로 지정
print("\n[집계 결과 이름 커스터마이징]")
result = df.groupby('product')['sales'].agg(
    total  ='sum',
    average='mean',
    count  ='count'
)
print(result)

# filter() — 매출 합계 150 이상인 그룹의 행만 추출
print("\n[매출 합계 150 이상 그룹만 (filter)]")
result = df.groupby('product')['sales'].filter(lambda x: x.sum() >= 150)
print(result)

# isin() 활용 — 평균 매출 70 이상 제품의 전체 데이터 추출
product_avg = df.groupby('product')['sales'].mean()
high_performers = product_avg[product_avg >= 70].index
print("\n[평균 매출 70 이상 제품 전체 데이터]")
print(df[df['product'].isin(high_performers)])

# ===== 고급 =====
# 핵심: 다중 레벨 그룹화 + 마케팅 실전 분석 (전환율 계산)

# 2가지 기준 그룹화 — 지역 × 제품별 집계
df2 = pd.DataFrame({
    '지역'   : ['서울', '서울', '부산', '부산', '서울', '부산'],
    'product': ['노트북', '마우스', '노트북', '마우스', '마우스', '노트북'],
    'sales'  : [100, 50, 80, 60, 45, 120]
})

print("\n[지역 × 제품 다중 그룹화]")
result = df2.groupby(['지역', 'product'])['sales'].agg(['sum', 'mean', 'count'])
print(result)

# 3가지 기준 그룹화 — 연도 × 월 × 제품별 합계
df3 = pd.DataFrame({
    '연도'   : [2024, 2024, 2024, 2024, 2024],
    '월'     : [1, 1, 2, 2, 2],
    'product': ['노트북', '마우스', '노트북', '마우스', '키보드'],
    'sales'  : [100, 50, 150, 60, 80]
})

print("\n[연도 × 월 × 제품 3단계 그룹화]")
print(df3.groupby(['연도', '월', 'product'])['sales'].sum())

# 마케팅 캠페인 실전 분석
campaign_df = pd.DataFrame({
    'campaign'   : ['이메일', '이메일', '소셜', '소셜', '이메일', '소셜'],
    'day'        : ['월', '화', '월', '화', '수', '수'],
    'clicks'     : [100, 120, 80, 90, 110, 95],
    'conversions': [10, 12, 8, 9, 11, 10]
})

# 캠페인별 클릭·전환 성과 요약
print("\n===== 캠페인별 성과 =====")
result = campaign_df.groupby('campaign').agg({
    'clicks'     : ['sum', 'mean'],
    'conversions': ['sum', 'mean']
})
print(result)

# 캠페인 × 요일별 클릭수
print("\n===== 캠페인 × 요일별 클릭수 =====")
print(campaign_df.groupby(['campaign', 'day'])['clicks'].sum())

# 전환율(CVR) 파생 변수 → 캠페인별 평균 전환율 비교
campaign_df['conversion_rate'] = campaign_df['conversions'] / campaign_df['clicks']
print("\n===== 캠페인별 평균 전환율 =====")
print(campaign_df.groupby('campaign')['conversion_rate'].mean())
