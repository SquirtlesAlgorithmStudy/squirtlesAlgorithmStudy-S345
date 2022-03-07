import sys

fin = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

T = int(fin())
for _ in range(T):
    M, N, K = map(int, fin().rstrip().split())
    graph = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, fin().rstrip().split())
        graph[x][y] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if dfs(i, j) == True:
                count += 1
    print(count)