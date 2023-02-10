# 처음에는 bfs에 x,y 값만 받아서 메인에서 수를 세려 하였으나 실패
from collections import deque
from sys import stdin
N,M=map(int,stdin.readline().rstrip().split())

war=[list(input()) for _ in range(M)]
visited=[[False]*N for _ in range(M)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,color):
    count=1
    queue=deque()
    queue.append((x,y))
    visited[x][y]=True

    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<M and 0<=ny<N:
                if war[nx][ny]==color and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    count+=1
    
    return count
white=0
blue=0
for i in range(M):
    for j in range(N):
        if war[i][j]=='W' and not visited[i][j]:
            white+=bfs(i,j,'W')**2
        elif war[i][j]=='B' and not visited[i][j]:
            blue+=bfs(i,j,'B')**2
            
            
print(white,blue)                