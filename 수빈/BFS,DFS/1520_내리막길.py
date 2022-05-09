#답은 맞는데 런타임에러

import sys
from traceback import print_tb
input = sys.stdin.readline


dx = [1,-1,0,0]  #좌/우 이동
dy = [0,0,1,-1]  #위/아래 이동


m,n = map(int, input().split())  # m이 세로
a = [list(map(int, input().split())) for _ in range(m)]
c = [[-1]*n for _ in range(m)]  #먼저 전체를 다 -1로 만들어두고

def dfs(x,y):
    if x==m-1 and y==n-1:
        return 1  #제일 오른쪽 아래에 도착하면 1을 반환
    if c[x][y] != -1:
        return c[x][y]  #이미 지나갔다면 해당 위치를 반환
    c[x][y] = 0  #반환한 위치를 0으로 만들기
    for i in range(4): #상하좌우 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <m and 0 <= ny <n:  #여기 3줄이 잘 이해 안감
            if a[nx][ny] <a[x][y]:
                c[x][y] +=dfs(nx,ny)
    return c[x][y]


# print(a)
# print(c)
print(dfs(0,0))
    