from collections import deque
import sys
read = sys.stdin.readline
def bfs(a,b):
    q = deque()
    q.append((a,1))
    while q: 
        n,cnt = q.popleft()
        if n == b:
            print(cnt)
            break
        if n > b:
            continue
        else:
            q.append((n * 2, cnt + 1))
            q.append((n * 10 + 1,cnt + 1))
    else:
        print(-1)


# def dfs(a, b):
#     if 
#     if a == b:
#         return 1
#     if a > b:
#         return -1
#     print(min(dfs(a * 2, b) + 1, dfs(int(str(a) + "1"), b) + 1))
    
a, b = map(int, read().split())
bfs(a,b)
