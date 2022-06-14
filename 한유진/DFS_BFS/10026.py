from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(y, x, check):
    q = deque()
    q.append((y, x))
    c = array[y][x]
    visited[y][x] = True
    while q:
        py, px = q.popleft()
        for index in range(4):
            nx = px + dx[index]
            ny = py + dy[index]
            if nx >= n or nx < 0 or ny >= n or ny < 0:
                continue
            if check == 1 and ((c == 'G' or c == 'R') and (array[ny][nx] == "G" or array[ny][nx] == "R")):
                c = array[ny][nx]
            # check를 통해 적록색약인 사람이면 지금 기준점(check)이 R or G 이고 다음 탐색할 곳이 R or G이면 기준점(check)를 변경해줌
            if c == array[ny][nx] and visited[ny][nx] == False:
                visited[ny][nx] = True
                q.append((ny, nx))


# 입력 받음
n = int(input())
array = []
for _ in range(n):
    array.append(list(input().strip()))

area = []
for c in range(0, 2):  # 적록색약이 아닌 경우와 적록색약인 경우
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = 0
    for i in range(n):  # 높이
        for j in range(n):  # 너비
            if visited[i][j] == False:
                bfs(i, j, c)
                result += 1
    area.append(result)

print(str(area[0]) + " " + str(area[1]))
