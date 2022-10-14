# idea : 딕셔너리의 key_순서 나타냄 / value_삭제유무 
# 삭제한 것들 저장하는 힙

# *시도해봤는데 아직 못 풀었어요ㅜ (오답코드)
# test case 5부터 런타임에러..
from collections import deque
calender = {}

def get_key(val):
    key_list = []
    for key, value in calender.items():
        if val == value:
            key_list.append(key)
    return key_list

def solution(n, k, cmd):
    locate = k
    deq_del_list = deque()
    
    #삭제되기 전 모두 0으로 초기화
    for i in range(n):
        calender [i] = 'O'
    
    # cmd 스캔
    for j in cmd:
        #아래로 이동하는 경우
        if j[0] == 'D':
            #삭제되지 않은 것들 중에서 위/아래 이동시 갯수 세줘야 함
            temp_list = list(get_key('O'))
            #삭제되지 않은 것들 중에서 현재 위치의 인덱스값 저장
            temp_locate = temp_list.index(locate)
            #삭제되지 않은 것들 중에서 현재 위치의 인덱스값 +2 의 값 locate에 저장
            locate =  temp_list[temp_locate + int(j[2])]
        #위로 이동하는 경우 (로직은 아래로 이동하는 경우와 동일)
        elif j[0] == 'U':
            temp_list = list(get_key('O'))
            temp_locate = temp_list.index(locate)
            locate =  temp_list[temp_locate - int(j[2])]
        #삭제하는 경우
        elif j[0] == 'C':
            #삭제한 것들 저장하는 힙에 현재 위치 추가
            deq_del_list.append(locate)
            
            #삭제된 위치가 가장 아래 값인 경우
            if locate == max(list(get_key('O'))):
                calender[locate] = 'X'
                locate -= 1
            
            else:
                calender[locate] = 'X'
                locate += 1
                
        #이전으로 돌아가는 경우    
        else:
            #삭제된 데크에서 맨 앞의 값 빼기
            temp = deq_del_list.pop()
            calender[temp] = 'O'
            
    answer = calender.values()
    answer = ''.join(answer)
    
    return answer