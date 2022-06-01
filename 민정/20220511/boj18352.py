import sys
from collections import deque
fastin = sys.stdin.readline

answer = []
n, m, k, x = map(int, fastin().split())
visited = [False] * (n + 1)
path = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, fastin().split())
    path[a].append(b)
    
q = deque()
q.append((x, 0))

while q:
    town, cnt = q.popleft()
    if cnt == k:
        answer.append(town)
    elif cnt < k:
        for i in path[town]:
            if not visited[i]:
                visited[i] = True
                q.append((i, cnt + 1))
                
if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for a in answer:
        print(a)