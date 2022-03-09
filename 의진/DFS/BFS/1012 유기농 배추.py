from collections import deque
import sys
input = sys.stdin.readline
t = int(input().strip())


def testcasein():
    global n, m, k
    global data
    m, n, k = map(int, input().strip().split())
    data = [list(map(int, input().strip().split())) for _ in range(k)]


def bfs(m, n, k, data):
    queue = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if data == 0:
        return 0
    complete = []
    warm = 0
    for i in range(k):
        if [data[i][0], data[i][1]] not in complete:
            nx = data[i][0]
            ny = data[i][1]
            queue.append([nx, ny])

            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (0 <= nx < m) and (0 <= ny < n):
                        if [nx, ny] in data and [nx, ny] not in complete:
                            queue.append([nx, ny])
                            complete.append([nx, ny])

            warm += 1

    return warm


result = []
for _ in range(t):
    testcasein()
    result.append(bfs(m, n, k, data))

for i in range(t):
    print(result[i])
