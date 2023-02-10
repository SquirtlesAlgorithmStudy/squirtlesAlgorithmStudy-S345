from sys import stdin

def dfs(x,y):
    global cnt
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0 or visited[nx][ny]:
            continue
        if field[nx][ny] != 0:
            visited[nx][ny] = 1
            dfs(nx, ny)

T = int(stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int,stdin.readline().split())
    field = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        a, b = map(int,stdin.readline().split())
        field[b][a] = 1
    for i in range(N):
        for j in range(M):
            if field[i][j] and not visited[i][j]:
                visited[i][j] = 1
                cnt += 1
                dfs(i,j)
    print(cnt)