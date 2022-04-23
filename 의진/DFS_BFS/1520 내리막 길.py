import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
count = 0
dp = [[-1] * n for _ in range(m)]


def dfs(y, x):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if x == n-1 and y == m-1:
        return 1
    elif dp[y][x] == -1:
        dp[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[ny][nx] < board[y][x]:
                dp[y][x] += dfs(ny, nx)

    return dp[y][x]


dfs(0, 0)
print(dp[0][0])
