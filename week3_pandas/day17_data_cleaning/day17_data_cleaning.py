# 오늘 배운 것: 데이터 정제(Data Cleaning) — 결측치·중복·타입변환·이상값·피벗 테이블
# "쓰레기를 넣으면 쓰레기가 나온다(GIGO)" — 분석 전에 데이터를 깨끗이 닦는 과정

# 개념 정리
# 결측치(NaN)    : 비어있는 칸 — dropna() 삭제 / fillna() 채우기
# 중복값         : drop_duplicates() — 동일 행 하나만 남기고 제거
# 타입 변환      : astype(int/float) — 문자열로 저장된 숫자를 계산 가능하게 변환
# 문자열 처리    : df["열"].str.strip() / .replace() — 공백·오타 정리
# 이상값(Outlier): 조건 필터링으로 말도 안 되는 값 제거
# apply()        : 열 전체에 사용자 정의 함수 적용
# map()          : 딕셔너리로 값 1:1 치환
# np.where()     : 조건부 치환 — 엑셀 IF 함수와 동일
# pivot_table()  : 행·열을 재구성한 요약 리포트 생성
# pd.to_datetime(): 문자열 날짜를 시간 객체로 변환 → 요일·월 추출 가능

import pandas as pd
import numpy as np

# ===== 초급 =====
# 핵심: 결측치·중복·타입 변환·이상값 처리 — 오염된 데이터 정제

# 오류가 포함된 원본 데이터 생성
data = {
    "고객명"  : ["Bob", "Alice", "Bob ", "Charlie", "David"],
    "나이"    : [25, 30, 25, np.nan, 200],   # NaN(결측치) + 200(이상값) 포함
    "가입일"  : ["2026-01-01", "2026-01-02", "2026-01-01", "2026-01-03", "2026-01-04"],
    "구매금액": ["10000", "20000", "10000", "15000", "missing"]  # 문자열 + 오류값
}
df = pd.DataFrame(data)

# 1. 문자열 공백 제거 — "Bob " → "Bob"
df["고객명"] = df["고객명"].str.strip()

# 2. 중복 행 제거 — 동일한 Bob 데이터 하나 삭제
df = df.drop_duplicates()

# 3. 결측치 처리 — 나이의 NaN을 평균값으로 채우기
df["나이"] = df["나이"].fillna(df["나이"].mean())

# 4. 타입 변환 — "missing"을 "0"으로 교체 후 int로 변환
df["구매금액"] = df["구매금액"].replace("missing", "0")
df["구매금액"] = df["구매금액"].astype(int)

# 5. 이상값 제거 — 나이 100 이상은 잘못된 데이터로 판단하고 필터링
df = df[df["나이"] < 100]

print("--- 정제된 데이터프레임 ---")
print(df)
print("\n--- 데이터 타입 확인 ---")
print(df.dtypes)

# ===== 중급 =====
# 핵심: apply() 함수 적용 / map() 값 치환 / np.where() 조건부 치환

data2 = {
    "고객명"  : ["Bob", "Alice", "Charlie", "David", "Eve"],
    "구매금액": [150000, 45000, 200000, 10000, 80000],
    "지역코드": [1, 2, 1, 3, 2]
}
df2 = pd.DataFrame(data2)

# apply() — 구매금액 기준으로 고객 등급 분류 함수 적용
def classify_grade(amount):
    if amount >= 100000:
        return "VIP"
    elif amount >= 50000:
        return "GOLD"
    else:
        return "SILVER"

df2["고객등급"] = df2["구매금액"].apply(classify_grade)

# map() — 딕셔너리로 지역코드 숫자 → 지역명 문자 1:1 치환
region_map = {1: "서울", 2: "경기", 3: "부산"}
df2["지역명"] = df2["지역코드"].map(region_map)

# np.where() — 조건이 참이면 "대상", 거짓이면 "제외" (엑셀 IF 함수와 동일)
df2["마케팅대상"] = np.where(df2["구매금액"] >= 50000, "대상", "제외")

print("\n--- 데이터 변환 결과 ---")
print(df2)

# ===== 고급 =====
# 핵심: pd.to_datetime() 시계열 변환 + pivot_table() 피벗 리포트 + resample() 월별 집계

data3 = {
    "날짜" : ["2026-05-01", "2026-05-01", "2026-05-02", "2026-05-02", "2026-05-03"],
    "채널" : ["Google", "Facebook", "Google", "Facebook", "Google"],
    "매출" : [150000, 200000, 180000, 150000, 300000],
    "클릭수": [450, 600, 500, 400, 900]
}
df3 = pd.DataFrame(data3)

# 문자열 날짜 → datetime 객체로 변환 (요일·월 추출 가능해짐)
df3["날짜"] = pd.to_datetime(df3["날짜"])
df3["요일"] = df3["날짜"].dt.day_name()   # 0=월(Monday) ~ 6=일(Sunday)

# 피벗 테이블 — 채널(행) × 요일(열) 기준 매출 합계 리포트
pivot_report = df3.pivot_table(
    values  ="매출",
    index   ="채널",
    columns ="요일",
    aggfunc ="sum",
    fill_value=0    # 데이터 없는 칸은 0으로 채우기
)
print("\n--- 요일별 / 채널별 매출 피벗 리포트 ---")
print(pivot_report)

# resample() — 월 단위(ME)로 리샘플링하여 월별 합산
monthly_summary = df3.resample("ME", on="날짜").sum(numeric_only=True)
print("\n--- 월별 성과 요약 ---")
print(monthly_summary)
