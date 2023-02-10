from collections import deque
vertical,horizon=map(int,input().split())
treasure=[list(input()) for _ in range(vertical)]
visited=[[0]*horizon for _ in range(vertical)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y,cnt):
    max_=-1
    queue=deque()
    queue.append((x,y,cnt))
    visited[x][y]=1

    while queue:
        x,y,current_count=queue.popleft()
        
        if max_<current_count:
            max_=current_count 
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<vertical and 0<=ny<horizon and treasure[nx][ny]=='L'and visited[nx][ny]==0:
                queue.append((nx,ny,current_count+1))
                visited[nx][ny]=1
    return max_

Max=-1
for  i in range(vertical):
    for j in  range(horizon):
        if treasure[i][j]=='L':
            visited=[[0]*(horizon) for _ in  range(vertical)]
            Max=max(Max,bfs(i,j,0))

print(Max)


"""
1.max():인자 안의 값 중 가장 큰 값을 출력
"""