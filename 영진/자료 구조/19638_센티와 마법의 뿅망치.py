import heapq
import sys
N,H,T=map(int,input().split())
gaint=[]

for _ in range(N):
    heapq.heappush(gaint,-int(input()))

count=0
for _ in range(T):
    
    if H<=-gaint[0] and -gaint[0]!=1:
        heapq.heappush(gaint,int(heapq.heappop(gaint)/2))
        count+=1
    
if H>-gaint[0]:
    print("YES")
    print(count)
else:
    print("NO")
    print(-gaint[0])   
        
"""
1.파이썬 힙정렬
* import heapq
*heapq.headpush(heap,item):item을 heap에 추가
*heapq.heappop(heap):heap에서 가장 작은 원소를 pop & 리턴, 비어있는 경우 IndexError
*heapq.heapify(x):리스트 x를 즉각적으로 heap으로 변경
*기본적으로 최소힙이지만 리스트의 값에 '-'를 붙여 최대힙 구현 가능
"""