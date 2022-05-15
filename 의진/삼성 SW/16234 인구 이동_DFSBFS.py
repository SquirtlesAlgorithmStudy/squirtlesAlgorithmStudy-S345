import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 1
visited = [[0] * N for _ in range(N)]
results = [0]


def bfs(r, c, visitedCount):
    flag = False
    queue = deque()
    queue.append((r, c))
    visited[r][c] = visitedCount
    populationCount = populations[r][c]
    nationCount = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0 and L <= abs(populations[y][x] - populations[ny][nx]) <= R:
                visited[ny][nx] = visitedCount
                populationCount += populations[ny][nx]
                nationCount += 1
                flag = True
                queue.append((ny, nx))
    results.append(populationCount // nationCount)
    return flag


flag = True
resultCount = 0
while flag:
    results = [0]
    visited = [[0] * N for _ in range(N)]
    flag = False
    visitedCount = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visitedCount += 1
                if not flag:
                    flag = bfs(r, c, visitedCount)
                else:
                    bfs(r, c, visitedCount)
    for r in range(N):
        for c in range(N):
            populations[r][c] = results[visited[r][c]]
    if flag:
        resultCount += 1

print(resultCount)
