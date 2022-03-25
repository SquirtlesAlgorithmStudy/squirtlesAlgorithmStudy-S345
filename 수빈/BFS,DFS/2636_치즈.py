import sys
input = sys.stdin.readline
from collections import deque

sero, garo = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(sero)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []

def BFS():
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    cnt = 0
    # while문이 한 번 반복될 때마다 1시간 지남
    while q:
        x,y = q.popleft()
        print('x, y ', x, y)
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            print('nx, ny ', nx,ny)
            if 0<=nx<sero and 0<=ny<garo and visited[nx][ny]==0:
                if graph[nx][ny] ==0:
                    visited[nx][ny] = 1
                    #치즈가 아닌 부분만 q에 넣어주고
                    #가장자리를 체크해 줌
                    q.append([nx,ny])
                    print('q 출력', q)
                elif graph[nx][ny] ==1:
                    ## 가장자리 부분만 처리해주기 때문에, 공기와 점촉한 칸은 q에 넣어주지 않음
                    ## 넣게되면, 안쪽 치즈까지 녹음 처리되기 때문
                    graph[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt +=1
    ans.append(cnt)
    return cnt

t=0   # 모두 사라지는데 걸린 시간
while 1:
    t +=1
    visited = [[0]*garo for _ in range(sero)]
    cnt = BFS()
    if cnt ==0:
        break
    
print(t-1)
print(ans[-2])