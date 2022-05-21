# Pypy3 으로 채점
# ㅗ 모양 제외 dfs 혹은 bfs로 되기 떄문에 ㅗ모양 체크하는 함수만 작성
import sys
# 상, 하, 좌, 우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# (0) Input
fastin = sys.stdin.readline
n, m = map(int, fastin().split())
tetromino = [list(map(int, fastin().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
# 최대값 저장 변수
maxValue = 0

# (1) ㅗ 제외 dfs
def dfs(x, y, dsum, cnt):   # ㅗ 제외 dfs
    global maxValue
    # cnt == 4, 즉 모양 완성되면 최대값 계산
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return
    # 상, 하, 좌, 우 이동
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, dsum + tetromino[nx][ny], cnt + 1)
            visited[nx][ny] = False


# (2) ㅗ 모양 함수
def excep(x, y):
    global maxValue
    for d in range(4):
        # 초기값 = 시작지점의 값
        tmp = tetromino[x][y]
        for k in range(3):
            # move배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 0-1-2, 1-2-3, 2-3-0, 3-0-1
            t = (d + k)%4
            nx = x + dx[t]
            ny = y + dy[t]
          
            if not (0<=nx<n and 0<=ny<m):
                tmp = 0
                break
            tmp += tetromino[nx][ny]
        maxValue = max(maxValue, tmp)


# (4) Simulation
for i in range(n):
    for j in range(m):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, tetromino[i][j], 1)
        visited[i][j] = False
        excep(i, j)

print(maxValue)