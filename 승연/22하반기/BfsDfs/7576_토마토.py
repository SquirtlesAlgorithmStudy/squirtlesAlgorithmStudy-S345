# bfs
# 한단계씩 퍼져야하는거기 때문에 (깊에 들어갈 필요가 없기에) bfs

import sys
input = sys.stdin.readline
from collections import deque

col, row = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(row)]

tomato = []
notyet = []
for i in range(row):
    for j in range(col):
        if box[i][j] == 1:
            tomato.append((i, j))
        if box[i][j] == 0:
            notyet.append((i, j))
          
# 조건 만족하면 종료할 때 exit() 함수 !
if len(notyet) == 0:
    print(0)
    exit()


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    dq = deque()
    # 이렇게 해주면 왼쪽부터 탐색하기 때문에 동시 전파 구현 가능
    for a, b in tomato:
        dq.append((a, b))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                dq.append((nx, ny))

bfs()

for i in range(row):
    for j in range(col):
        if box[i][j] == 0:
            print(-1)
            exit()

# 이부분때문에 시간이 오래걸렸다. 잘못 알고 있었던 부분
# 2차원 리스트에서 max값 출력시 max(map(max, list명)) !!!
print(max(map(max, box))-1)
