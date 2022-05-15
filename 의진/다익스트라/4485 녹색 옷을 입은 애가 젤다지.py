import sys
import heapq
fastin = sys.stdin.readline
INF = sys.maxsize
tc = 0
while True:
    tc += 1
    n = int(fastin())
    if n == 0:
        break
    cave = [[INF] * (n+1)]
    cave += [[INF] + list(map(int, list(fastin().strip().split())))
             for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = []
    visited = [[INF] * (n+1) for _ in range(n+1)]
    visited[1][1] = cave[1][1]
    q.append((visited[1][1], 1, 1))
    while q:
        vis, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 < nx <= n) and (0 < ny <= n):
                if visited[nx][ny] > (vis + cave[nx][ny]):
                    visited[nx][ny] = vis + cave[nx][ny]
                    heapq.heappush(q, (visited[nx][ny], nx, ny))

    print("Problem %d: %d" % (tc, visited[n][n]))
