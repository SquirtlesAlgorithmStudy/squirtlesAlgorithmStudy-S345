import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))


d = [(1,0),(-1,0),(0,-1),(0,1)]

def bfs(x,y,cnt):
    max_ = -1
    queue= deque()
    queue.append((x,y,cnt))
    visited[x][y] = 1
    while queue:
        x,y,cur_cnt = queue.popleft()
        if max_ < cur_cnt:
            max_ = cur_cnt
        for dx,dy in d:
            nx = x + dx
            ny = y + dy
            if 0<= nx < n and 0<=ny<m and graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                queue.append((nx,ny,cur_cnt+1))
                visited[nx][ny] = 1

    return max_

Max = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            visited = [[0] * (m) for _ in range(n)]
            Max = max(Max,bfs(i,j,0))
print(Max)

#54782424	grvty0717	 2589	맞았습니다!!	122292	772	PyPy3 / 수정	861	24초 전