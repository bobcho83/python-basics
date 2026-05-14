# 오늘 배운 것: 데이터 필터링과 정렬 — 조건 필터링·정렬·isin·groupby·시계열·query
# 수만 개의 데이터 중 내가 원하는 정보만 쏙쏙 골라내는 법

# 개념 정리
# 조건 필터링   : df[df['열'] >= 값] — True인 행만 추출
# 다중 조건     : & (AND) / | (OR) — 각 조건은 반드시 ()로 감쌀 것
# sort_values   : 특정 열 기준 정렬, ascending=False → 내림차순
# loc / iloc    : loc[라벨] 이름 기준(끝 포함) / iloc[번호] 위치 기준(끝 제외)
# isin()        : 리스트에 포함된 값만 한꺼번에 필터링
# groupby + agg : 그룹별 합계·평균·개수 집계
# map()         : 딕셔너리로 값 1:1 치환
# pd.to_datetime: 문자열 날짜 → 시간 객체 → 월·요일 추출
# np.where()    : 조건부 값 할당 — 엑셀 IF 함수와 동일
# df.query()    : SQL 스타일의 직관적 복합 필터링
# pivot_table() : 행·열 기준 집계 리포트 생성

import pandas as pd
import numpy as np

# ===== 초급 =====
# 핵심: 단일·다중 조건 필터링 + sort_values + loc/iloc + isin

data = {
    '캠페인': ['여름세일', '신규가입', '리마케팅', '브랜드홍보', '반짝특가'],
    '채널'  : ['Google', 'Facebook', 'Instagram', 'Google', 'YouTube'],
    '클릭수': [1200, 800, 450, 2100, 300],
    '비용'  : [500000, 300000, 200000, 1000000, 150000],
    '지역'  : ['서울', '경기', '부산', '서울', '전국']
}
df = pd.DataFrame(data)

# 1. 단일 조건 필터링 — 클릭수 1000회 이상
high_clicks = df[df['클릭수'] >= 1000]
print("--- 클릭수 1000회 이상 ---")
print(high_clicks)

# 2. 다중 조건 — 지역 '서울' AND 비용 80만원 이하 (각 조건 () 필수!)
seoul_efficient = df[(df['지역'] == '서울') & (df['비용'] <= 800000)]
print("\n--- 서울 지역 가성비 캠페인 ---")
print(seoul_efficient)

# 3. 정렬 — 클릭수 내림차순 (높은 순)
sorted_df = df.sort_values(by='클릭수', ascending=False)
print("\n--- 클릭수 높은 순 정렬 ---")
print(sorted_df)

# 4. loc — 0~2번 행, '캠페인'·'클릭수' 열만 선택 (열 선택은 loc[] 안에)
print("\n--- 0~2번 행, 캠페인·클릭수만 보기 (loc) ---")
print(df.loc[0:2, ['캠페인', '클릭수']])

# 5. isin() — Google·Instagram 채널만 한꺼번에 필터링
target_channels = df[df['채널'].isin(['Google', 'Instagram'])]
print("\n--- 주요 채널 성과 조회 (isin) ---")
print(target_channels)

# ===== 중급 =====
# 핵심: 파생 변수(CTR) 생성 + groupby + agg + map() 값 치환

data2 = {
    '채널'  : ['Google', 'Facebook', 'Instagram', 'Google', 'Facebook', 'Instagram'],
    '노출수': [10000, 8000, 12000, 15000, 9000, 11000],
    '클릭수': [450, 320, 580, 700, 400, 550],
    '비용'  : [150000, 120000, 180000, 250000, 140000, 170000]
}
df2 = pd.DataFrame(data2)

# 파생 변수 — 클릭률(CTR) = 클릭수 / 노출수 × 100
df2['CTR(%)'] = (df2['클릭수'] / df2['노출수']) * 100

# groupby + agg — 채널별 클릭수 합계·비용 평균·CTR 평균
channel_summary = df2.groupby('채널').agg({
    '클릭수'  : 'sum',
    '비용'    : 'mean',
    'CTR(%)' : 'mean'
})
print("\n--- 채널별 성과 요약 ---")
print(channel_summary)

# CTR 높은 순으로 정렬 — 가성비 채널 순위
sorted_summary = channel_summary.sort_values(by='CTR(%)', ascending=False)
print("\n--- 가성비 채널 순위 (CTR 기준) ---")
print(sorted_summary)

# map() — 영문 채널명 → 한글 치환
name_map = {'Google': '구글', 'Facebook': '페이스북', 'Instagram': '인스타'}
df2['채널_한글'] = df2['채널'].map(name_map)
print("\n--- 채널명 한글 치환 결과 ---")
print(df2[['채널', '채널_한글']].head())

# ===== 고급 =====
# 핵심: pd.to_datetime() 시계열 처리 + np.where() 조건부 등급 + query() 복합 필터링 + pivot_table()

data3 = {
    '날짜'  : ['2026-05-01', '2026-05-15', '2026-06-01', '2026-06-20', '2026-07-05'],
    '채널'  : ['Google', 'Facebook', 'Google', 'Instagram', 'YouTube'],
    '클릭수': [1200, 800, 2100, 450, 3000],
    '비용'  : [500000, 300000, 800000, 200000, 1200000]
}
df3 = pd.DataFrame(data3)

# 문자열 날짜 → datetime 변환 후 월·요일 추출
df3['날짜'] = pd.to_datetime(df3['날짜'])
df3['월']   = df3['날짜'].dt.month
df3['요일'] = df3['날짜'].dt.day_name()

# np.where() — 클릭수 ≥ 1000 AND 비용 ≤ 60만원이면 '우수', 아니면 '일반'
df3['효율등급'] = np.where(
    (df3['클릭수'] >= 1000) & (df3['비용'] <= 600000),
    '우수', '일반'
)

# query() — 5월 데이터 중 클릭수 1000 이상 추출 (SQL 스타일)
may_top_ads = df3.query("월 == 5 and 클릭수 >= 1000")
print("\n--- 5월 고효율 광고 추출 (query) ---")
print(may_top_ads)

# pivot_table() — 월별 × 채널별 총 비용 요약
monthly_pivot = df3.pivot_table(
    index    ='월',
    columns  ='채널',
    values   ='비용',
    aggfunc  ='sum',
    fill_value=0
)
print("\n--- 월별 / 채널별 지출 요약 (pivot_table) ---")
print(monthly_pivot)
