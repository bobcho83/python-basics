# 오늘 배운 것: DataFrame 생성 및 조회 — 필터링·정렬·병합·그룹화
# DataFrame의 구조 이해부터 데이터를 자유자재로 다루는 법까지

# 개념 정리
# DataFrame : 행(Row) + 열(Column)로 구성된 2차원 표 구조 — 엑셀 시트 그 자체
# 열 접근    : df["컬럼명"] → Series 반환
# 행 접근    : df.loc[라벨]  — 이름표 기반 / df.iloc[번호] — 순서 번호 기반
# 필터링     : df[조건] — Boolean Indexing, & (AND) · | (OR) 다중 조건
# 정렬       : df.sort_values(by="열", ascending=True/False)
# 병합       : pd.merge(df1, df2, on="공통열") — 엑셀 VLOOKUP과 동일
# 그룹화     : df.groupby("열")["집계열"].sum() / .agg(["sum","mean","count"])

import pandas as pd

# ===== 초급 =====
# 핵심: DataFrame 생성 + df.shape + 열/행 접근 (.loc / .iloc)

# 딕셔너리로 DataFrame 생성
data = {
    "캠페인명": ["여름세일", "신규가입", "리마케팅", "브랜드홍보"],
    "예산"   : [500000, 300000, 200000, 1000000],
    "클릭수" : [1200, 800, 450, 2100],
    "지역"   : ["서울", "경기", "부산", "전국"]
}

df = pd.DataFrame(data)

print("--- 전체 데이터프레임 ---")
print(df)
print(f"\n데이터 크기 (행, 열): {df.shape}")   # (4, 4) — 행 수, 열 수

# 열(Column) 접근 — Series로 반환
print("\n[예산 컬럼 정보]")
print(df["예산"])

# 행(Row) 접근 — loc: 라벨 기준
print("\n[첫 번째 행 상세 정보 (loc)]")
print(df.loc[0])

# iloc: 순서(정수) 기준 슬라이싱 — 인덱스 1~2 (2번째·3번째 행)
print("\n[두 번째부터 세 번째 행까지 (iloc)]")
print(df.iloc[1:3])

# 행·열 동시 접근 — loc[행, 열]
print(f"\n세 번째 캠페인의 클릭수: {df.loc[2, '클릭수']}")

# ===== 중급 =====
# 핵심: 파생 변수 추가 + 조건 필터링 + 다중 조건(&) + sort_values

# 파생 변수(새 열) — 기존 열 계산으로 클릭당 비용 생성
df["클릭당_비용"] = df["예산"] / df["클릭수"]

# 단일 조건 필터링 — 클릭수 1000회 이상
high_clicks = df[df["클릭수"] >= 1000]
print("\n--- 클릭수 1000회 이상 캠페인 ---")
print(high_clicks)

# 다중 조건 — 지역이 '서울' AND 예산 20만원 이상 (&로 연결)
seoul_expensive = df[(df["지역"] == "서울") & (df["예산"] >= 200000)]
print("\n--- 서울 + 예산 20만원 이상 캠페인 ---")
print(seoul_expensive)

# 정렬 — 클릭당 비용 오름차순 (가성비 순)
sorted_df = df.sort_values(by="클릭당_비용", ascending=True)
print("\n--- 클릭당 비용 낮은 순 정렬 ---")
print(sorted_df)

# ===== 고급 =====
# 핵심: 데이터 병합(merge) + 그룹화(groupby) + 복합 집계(agg)

# 두 개의 DataFrame 준비
df_campaign = pd.DataFrame({
    "캠페인명": ["여름세일", "신규가입", "리마케팅", "반짝특가"],
    "클릭수"  : [1200, 800, 450, 300],
    "지역코드": ["A", "B", "A", "C"]
})

df_region = pd.DataFrame({
    "지역코드": ["A", "B", "C"],
    "지역명"  : ["서울", "경기", "부산"]
})

# 데이터 병합 — '지역코드'를 공통 키로 두 표 합치기 (VLOOKUP과 동일)
merged_df = pd.merge(df_campaign, df_region, on="지역코드")
print("\n--- 병합된 데이터프레임 ---")
print(merged_df)

# 그룹화 — 지역명별 클릭수 합계
region_summary = merged_df.groupby("지역명")["클릭수"].sum()
print("\n--- 지역별 총 클릭수 ---")
print(region_summary)

# agg() — 여러 통계(합계·평균·개수)를 한 번에 집계
detail_summary = merged_df.groupby("지역명")["클릭수"].agg(["sum", "mean", "count"])
print("\n--- 지역별 상세 통계 (합계·평균·개수) ---")
print(detail_summary)
