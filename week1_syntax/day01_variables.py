# 오늘 배운 것: 변수와 자료형 - int, str, list, dict의 기초부터 고급 활용까지

# ===== 초급 =====

# 1. 숫자(int)와 문자(str) 만들기
age = 10        # 정수형 (int)
name = "코딩천재"  # 문자열 (str)

# 2. 리스트(list) - 여러 개를 한 번에 담기 (0번부터 인덱스 시작)
fruits = ["사과", "바나나", "포도"]
print(fruits[0])  # 0번에 있는 과일은?

# 3. 딕셔너리(dict) - '사전'처럼 뜻을 연결하기 {키: 값}
user_info = {
    "name": "Bob",
    "level": 1,
    "hobby": "Python"
}
print(user_info["name"])  # "name"에 담긴 값은?

# ===== 연습용 코드 =====

# [미션 1] 소개 변수 만들기 (str, int, list)
my_name = "Bob"
my_age = 43
my_goal = ["파이썬 마스터", "깃허브 1일 1커밋", "AI 전문가"]

# [미션 2] 정보 딕셔너리 만들기
my_profile = {
    "이름": "Bob cho",
    "나이": 43,
    "목표": my_goal[1]
}

print(f"안녕하세요! 제 이름은 {my_profile['이름']}입니다.")
print(f"올해 제 나이는 {my_profile['나이']}입니다.")
print(f"올해 목표는 {my_profile['목표']}입니다.")

# ===== 중급 =====

# 샘플 데이터 (마케팅 캠페인 성과 데이터)
campaign_results = [
    {"name": "SNS 광고",       "Clicks": 150, "Cost": 500},
    {"name": "이메일 뉴스레터", "Clicks": 80,  "Cost": 100},
    {"name": "검색 광고",       "Clicks": 200, "Cost": 800},
    {"name": "인플루언서 협찬", "Clicks": 300, "Cost": 1500}
]

# 리스트 컴프리헨션 - 클릭 수 100 이상인 캠페인만 필터링
successful_campaigns = [c["name"] for c in campaign_results if c["Clicks"] >= 100]

# .get()으로 없는 키 안전하게 접근 (기본값 0)
for camp in campaign_results:
    conv = camp.get("conversion", 0)
    print(f"[{camp['name'][:2]}] 클릭: {camp['Clicks']}, 전환: {conv}")

# 딕셔너리 컴프리헨션으로 CPC(클릭당 비용) 보고서 생성
cpc_report = {c["name"]: c["Cost"] / c["Clicks"] for c in campaign_results}

print("\n--- 캠페인 CPC 보고서 ---")
for name, cpc in cpc_report.items():
    print(f"{name}: {cpc:.2f}원")

# ===== 고급 =====

# 1. 딕셔너리 병합과 언팩킹 (**) - 뒤에 오는 값이 우선순위
default_setting = {"theme": "dark", "font": "Nanum", "debug": False}
user_setting    = {"font": "Fira Code", "debug": True}
merged_setting  = {**default_setting, **user_setting}
print(f"설정 적용 결과: {merged_setting}")

# 2. 리스트 언팩킹 - 첫/마지막/나머지 분리
scores = [95, 80, 85, 70, 100]
first, *middle, last = scores
print(f"첫 점수: {first}, 마지막 점수: {last}, 중간 점수들: {middle}")

# 3. 제너레이터 - 메모리 효율적으로 대용량 데이터 처리
# [] 대신 ()를 쓰면 필요할 때만 값을 하나씩 생성
huge_data = (x**2 for x in range(1_000_000))
print(f"제너레이터 객체: {huge_data}")
print(f"첫 번째 결과값: {next(huge_data)}")

# 4. 딕셔너리 컴프리헨션 - 5글자 이상 단어만 {단어: 길이}로
words    = ["python", "ai", "marketing", "data", "developer"]
word_map = {w: len(w) for w in words if len(w) >= 5}
print(f"필터링된 단어 사전: {word_map}")
