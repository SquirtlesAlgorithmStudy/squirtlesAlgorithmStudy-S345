

#뿅망치 : 사람 키 /2 
#키가 1인 경우 뿅망치의 영향을 받지 않는다

# 매번 가장 키가 큰 거인을 때리자 : 센티의 전략 

# 하려 하는 것: 거인 나라의 모든 거인이 센티보다 키가 작도록 


# input: n , h , t (# of 거인 ,  센티의 키, 뿅망치 횟수)
# input: 각 거인의 키를 나타내는 정수 

import sys 
import heapq
input = sys.stdin.readline

n,h,t =map(int,input().split())

#최대 힙을 써야 하기 때문에, 부호를 - 로 받는다

giants = [-int(input()) for _ in range(n)]
heapq.heapify(giants)

min_try = 0 
chk = False

for i in range(1,t+1):
    if -h <max(giants):
        min_try=i
        chk=False
        break
    giant = heapq.heappop(giants)
    if giant==-1:
        pass
    else:
        giant = int(giant/2)    
    heapq.heappush(giants,giant)
    
    
     
    
    
if chk: 
    print("YES")
    print(min_try)
else:
    print("NO")
    giant = heapq.heappop(giants)
    giant = -giant
    print(int(giant))
    
    
    

# 예제는 다 맞게 나왔는데, 채점시 2% 에서 틀림 


