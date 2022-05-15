# 1932 - 회의실 배정

import sys
input = sys.stdin.readline

n = int(input().split())            # 입력받을 회의 개수
conf = [[]*2 for _ in range(n)]     # 회의 입력
for i in range(n) :
    start, end = map(int, input().split())      # 회의의 시작시간과 종료 시간 저장
    conf[i][0] = start
    conf[i][1] = end

conf.sort(key = lambda x : (x[1, x[0]]))

count = 1
endTime = conf[0][1]

for i in range(1, n) :                      # 첫번째 회의는 제일 먼저 시작, 볼 필요 없음
    if conf[i][0] >= endTime :              # 지금 회의가 끝나는 시간보다 다음회의의 시작시간이 늦으면
        count += 1
        endTime = conf[i][1]
        
print(count)
 

