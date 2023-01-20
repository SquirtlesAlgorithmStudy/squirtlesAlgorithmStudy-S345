from sys import stdin
import sys
sys.setrecursionlimit(10**9) ##재귀함수 사용시 깊이 제한을 걸어주는 함수
T=int(input())

def dfs(x,y):
    if x<=-1 or x>=M or y<=-1 or y>=N:
        return 
    if field[x][y]==0:
        return 
    
    field[x][y]=0
    
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)

for _ in range(T):
    N,M,K=map(int,stdin.readline().rstrip().split())
    field=[[0]*(N) for _ in range(M)]
    num_of_warm=0
    for _ in range(K):
        X,Y=map(int, stdin.readline().rstrip().split())
        field[Y][X]=1
    for i in range(M):
        for j in range(N):
            if field[i][j]==1:
                dfs(i,j)
                num_of_warm+=1
    
    print(num_of_warm)



