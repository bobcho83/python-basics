# 오늘 배운 것: 문자열 메서드 — 변신·검색·치환·분할부터 정규표현식까지

# 개념 정리
# 문자열 = '글자들의 기차' → 늘리고, 줄이고, 바꾸고, 쪼개는 메서드 도구 모음
# 변신 도구  : upper() / lower() / strip()
# 돋보기     : find() / count()
# 수정테이프 : replace()
# 가위와 풀  : split() / join()

# ===== 기초 개념 =====

text = " Python is Easy "
print(text.upper())       # 전부 대문자
print(text.lower())       # 전부 소문자
print(text.count("i"))    # 'i'가 몇 개?

# replace: 바꾸기
new_text = "I Love Java".replace("Java", "Python")
print(new_text)

# split: 콤마 기준으로 쪼개기 → 리스트로 반환
words = "사과,바나나,포도".split(",")
print(words)

# join: 리스트를 공백으로 합치기
joined = " ".join(["Hello", "World"])
print(joined)

# ===== 초급 =====

# 1. 지저분한 입력 정리 — strip()으로 공백 제거 + lower()로 소문자 통일
user_input = " BoB_mArKeTeR  "
clean_name = user_input.strip().lower()
print(f"정리된 이름: {clean_name}")

# 2. 개인정보 마스킹 — replace()로 뒷자리 별표 처리
phone = "010-1234-5678"
hidden_phone = phone.replace("5678", "****")
print(f"보안 처리: {hidden_phone}")

# 3. f-string 포맷팅
name  = "Bob"
level = 6
print(f"안녕하세요 {name}님! 벌써 {level}일차 공부 중이시네요!")

# 4. count()로 단어 등장 횟수 세기
sentence = "Apple is red, Apple is sweet, I like an Apple."
print(f"Apple은 {sentence.count('Apple')}번 나옵니다.")

# ===== 중급 =====
# 핵심: endswith / startswith + zfill + 슬라이싱 보폭 + f-string 숫자 포맷

# 1. 파일 확장자 확인 (endswith)
filename = "report_2026_data.pdf"
if filename.endswith(".pdf"):
    print("이 파일은 PDF 문서입니다.")

# 2. 자릿수 맞추기 — zfill(3): 1 → "001"
for i in range(1, 4):
    print(f"이미지 번호: {str(i).zfill(3)}")

# 3. 문자열 뒤집기 — [::-1] (보폭 -1 = 뒤에서부터 한 칸씩)
original      = "파이썬공부재밌다"
reversed_text = original[::-1]
print(f"거꾸로 하면? : {reversed_text}")

# 4. f-string 숫자 콤마 포맷 — {:,}
ad_cost = 1550000
print(f"총 광고 비용: {ad_cost:,}원")

# 5. 단어 개수 세기 — split() + len()
sentence2  = "python is simple python is powerful python is great"
word_count = len(sentence2.split())
print(f"문장의 총 단어 수: {word_count}")

# ===== 고급 =====
# 핵심: 정규표현식(re 모듈) + 유니코드 인코딩/디코딩

import re

# 원본 텍스트 (마케팅 뉴스레터 구독자 명단 가정)
raw_data = """
회원1: bob@google.com, 가입일: 2026-01-01
회원2: marketer_ai@naver.co.kr, 가입일: 2026-02-15
회원3: 잘못된아매알@test, 가입일: 2026-03-20
"""

# 이메일 패턴 정의
# [a-zA-Z0-9._%+-]+ : 영어·숫자·특수문자 아이디
# @[a-zA-Z0-9.-]+   : @ 뒤 도메인
# \.[a-zA-Z]{2,}    : .com / .kr 같은 확장자
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# re.findall() — 패턴에 맞는 모든 문자열 추출
emails = re.findall(email_pattern, raw_data)
print("--- 추출된 이메일 리스트 ---")
for email in emails:
    print(f"발견된 이메일: {email}")

# 유니코드 인코딩 — 문자 → 바이트, 바이트 → 문자
korean_text = "파이썬"
encoded     = korean_text.encode("utf-8")
print(f"\n'파이썬'의 UTF-8 바이트: {encoded}")
print(f"다시 사람의 언어로: {encoded.decode('utf-8')}")
