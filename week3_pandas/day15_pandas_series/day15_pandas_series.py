# 오늘 배운 것: Pandas 기초 — Series·DataFrame·필터링·정렬
# 2주차까지의 파이썬 문법이 '도구'였다면, 이제는 그 도구로 실제 데이터를 요리하는 법을 다룸

# 개념 정리
# pandas  : 데이터 분석 전용 라이브러리 (설치: pip install pandas)
# Series  : 인덱스(라벨)가 붙은 1차원 배열 — 리스트 + 딕셔너리의 장점을 결합
# DataFrame: 여러 Series가 나란히 붙은 2차원 표 구조 — 엑셀 시트와 동일한 형태
#
# 주요 접근법
#   series['라벨']       : 라벨(이름표)로 값 접근
#   df["열이름"]         : 특정 열 선택 → Series 반환
#   df[조건]             : Boolean Indexing — 조건에 맞는 행만 추출
#   .loc[행, 열]         : 라벨 기반 행·열 선택
#   .iloc[행, 열]        : 정수 순서 기반 행·열 선택
#   .sort_values(by=...) : 특정 열 기준 정렬

import pandas as pd  # 관례적으로 pd라는 별명 사용

# ===== 초급 =====
# 핵심: Series 생성 + 인덱싱 + 기본 통계 메서드 + 조건 필터링

# 일주일간의 광고 클릭 수 데이터로 Series 생성
data = [120, 150, 90, 200, 180, 130, 210]
days = ['월', '화', '수', '목', '금', '토', '일']

clicks = pd.Series(data, index=days)  # index 파라미터로 나만의 라벨 부여

print("--- 주간 클릭 수 Series ---")
print(clicks)

# 라벨(이름표)로 접근
print(f"\n수요일 클릭 수: {clicks['수']}")
# 위치(순서)로 접근 — .iloc 사용 권장 (FutureWarning 방지)
print(f"첫 번째 데이터: {clicks.iloc[0]}")

# 기본 통계 메서드 — 한 줄 명령으로 집계
print("\n--- 데이터 요약 ---")
print(f"총 클릭 수  (sum) : {clicks.sum()}")
print(f"평균 클릭 수 (mean): {clicks.mean():.2f}")
print(f"최대 클릭 수 (max) : {clicks.max()}")
print(f"최소 클릭 수 (min) : {clicks.min()}")

# 조건 필터링 — 150 이상인 날만 추출
print("\n[클릭 수가 150회 이상인 날]")
print(clicks[clicks >= 150])

# ===== 중급 =====
# 핵심: DataFrame 생성 + 열 선택 + 파생 변수 추가 + describe()

# 딕셔너리로 DataFrame 생성 — Key: 열 이름, Value: 데이터 리스트
data = {
    "채널"  : ["Google", "Facebook", "Instagram", "YouTube", "X"],
    "노출수" : [10000, 8500, 12000, 15000, 5000],
    "클릭수" : [450, 320, 580, 700, 150],
    "비용"  : [150000, 120000, 180000, 250000, 50000]
}

df = pd.DataFrame(data)

print("\n--- 마케팅 성과 데이터프레임 ---")
print(df)

# 특정 열만 선택 → Series 반환
print("\n[채널명 리스트]")
print(df["채널"])

# 파생 변수(새 열) 추가 — 기존 열 계산으로 새로운 열 생성
# 클릭률(CTR) = 클릭수 / 노출수 * 100
df["CTR(%)"] = (df["클릭수"] / df["노출수"]) * 100

print("\n--- CTR이 추가된 데이터 (상단 3개) ---")
print(df.head(3))   # head(n): 상위 n개 행만 출력

# 수치 데이터 전체 요약 통계 — 평균·표준편차·최솟값·사분위수 등 한눈에
print("\n--- 수치 데이터 요약 (describe) ---")
print(df.describe())

# ===== 고급 =====
# 핵심: 조건 필터링(Boolean Indexing) + .loc + sort_values + 다중 조건

# 동일 데이터 재구성
df["CTR(%)"] = (df["클릭수"] / df["노출수"]) * 100

# 1. 조건 필터링 — CTR 4% 이상인 채널만 추출
high_ctr = df[df["CTR(%)"] >= 4.0]
print("\n--- CTR 4% 이상 채널 ---")
print(high_ctr)

# 2. 정렬 — 클릭수 기준 내림차순 (ascending=False: 큰 값부터)
sorted_df = df.sort_values(by="클릭수", ascending=False)
print("\n--- 클릭수 기준 내림차순 정렬 ---")
print(sorted_df)

# 3. .loc — 라벨 기반으로 특정 행·열 선택
# 인덱스 0~2행, '채널'과 'CTR(%)' 열만 추출
print("\n--- 특정 범위 선택 (.loc) ---")
print(df.loc[0:2, ["채널", "CTR(%)"]])

# 4. 다중 조건 — 노출수 1만 이상 AND 비용 20만 이하 (가성비 채널)
filtered_ads = df[(df["노출수"] >= 10000) & (df["비용"] <= 200000)]
print("\n--- 가성비 채널 (노출 1만 이상 & 비용 20만 이하) ---")
print(filtered_ads)
