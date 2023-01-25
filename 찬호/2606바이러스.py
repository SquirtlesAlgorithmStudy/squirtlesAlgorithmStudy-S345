import sys 

def DFS(start,computer,visited):
    
    visited[start] = 1
    for i in computer[start]:
        if visited[i]==0:
            DFS(i)
            
    return (sum(visited)-1)

 


input = sys.stdin.readlines
N = map(int,input())
M = map(int,input())
computer = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    x,y = map(int,input().split())
    computer[x].append(y)
    computer[y].append(x)
    




ans = DFS(1,computer,visited)
print(ans)