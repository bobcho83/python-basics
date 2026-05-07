# 오늘 배운 것: 파일 입출력(File I/O) — TXT / JSON / CSV 읽기·쓰기·예외 처리

# 개념 정리
# open() 모드
#   'r' (Read)  : 읽기용 — 파일 없으면 FileNotFoundError
#   'w' (Write) : 쓰기용 — 새로 만들거나 기존 내용 덮어씀
#   'a' (Append): 추가용 — 기존 내용 뒤에 덧붙임
# 파일 읽기 방법
#   read()      : 전체 내용을 하나의 문자열로
#   readline()  : 한 줄만 읽기
#   readlines() : 모든 줄을 리스트로
# with 문     : 블록 종료 시 파일 자동으로 안전하게 닫음 (close() 불필요)

# ===== 초급 =====
# 핵심: TXT 파일 쓰기('w') / 추가('a') / 읽기('r') + with 문

file_path = "daily_report.txt"

# 파일 쓰기 — with 문으로 자동 close
with open(file_path, "w", encoding="utf-8") as f:
    f.write("--- 12일차 마케팅 리포트 ---\n")
    f.write("1. 파이썬 파일 입출력 공부 완료\n")
    f.write("2. 깃허브 12일 연속 잔디 심기 성공\n")
    print(f"'{file_path}' 파일에 기록을 완료했습니다.")

# 파일 추가 — 기존 내용 뒤에 덧붙임
with open(file_path, "a", encoding="utf-8") as f:
    f.write("3. 내일은 예외 처리 공부 예정\n")

# 파일 읽기 — readlines()로 줄 단위 리스트 반환
print("\n[저장된 파일 내용 읽기]")
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())  # strip()으로 줄바꿈 문자 제거

# ===== 중급 =====
# 핵심: JSON 파일 저장(dump) / 불러오기(load) — 파이썬 딕셔너리 ↔ JSON 변환

import json

campaign_config = {
    "campaign_name"  : "여름 신제품 프로모션",
    "budget"         : 5_000_000,
    "target_platform": ["Instagram", "Facebook", "Youtube"],
    "is_active"      : True
}

file_name = "config.json"

# JSON 저장 — ensure_ascii=False: 한글 깨짐 방지 / indent=4: 들여쓰기로 가독성 향상
with open(file_name, "w", encoding="utf-8") as f:
    json.dump(campaign_config, f, ensure_ascii=False, indent=4)
    print(f"\n설정 파일 '{file_name}' 생성 완료.")

# JSON 불러오기 — load 후 딕셔너리처럼 사용
print("[설정 파일 불러오기]")
with open(file_name, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(f"캠페인명: {loaded_data['campaign_name']}")
    print(f"활성화 상태: {'진행 중' if loaded_data['is_active'] else '중단'}")

# ===== 고급 =====
# 핵심: CSV 읽기·쓰기 + try-except 예외 처리(FileNotFoundError)

import csv

performance_data = [
    ["날짜",       "채널",      "클릭수", "전환율"],
    ["2026-05-01", "Google",    1200,    "3.5%"],
    ["2026-05-02", "Instagram", 850,     "4.2%"],
    ["2026-05-03", "Facebook",  600,     "2.1%"],
]

csv_file = "marketing_data.csv"

try:
    # CSV 쓰기 — newline="": 빈 줄 방지 / utf-8-sig: 엑셀 한글 깨짐 방지
    with open(csv_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(performance_data)
    print(f"\n✅ '{csv_file}' 저장 완료!")

    # CSV 읽기 — reader로 줄 단위 리스트 반환
    print("[데이터 읽기 결과]")
    with open(csv_file, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        for row in reader:
            print(f"| {'|'.join(str(v) for v in row)} |")

except FileNotFoundError:
    print("❌ 오류: 파일을 찾을 수 없습니다. 경로를 확인하세요.")
except Exception as e:
    print(f"❌ 알 수 없는 오류: {e}")
