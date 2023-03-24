# #1초당 2000만회 연산가능
# #5초에 1억회
# #sum, len 등의 간단한 연산(O(n)) 매번하는 것은 좋지않다.

# from collections import deque

# def solution(queue1, queue2):
    
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)
#     limit = len(queue1) * 4
#     cnt = 0
    
#     if (sum(queue1) + sum(queue2))%2 != 0: # 총 합이 홀수이면 절대 답을 낼 수 없음.
#         return -1
    
#     for i in range(len(queue1)*2): # 충분한 횟수만큼 반복
#         if sum(queue1) > sum(queue2):
#             queue2.append(queue1.popleft()) # 큰큐에서 작은큐로 숫자 이동시킴
#             cnt += 1
#         elif sum(queue1) < sum(queue2):
#             queue1.append(queue2.popleft())
#             cnt += 1
#         else: # 두개의 큐가 같을 때
#             return cnt
    
#     return -1

#1초당 2000만회 연산가능
#5초에 1억회
#sum, len 등의 간단한 연산(O(n))도 매번하는 것은 좋지않다.

from collections import deque

def solution(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limitation = len(queue1) * 4
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1 + sum2
    cnt = 0
    
    if (total)%2 != 0: # 총 합이 홀수이면 절대 답을 낼 수 없음.
        return -1
    
    for i in range(limitation): # 충분한 횟수만큼 반복
        if sum1 > sum2: # 큰큐에서 작은큐로 숫자 이동시킴
            target = queue1.popleft()
            queue2.append(target)
            cnt += 1
            sum1 -= target
            sum2 += target
        elif sum1 < sum2:
            target = queue2.popleft()
            queue1.append(target)
            cnt += 1
            sum2 -= target
            sum1 += target
        else: # 두개의 큐가 같을 때
            return cnt
    
    return -1