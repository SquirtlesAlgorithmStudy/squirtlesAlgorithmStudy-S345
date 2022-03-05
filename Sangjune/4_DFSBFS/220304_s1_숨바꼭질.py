from collections import deque
import sys

fin = sys.stdin.readline

def bfs(x, k):
    arr = [0] * 200000
    if x == k:
        return 0
    queue = deque()
    queue.append(x)

    while queue:
        x = queue.popleft()
        for i in range(3):
            if i == 2:
                nx = 2 * x
            else:
                nx = x + dx[i]
            if nx < 0 or nx >= 200000:
                continue
            if arr[nx] == 0:
                arr[nx] = arr[x] + 1
                queue.append(nx)
        if arr[k] != 0:
            return arr[k]


N, K = map(int, fin().rstrip().split())
dx = [-1, 1, 0]

print(bfs(N, K))