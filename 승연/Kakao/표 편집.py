# idea : 딕셔너리의 key_순서 나타냄 / value_삭제유무 
# 삭제한 것들 저장하는 힙

# *시도해봤는데 아직 못 풀었어요ㅜ (오답코드)
from collections import deque

def get_key(val):
    key_list = []
    for key, value in calender.items():
        if val == value:
            key_list.append(key)
    return key_list

def solution(n, k, cmd):
    calender = {}
    locate = k
    deq_del_list = deque()
    for i in range(n):
        calender [i] = 'O'
    
    for j in cmd:
        if j[0] == 'D':
            temp_list = list(get_key('O'))
            temp_locate = temp_list.index(locate)
            locate =  temp_list[temp_locate + int(j[2])]
        elif j[0] == 'U':
            temp_list = list(get_key('O'))
            temp_locate = temp_list.index(locate)
            locate =  temp_list[temp_locate - int(j[2])]
        elif j[0] == 'C':
            deq_del_list.append(locate)
            calender[locate] = 'X'
            if locate == max(list(get_key('O'))):
                locate -= 1
            else:
                locate += 1
        else:
            temp = deq_del_list.deq.popleft()
            calender[temp] = 'O'
            
    answer = calender.values()
    answer = ''.join(answer)
    
    return answer