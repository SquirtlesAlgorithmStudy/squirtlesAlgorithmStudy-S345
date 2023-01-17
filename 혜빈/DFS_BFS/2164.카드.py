import sys
input = sys.stdin.readline
from collections import deque

queue=deque()

N=int(input())

for i in range(N):
    queue.append(i+1)

for _ in range(N-1):
    queue.popleft()
    num=queue.popleft()
    queue.append(num)
  

print(queue.popleft())