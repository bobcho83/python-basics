# 오늘 배운 것: 상속(Inheritance) — 단일 상속·다중 상속·MRO·추상 클래스까지

# 개념 정리
# 부모 클래스(Parent/Super) : 공통 기능을 담은 기본 클래스
# 자식 클래스(Child/Sub)    : 부모를 물려받아 기능을 추가·재정의한 클래스
# super()                   : 부모 클래스의 메서드를 호출하는 초인종
# 오버라이딩                 : 부모 메서드를 자식에게 맞게 재정의

# ===== 초급 =====
# 핵심: 단일 상속 / super() / 메서드 오버라이딩

# 부모 클래스
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model}이(가) 달립니다. 부릉부릉!")

# 자식 클래스 — 괄호 안에 부모 클래스 이름을 넣어 상속
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)   # 부모 생성자 호출 (brand, model 세팅)
        self.battery_size = battery_size # 자식만 가진 추가 속성

    # 오버라이딩: 부모의 drive()를 전기차 방식으로 재정의
    def drive(self):
        print(f"{self.brand} {self.model}이(가) 조용히 달립니다. 위이잉~")

    def charge(self):
        print(f"{self.battery_size}kWh 배터리를 충전 중입니다.")

my_car = Car("현대", "아반떼")
my_ev  = ElectricCar("테슬라", "Model 3", 75)

my_car.drive()   # 부모의 기능 실행
my_ev.drive()    # 자식이 재정의한 기능 실행
my_ev.charge()   # 자식만 가진 기능 실행

# ===== 중급 =====
# 핵심: 다중 상속 / MRO(Method Resolution Order)

# 부모 1: 이메일 발송 기능
class EmailSender:
    def send(self, message):
        print(f"📧 이메일 발송: {message}")

# 부모 2: SMS 발송 기능
class SMSSender:
    def send(self, message):
        print(f"📱 SMS 발송: {message}")

# 다중 상속 — 괄호 안에 두 클래스를 쉼표로 연결
# send() 충돌 시 앞에 적힌 EmailSender가 우선
class MarketingBot(EmailSender, SMSSender):
    def announce(self):
        print("--- 광고 캠페인 시작 ---")

bot = MarketingBot()
bot.announce()
bot.send("신제품 출시 이벤트!")  # EmailSender의 send() 호출

# MRO 확인: 파이썬이 메서드를 탐색하는 순서
print(f"\n탐색 순서(MRO): {[c.__name__ for c in MarketingBot.mro()]}")

# ===== 고급 =====
# 핵심: 추상 클래스(ABC) / @abstractmethod — 자식에게 구현을 강제하는 설계도

from abc import ABC, abstractmethod

# 추상 클래스 — ABC를 상속받아야 함 / 직접 객체 생성 불가
class AdPlatform(ABC):
    def __init__(self, name):
        self.name = name

    # 추상 메서드: 자식이 반드시 오버라이딩해야 함 (안 하면 TypeError)
    @abstractmethod
    def post_ad(self, content):
        pass

    # 일반 메서드: 공통 기능으로 자식에게 그대로 물려줌
    def welcome(self):
        print(f"[{self.name}] 광고 플랫폼에 오신 것을 환영합니다.")

# 자식 클래스 1: 구글 광고 — post_ad() 구현 (필수!)
class GoogleAd(AdPlatform):
    def post_ad(self, content):
        print(f"🌏 Google 검색 결과에 광고 노출: {content}")

# 자식 클래스 2: 페이스북 광고 — post_ad() 구현 (필수!)
class FacebookAd(AdPlatform):
    def post_ad(self, content):
        print(f"🧍 Facebook 타임라인에 광고 노출: {content}")

platforms = [GoogleAd("구글"), FacebookAd("페이스북")]

for p in platforms:
    p.welcome()
    p.post_ad("신학기 맞이 파이썬 강의 할인!")
    print("-" * 30)

# 추상 클래스 직접 생성 시 TypeError 발생
# test = AdPlatform("에러발생")  # ← 주석 해제 시 에러 확인 가능
