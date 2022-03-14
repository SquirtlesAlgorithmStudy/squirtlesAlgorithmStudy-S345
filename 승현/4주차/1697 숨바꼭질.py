import sys
from collections import deque
fastin = sys.stdin.readline

def bfs (x):
  queue = deque()
  queue.append(x)
  
  while queue:
    dx = [x-1, x+1 , 2*x]
    x = queue.popleft()
    
    if x < 0 or x > 1000001:
      continue
      
    if x == young:
      print(line[x])
      break
      
    for a in dx:
      if line[a] == 0 and not line[a]:
        line[a] = line[x] + 1
        queue.append(a)

#언니와 동생 좌표 입력
old, young = map(int,fastin().split())
line = [0] * 1000000

bfs(old)