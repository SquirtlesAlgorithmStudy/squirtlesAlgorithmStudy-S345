from collections import deque
import sys
fastin = sys.stdin.readline
start, end = map(int, fastin().split())
visited = [-1] * 100001
dx = [1, -1, 0]


def bfs(x):
    if x == end:
        return 0
    queue = deque()
    queue.append(x)
    visited[x] = 0

    while queue:
        # print(queue)
        x = queue.popleft()
        for i in range(3):
            if dx[i] == 0:
                if x == 0:
                    continue
                nx = 2*x
            else:
                nx = x + dx[i]
            if nx < 0 or nx >= 100001:
                continue

            if nx == end:
                return visited[x] + 1
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)
    return -1


print(bfs(start))
