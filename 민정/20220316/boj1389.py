import sys
from collections import deque
fastin = sys.stdin.readline

def bfs(graph, start):
    num = [0] * (n+1)
    visited = [start]
    q = deque()
    q.append(start)

    while q:
        a = q.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                q.append(i)

    return sum(num)

n, m = map(int, fastin().split())
board = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, fastin().split())
    board[a].append(b)
    board[b].append(a)

result = []
for i in range(1, n+1):
    result.append(bfs(board, i))

print(result.index(min(result))+1)