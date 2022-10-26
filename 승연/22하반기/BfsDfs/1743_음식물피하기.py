# 음식물 피하기

# 음식물 표시, 인접한 것끼리 묶어서 한덩이로 세주기, 마지막 max값 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
row, col, n = map(int, input().split())
graph = [[-1]*(col+1) for _ in range(row+1)]
# 음쓰 있는 부분 방문처리
visited = [[False]*(col+1) for _ in range(row+1)]
food_trash = [list(map(int, input().split())) for _ in range(n)]

# 음쓰 있는 부분 1
for x, y in food_trash:
    graph[x][y] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maximum = -1e9
def dfs(x, y):
    global count, maximum
    # 음쓰인 부분 방문처리, count올려서 음쓰 크기 세어줌
    visited[x][y] = True
    count += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 1 <= nx <= row and 1 <= ny <= col and not visited[nx][ny]:
            if graph[nx][ny] == 1:
                # 방문한 적 없고 음쓰가 있는 칸이면
                dfs(nx, ny) # 재귀 호출 (방문처리, 음쓰 크기 1 증가)
    # 한 영역 탐색 끝나면 (음쓰 인접한 영역 크기 측정 끝나면) 가장 큰 음쓰 크기로 maximum 갱신
    maximum = max(maximum, count)

answer = []
for i in range(1, row+1):
    for j in range(1, col+1):
        if graph[i][j] == 1 and not visited[i][j]:
            # 음쓰 있는 칸인데 아직 방문 안했으면
            count = 0
            dfs(i, j)
print(maximum)