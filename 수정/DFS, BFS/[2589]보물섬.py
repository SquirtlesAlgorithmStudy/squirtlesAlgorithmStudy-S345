#시간초과
from collections import deque
import sys
fastin = sys.stdin.readline

Y, X = map(int, fastin().rstrip().split())
treasure_map = []
for i in range(Y):
    treasure_map.append(list(map(str, fastin().rstrip())))
# print(treasure_map)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    tm = [[-1] * X for _ in range(Y)]
    tm[y][x] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                continue
            if treasure_map[ny][nx] == 'W':
                continue
            if treasure_map[ny][nx] == 'L' and tm[ny][nx] == -1:
                tm[ny][nx] = tm[y][x] + 1
                queue.append((nx, ny))
    maxd = 0
    for i in range(Y):
        m = max(tm[i])
        if m > maxd:
            maxd = m
    return maxd

hours = 0
maxh = 0

for y in range(Y):
    for x in range(X):
        if treasure_map[y][x] == 'L':
            hours = bfs(x, y)
            if hours > maxh:
                maxh = hours

print(maxh)