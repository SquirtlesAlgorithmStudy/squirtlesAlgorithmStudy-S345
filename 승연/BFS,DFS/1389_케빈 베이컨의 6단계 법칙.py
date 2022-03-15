import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
# print(graph)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # print(graph, 'a')
    graph[b].append(a)
    # print(graph, 'b')

# print(graph)

###
def bfs(graph, start):
    num = [0] * (n + 1)
    q = deque()
    visited[start] = 1
    q.append(start)
    while q:
        a = q.popleft()
        # print(a)
        for i in graph[a]:
            if visited[i] == 0:
                num[i] = num[a] + 1
                q.append(i)
                visited[i] = 1
    return sum(num)
###

result = []
for i in range(1, n + 1):
    visited = [0 for _ in range(n + 1)]
    result.append(bfs(graph, i))

print(result.index(min(result))+ 1)