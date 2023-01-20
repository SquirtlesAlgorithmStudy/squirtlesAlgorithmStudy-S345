""" 
1.
(0,0)(0,1)(0,2)
(1,0)(1,1)(1,2)
(2,0)(2,1)(2,2)
=>재귀함수 dfs_x에서 dfs_x(x+1,y)가 아니라 dfs_x(x,y+1)인 이유
  행렬 좌표 조심!
 
"""
from sys import stdin
N,M=map(int,stdin.readline().rstrip().split())

floor=[]
for i in range(N):
    floor.append(list(map(str,input())))

def dfs_x(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    if floor[x][y]=='-':
        floor[x][y]=1 
        dfs_x(x,y+1)
        return True
    return False

def dfs_y(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    if floor[x][y]=='|':
        floor[x][y]=1
       
        dfs_y(x+1,y)
        return True
    return False

num_of_board=0

for i in range(N):
    for j in range(M):
        if floor[i][j]=='-':
            if dfs_x(i,j)==True:
                num_of_board+=1
        elif floor[i][j]=='|':
            if dfs_y(i,j)==True:
                num_of_board+=1




print(num_of_board)            