# Python Basics 학습 저장소

깃허브 1일 1커밋을 목표로 Python 기초부터 AI 활용까지 단계적으로 학습합니다.

---

## 📅 학습 진행 현황

### 1주차 — Python 핵심 문법 (`week1_syntax/`)

| 날짜 | 파일 | 주제 |
|------|------|------|
| Day 01 | `day01_variables/day01_variables.py` | 변수와 자료형 — int, str, list, dict |
| Day 02 | `day02_conditionals/day02_conditionals.py` | 조건문 — if / elif / else |
| Day 03 | `day03_loops/day03_loops.py` | 반복문 — for / while |
| Day 04 | `day04_data_structures/day04_data_structures.py` | 리스트와 딕셔너리 심화 |
| Day 05 | `day05_functions/day05_functions.py` | 함수 — def / lambda / 데코레이터 |
| Day 06 | `day06_string_methods/day06_string_methods.py` | 문자열 메서드 — 변환·검색·정규표현식 |
| Day 07 | `day07_mini_project/day07_mini_project.py` | 1주차 미니 프로젝트 — 계산기·To-Do·분석기·게임 |

#### Day 01 요약
- **초급**: 숫자·문자 변수 선언, 리스트 인덱싱, 딕셔너리 키-값 접근
- **중급**: 리스트 컴프리헨션으로 데이터 필터링, `.get()`으로 안전한 딕셔너리 접근, 딕셔너리 컴프리헨션으로 CPC 보고서 생성
- **고급**: `**` 언팩킹으로 딕셔너리 병합, `*` 언팩킹으로 리스트 분리, 제너레이터 표현식으로 메모리 효율적 데이터 처리

#### Day 02 요약
- **초급**: `if / elif / else` 기본 구조, 콜론·들여쓰기 규칙 — 놀이공원 입장료 판별기
- **중급**: `and / or / not` 논리 연산자, 중첩 조건문, 조건부 표현식(Ternary) — 스마트 로그인 시스템
- **고급**: `match-case` 패턴 매칭(Python 3.10+), 딕셔너리 매핑으로 if-elif 대체, `all() / any()` 다중 조건 검사, 단축 평가(Short-circuit)로 안전한 코드, 컴프리헨션 안의 다중 조건 분류

#### Day 03 요약
- **초급**: `for` + `range()` 기본 순회, 리스트 순회, `while` 조건 반복 — 구구단·출석부·숫자 세기
- **중급**: 이중 `for`문으로 구구단 전체 출력, `continue`로 짝수단만 필터링, `enumerate()`로 인덱스+값 동시 순회
- **고급**: 리스트 컴프리헨션으로 한 줄 압축, `zip()`으로 두 리스트 병렬 순회, 제너레이터 표현식으로 대용량 데이터 메모리 절약

#### Day 04 요약
- **초급**: 리스트 `append / insert / pop / 슬라이싱`, 딕셔너리 `keys() / values() / items()` — 간식 기차·사물함 실습
- **중급**: 리스트 안의 딕셔너리 복합 구조, 컴프리헨션으로 조건 필터링, `.get()`으로 안전 접근, `update()`로 일괄 수정, 딕셔너리 컴프리헨션으로 성적표 생성
- **고급**: 얕은 복사(`.copy()`)의 함정, `copy.deepcopy()`로 완전 분리, 딕셔너리 키-값 반전 컴프리헨션 / 실습: 전화번호부 검색 프로그램, `numpy`로 리스트 평균 계산

#### Day 05 요약
- **초급**: `def` 함수 정의·호출, 기본값 매개변수, 다중 반환값 언팩킹 — 주스 기계·사각형 정보·합격 판정
- **중급**: `*args`로 가변 인자 수집, `**kwargs`로 키워드 인자 딕셔너리 수집, `lambda`로 한 줄 익명 함수 + 정렬 키 활용
- **고급**: 데코레이터(`@`) — 함수를 수정하지 않고 앞뒤에 기능 장식, `wrapper` 패턴으로 로그 출력 / 실습: 곱하기·성적 판정·리스트 역순 함수 3개

#### Day 06 요약
- **초급**: `upper() / lower() / strip()` 변신 도구, `count()` 등장 횟수, `replace()`로 마스킹, `split() / join()` 가위·풀, f-string 포맷팅
- **중급**: `endswith()`로 파일 확장자 확인, `zfill()`로 자릿수 맞추기, `[::-1]` 보폭 슬라이싱으로 문자열 뒤집기, `{:,}` 천단위 콤마 포맷, `split() + len()`으로 단어 수 세기
- **고급**: `re` 모듈 정규표현식으로 이메일 패턴 추출(`findall`), UTF-8 인코딩(`encode`) / 디코딩(`decode`)으로 글자↔바이트 변환 원리 이해

