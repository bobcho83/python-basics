# 오늘 배운 것: 3주차 종합 미니 프로젝트 — 쇼핑몰 판매 데이터 분석 파이프라인
# CSV 로드 → 데이터 정제 → 분석(필터링·그룹화) → 시각화 리포트 완성

# 개념 정리 — 전체 파이프라인 4단계
# 1단계 (로드)    : CSV 파일 생성 후 pd.read_csv()로 불러오기
# 2단계 (정제)    : drop_duplicates() 중복 제거 / fillna(median()) 결측치 처리 / astype(int) 타입 변환
# 3단계 (분석)    : describe() 기본 통계량 / 조건 필터링 / groupby + agg() 카테고리별 집계
# 4단계 (시각화)  : subplots(1,3) 3칸 대시보드 — 선 그래프(추이) · 막대(비교) · 히스토그램(분포)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# [필수] 한글 깨짐 방지
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

# ===== 1단계: 데이터 로드 =====
# 가상 쇼핑몰 CSV 데이터 생성 (결측치·중복 포함)
raw_data = """날짜,고객명,카테고리,수량,금액
2026-05-01,Bob,의류,2,50000
2026-05-01,Alice,전자제품,1,120000
2026-05-02,Bob,의류,2,50000
2026-05-02,Charlie,식품,5,25000
2026-05-03,David,전자제품,,300000
2026-05-03,Alice,식품,3,15000
2026-05-04,Eve,의류,1,25000
2026-05-04,Eve,의류,1,25000
"""

with open("sales_data.csv", "w", encoding="utf-8") as f:
    f.write(raw_data)

df = pd.read_csv("sales_data.csv")
print("--- 1. 원본 데이터 로드 ---")
print(df)
print("\n[데이터 타입 확인]")
print(df.dtypes)

# ===== 2단계: 데이터 정제 =====
print("\n--- 2. 데이터 정제 ---")

# 중복 행 제거 — Eve 2026-05-04 의류 중복 건 1개 삭제
df = df.drop_duplicates()

# 결측치 처리 — 수량 NaN(David)을 중앙값으로 대체
df['수량'] = df['수량'].fillna(df['수량'].median())

# 타입 변환 — 수량을 float → int
df['수량'] = df['수량'].astype(int)

print("[정제 완료 후 데이터]")
print(df)

# ===== 3단계: 데이터 분석 =====
print("\n--- 3. 데이터 분석 ---")

# 기본 통계량 — count·mean·std·min·max 한눈에 확인
print("[전체 수치 데이터 기본 통계량]")
print(df.describe())

# 조건 필터링 — 금액 3만원 이상 판매 건
high_sales = df[df['금액'] >= 30000]
print("\n[필터링: 3만원 이상 판매 데이터]")
print(high_sales)

# 그룹화 + agg() — 카테고리별 총 금액 & 평균 수량
category_summary = df.groupby('카테고리').agg(
    총매출=('금액', 'sum'),
    평균수량=('수량', 'mean')
).reset_index()
print("\n[그룹화: 카테고리별 성과 요약]")
print(category_summary)

# ===== 4단계: 데이터 시각화 =====
print("\n--- 4. 시각화 대시보드 생성 ---")

# 날짜별 일일 매출 집계 (시계열 변환 포함)
df['날짜'] = pd.to_datetime(df['날짜'])
daily_sales = df.groupby('날짜')['금액'].sum().reset_index()

# 1행 3열 종합 대시보드
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# [첫 번째 칸] 일별 판매 추이 — 선 그래프
axes[0].plot(
    daily_sales['날짜'].dt.strftime('%m-%d'),
    daily_sales['금액'],
    marker='o', color='blue', linewidth=2
)
axes[0].set_title("일별 판매 금액 추이")
axes[0].set_xlabel("날짜")
axes[0].set_ylabel("총 판매 금액 (원)")
axes[0].grid(True, linestyle=':')

# [두 번째 칸] 카테고리별 총 매출 — 막대 그래프
axes[1].bar(
    category_summary['카테고리'],
    category_summary['총매출'],
    color=['orange', 'lightgreen', 'pink'],
    edgecolor='black'
)
axes[1].set_title("카테고리별 총 매출 비교")
axes[1].set_xlabel("카테고리")
axes[1].set_ylabel("총 매출액 (원)")

# [세 번째 칸] 금액대별 빈도 분포 — 히스토그램
axes[2].hist(df['금액'], bins=4, color='purple', edgecolor='black', alpha=0.7)
axes[2].set_title("판매 금액대별 빈도 분포")
axes[2].set_xlabel("금액 구간")
axes[2].set_ylabel("주문 건수")

plt.tight_layout()
plt.savefig('sales_dashboard_day21.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ 분석 파이프라인 완료 — 대시보드 저장: 'sales_dashboard_day21.png'")
