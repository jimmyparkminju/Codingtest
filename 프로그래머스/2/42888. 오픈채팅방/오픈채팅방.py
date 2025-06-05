def solution(record):
    answer = []
    user = {}  # uid -> 닉네임 저장

    # 1. 모든 record 순회하면서 닉네임 정보 최신화
    for r in record:
        parts = r.split()
        action = parts[0]
        uid = parts[1]
        if action in ("Enter", "Change"):
            nickname = parts[2]
            user[uid] = nickname  # uid에 해당하는 닉네임 최신화

    # 2. 메시지 만들기 (최종 닉네임 기준)
    for r in record:
        parts = r.split()
        action = parts[0]
        uid = parts[1]
        if action == "Enter":
            answer.append(f"{user[uid]}님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(f"{user[uid]}님이 나갔습니다.")

    return answer
