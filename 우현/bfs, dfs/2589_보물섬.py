from collections import deque

def bfs(x,y):
  cnt = 0
  land = []
  q = deque()
  q.append((x,y))
  visited = [[0]*m for _ in range(n)]
  visited[x][y] = 1

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
    
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if graph[nx][ny] == 'L' and visited[nx][ny] == 0:
        visited[nx][ny] = visited[x][y] + 1
        cnt = max(cnt, visited[nx][ny])
        q.append((nx, ny))
  
  return cnt-1

n, m = map(int, input().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
graph = []
for i in range(n):
  graph.append(list(map(str,input())))

#c = 0
distance = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 'L':
      #print("i:",i,"j:",j,"graph[",i,"][",j,"]:",graph[i][j],bfs(i,j))
      #c += 1 
      distance.append(bfs(i,j))
#print(c)
      #max_distance = max(max_distance, bfs(i,j))
print(max(distance))