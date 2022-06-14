# pypy로 돌려야지 성공됨
from collections import deque
import queue
import sys
input = sys.stdin.readline


def bfs(v):
    visited = [False] * (n + 1)
    q = deque()
    q.append(v)
    count = 1
    visited[v] = True
    while q:
        x = q.popleft()
        for i in array[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1
    return count


n, m = map(int, input().split())
array = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    array[b].append(a)


computer = []
for i in range(1, n+1):
    computer.append(bfs(i))
max = max(computer)

for i in range(len(computer)):
    if max == computer[i]:
        print(i + 1, end=" ")
