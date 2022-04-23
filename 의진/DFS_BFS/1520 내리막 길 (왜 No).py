import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
count = 0
dp = [[0] * n for _ in range(m)]


def dfs(y, x):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if x == n-1 and y == m-1:
        return 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[ny][nx] < board[y][x]:
                if dp[ny][nx] > 0:
                    dp[y][x] += dp[ny][nx]
                else:
                    dp[y][x] += dfs(ny, nx)

    return dp[y][x]


dfs(0, 0)
print(dp[0][0])
