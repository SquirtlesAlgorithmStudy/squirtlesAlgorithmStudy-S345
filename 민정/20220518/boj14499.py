import sys
fastin = sys.stdin.readline
# 동: 1 / 서: 2 / 북: 3 / 남: 4
# 세로 n, 가로 m
# 1 ≤ n ≤ 20, 1 ≤ m ≤ 20
# 0 ≤ x ≤ n-1, 0 ≤ y ≤ m-1
# 1 ≤ k ≤ 1000
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

# (1) Input
n, m, y, x, k = map(int, fastin().split())
maps = [list(map(int, fastin().split())) for _ in range(n)]
cmd = list(map(int, fastin().split()))
dice = [0] * 6


# (2) Function; Roll dice
def move_dice(dir):
    if dir == 1:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
    elif dir == 2:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif dir == 4:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
# 원래 방향이 [0, 1, 2, 3, 4, 5] 라면
# 동: [0, 2, 4, 1, 3, 5]
# 서: [0, 3, 1, 4, 2, 5]
# 북: [4, 0, 2, 3, 5, 1]
# 남: [1, 5, 2, 3, 0, 4]


# (3) Simulation
for i in cmd:
    # print('cmd:', i, '| maps[x][y] =', maps[y][x])
    # print()
    # ny = y + dy[i]
    # nx = x + dx[i]

    if y + dy[i] < 0 or y + dy[i] >= n or x + dx[i] < 0 or x + dx[i] >= m:
        continue
    else:
        x += dx[i]
        y += dy[i]
        move_dice(i)    # 주사위 함수
        if maps[y][x] != 0:
            dice[2] = maps[y][x]
            maps[y][x] = 0
        else:
            maps[y][x] = dice[2]
        # x, y = nx, ny
        print(dice[0])
