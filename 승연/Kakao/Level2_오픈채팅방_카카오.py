from collections import deque

def solution(record):
    enter_leave_q = deque()
    # key:아이디, value:닉네임 딕셔너리
    id_name = {}
    for i in range(len(record)):
        temp = list(record[i].split(" "))
        # key:아이디, value:닉네임
        if len(temp) == 3:
            id_name[temp[1]] = temp[2]

        # 들어온 사람과 나온 사람의 아이디 데큐에 저장
        if (temp[0] == 'Enter') or (temp[0] == 'Leave'):
            enter_leave_q.append(temp[1])

    # 정답 출력하는 부분 (아이디가 첫 번째 나오면 enter, 두 번째 나오면 leave)
    answer = []
    chatroom_people = []

    for i in range(len(enter_leave_q)):
        temp = enter_leave_q.popleft()
        if temp in chatroom_people:
            answer.append(id_name[temp] + "님이 나갔습니다.")
            chatroom_people.remove(temp)
        else:
            answer.append(id_name[temp] + "님이 들어왔습니다.")
            chatroom_people.append(temp)

    return answer