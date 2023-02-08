import sys 
from collections import deque 
def bfs(x,y,p):
    queue = deque()
    visited[x][y]=1
    queue.append([x,y])
    cnt=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and place[nx][ny]==p: #연속으로이동할 수있는조건:값이같다
                    cnt+=1
                    visited[nx][ny]=1
                    queue.append([nx,ny])
    return cnt
input =sys.stdin.readline
dx=[0,1,0,-1] # 동남서북
dy=[1,0,-1,0] # 동남서북
x,y = 0,0
direction = 0 # dx, dy 인덱싱, 조건에 따라 direction 값을 바꿔준다 0,1,2,3 동서남북
ans = 0
n,m,k = map(int,input().split())
place = [list(map(int,input().split())) for _ in range(n)]

dice =[1,2,3,4,5,6] # 위,북,동,서,남,아래

for _ in range(k):
    visited = [[0]*m for _ in range(n)]
    
    #벽에 부딪히는 경우 
    if not 0 <=x+dx[direction] < n or not 0<=y+dy[direction] < m:
        direction = (direction+2)%4 # 방향 반대로 바꿀 것 
    

    x= x +dx[direction]
    y= y +dy[direction]
    ans +=bfs(x,y,place[x][y])*place[x][y] # c(갯수) * b(지금 위치)
    '''
    다음 turn에 해당하는 방향전환
    '''
    #A=B
    if direction == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif direction == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif direction == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    if dice[5] > place[x][y]: #5th-index=아래
        direction = (direction + 1) % 4 #cw
    elif dice[5] < place[x][y]:
        direction = (direction + 3) % 4 #ccw
        
print(ans)