import copy
from collections import deque

#입력받기
n,m=map(int,input().split())
graph = []

for i in range(n):
  graph.append(list(input()))

# 숫자로 바꾸기 
for i in range(n):
  for j in range(m):
    if graph[i][j] == "W":
      graph[i][j] = 0
    else:
      graph[i][j] = 1

  
#L 위치를 리스트로 받기
location = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      location.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(graph)
print(location)

def bfs(x,y,a,b):
  queue = deque()
  queue.append((x,y))
  
  while queue:
    x,y= queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      #범위를 벗어난 경우 9가지 

      if nx<0 or nx>=a or ny<0 or ny>=b:
        continue
      if p[nx][ny] == 0:
        continue
      if p[nx][ny] == 1:
        p[nx][ny] = p[x][y]+1
        queue.append((nx,ny))

    if x==a and y ==b:   
      return p[a-1][b-1]
    else:
      return 0

distance = []

p = copy.copy(graph)
# nC2만큼 좌표를 옮겨가며 개수 세기
for x,y in location:
  for a,b in location:
    if x==a and y==b:
      continue
    p = copy.copy(graph)
    l = bfs(x,y,n,m)
    distance.append(l)

print(max(distance))
        