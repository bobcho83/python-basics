# 오늘 배운 것: 리스트(List)와 딕셔너리(Dictionary) — 초급 기본 조작부터 고급 복사 원리까지

# 개념 정리
# 리스트     : 순서대로 담는 '기차' — 몇 번째 칸인지(인덱스)가 중요
# 딕셔너리   : 이름표 붙은 '사물함' — 번호 대신 키(이름표)로 값을 찾음

# ===== 초급 =====
# 리스트 주요 메서드: append / insert / pop / remove / 슬라이싱
# 딕셔너리 주요 메서드: keys() / values() / items()

# 간식 기차 만들기 (리스트)
snacks = ["초코파이", "사탕", "젤리"]
snacks.append("과자")        # 맨 뒤에 추가
snacks.insert(1, "초콜릿")   # 1번 자리에 끼워 넣기
snacks.pop()                 # 마지막 '과자' 삭제

print("--- 우리 반 간식 기차 ---")
print(f"전체 간식: {snacks}")
print(f"앞에서 2개만 슬라이싱: {snacks[0:2]}")  # 끝 번호는 포함 안 됨!

# 친구들의 최애 간식 사물함 (딕셔너리)
favorite_snacks = {
    "철수": "사탕",
    "영희": "초콜릿",
    "Bob": "엿"
}

print("\n--- 최애 간식 사물함 ---")
favorite_snacks["민수"] = "쿠키"  # 새 친구 추가

print(f"이름표 목록: {list(favorite_snacks.keys())}")
print(f"간식 목록:   {list(favorite_snacks.values())}")

for name, snack in favorite_snacks.items():
    print(f"{name} 친구는 {snack}을/를 좋아해요!")

# ===== 중급 =====
# 핵심: 리스트 안의 딕셔너리(복합 구조) + 컴프리헨션 + .get() / update()

# 복합 데이터 구조 — 기차 칸마다 보물 상자(딕셔너리)가 실린 구조
students = [
    {"name": "철수", "score": 85, "grade": "B"},
    {"name": "영희", "score": 95, "grade": "A"},
    {"name": "민수", "score": 70, "grade": "C"},
    {"name": "Bob",  "score": 100, "grade": "A+"}
]

# 리스트 컴프리헨션: 90점 이상 학생 이름만 뽑기
honor_students = [s["name"] for s in students if s["score"] >= 90]
print(f"\n우수 학생 명단: {honor_students}")

# update()로 딕셔너리 데이터 수정
students[1].update({"score": 98, "grade": "A+"})

# .get(key, 기본값): 키가 없어도 에러 대신 기본값 반환
for s in students:
    comment = s.get("comment", "내용 없음")
    print(f"학생: {s['name']}, 점수: {s['score']}, 코멘트: {comment}")

# 딕셔너리 컴프리헨션: {이름: 점수} 형태의 성적표 한 줄로 생성
score_map = {s["name"]: s["score"] for s in students}
print(f"\n한눈에 보는 성적표: {score_map}")

# ===== 고급 =====
# 핵심: 얕은 복사 vs 깊은 복사 + 딕셔너리 키-값 반전

import copy

# 1. 얕은 복사(Shallow Copy)의 함정
# B = A 또는 .copy()는 내부 리스트의 '주소'만 복사 → B 수정 시 A도 바뀜!
original_list = [[1, 2], [3, 4]]
shallow_copy  = original_list.copy()

shallow_copy[0][0] = "바뀜!"
print("\n--- 얕은 복사 결과 ---")
print(f"원본:   {original_list}")  # 원본도 같이 바뀜!!!
print(f"복사본: {shallow_copy}")

# 2. 깊은 복사(Deep Copy)로 완벽하게 분리
# copy.deepcopy()는 내부 리스트·딕셔너리까지 통째로 새로 만듦
original_data = {"skills": ["Python", "AI"], "level": 1}
deep_copy     = copy.deepcopy(original_data)

deep_copy["skills"].append("CUDA")
print("\n--- 깊은 복사 결과 ---")
print(f"원본 데이터: {original_data}")  # 원본 보존!
print(f"깊은 복사본: {deep_copy}")

# 3. 딕셔너리 키-값 반전 (고급 컴프리헨션 응용)
# {"a": 1} → {1: "a"}
original_map = {"a": 1, "b": 2, "c": 3}
reversed_map = {v: k for k, v in original_map.items()}
print(f"\n키-값 반전 결과: {reversed_map}")

# ===== 실습 과제 =====

# 과제 1: 전화번호부 (딕셔너리 + while + .get())
print("\n--- 과제 1: 전화번호부 ---")
phone_num = {}
phone_num["철수"] = "010-1234-5678"
phone_num.update({"영희": "010-1111-2222", "민수": "010-2222-3333"})
print(phone_num)

while True:
    search_name = input("찾을 이름을 입력하세요: ")
    if search_name in phone_num:
        print(f"{search_name}의 연락처는 {phone_num[search_name]} 입니다.")
        break
    else:
        print("찾는 이름이 없습니다. 다시 입력해주세요.")

# 과제 2: 리스트 평균 구하기
print("\n--- 과제 2: 리스트 평균 구하기 ---")
import numpy as np
scores      = [85, 90, 78, 92, 88]
mean_result = np.mean(scores)
print(f"평균 점수: {mean_result}")
