## 가장 왼쪽에서 정무만큼 떨어진 거리만 물이 샐 때,
## 테이프를 이용하여 물이 새는 곳을 기준으로 좌우 0.5만큼 간격울 주어 막음
## 물이 새는 위치(물이 새는 곳의 개수N), 테이프의 길이(L)가 주어짐
## 필요한 최소한의 테이프의 수?(N,L<=1000인 자연수)

"""
<분석>

(1)
4 2
1 2 100 101
->2

=> 물이 새는 곳마다 최소 1만큼의 테이프를 사용
   연속한 물의 새는 곳의 개수가 테이프의 길이 보다 작거나 같을 경우,
   하나의 테이프로 막을 수 있음

(2)
4 3
1 2 3 4
->2

=> 물이 새는 곳마다 최소 1만큼의 테이프를 사용
   연속한 물의 새는 곳의 개수가 테이프의 길이 보다 작거나 같을 경우,
   하나의 테이프로 막을 수 있음


(3)
3 1
3 2 1
->3

=>물이 새는 곳마다 최소 1만큼의 테이프를 사용
   연속한 물의 새는 곳의 개수가 테이프의 길이 보다 작거나 같을 경우,
   하나의 테이프로 막을 수 있음
   
<시도1>
1.물이 새는 위치를 입력받음
2.물이 새는 위치가 연속한지 확인
3.연속한 위치의 수가 테이프의 길이보다 작거나 같은지 확인
4(1).작거나 같을 경우, 같은 테이프 사용(테이프의 수 카운트x)
4(2).작거나 같지 않을 경우, 테이프의 수 카운트
5.카운트한 테이프의 수 출력

<알게된 점>
1. map(int, sys.stdin.readline().split())
2. list(int,sys.stdin.readline().split())
"""

num_LeakingSpot,length_tape=map(int,input().split())
leaking_spot=list(map(int, input().split()))
leaking_spot.sort(reverse=False)
     
num_needed_tape=0
needed_length_tape=1
start_spot=leaking_spot[0]

for i in range(len(leaking_spot)):
    if leaking_spot[i]-start_spot+1<=length_tape:
        break
    else:
        start_spot=leaking_spot[i]
        num_needed_tape+=1
    num_needed_tape+=1
print(num_needed_tape)
