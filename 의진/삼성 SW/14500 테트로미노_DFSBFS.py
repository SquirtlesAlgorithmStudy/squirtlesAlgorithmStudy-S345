import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, 0]
dy = [0, 1, -1]
result = 0
visited = [[0] * m for _ in range(n)]
MAX_VAL = max(map(max, board))


def dfs(y, x, recursionCount, sumValue):
    global result
    if result >= sumValue + MAX_VAL * (3-recursionCount):
        return
    if recursionCount == 3:
        result = max(result, sumValue)
        return

    for i in range(3):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
            if recursionCount == 1:
                visited[ny][nx] = 1
                dfs(y, x, recursionCount + 1, sumValue + board[ny][nx])
                visited[ny][nx] = 0
            visited[ny][nx] = 1
            dfs(ny, nx, recursionCount + 1, sumValue + board[ny][nx])
            visited[ny][nx] = 0


for y in range(n):
    for x in range(m):
        visited[y][x] = 1
        dfs(y, x, 0, board[y][x])
        visited[y][x] = 0


print(result)