#### Day 07 요약 (1주차 미니 프로젝트 🎉)
- **프로젝트 1 — 스마트 계산기**: `try-except`로 잘못된 입력·0 나누기 에러 방지, `float()`으로 소수점 연산 지원, `if-elif-else`로 연산자 분기
- **프로젝트 2 — To-Do List**: `append()`로 항목 추가, `pop()`으로 항목 삭제, `enumerate()`로 번호 매겨 출력, `while` 루프로 메뉴 반복
- **프로젝트 3 — 마케팅 성과 분석기**: `sum() / len()`으로 평균 계산, `for` 필터링으로 평균 초과 캠페인 추출, `max()`로 최고 기록 출력
- **프로젝트 4 — 업다운 게임 & 명예의 전당**: `random.randint()`로 랜덤 숫자 생성, 중첩 `while`로 게임 루프, `sort()`로 시도 횟수 랭킹 정렬

---

### 2주차 — 객체지향 프로그래밍 (`week2_oop/`)

| 날짜 | 파일 | 주제 |
|------|------|------|
| Day 08 | `Day08_class_basics/Day08_class_basics.py` | 클래스와 객체 — 생성자·상속·추상 클래스 |
| Day 09 | `day09_constructor_methods/day09_constructor_methods.py` | 생성자와 메서드 — 인스턴스/클래스 변수·@property |
| Day 10 | `day10_inheritance/day10_inheritance.py` | 상속 — 단일·다중 상속·MRO·추상 클래스 |
| Day 11 | `day11_polymorphism_encapsulation/day11_polymorphism_encapsulation.py` | 다형성과 캡슐화 — 오버라이딩·접근제어·덕 타이핑 |
| Day 12 | `day12_file_io/day12_file_io.py` | 파일 입출력 — TXT·JSON·CSV 읽기·쓰기 |
| Day 13 | `day13_exception_handling/day13_exception_handling.py` | 예외 처리 — try-except·사용자 정의 예외·traceback |
| Day 14 | `day14_mini_project/day14_mini_project.py` | 2주차 미니 프로젝트 — 스마트 은행 시스템 |

#### Day 08 요약
- **초급**: `class` 정의, `__init__` 생성자, `self` 키워드, 메서드 호출 — 스마트폰 설계도로 객체 2개 생성
- **중급**: 상속(`super()`로 부모 생성자 호출), 메서드 오버라이딩으로 자식 클래스 재정의, `__`(더블 언더바)로 비공개 속성 보호 — 마케팅 캠페인 클래스
- **고급**: `ABC / @abstractmethod`로 추상 클래스 강제 설계, `@classmethod`로 클래스 변수 관리, `__str__` 매직 메서드로 출력 형태 정의 / 실습: 학생 클래스·은행 계좌 클래스

#### Day 09 요약
- **초급**: `__init__` 생성자로 초기 상태 설정, 인스턴스 변수(`self.name`)와 클래스 변수(`ClassName.var`) 차이 이해 — 게임 캐릭터 생성기
- **중급**: 인스턴스 메서드(`self`) / `@classmethod`(`cls`) / `@staticmethod` 3총사 역할 구분 — 피자 클래스로 판매량 관리·가격 계산
- **고급**: `@property`(Getter)로 변수처럼 값 읽기, `@속성명.setter`(Setter)로 유효성 검사, `__`(정보 은닉)으로 외부 직접 수정 차단 — 회원 나이 검증 시스템

#### Day 10 요약
- **초급**: 단일 상속 구조(부모→자식), `super().__init__()`으로 부모 생성자 호출, 메서드 오버라이딩으로 자식 클래스 재정의 — 자동차·전기차 관계
- **중급**: 다중 상속(두 부모를 쉼표로 연결), 메서드 충돌 시 `MRO` 우선순위 규칙, `클래스명.mro()`로 탐색 순서 확인 — 마케팅봇(이메일·SMS 동시 상속)
- **고급**: `ABC / @abstractmethod`로 자식에게 구현 강제, 추상 클래스 직접 객체 생성 불가, 일반 메서드는 공통 기능으로 그대로 물려줌 — 광고 플랫폼 설계도

