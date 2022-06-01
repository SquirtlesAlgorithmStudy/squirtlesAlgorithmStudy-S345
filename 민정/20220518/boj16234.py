import sys
import math
from collections import deque
fastin = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 1 <= n <= 50 / 1 <= l <= r <= 100
# 0 <= A[r][c] <= 100


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    uni = [(i, j)]
    cnt = A[i][j]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if l <= abs(A[x][y] - A[nx][ny]) <= r:
                uni.append((nx, ny))
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += A[nx][ny]

    for x, y in uni:
        A[x][y] = math.floor(cnt / len(uni))

    return len(uni)


n, l, r = map(int, fastin().split())
A = [list(map(int, fastin().split())) for _ in range(n)]
# print(A)
answer = 0

while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:
        break
    answer += 1

print(answer)

