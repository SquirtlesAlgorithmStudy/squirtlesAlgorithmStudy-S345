import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(m, n):
    queue = deque()
    queue.append((m, n))
    board[n][m] = 2

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 1:
                board[ny][nx] = 2
                queue.append((nx, ny))


T = int(input())
for _ in range(T):
    # M = 가로 = Col = X / N = 세로 = Row = Y board[N][M] board[y][x]
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    result = 0

    for m in range(M):
        for n in range(N):
            if board[n][m] == 1:
                bfs(m, n)
                result += 1

    print(result)