#### Day 11 요약
- **초급**: 다형성 — 같은 `run()` 메서드명으로 VideoAd·BannerAd가 각자 다르게 동작, `__cost` Private 속성 + `@property` Getter/Setter로 광고비 보호
- **중급**: 덕 타이핑 — 상속 없이 메서드 이름만 같으면 동일하게 취급(KakaoTalk·Line), `@property` 계산된 가상 속성으로 잔여 예산·상태를 변수처럼 읽기
- **접근 제어 3단계**: `name`(Public) / `_name`(Protected) / `__name`(Private) 레벨 이해

#### Day 12 요약
- **초급**: `open()` 모드(`r/w/a`) 이해, `with` 문으로 자동 파일 닫기, `readlines()`로 줄 단위 읽기 — 업무 일지 TXT 파일 시스템
- **중급**: `json.dump()`로 딕셔너리→파일 저장, `json.load()`로 파일→딕셔너리 복원, `ensure_ascii=False`(한글 보존)·`indent=4`(가독성) 옵션 — 캠페인 설정 JSON 저장
- **고급**: `csv.writer/reader`로 표 형식 데이터 읽기·쓰기, `utf-8-sig`로 엑셀 한글 깨짐 방지, `try-except`로 `FileNotFoundError` 안전 처리 — 마케팅 성과 CSV 분석

#### Day 13 요약
- **초급**: `try-except-else-finally` 구조 이해, `raise`로 직접 예외 발생, 다중 `except`로 상황별 대처 — 광고 수익률(ROI) 계산기
- **중급**: `Exception` 상속으로 사용자 정의 예외 클래스(`ForbiddenWordError`) 생성, 예외 객체에 데이터(`word`, `message`) 담아 구체적 안내 — 광고 문구 검토 시스템
- **고급**: `raise ... from ...` 예외 체이닝으로 원인 오류 보존(`MarketingDataError`), `traceback.format_exc()`로 파일·줄 번호·호출 스택 문자열 추출 — 마케팅 데이터 처리 로그

#### Day 14 요약 (2주차 미니 프로젝트 🎉)
- **프로젝트 — 스마트 은행 시스템**: 클래스·상속·캡슐화·파일 입출력·예외 처리를 하나로 결합한 종합 실습
- **초급**: `BankError` → `InsufficientFundsError` 커스텀 예외 계층 정의, `BankAccount` 부모 클래스에 `__balance`(Private) + `@property` Getter 적용
- **중급**: `SavingsAccount`(이자 자동 입금) / `CheckingAccount`(출금 수수료) 자식 클래스로 상속·다형성 구현, `withdraw()` 오버라이딩 + `super()` 활용
- **고급**: 거래 발생 시마다 `bank_log.txt`에 타임스탬프 포함 로그 기록(파일 입출력), `InsufficientFundsError` 정확히 캐치하는 예외 처리로 안전한 시스템 완성

---

### 3주차 — 데이터 분석 (`week3_pandas/`)

| 날짜 | 파일 | 주제 |
|------|------|------|
| Day 15 | `day15_pandas_series/day15_pandas_series.py` | Pandas 기초 — Series·DataFrame·필터링·정렬 |
| Day 16 | `day16_dataframe_basics/day16_dataframe_basics.py` | DataFrame 심화 — 필터링·정렬·병합·그룹화 |
| Day 17 | `day17_data_cleaning/day17_data_cleaning.py` | 데이터 정제 — 결측치·중복·타입변환·apply·피벗 테이블 |
| Day 18 | `day18_filtering_sorting/day18_filtering_sorting.py` | 필터링과 정렬 — isin·groupby·시계열·query·피벗 테이블 |
| Day 19 | `day19_groupby_aggregate/day19_groupby_aggregate.py` | 그룹화와 집계 — groupby·agg·filter·다중 그룹화 |
| Day 20 | `day20_visualization/day20_visualization.py` | 데이터 시각화 — Matplotlib 선·막대·산점도·서브플롯·이중 축 |

#### Day 15 요약
- **초급**: `pd.Series(data, index=...)` 생성, 라벨 인덱싱, `sum()·mean()·max()·min()` 통계 메서드, Boolean 조건 필터링 — 주간 광고 클릭 수 분석
- **중급**: 딕셔너리로 `pd.DataFrame` 생성, `df["열"]`로 열 선택, 파생 변수(`CTR(%)`) 계산·추가, `head()`·`describe()`로 데이터 탐색 — 마케팅 채널 성과 표
- **고급**: Boolean Indexing으로 조건 행 추출, `sort_values(by=..., ascending=False)` 내림차순 정렬, `.loc[행, 열]` 라벨 기반 선택, `&` 다중 조건으로 가성비 채널 필터링

