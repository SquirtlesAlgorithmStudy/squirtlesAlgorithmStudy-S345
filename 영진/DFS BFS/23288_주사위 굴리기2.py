from sys import stdin
from collections import deque
N,M,K=map(int,input().split())
board=[]
for _ in range(N):
    board.append(list(map(int,input().split())))
visited=[[0]*(M+1) for _ in range(N+1)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

dice=[0,0,0,0,0,0,0]
def roll(c):
    if c == 1:#동
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif c == 2:#서
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif c == 3:#북
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif c == 4:#남
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    visited[y][x]=1
    while queue:
       x,y=queue.popleft()
       for i in range(4):
           nx=x+dx[i]
           ny=y+dy[i]
           if 0<=nx<M and 0<=ny<N and not visited[ny][nx]:
               visited[ny][nx]=visited[y][x]+1
               queue.append((nx,ny))

sum=0
while 1:
    