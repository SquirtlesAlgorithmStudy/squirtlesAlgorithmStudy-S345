from collections import deque
from sys import stdin
N,L,R=map(int,input().split())

world=[]
for _ in range(N):
    world.append(list(map(int,input().split())))
    
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    union=[] 
    queue.append((x,y))
    union.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if L<=abs(world[nx][ny]-world[x][y])<=R:
                    visited[nx][ny]=1
                    queue.append((nx,ny))
                    union.append((nx,ny))
    return union

num_of_days=0
while True:
    visited=[[0]*(N+1) for _ in range(N+1)] #인덱스 직관적으로 표현
    united=False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j]=1
                country=bfs(i,j)
                if len(country)>1:
                    united=True
                    number=sum([world[x][y] for x,y in country])//len(country)
                    for x,y in country:
                        world[x][y]=number
    if united==False:
        break
    num_of_days+=1
print(num_of_days)                       