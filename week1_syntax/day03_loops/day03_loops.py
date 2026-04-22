# 오늘 배운 것: 반복문 for / while — 구구단부터 제너레이터까지, 컴퓨터가 지치지 않고 일하게 만드는 기술

# ===== 개념 정리 =====
# for  문: 끝이 정해진 반복 (바구니 안 알맹이 수만큼)
# while문: 조건이 맞는 동안 계속 반복 (특정 상황이 끝날 때까지)

# ===== 초급 =====

# 1. for문과 range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
print("=" * 30)

fruits = ["사과", "배", "포도"]
for f in fruits:
    print(f)  # 사과, 배, 포도 차례대로 출력

# 미션 1: 구구단 2단 만들기 (for문)
print("--- 미션 1: 구구단 2단 만들기 ---")
for i in range(1, 10):
    print(f"2 * {i} = {2 * i}")
print("=" * 30)

# 미션 2: 출석부 부르기 (리스트 순회)
print("--- 미션 2: 출석부 부르기 ---")
students = ["철수", "영희", "민수", "Bob"]
for name in students:
    print(f"{name} 학생! 왔나요?")
print("=" * 30)

# 미션 3: 1부터 5까지 숫자 세기 (while)
print("--- 미션 3: 1부터 5까지 숫자 세기 ---")
number = 1
while number <= 5:
    print(f"현재 숫자는 {number} 입니다.")
    number += 1  # 숫자를 1씩 키워줘야 끝이 남

# 구구단 변형 — input으로 입력받아 원하는 단 출력
# break: 성공하면 while에서 탈출, else 생략으로 코드 심플하게!
while True:
    num = int(input("2~9까지만 입력해주세요! "))
    if 1 < num < 10:
        print(f"{num}단 시작!!")
        for i in range(1, 10):
            print(f"{num} * {i} = {num * i}")
        break
    print("2~9까지만 입력해주세요!!")  # else 생략 가능

# ===== 중급 =====
# 핵심: 이중 for문(중첩 루프) + break / continue + enumerate()

# 미션 1: 구구단 전체 출력 (이중 for문)
print("--- 미션 1: 구구단 전체 출력 ---")
for dan in range(2, 10):
    print(f"{dan}단 시작!")
    for i in range(1, 10):
        print(f"{dan} * {i} = {dan * i}")

# 미션 2: 짝수단만 출력 (continue 활용)
# continue → 이번 판은 건너뛰고 다음 반복으로
print("--- 미션 2: 짝수단만 출력 ---")
for dan in range(2, 10):
    if dan % 2 != 0:  # 홀수단이면 건너뜀
        continue
    print(f"{dan}단 시작!")
    for i in range(1, 10):
        print(f"{dan} * {i} = {dan * i}")

# 미션 3: 인덱스와 값 동시 출력 (enumerate)
# enumerate(리스트, start=1) → (순번, 값) 쌍으로 반환
print("--- 미션 3: 인덱스와 함께 출력 ---")
tasks = ["메일 확인", "파이썬 공부", "운동", "깃허브 업로드"]
for index, task in enumerate(tasks, start=1):
    print(f"{index}순위 할 일: {task}")

# ===== 고급 =====
# 핵심: 리스트 컴프리헨션 + zip() + 제너레이터 표현식

# 1. 리스트 컴프리헨션 — 한 줄로 압축
# 형식: [표현식 for 항목 in 이터러블 if 조건]
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"짝수 제곱 리스트: {even_squares}")

# 2. zip() — 두 리스트를 지퍼처럼 맞물려 병렬 순회
subjects = ["python", "AI", "Marketing"]
scores   = [100, 95, 85]

print("\n--- 과목별 성적표 ---")
for sub, score in zip(subjects, scores):
    print(f"{sub} 과목 점수: {score}점")

# 3. 제너레이터 표현식 — 메모리 절약형 반복
# [] 대신 ()를 사용 → 값을 미리 다 만들지 않고 필요할 때 하나씩 생성
# range가 10억이어도 메모리 거의 사용 안 함!
huge_range = (n * 10 for n in range(1_000_000))
print(f"\n제너레이터 객체 상태: {huge_range}")
print(f"첫 번째 값 꺼내기: {next(huge_range)}")
print(f"두 번째 값 꺼내기: {next(huge_range)}")
