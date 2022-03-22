import sys
from collections import deque
fastin = sys.stdin.readline

m, n = map(int, fastin().split())
board = [list(fastin()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
W, B = 0, 0

visited = [[False] * m for _ in range(n)]

q = deque()

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = True
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[x][y] == board[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            answer = bfs(i, j)
            if board[i][j] == 'W':
                W += answer ** 2
            else:
                B += answer ** 2

print(W, B)