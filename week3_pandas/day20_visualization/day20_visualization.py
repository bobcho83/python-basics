# 오늘 배운 것: 데이터 시각화 — Matplotlib 선·막대·산점도·히스토그램·서브플롯·이중 축
# 숫자로 가득한 데이터를 한눈에 들어오는 그림으로 바꿔주는 기술

# 개념 정리
# plt.plot()      : 선 그래프 — 시간에 따른 추이 파악
# plt.bar()       : 막대 그래프 — 그룹 간 크기 비교
# plt.scatter()   : 산점도 — 두 변수의 상관관계 시각화
# plt.hist()      : 히스토그램 — 데이터 빈도·분포 확인
# plt.subplots()  : 화면 분할 — 여러 그래프를 한 화면에 배치
# ax.twinx()      : 이중 y축 — 단위가 다른 두 지표를 같은 x축에 표시
# plt.savefig()   : 그래프를 PNG/JPG 파일로 저장 (보고서·PPT 첨부용)
# plt.rc('font')  : 한글 깨짐 방지 필수 설정 (맥: 'AppleGothic')

import matplotlib.pyplot as plt
import numpy as np

# [필수] 한글 깨짐 방지 설정 — macOS 기준 'AppleGothic' / Windows: 'Malgun Gothic'
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False  # 마이너스(-) 기호 깨짐 방지

# ===== 초급 =====
# 핵심: 4가지 기본 그래프 — 선·막대·산점도·히스토그램

# 샘플 데이터
months       = ['1월', '2월', '3월', '4월', '5월']
sales        = [1000, 1500, 1300, 2000, 2500]
channels     = ['구글', '페이스북', '인스타', '유튜브']
clicks       = [450, 320, 580, 700]
cost         = [15, 12, 18, 25, 5]       # 광고 비용 (만원)
actual_clicks = [450, 320, 580, 700, 150] # 실제 클릭수
age_data     = [22, 25, 25, 30, 32, 35, 38, 42, 45, 50, 55]  # 고객 나이 분포

# 1. 선 그래프 — 월별 매출 추이
plt.figure(figsize=(6, 4))
plt.plot(months, sales, marker='o', color='blue', linestyle='--', linewidth=2)
plt.title("월별 매출 성장 추이")
plt.xlabel("월")
plt.ylabel("매출 (만원)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. 막대 그래프 — 광고 채널별 클릭수 비교
plt.figure(figsize=(6, 4))
plt.bar(channels, clicks, color='orange', alpha=0.8)
plt.title("광고 채널별 클릭수 비교")
plt.xlabel("마케팅 채널")
plt.ylabel("클릭수 (회)")
plt.tight_layout()
plt.show()

# 3. 산점도 — 광고 비용 vs 클릭수 상관관계
plt.figure(figsize=(6, 4))
plt.scatter(cost, actual_clicks, color='red', s=100, edgecolors='black')
plt.title("광고 비용과 클릭수의 상관관계")
plt.xlabel("광고 비용 (만원)")
plt.ylabel("클릭수 (회)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 4. 히스토그램 — 고객 나이대 분포
plt.figure(figsize=(6, 4))
plt.hist(age_data, bins=5, color='green', edgecolor='black', alpha=0.7)
plt.title("주요 구매 고객 나이대 분포")
plt.xlabel("나이")
plt.ylabel("고객 수 (명)")
plt.tight_layout()
plt.show()

# ===== 중급 =====
# 핵심: plt.subplots()로 화면 분할 + 스타일링(color·alpha·legend) + tight_layout()

google_clicks = [450, 520, 480, 600, 750]
fb_clicks     = [320, 380, 410, 390, 420]

# 1행 2열 분할 화면 생성
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 첫 번째 칸 — 구글 vs 페이스북 클릭 추이 (선 그래프 + 범례)
axes[0].plot(months, google_clicks, marker='o', color='blue',  label='구글')
axes[0].plot(months, fb_clicks,     marker='s', color='red',   label='페이스북', linestyle='--')
axes[0].set_title("주요 채널별 클릭수 변화 추이")
axes[0].set_xlabel("월별")
axes[0].set_ylabel("클릭수 (회)")
axes[0].grid(True, linestyle=':', alpha=0.6)
axes[0].legend()   # 범례(이름표) 표시

# 두 번째 칸 — 채널별 누적 광고 비용 (막대 그래프)
total_cost = [1200000, 850000]
axes[1].bar(['구글', '페이스북'], total_cost,
            color=['royalblue', 'crimson'], alpha=0.7, edgecolor='black')
axes[1].set_title("채널별 누적 광고 집행 비용")
axes[1].set_xlabel("마케팅 채널")
axes[1].set_ylabel("비용 (원)")

plt.tight_layout()  # 그래프 간격 자동 조정 — 글자 겹침 방지
plt.show()

# ===== 고급 =====
# 핵심: ax.twinx() 이중 y축 + plt.savefig() 이미지 파일 저장

marketing_cost = [150, 200, 180, 300, 400]  # 광고 비용 (만원)
ctr_revenue    = [2.5, 3.8, 3.2, 4.5, 5.2] # 클릭률 CTR (%)

fig, ax1 = plt.subplots(figsize=(8, 5))

# 첫 번째 y축 (왼쪽) — 광고 비용 막대 그래프
ax1.bar(months, marketing_cost, color='skyblue', alpha=0.7, label='광고 비용')
ax1.set_xlabel('집행 월')
ax1.set_ylabel('광고 비용 (만원)', color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue')

# twinx() — x축 공유, 두 번째 y축 (오른쪽) 생성
ax2 = ax1.twinx()

# 두 번째 y축 (오른쪽) — 클릭률 선 그래프
ax2.plot(months, ctr_revenue, color='crimson', marker='o', linewidth=2, label='클릭률(CTR)')
ax2.set_ylabel('클릭률 (%)', color='crimson')
ax2.tick_params(axis='y', labelcolor='crimson')

plt.title("월별 광고 비용 대비 클릭률(CTR) 트렌드 분석")

# savefig() — PNG 파일로 저장 (dpi=300: 인쇄용 고화질 / bbox_inches='tight': 여백 자동 정리)
plt.savefig('marketing_report_day20.png', dpi=300, bbox_inches='tight')
plt.show()
print("✅ 그래프 저장 완료 → 'marketing_report_day20.png'")
