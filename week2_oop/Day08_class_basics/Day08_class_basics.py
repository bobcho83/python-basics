# 오늘 배운 것: 클래스와 객체 — 초급 설계도부터 고급 추상 클래스·매직 메서드까지

# 개념 정리
# 클래스(Class)   : 붕어빵을 찍어내는 '틀' (설계도)
# 객체(Object)    : 틀에서 구워진 실제 '붕어빵' (인스턴스)
# 속성(Attribute) : 붕어빵 안의 '팥·슈크림' 같은 특징
# 메서드(Method)  : 붕어빵이 하는 '행동' (함수)
# self            : "이 객체 자신"을 가리키는 키워드

# ===== 초급 =====
# 핵심: class 정의 / __init__ 생성자 / self / 메서드 호출

class SmartPhone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on  = False  # 기본값: 꺼짐

    def power_on(self):
        self.is_on = True
        print(f"[{self.model}] 전원이 켜졌습니다. 📱")

    def show_info(self):
        status = "켜짐" if self.is_on else "꺼짐"
        print(f"기기 정보: {self.brand} {self.model} (상태: {status})")

# 객체 생성 — 클래스 이름 뒤에 ()를 붙임
my_phone  = SmartPhone("애플",  "iPhone 15 Pro")
bob_phone = SmartPhone("삼성", "Galaxy S26")

my_phone.power_on()
my_phone.show_info()
bob_phone.show_info()

# ===== 중급 =====
# 핵심: 상속(Inheritance) / 메서드 오버라이딩 / 비공개 속성(__)

# 부모 클래스
class Campaign:
    def __init__(self, name, budget):
        self.name    = name
        self.__budget = budget  # __ : 외부 접근 차단 (비공개 속성)

    def get_budget(self):       # 비공개 속성은 메서드로만 접근
        return self.__budget

    def show_report(self):
        print(f"[{self.name}] 캠페인 진행 중. 예산: {self.__budget}원")

# 자식 클래스 — Campaign 을 상속
class SNSCampaign(Campaign):
    def __init__(self, name, budget, platform):
        super().__init__(name, budget)  # 부모 생성자 호출
        self.platform = platform

    # 메서드 오버라이딩: 부모의 show_report를 SNS 전용으로 재정의
    def show_report(self):
        print(f"[{self.platform} 전용] {self.name} 리포트")
        print(f"남은 예산: {self.get_budget()}원")

general_ad = Campaign("기본 광고", 1_000_000)
insta_ad   = SNSCampaign("신제품 홍보", 500_000, "Instagram")

print("--- 일반 광고 리포트 ---")
general_ad.show_report()

print("\n--- SNS 광고 리포트 ---")
insta_ad.show_report()

# 아래 코드는 AttributeError 발생 (비공개 속성 보호)
# print(insta_ad.__budget)

# ===== 고급 =====
# 핵심: 추상 클래스(ABC) / @classmethod / @staticmethod / 매직 메서드(__str__)

from abc import ABC, abstractmethod

# 추상 클래스 — 상속받는 자식은 반드시 open_store()를 구현해야 함
class Shop(ABC):
    @abstractmethod
    def open_store(self):
        pass

class StarBread(Shop):
    total_sales = 0  # 클래스 변수: 모든 객체가 공유

    def __init__(self, location):
        self.location = location

    # 추상 메서드 구현 (필수!)
    def open_store(self):
        print(f"{self.location}점이 문을 열었습니다! 🍞")

    # @classmethod: 클래스 변수(전체 매출)를 다루는 메서드
    @classmethod
    def add_sales(cls, amount):
        cls.total_sales += amount
        print(f"전체 누적 매출: {cls.total_sales:,}원")

    # 매직 메서드: print(객체) 시 출력 형태 정의
    def __str__(self):
        return f"이곳은 스타브레드 {self.location}점입니다."

gangnam = StarBread("강남")
hongdae = StarBread("홍대")

gangnam.open_store()
print(gangnam)              # __str__ 덕분에 예쁘게 출력

StarBread.add_sales(50_000)
StarBread.add_sales(30_000)

# ===== 실습 =====

# 실습 1: 학생 클래스 (__init__ 방식)
class Student:
    def __init__(self, name, student_id, score):
        self.name       = name
        self.student_id = student_id
        self.score      = score

    def info(self):
        print(f"이름: {self.name}, 학번: {self.student_id}, 점수: {self.score}")

student1 = Student("철수", "2024001", 85)
student1.info()

# 실습 2: 은행 계좌 클래스 (입금·출금 메서드)
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance        = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"입금 완료. 잔액: {self.balance:,}원")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount:,}원 인출 완료. 잔액: {self.balance:,}원")
        else:
            print("잔액이 부족합니다!")

account = BankAccount("123-456-789", 10_000)
account.deposit(5_000)
account.withdraw(3_000)
