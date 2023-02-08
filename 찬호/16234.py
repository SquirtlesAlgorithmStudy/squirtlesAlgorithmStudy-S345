#인구이동 

import sys
import math 
from collections import deque
input = sys.stdin.readline
dx =[1,0,-1,0]
dy =[0,1,0,-1]

n,l,r =map(int,input().split())
place = [list(map(int, input().split(' '))) for _ in range(n)]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visit[x][y] =True
    
    #연합 
    unioned =[(x,y)]
    count = place[x][y]
    
    while queue:
        xx,yy =queue.popleft()
        
        for i in range(4):
            nx =xx+dx[i]
            ny =yy+dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
        if visit[nx][ny]:
                continue
        if l<=abs(place[nx][ny]-place[nx][ny])<=r:
            unioned.append((nx,ny))
            visit[nx][ny] =True
            queue.append((nx,ny))
            count+=place[nx][ny]
    for x,y in unioned:
        place[x][y] =math.floor(count / len(unioned))
        
    return len(unioned)

ans = 0 
while True:
    visit =[[False]*n for _ in range(n)]
    
    flag = False
    
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if bfs(i,j) >1:
                    flag =True 
                    
    if not flag:
        break
    ans +=1
    
print(ans)
    