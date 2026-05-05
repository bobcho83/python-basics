# 오늘 배운 것: 다형성(Polymorphism)과 캡슐화(Encapsulation)

# 개념 정리
# 다형성(Polymorphism) : "이름은 같은데 행동은 다르다!" — 같은 메서드명, 다른 결과
# 캡슐화(Encapsulation): 중요한 데이터를 클래스 안에 잠가 보호하는 것
# 접근 제어 레벨
#   Public    (공개) : name       — 누구나 접근 가능
#   Protected (보호) : _name      — 자식 클래스까지만 사용 권장
#   Private   (비밀) : __name     — 클래스 내부에서만 접근 가능
# Getter/Setter      : 잠긴 데이터를 안전하게 읽고 수정하는 통로 (@property)

# ===== 초급 =====
# 핵심: 다형성(오버라이딩) + 캡슐화(Private 속성) + @property Getter/Setter

# 부모 클래스
class Ad:
    def __init__(self, title):
        self.title   = title
        self.__cost  = 0      # Private — 외부 직접 접근 차단

    # Getter: ()없이 변수처럼 읽기
    @property
    def cost(self):
        return self.__cost

    # Setter: 유효성 검사 후 수정
    @cost.setter
    def cost(self, value):
        if value < 0:
            print("오류: 광고비는 0보다 작을 수 없습니다.")
        else:
            self.__cost = value

    def run(self):
        print("광고를 송출합니다.")

# 다형성 구현 — 같은 run() 이름, 자식마다 다른 행동
class VideoAd(Ad):
    def run(self):
        print(f"🎥 영상 광고 '{self.title}'를 유튜브에 재생합니다.")

class BannerAd(Ad):
    def run(self):
        print(f"🖼️  배너 광고 '{self.title}'를 네이버에 노출합니다.")

# 다형성 실행 — 같은 for 루프에서 각자 다르게 동작
ads = [VideoAd("AI 강의"), BannerAd("파이썬 챌린지")]
for a in ads:
    a.run()  # ← 이것이 다형성!

# 캡슐화 확인
my_ad       = Ad("기초 마케팅")
my_ad.cost  = 5000   # Setter 통해 수정
print(f"현재 광고비: {my_ad.cost}")  # Getter 통해 읽기

# ===== 중급 =====
# 핵심: 덕 타이핑(Duck Typing) + @property 계산된 속성(가상 속성)

# 1. 덕 타이핑 — 상속 관계 없이 메서드 이름만 같으면 동일하게 취급
class KakaoTalk:
    def send(self, msg):
        print(f"💬 카카오톡 발송: {msg}")

class Line:
    def send(self, msg):
        print(f"📗 라인 발송: {msg}")

# send() 메서드만 있으면 어떤 클래스든 OK — 상속 불필요!
def send_notification(service, message):
    service.send(message)

print("--- 다형성(덕 타이핑) 테스트 ---")
send_notification(KakaoTalk(), "오늘의 뉴스레터 도착!")
send_notification(Line(),      "오늘의 뉴스레터 도착!")

# 2. 고급 캡슐화 — @property로 계산된 가상 속성 만들기
class Campaign:
    def __init__(self, name, budget, spent):
        self.name       = name
        self.__budget   = budget  # Private
        self.__spent    = spent   # Private

    # 계산된 속성 — 변수처럼 호출하지만 내부적으로 계산 수행
    @property
    def remaining_budget(self):
        return self.__budget - self.__spent

    @property
    def status(self):
        return "진행 중" if self.remaining_budget > 0 else "예산 소진"

print("\n--- 고급 캡슐화(계산된 속성) 테스트 ---")
cp = Campaign("여름 세일", 1_000_000, 450_000)
print(f"캠페인: {cp.name} | 상태: {cp.status}")
print(f"남은 예산: {cp.remaining_budget:,}원")
