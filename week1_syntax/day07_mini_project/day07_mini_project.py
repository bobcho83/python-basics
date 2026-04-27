# 오늘 배운 것: 1주차 복습 미니 프로젝트 — 스마트 계산기 / To-Do List / 마케팅 분석 / 업다운 게임

# 핵심 포인트
# try-except : 에러가 나도 프로그램이 멈추지 않는 '안전벨트'
# float()    : 소수점까지 담는 넉넉한 상자 (int보다 범용적)
# enumerate(): 리스트 순회 시 번호(인덱스)와 값을 동시에 제공
# random     : 매번 다른 숫자를 만들어내는 도구

# ===================================================
# 미니 프로젝트 1: 스마트 계산기 (예외 처리 포함)
# ===================================================
# 활용 문법: def / input / float / if-elif-else / try-except

def calculator():
    print("--- 밥(Bob)의 스마트 계산기 시작 ---")

    try:
        num1     = float(input("첫 번째 숫자를 입력하세요: "))
        num2     = float(input("두 번째 숫자를 입력하세요: "))
        operator = input("어떤 연산을 할까요? (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "오류: 0으로 나눌 수 없습니다."  # ZeroDivisionError 방지
            result = num1 / num2
        else:
            return "오류: 지원하지 않는 연산자입니다."

        return f"결과: {num1} {operator} {num2} = {result}"

    except ValueError:
        # 숫자가 아닌 문자 입력 시 처리
        return "오류: 숫자만 입력해주세요!"

print(calculator())

# ===================================================
# 미니 프로젝트 2: 스마트 할 일 관리 (To-Do List)
# ===================================================
# 활용 문법: list.append() / list.pop() / enumerate() / while

todo_list = []

while True:
    print(f"\n현재 할 일({len(todo_list)}개): {todo_list}")
    menu = input("1.추가  2.삭제  3.종료 → ")

    if menu == "1":
        job = input("할 일을 입력하세요: ")
        todo_list.append(job)

    elif menu == "2":
        for idx, item in enumerate(todo_list):  # 번호를 매겨 출력
            print(f"{idx}: {item}")
        delete_idx = int(input("삭제할 번호를 선택하세요: "))
        todo_list.pop(delete_idx)

    elif menu == "3":
        print("할 일 관리를 종료합니다.")
        break

# ===================================================
# 미니 프로젝트 3: 마케팅 성과 분석기 (Daily Report)
# ===================================================
# 활용 문법: sum() / len() / for 필터링 / max()

campaign_clicks  = [120, 340, 50, 210, 400]
high_performance = []

avg_clicks = sum(campaign_clicks) / len(campaign_clicks)

for click in campaign_clicks:
    if click > avg_clicks:
        high_performance.append(click)

print("--- 오늘의 마케팅 리포트 ---")
print(f"전체 평균 클릭 수: {avg_clicks}")
print(f"평균 돌파 캠페인 수: {len(high_performance)}개")
print(f"최고 기록: {max(campaign_clicks)}")

# ===================================================
# 미니 프로젝트 4: 숫자 맞히기 & 명예의 전당
# ===================================================
# 활용 문법: random.randint / while True / if-elif / list.sort()

import random

hall_of_fame = []  # 시도 횟수 기록 리스트

while True:
    target = random.randint(1, 100)  # 1~100 랜덤 숫자 생성
    count  = 0
    print("\n--- 새로운 게임 시작 (1~100) ---")

    while True:
        guess  = int(input("숫자를 맞춰보세요: "))
        count += 1

        if guess == target:
            print(f"정답! {count}번 만에 맞히셨네요.")
            hall_of_fame.append(count)
            break
        elif guess < target:
            print("UP!")
        else:
            print("DOWN!")

    hall_of_fame.sort()  # 시도 횟수 오름차순 정렬
    print(f"현재 1등 기록: {hall_of_fame[0]}회")

    retry = input("다시 하시겠습니까? (y/n): ")
    if retry.lower() != 'y':
        break
