# 오늘 배운 것: 생성자와 메서드 — 인스턴스/클래스 변수부터 @property 속성 관리까지

# 개념 정리
# __init__        : 객체 탄생 시 딱 한 번 자동 실행되는 '자동 시작 버튼'
# self            : "지금 만들어진 바로 그 객체"를 가리키는 손가락
# 인스턴스 변수    : 각 객체마다 개별로 갖는 값 (self.name)
# 클래스 변수     : 해당 클래스의 모든 객체가 공유하는 값 (ClassName.var)

# ===== 초급 =====
# 핵심: __init__ 생성자 / 인스턴스 변수 vs 클래스 변수 / self

class GameCharacter:
    game_name        = "파이썬 온라인"  # 클래스 변수 — 모든 캐릭터 공유
    total_characters = 0               # 클래스 변수 — 생성된 전체 수

    def __init__(self, nickname, job):
        self.nickname = nickname  # 인스턴스 변수 — 개별 닉네임
        self.job      = job       # 인스턴스 변수 — 개별 직업
        GameCharacter.total_characters += 1
        print(f"\n--- {self.nickname}님이 입장하셨습니다 ---")

    def show_info(self):
        print(f"게임: {GameCharacter.game_name}")       # 클래스 변수 접근
        print(f"닉네임: {self.nickname}")                # 인스턴스 변수 접근
        print(f"직업: {self.job}")
        print(f"현재 접속자 수: {GameCharacter.total_characters}")

user1 = GameCharacter("전사Bob",   "기사")
user1.show_info()

user2 = GameCharacter("마법사Karl", "위저드")
user2.show_info()

# ===== 중급 =====
# 핵심: 메서드 3총사 — 인스턴스 메서드 / @classmethod / @staticmethod

class Pizza:
    total_pizzas = 0  # 클래스 변수 — 전체 판매량

    def __init__(self, name, toppings):
        self.name     = name
        self.toppings = toppings
        Pizza.total_pizzas += 1

    # 인스턴스 메서드: self를 통해 개별 객체 데이터 접근
    def show_pizza(self):
        print(f"{self.name} 피자 (토핑: {', '.join(self.toppings)})")

    # 클래스 메서드: cls를 통해 클래스 변수(공유 데이터) 관리
    @classmethod
    def get_total_sales(cls):
        print(f"오늘 팔린 전체 피자 수: {cls.total_pizzas}판")

    # 정적 메서드: self/cls 없이 단순 계산 도구로 활용
    @staticmethod
    def calculate_price(size_inch):
        return size_inch * 1000  # 인치당 1,000원 가정

my_pizza   = Pizza("페퍼로니", ["치즈", "페퍼로니"])
your_pizza = Pizza("불고기",   ["불고기", "양파"])

my_pizza.show_pizza()           # 인스턴스 메서드 호출
Pizza.get_total_sales()         # 클래스 메서드 호출 (클래스 이름으로!)

price = Pizza.calculate_price(12)
print(f"12인치 피자 예상 가격: {price:,}원")

# ===== 고급 =====
# 핵심: @property(Getter) + @속성명.setter(Setter) + 정보 은닉(__)

class Member:
    def __init__(self, name, age):
        self.name  = name
        self.__age = age  # __ : 외부 직접 접근 차단 (정보 은닉)

    # Getter — ()없이 변수처럼 읽기 가능
    @property
    def age(self):
        return self.__age

    # Setter — 값 수정 시 유효성 검사 수행
    @age.setter
    def age(self, value):
        if value < 0:
            print("오류: 나이는 0보다 작을 수 없습니다!")
        else:
            self.__age = value
            print(f"나이가 {value}(으)로 변경되었습니다.")

m = Member("Bob", 25)

print(f"회원 이름: {m.name}, 나이: {m.age}")  # @property 덕분에 ()없이 호출

m.age = 30   # 정상 수정 → Setter 통과
m.age = -5   # 잘못된 값 → Setter가 차단
