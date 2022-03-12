from collections import deque

def bfs(x,y,team):
  cnt = 1
  q = deque()
  q.append((x,y))
  visited[x][y] = True

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue

      if war[nx][ny] == team and not visited[nx][ny]:
        visited[nx][ny] = True
        q.append((nx, ny))
        cnt += 1
    
  return cnt

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
war = []
for _ in range(m):
  war.append(list(input()))

visited = [[False] * n for _ in range(m)]

b = 0
w = 0

for i in range(m):
  for j in range(n):
    if war[i][j] == 'W' and not visited[i][j]:
      w += bfs(i,j,'W')**2
    elif war[i][j] == 'B' and not visited[i][j]:
      b += bfs(i,j,'B')**2

print(w, b)