import sys
fastin = sys.stdin.readline

n, m = map(int, fastin().split())
board = [list(fastin().rstrip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]


def dfs_x(x, y):
    if x < 0 or x >= m:
        return False
    if visited[y][x] == 0 and board[y][x] == '-':
        visited[y][x] = 1
        dfs_x(x-1, y)
        dfs_x(x+1, y)
        return True
    return False


def dfs_y(x, y):
    if y < 0 or y >= n:
        return False
    if visited[y][x] == 0 and board[y][x] == '|':
        visited[y][x] = 1
        dfs_y(x, y-1)
        dfs_y(x, y+1)
        return True
    return False


count = 0
for i in range(m):
    for j in range(n):
        if dfs_x(i, j) == True:
            count += 1
visited = [[0] * m for _ in range(n)]
for i in range(m):
    for j in range(n):
        if dfs_y(i, j) == True:
            count += 1

print(count)
