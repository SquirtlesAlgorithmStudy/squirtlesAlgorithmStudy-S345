import sys 
from collections import deque
input =sys.stdin.readline
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(where):
    q = deque([])


    visited[x][y] = 1 
    q.append((x,y))
    if sum(place) ==0:
        return hours,leftover
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<nx<n and 0<ny<m and not visited[nx][ny]:
                visited[nx][ny] = 1 #방문 처리 
                if place[nx][ny] == 0: # 가장자리 라면
                    place[x][y] = 0  
                    hours +=1 

hours = 0 
leftover = 0 
n ,m = map(int,input().split()) # n 세로길이 m 가로길이 # 최대 길이 100
place = [input().rsplit() for _ in range(n)]
visited = [[0]*m for _ in n]
 # 치즈가 모두 없어질때 까지  
hours, leftover = bfs((n/2,m/2))