# 오늘 배운 것: 함수(Function) — def 기초부터 람다, 데코레이터까지

# 개념 정리
# 함수 = 자동 요리 기계
# def(정의)   : 기계를 만드는 것
# 매개변수     : 기계에 넣는 재료
# return(반환) : 기계가 내뱉는 완성품
# 호출         : 기계의 버튼을 눌러 실행하는 것

# ===== 기초 개념 =====

# 1. 함수 정의와 호출
def 인사하기():
    print("안녕하세요! 반가워요!")

인사하기()

# 2. 매개변수와 기본값 — 재료를 안 주면 미리 준비된 기본값 사용
def 선물하기(물건, 개수=1):
    print(f"{물건} {개수}개를 선물했습니다!")

선물하기("사과")       # 기본값 1 사용
선물하기("포도", 3)

# 3. 반환값이 있는 함수 + 여러 값 동시 반환 (언팩킹)
def add(a, b):
    return a + b

def get_name_and_age():
    return "철수", 25  # 튜플로 반환 → 언팩킹으로 나눠 받기

name, age = get_name_and_age()
print(f"{name}의 나이는 {age}입니다.")

# ===== 초급 =====

# 기본값 매개변수 — 입력 없으면 '오렌지' 주스
def make_juice(fruit="오렌지"):
    return f"상큼한 {fruit} 주스가 나왔습니다!"

print(make_juice("딸기"))
print(make_juice())

# 여러 값을 반환하는 함수 (면적 + 둘레 동시 반환)
def get_rectangle_info(width, height):
    area      = width * height
    perimeter = (width + height) * 2
    return area, perimeter

area, peri = get_rectangle_info(10, 5)
print(f"\n가로 10, 세로 5 사각형 → 면적: {area}, 둘레: {peri}")

# 조건문 + 반환
def check_score(score):
    return "합격" if score >= 80 else "재시험"

print(f"나의 결과: {check_score(95)}")

# ===== 중급 =====
# 핵심: *args / **kwargs + 람다(Lambda) 함수

# 1. *args — 개수가 정해지지 않은 인자를 튜플로 수집
def calculate_sum(*numbers):
    return sum(numbers)

print(f"\n3개 더하기: {calculate_sum(1, 2, 3)}")
print(f"5개 더하기: {calculate_sum(10, 20, 30, 40, 50)}")

# 2. **kwargs — 키워드 인자를 딕셔너리로 수집
def print_user_report(name, **details):
    print(f"\n--- {name}님의 리포트 ---")
    for key, value in details.items():
        print(f"- {key}: {value}")

print_user_report("Bob", 나이=25, 목표="1일 1커밋", 주언어="Python")

# 3. Lambda 함수 — 이름 없는 한 줄짜리 함수
# 형식: lambda 매개변수: 표현식
students = [("철수", 80), ("영희", 95), ("민수", 70)]
students.sort(key=lambda x: x[1], reverse=True)  # 점수(x[1]) 기준 내림차순
print(f"\n성적 우수자 순위: {students}")

# ===== 고급 =====
# 핵심: 일급 객체 + 클로저(Closure) + 데코레이터(Decorator)

# 데코레이터 정의 — 함수 앞뒤에 기능을 '장식'하는 @기호 사용
# 원본 함수를 수정하지 않고 새 기능 추가 가능
def start_end_decorator(func):
    def wrapper():
        print(f"--- '{func.__name__}' 함수 작업을 시작합니다 ---")
        func()  # 실제 함수 실행
        print("--- 작업을 모두 마쳤습니다 ---\n")
    return wrapper

@start_end_decorator
def say_hello():
    print("안녕하세요, 밥(Bob)님! 파이썬 공부를 열심히 하시는군요!")

@start_end_decorator
def study_python():
    print("열심히 깃허브에 잔디를 심고 있습니다....🌱")

say_hello()
study_python()

# ===== 실습 과제 =====

# 과제 1: 두 수 곱하기
def multiply(a, b):
    return a * b

print(f"5 곱하기 3 = {multiply(5, 3)}입니다.")
print(multiply(10, 2))

# 과제 2: 성적 판정 함수
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(grade(95))  # A
print(grade(75))  # C

# 과제 3: 리스트 역순 함수
def reverse_list(a):
    return list(reversed(a))

print(reverse_list([1, 2, 3, 4, 5]))   # [5, 4, 3, 2, 1]
print(reverse_list([10, 9, 8, 7, 6]))  # [6, 7, 8, 9, 10]
