import sys
from collections import deque
fastin = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    max_n = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m  and not visited[nx][ny] and s[nx][ny] != "W":
                visited[nx][ny] = True
                s[nx][ny] = s[x][y] + 1
                max_n = max(max_n, s[nx][ny])
                q.append([nx, ny])

    return max_n


n, m = map(int, fastin().split())
s = []
result = 0

for i in range(n):
    s.append(list(fastin().strip()))

for i in range(n):
    for j in range(m):
        if s[i][j] != "W":
            visited = [[False] * m for  _ in range(n)]
            s[i][j] = 0
            visited[i][j] = True
            result = max(result, bfs(i, j))

print(result)