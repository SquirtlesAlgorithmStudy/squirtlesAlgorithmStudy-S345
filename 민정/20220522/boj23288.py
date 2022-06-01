import sys
from collections import deque
fastin = sys.stdin.readline
'''
세로 n: 2 <= n <= 20
가로 m: 2 <= m <= 20
이동 횟수 k: 1 <= k <= 1000
주사위 초기 위치 좌표는 (1, 1) = maps[0][0]
'''
# (0) Input
# 동 > 남 > 서 > 북 (시계방향 Defaul)
# 동: 0, 남: 1, 서: 2, 북: 3
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
n, m, k = map(int, fastin().split())
maps = [list(map(int, fastin().split())) for _ in range(n)]
# 주사위 각 면 원소는 1 ~ 6
dice = [i for i in range(7)]


# (1) 현재 칸에서 이동 가능한 칸 수 확인
def bfs(sy, sx):
    visited = [[False] * m for _ in range(n)]
    q = deque()

    q.append([sy, sx])
    visited[sy][sx] = True
    cnt_maps = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and maps[ny][nx] == maps[y][x]:
                    cnt_maps += 1
                    visited[ny][nx] = True
                    q.append([ny, nx])
    return cnt_maps


# (2) 회전 방향 결정
def rotate_decision(dir, A, B):
    if A > B:
        dir = (dir + 1) % 4
    elif A < B:
        dir = (dir + 3) % 4

    return dir


# (3) 주사위 굴리기 함수 (주사위 굴리기 1 참고)
def roll_dice(dir):
    if dir == 0:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif dir == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif dir == 1:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif dir == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


# (4) Simulation
def move_dice():
    # 이동 횟수 체크. 0이면 dir=0 상태에서 시작
    x, y = 0, 0
    cnt = 0
    dir = 0
    ans = 0
    while cnt < k:
        if cnt > 0:  # cnt = 0일 때
            # (1) A, B 비교해 dir 결정; rotate_decision()
            dir = rotate_decision(dir, dice[6], maps[y][x])

        if y + dy[dir] < 0 or y + dy[dir] >= n or x + dx[dir] < 0 or x + dx[dir] >= m:
            dir = (dir + 2) % 4

        y += dy[dir]
        x += dx[dir]

        roll_dice(dir)
        ans += (bfs(y, x) + 1) * maps[y][x]
        cnt += 1
    print(ans)

move_dice()