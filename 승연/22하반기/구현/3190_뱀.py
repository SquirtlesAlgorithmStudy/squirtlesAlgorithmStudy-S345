import sys
input = sys.stdin.readline
from collections import deque

maplen = int(input())
apples = int(input())
apple_list = [list(map(int, input().split())) for _ in range(apples)]
moves = int(input())

map = [[0]*(maplen + 2) for _ in range(maplen + 2)]
# 사과 있는 곳 2로 변경
for r, c in apple_list:
    map[r][c] = 2

# 벽 1로 변경
for i in range(maplen + 2):
    map[0][i] = 1
    map[maplen + 1][i] = 1
    map[i][0] = 1
    map[i][maplen + 1] = 1

# key : 방향 틀 순간(Time) value : 틀 방향(L/D)
move_dict = {}
for i in range(moves):
    a, b = input().split()
    move_dict[int(a)] = b
turn_times = list(move_dict.keys())

time = 0
# direction : 0상 1하 2좌 3우
direction = 3
snake = deque([(1, 1)])
map[1][1] = 1
# dx[0] dy[0] : 상
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 인덱스 : 현재 방향 / 좌, 우 : 0, 1 인덱스
change_direction = [[2, 3], [3, 2], [1, 0], [0, 1]]
while True:
    # 방향 바꿔야할 타임이면 direction 값 바꿔주기
    if time in turn_times:
        if move_dict[time] == 'L':
            direction = change_direction[direction][0]
        elif move_dict[time] == 'D':
            direction = change_direction[direction][1]

    x, y = snake.pop()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 벽이나 몸통 만나면 종료
    if map[nx][ny] == 1:
        time += 1
        break
    # 사과 먹고 길이 신장 (머리 추가)
    elif map[nx][ny] == 2:
        snake.append((x, y))
        snake.append((nx, ny))
        map[nx][ny] = 1
        time += 1
    # 사과 안먹고 그냥 이동 (머리 하나 추가, 꼬리 하나 제거)
    elif map[nx][ny] == 0:
        snake.append((x, y))
        snake.append((nx, ny))
        map[nx][ny] = 1
        del_x, del_y = snake.popleft()
        map[del_x][del_y] = 0
        time += 1


print(time)