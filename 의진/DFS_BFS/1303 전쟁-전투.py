from collections import deque
import sys
fastin = sys.stdin.readline

n, m = map(int, fastin().split())
board = [list(fastin().rstrip()) for _ in range(m)]
visited_W = [[0] * n for _ in range(m)]
visited_B = [[0] * n for _ in range(m)]
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, wb, visited):
    if visited[x][y] != 0 or board[x][y] != wb:
        return 0
    result = 1
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not ((0 <= nx < m) and (0 <= ny < n)):
                continue

            if board[nx][ny] != wb:
                continue

            if visited[nx][ny] == 0:
                visited[nx][ny] = result + 1
                result += 1
                queue.append((nx, ny))
    return result


wPower = 0
bPower = 0

for i in range(m):
    for j in range(n):
        wPower += (bfs(i, j, 'W', visited_W) ** 2)
        bPower += (bfs(i, j, 'B', visited_B) ** 2)
print(wPower, bPower)
