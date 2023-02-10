import sys 
from collections import deque
input = sys.stdin.readline
T = map(int,input())
#인접 : 상화좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것 

#1: 배추가 심어져 있는 땅 , otherwise 0
# K 줄에는 배추의 위치 X,Y 가 주어진다. 두 배추의 위치가 같은 경우는 없다 
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(i,j,graph):
   queue = deque([(i,j)])
   graph[i][j] = 0 # 0 으로 처리하지 않으면 빙글빙글 돌 수 도 있다.
   while queue:
      pos = queue.pop(0)
      x,y = pos 
      for i in range(4):
         nx = x+dx[i]
         ny = y+dy[i]
         if nx < 0 or nx>=M or ny < 0 or ny >=N:
            continue
         if graph[nx][ny] ==1:
            queue.append((nx,ny))
            graph[nx][ny] = 0 
      
           
      
       
#idea : BFS를 통해서 문제를 해결해보자-> 왜냐면 인근에 
while T:
   
   M, N, K = map(int,input().split())
   cabbage = [[0]*M for _ in range(N)]
   visited = [[0]*M for _ in range(N)]
   count = 0
   
   for _ in range(K):
      xx, yy = map(int,input().split())
      cabbage[xx][yy] = 1 
      
   for x in range(N):
      for y in range(M):
         if cabbage[x][y] == 1 and visited[x][y] == 0 :
            BFS(x,y,cabbage)
            count +=1
            
   T = T -1 
   print(count)
 