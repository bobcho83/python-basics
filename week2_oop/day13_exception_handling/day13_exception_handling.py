# 오늘 배운 것: 예외 처리(Exception Handling) — try-except부터 사용자 정의 예외·traceback까지

# 개념 정리
# try     : "일단 해보고, 안 되면 넘어와!" — 오류가 날 것 같은 코드를 감쌈
# except  : "안전 매트" — 오류 발생 시 처리할 내용
# else    : 오류가 없을 때만 실행
# finally : "무슨 일이 있어도 이건 꼭!" — 오류 여부와 관계없이 마지막에 무조건 실행
# raise   : "이건 내가 정한 오류야!" — 개발자가 직접 예외를 발생시킴
#
# 대표 예외 종류
#   ValueError       : 타입은 맞지만 값이 부적절할 때
#   ZeroDivisionError: 숫자를 0으로 나누려 할 때
#   IndexError       : 리스트 범위를 벗어난 인덱스 접근
#   FileNotFoundError: 파일이 존재하지 않을 때

# ===== 초급 =====
# 핵심: try-except-else-finally / raise / 다중 except

def calculate_roi(profit, cost):
    if cost < 0:
        raise ValueError("광고비는 음수가 될 수 없습니다!")  # 직접 예외 발생
    return (profit / cost) * 100

try:
    print("--- 광고 수익률(ROI) 계산기 ---")
    p = int(input("이익을 입력하세요: "))
    c = int(input("광고비를 입력하세요: "))
    roi = calculate_roi(p, c)

except ValueError as e:
    print(f"❌ 값 오류: {e} (숫자를 정확히 입력해 주세요)")

except ZeroDivisionError:
    print("❌ 나누기 오류: 광고비가 0원이면 수익률을 계산할 수 없습니다.")

except Exception as e:
    print(f"❌ 예상치 못한 오류 발생: {e}")

else:
    # 오류가 없을 때만 실행
    print(f"✅ 계산 성공! 수익률은 {roi}% 입니다.")

finally:
    # 오류 여부와 관계없이 무조건 실행
    print("--- 계산기 프로그램을 종료합니다 ---")

# ===== 중급 =====
# 핵심: 사용자 정의 예외 클래스(Exception 상속) + 예외에 데이터 담기

# Exception을 상속해 나만의 예외 클래스 정의
class ForbiddenWordError(Exception):
    def __init__(self, word, message="사용 금지 단어가 포함되어 있습니다."):
        self.word    = word
        self.message = message
        super().__init__(self.message)  # 부모 Exception 초기화

def check_ad_text(text):
    forbidden_list = ["무조건", "100% 당첨", "도박"]
    for word in forbidden_list:
        if word in text:
            raise ForbiddenWordError(word)  # 직접 정의한 예외 발생
    print("✅ 광고 문구 검토 통과!")

ad_draft = "이번 이벤트는 100% 당첨 보장입니다!"

try:
    check_ad_text(ad_draft)
except ForbiddenWordError as e:
    print(f"❌ 광고 승인 거절: {e.message}")
    print(f"👉 문제가 된 단어: '{e.word}'")  # 예외 객체에 담긴 데이터 활용
finally:
    print("--- 광고 검토 프로세스 종료 ---")

# ===== 고급 =====
# 핵심: 예외 체이닝(raise ... from ...) + traceback 모듈로 상세 로그 추출

import traceback

class MarketingDataError(Exception):
    """마케팅 데이터 처리 중 발생하는 상위 에러"""
    pass

def process_raw_data(data):
    try:
        return int(data) * 1.1
    except ValueError as original_error:
        # raise ... from ... : 원인(ValueError)을 밝히며 새 예외 발생
        raise MarketingDataError("데이터 변환 중 치명적 오류 발생") from original_error

data_list = ["100", "200", "300원"]  # '300원'에서 에러 발생 예상

for item in data_list:
    try:
        result = process_raw_data(item)
        print(f"결과: {result:.1f}")
    except MarketingDataError as e:
        print(f"❌ 비즈니스 로직 에러: {e}")

        # traceback.format_exc(): 에러 발생 경로(파일·줄 번호·호출 스택)를 문자열로 반환
        print("\n--- [개발자용 상세 로그] ---")
        print(traceback.format_exc())
        # 필요 시 error_log.txt 파일에 저장 가능
