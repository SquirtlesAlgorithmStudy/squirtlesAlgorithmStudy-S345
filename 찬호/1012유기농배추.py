import sys 
from collections import deque
input = sys.stdin.readlines
T = map(int,input())


#인접 : 상화좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것 

#1: 배추가 심어져 있는 땅 , otherwise 0
# K 줄에는 배추의 위치 X,Y 가 주어진다. 두 배추의 위치가 같은 경우는 없다 
ans = []

def is_close(pos,cabbage):
   x,y = pos 
   if cabbage[x+1][y] or cabbage[x-1][y] or cabbage[x][y+1] or cabbage[x][y-1] is 1:
      return True 
   else :return False 
def BFS(visited,i,graph):
   count = 0 
   queue = deque([i])
   
   while queue:
      n = queue.popleft()
      if n not in visited:
             visited.append(n)
   
       
#idea : BFS를 통해서 문제를 해결해보자-> 왜냐면 인근에 
while T:
   M, N, K = map(int,input().split())
   visited = [[0]*M for _ in range(N)] 
   cabbage = [[0]*M for _ in range(N)] 
   for _ in range(K):
      xx, yy = input().split()
      cabbage[xx][yy] = 1 
   
   answer = BFS(visited,1,cabbage)
 