# pyhon3 시간초과 pypy3 통과.....
import sys
input = sys.stdin.readline
from collections import deque

row, col = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True
    while dq:
        # 이부분 그냥 pop()으로 해서 틀렸었음
        # bfs사용시 꼭 'popleft()' 사용해야 함을 명심 !
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                if graph[nx][ny] == 'L':
                    distance_graph[nx][ny] = distance_graph[x][y]+1
                    # bfs 방문처리 잊지말기
                    visited[nx][ny] = True
                    dq.append((nx, ny))
    return max(map(max, distance_graph))
# L 발견할 때마다 거리 세주는 그래프 새로, graph는 바꾸지 않음, 탐색 끝나면 max값 추출
result = []
L_list = []
for i in range(row):
    for j in range(col):
        if graph[i][j] == 'L':
            L_list.append([i, j])

for i in range(len(L_list)-1):
    j, k = L_list[i]
    distance_graph = [[0] * col for _ in range(row)]
    visited = [[False] * col for _ in range(row)]
    distance_graph[j][k] = 1
    result.append(bfs(j, k))

print(max(result)-1)