# 오늘 배운 것: 2주차 종합 미니 프로젝트 — 스마트 은행 시스템
# 클래스·상속·다형성·캡슐화·파일 입출력·예외 처리를 하나로 결합

# 개념 정리
# 이번 프로젝트의 핵심 — 각 개념이 서로 어떻게 '협력'하는지 이해하기
# 1. 커스텀 예외  : 우리 은행만의 규칙 위반 시 발생할 에러를 직접 정의
# 2. 클래스 구조  : 부모(BankAccount) — 공통 기능 보유
#                  자식(SavingsAccount) — 이자율 개념 추가
#                  자식(CheckingAccount) — 수수료 개념 추가 (설계 포함)
# 3. 캡슐화       : __balance(Private) + @property로 안전한 잔액 관리
# 4. 파일 입출력  : 거래 발생 시마다 bank_log.txt에 기록 → 데이터 영속성

import datetime

# ===== 초급 =====
# 핵심: 커스텀 예외 정의 + 부모 클래스(BankAccount) 기본 구조

# 1. 커스텀 예외 클래스 (예외 처리)
class BankError(Exception):
    """은행 관련 최상위 커스텀 에러"""
    pass

class InsufficientFundsError(BankError):
    """잔액 부족 에러 — BankError 상속"""
    pass

# 2. 부모 클래스 — 캡슐화 적용
class BankAccount:
    def __init__(self, account_num, owner, balance=0):
        self.account_num = account_num
        self.owner       = owner
        self.__balance   = balance   # Private — 외부 직접 접근 차단

    # Getter — 변수처럼 잔액 읽기
    @property
    def balance(self):
        return self.__balance

    # Protected 메서드 — 자식 클래스까지만 사용
    def _log_transaction(self, msg):
        # 3. 파일 입출력 — 거래 내역을 bank_log.txt에 추가 기록
        with open("bank_log.txt", "a", encoding="utf-8") as f:
            now = datetime.datetime.now()   # () 필수 — 함수 호출로 현재 시각 획득
            f.write(f"[{now}] {self.owner}({self.account_num}): {msg}\n")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 합니다.")
        self.__balance += amount
        self._log_transaction(f"{amount}원 입금 (잔액: {self.__balance}원)")
        print(f"✅ {amount}원 입금 완료")

    def withdraw(self, amount):
        if amount > self.__balance:
            # 커스텀 예외 발생 — 잔액 부족 상황
            raise InsufficientFundsError(f"잔액 부족 (현재: {self.__balance}원)")
        self.__balance -= amount
        self._log_transaction(f"{amount}원 출금 (잔액: {self.__balance}원)")
        print(f"✅ {amount}원 출금 완료")

# ===== 중급 =====
# 핵심: 자식 클래스(상속 + 다형성) — SavingsAccount / CheckingAccount

# 4. 자식 클래스 — 이자율이 있는 정기적금
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        """이자 계산 후 잔액에 자동 입금"""
        interest = self.balance * rate
        self.deposit(interest)          # 부모의 deposit() 그대로 활용
        print(f"💰 이자 {interest:,.1f}원이 추가되었습니다.")

# 자식 클래스 — 출금 수수료가 있는 입출금 계좌
class CheckingAccount(BankAccount):
    def __init__(self, account_num, owner, balance=0, fee=500):
        super().__init__(account_num, owner, balance)
        self.fee = fee   # 출금 수수료

    def withdraw(self, amount):
        """수수료 포함한 금액으로 출금 — 부모 withdraw 오버라이딩"""
        total = amount + self.fee
        print(f"ℹ️  수수료 {self.fee}원 포함, 총 {total}원이 출금됩니다.")
        super().withdraw(total)   # 부모의 withdraw로 실제 처리

# ===== 고급 =====
# 핵심: 전체 흐름 통합 실행 — 예외 처리 + 파일 로그 확인

# 5. 실행 및 테스트
print("===== 스마트 은행 시스템 =====")

try:
    # SavingsAccount — 초기 잔액 10,000원
    bob_acc = SavingsAccount("123-456", "Bob", 10000)
    bob_acc.deposit(5000)          # 15,000원
    bob_acc.withdraw(3000)         # 12,000원
    bob_acc.add_interest(0.2)      # 이자 20% → 2,400원 추가 → 14,400원

    # CheckingAccount — 수수료 테스트
    print()
    alice_acc = CheckingAccount("789-012", "Alice", 20000, fee=300)
    alice_acc.withdraw(5000)       # 수수료 300원 포함 → 5,300원 출금

    # 예외 발생 테스트 — 잔액 부족
    print()
    bob_acc.withdraw(50000)        # InsufficientFundsError 발생 예상

except InsufficientFundsError as e:
    # 커스텀 예외를 정확히 잡아서 사용자 친화적 메시지 출력
    print(f"❌ 은행 오류: {e}")
except ValueError as e:
    print(f"❌ 입력 오류: {e}")
except Exception as e:
    print(f"❌ 알 수 없는 오류: {e}")
finally:
    print("\n--- 거래를 종료합니다. 로그 파일(bank_log.txt)을 확인하세요. ---")

# 6. 저장된 로그 파일 출력
print("\n[bank_log.txt 거래 내역]")
try:
    with open("bank_log.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("(로그 파일 없음 — 거래가 기록되지 않았습니다.)")
