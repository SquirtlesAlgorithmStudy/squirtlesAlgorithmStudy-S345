import sys 

input =sys.stdin.readline
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def dfs(place,where):
    x,y = where
    visited[x][y] = 1 

    for 
n,m = map(int,input().split()) # n 세로길이 m 가로길이 # 최대 길이 100
place = [input().rsplit() for _ in range(n)]
visited = [[0]*m for _ in n]
 # 치즈가 모두 없어질때 까지  
hours, leftover = dfs(place,(0,0))