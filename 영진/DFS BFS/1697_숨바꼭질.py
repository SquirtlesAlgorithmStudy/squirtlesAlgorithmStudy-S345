from collections import deque
N,K=map(int,input().split())
MAX=100000
graph=[0]*(MAX+1)

def bfs():
    queue=deque()
    queue.append(N)
    
    while queue:
        n=queue.popleft()
        if n==K:
            print(graph[n])
            return
        for nx in (n-1,n+1,2*n):
            if 0<=nx<=MAX and not graph[nx]:
                queue.append(nx)
                graph[nx]=graph[n]+1
                
bfs()