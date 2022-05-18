
#16234 인구이동
from collections import deque
import sys
input = sys.stdin.readline

def BFS(x, y):
  graph = []
  queue = deque()
  queue.append((0,0))

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= line or ny < 0 or ny >= line:
        continue
      if graph[nx][ny]: #
        continue
      
      if abs(array[x][y] - array[nx][ny]) < over and abs(array[x][y] - array[nx][ny]) > under:
        queue.append((nx,ny))
        graph[x][y] = True
        graph[nx][ny] = True
        cnt += 1
        
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))
               



##Main##
#칸 수, 최소값, 최댓값
line, under, over = map(int, input().split())
array = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(line):
  array.append(input().split())
  
#union[(i,j)]