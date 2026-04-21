# 오늘 배운 것: 조건문 if / elif / else — 초급 판별기부터 고급 패턴 매칭까지

# ===== 초급 =====
# 신호등처럼 이해하기: if(초록) → elif(노랑) → else(빨강)
# 규칙 1) 조건 끝에 콜론(:) 필수
# 규칙 2) 실행할 코드는 들여쓰기(스페이스 4칸 or Tab) 필수

# [놀이공원 입장료 판별기]
# input()은 문자(str)로 받아오므로 int()로 변환 필요
age = int(input("나이가 어떻게 되세요? (나이를 입력해주세요!)"))

if age >= 20:
    print("성인입니다. 티켓 가격은 50,000원입니다.")
elif age >= 14:
    print("청소년입니다. 티켓 가격은 30,000원입니다.")
elif age >= 8:
    print("어린이입니다. 티켓 가격은 10,000원입니다.")
else:
    print("미취학 아동입니다. 티켓은 무료입니다.")

# ===== 중급 =====
# 핵심: 논리 연산자(and / or / not) + 중첩 조건문 + 조건부 표현식(Ternary)

# [스마트 로그인 시스템]
stored_id = "admin"
stored_pw = "1234"
is_premium = True

user_id = input("아이디를 입력하세요: ")
user_pw = input("비밀번호를 입력하세요: ")

if user_id == stored_id and user_pw == stored_pw:
    print("✅ 로그인이 완료되었습니다.")

    # 중첩 조건문: 로그인 성공한 사용자 안에서 등급 분기
    if is_premium:
        print("💎 프리미엄 회원님, 환영합니다! 모든 기능을 사용하실 수 있습니다.")
    else:
        print("👶 일반 회원님, 환영합니다.")

elif user_id != stored_id:
    print("❌ 아이디가 일치하지 않습니다.")
else:
    print("🔑 비밀번호가 틀렸습니다.")

# 조건부 표현식(Ternary): 한 줄로 결과 만들기
# 형식: 참일 때 값  if  조건  else  거짓일 때 값
status = "접근 승인" if is_premium or user_id == "admin" else "접근 제한"
print(f"현재 사용자 상태: {status}")

# ===== 고급 (1) — 패턴 매칭과 딕셔너리 매핑 =====

# 1. Match-Case 문 (Python 3.10+): 명령어 패턴을 분석해 처리
def process_command(command):
    match command.split():
        case ["quit"]:
            return "프로그램을 종료합니다."
        case ["move", direction]:
            return f"{direction} 방향으로 이동합니다."
        case ["attack", target, "with", weapon]:
            return f"{target}를 {weapon}로 공격합니다."
        case _:
            return "알 수 없는 명령입니다."

print(process_command("move North"))
print(process_command("attack Zombie with Sword"))

# 2. 딕셔너리 매핑: 복잡한 if-elif 대신 dict.get()으로 즉시 조회
def get_user_grade(score):
    grade = {9: "A", 8: "B", 7: "C"}
    return grade.get(score // 10, "F")

print(f"내 등급은: {get_user_grade(85)}")

# 3. all() / any(): 여러 조건을 한 줄로 검사
requirements = [
    True,   # 이메일 인증 완료
    True,   # 휴대폰 인증 완료
    False   # 마케팅 수신 동의
]

if all(requirements):
    print("✅ 모든 필수 조건을 만족했습니다!")
else:
    print("⚠️ 아직 완료되지 않은 필수 조건이 있습니다.")

# ===== 고급 (2) — 동적 처리와 단축 평가 =====
import operator

# 1. 동적 연산 처리: 딕셔너리로 if-elif 완전 제거
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

def smart_calc(a, op, b):
    return ops.get(op, lambda x, y: "지원하지 않는 연산자")(a, b)

print(f"계산 결과: {smart_calc(10, '*', 5)}")

# 2. 단축 평가(Short-circuit): None 에러를 방지하는 안전한 코드
# and → 앞이 False면 뒤를 아예 실행하지 않음
# or  → 앞이 False면 뒤를 실행
user_data = {"name": "Bob"}
user_name = user_data and user_data.get("name") or "익명 사용자"
print(f"로그인 유저: {user_name}")

# 3. 컴프리헨션 안의 다중 조건: 데이터 분류를 한 줄로
# 95점 이상 → "honors" / 80점 이상 → "pass" / 나머지 → "fail"
scores  = [98, 75, 82, 60, 91]
results = [
    "honors" if s >= 95 else "pass" if s >= 80 else "fail"
    for s in scores
]
print(f"성적 결과 리스트: {results}")
