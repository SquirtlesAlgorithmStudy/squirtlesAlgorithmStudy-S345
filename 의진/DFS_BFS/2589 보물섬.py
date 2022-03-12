from collections import deque
import sys
fastin = sys.stdin.readline

n, m = map(int, fastin().split())
board = [list(fastin().rstrip()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
landlist = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            landlist.append((i, j))


def bfs(start):
    queue = deque()
    visited = [[-1] * m for _ in range(n)]
    queue.append(start)
    visited[start[0]][start[1]] = 0
    result = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not(0 <= nx < n and 0 <= ny < m):
                continue

            if board[nx][ny] == 'W':
                continue

            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                result = max(result, visited[nx][ny])
                queue.append((nx, ny))

    return result


result = 0

for land in landlist:
    result = max(result, bfs(land))

print(result)
