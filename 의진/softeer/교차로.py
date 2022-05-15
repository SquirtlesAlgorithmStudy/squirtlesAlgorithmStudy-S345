import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
carInfos = [tuple(input().rstrip().split()) for _ in range(n)]
INF = 10 ** 7
results = [-1] * n
position = ['A', 'B', 'C', 'D']

queues = [deque(), deque(), deque(), deque()]

# 큐에 차량 추가
for index, carInfo in enumerate(carInfos):
    min_time = INF
    if carInfo[0] < min_time:
        min_time = carInfo[0]
    for i in range(4):
        if carInfo[1] == position[i]:
            queues[i].append((index, carInfo[0]))
            break
# Current Time을 이용하여 Current Time 때마다 1대 또는 2대의 차량이 통과하게끔 구현
cur_time = min_time
min_val = [INF] * 4
while queues[0] or queues[1] or queues[2] or queues[3]:
    min_val =


for result in results:
    print(result)