#### Day 16 요약
- **초급**: 딕셔너리로 `pd.DataFrame` 생성, `df.shape`으로 크기 확인, `df["열"]` 열 선택, `df.loc[라벨]`·`df.iloc[번호]` 행 접근, `df.loc[행, 열]` 동시 접근 — 마케팅 캠페인 표
- **중급**: 파생 변수(`클릭당_비용`) 계산·추가, 단일 조건·`&` 다중 조건 Boolean Indexing, `sort_values(ascending=True)` 오름차순 정렬 — 가성비 캠페인 필터링
- **고급**: `pd.merge(df1, df2, on="공통열")`로 두 표 병합(VLOOKUP과 동일), `groupby("열")["집계열"].sum()`으로 그룹 합계, `.agg(["sum","mean","count"])`로 복합 통계 — 지역별 클릭 성과 분석

#### Day 17 요약
- **초급**: `str.strip()`으로 공백 제거, `drop_duplicates()`로 중복 행 삭제, `fillna(mean())`으로 결측치 평균 대체, `replace()`+`astype(int)`로 타입 변환, 조건 필터링으로 이상값 제거 — 고객 데이터 정제
- **중급**: `apply(함수)`로 구매금액 → 고객 등급(VIP·GOLD·SILVER) 분류, `map(딕셔너리)`로 지역코드 → 지역명 1:1 치환, `np.where(조건, 참, 거짓)`으로 마케팅 대상 조건부 치환
- **고급**: `pd.to_datetime()`으로 문자열 날짜 → 시간 객체 변환 + `dt.day_name()`으로 요일 추출, `pivot_table()`로 채널×요일 매출 리포트, `resample("ME")`으로 월별 성과 합산

#### Day 20 요약
- **초급**: `plt.plot()` 선 그래프(추이), `plt.bar()` 막대 그래프(비교), `plt.scatter()` 산점도(상관관계), `plt.hist()` 히스토그램(분포) — 4가지 기본 그래프 + `marker·color·grid` 스타일 옵션
- **중급**: `plt.subplots(1, 2)` 화면 분할 후 `axes[0]·axes[1]`에 개별 그래프 배치, `legend()`로 범례 추가, `tight_layout()`으로 글자 겹침 방지 — 구글 vs 페이스북 채널 비교 대시보드
- **고급**: `ax.twinx()`로 x축 공유·y축 이중 분리(왼쪽: 비용 막대 / 오른쪽: CTR 선), `plt.savefig('파일.png', dpi=300, bbox_inches='tight')`로 고화질 이미지 저장 — 광고비 vs CTR 혼합 리포트

#### Day 19 요약
- **초급**: `groupby('열')` 그룹 객체 생성, `for name, group in grouped` 반복 확인, `.sum()·.mean()·.count()` 단일 집계, `agg(['sum','mean','count'])` 리스트로 한 번에 집계 — 제품별 매출 분석
- **중급**: `agg({'열':['sum','mean'], '열2':'count'})` 딕셔너리로 컬럼별 다른 함수 적용, `agg(total='sum', average='mean')` 결과 열 이름 커스터마이징, `filter(lambda x: x.sum() >= 150)` 그룹 단위 조건 필터링, `isin()` 조합으로 고성과 제품 전체 데이터 추출
- **고급**: `groupby(['지역','product'])` 2단계·`groupby(['연도','월','product'])` 3단계 다중 레벨 집계, 마케팅 캠페인 실전 분석 — `conversions/clicks`으로 전환율(CVR) 파생 변수 생성 후 캠페인별 평균 전환율 비교

#### Day 18 요약
- **초급**: 단일·다중 조건 Boolean Indexing, `sort_values(ascending=False)` 내림차순, `df.loc[0:2, ['열1','열2']]` 행·열 동시 선택, `isin(['Google','Instagram'])` 리스트 일괄 필터링 — 캠페인 성과 조회
- **중급**: `클릭수/노출수×100`으로 CTR 파생 변수 생성, `groupby().agg({'열':'sum','열':'mean'})`로 채널별 복합 집계, `sort_values`로 가성비 순위 도출, `map(딕셔너리)`로 채널명 한글 치환
- **고급**: `pd.to_datetime()` + `dt.month` / `dt.day_name()`으로 월·요일 추출, `np.where()` 이중 조건 효율 등급 부여, `df.query("월 == 5 and 클릭수 >= 1000")` SQL 스타일 복합 필터, `pivot_table()`로 월별×채널별 지출 요약
