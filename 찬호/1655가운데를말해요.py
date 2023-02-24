# 중간값을 어떻게 표현하는지
# listen 을 받으면, 힙정렬(효율)을 하고, 인덱스 /2 를 통해 중간값을 
# 효율적인 (0.1 python 은 0.6 초) 코드를 작성하는지
# 관건 

import sys 
import heapq
input =sys.stdin.readline

n = int(input())

heap1 = [] # 최소 힙 
heap2 = [] # 최대 힙  

for i in range(n):
    num = int(input())
    
    if len(heap1) ==len(heap2):
        heapq.heappush(heap1,-num)
    else:
        heapq.heappush(heap1,num)
        
    if heap2 and heap2[0] < - heap1[0]:
        left =heapq.heappop(heap1)
        right = heapq.heappop(heap2)
        
        heapq.heappush(heap1,-right)
        heapq.heappush(heap2,-left)
        
    print(-heap1[0])