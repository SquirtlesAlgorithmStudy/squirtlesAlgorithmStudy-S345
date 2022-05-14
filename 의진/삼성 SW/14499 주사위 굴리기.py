import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
diceFront = 1
dice = [0] * 7
diceIndex = [1, 4, 3, 5, 2, 6]


def moveDice(command):
    if command == 1:
        temp = diceIndex[0]
        diceIndex[0] = diceIndex[1]
        diceIndex[1] = diceIndex[5]
        diceIndex[5] = diceIndex[2]
        diceIndex[2] = temp

    elif command == 2:
        temp = diceIndex[0]
        diceIndex[0] = diceIndex[2]
        diceIndex[2] = diceIndex[5]
        diceIndex[5] = diceIndex[1]
        diceIndex[1] = temp

    elif command == 3:
        temp = diceIndex[0]
        diceIndex[0] = diceIndex[3]
        diceIndex[3] = diceIndex[5]
        diceIndex[5] = diceIndex[4]
        diceIndex[4] = temp

    elif command == 4:
        temp = diceIndex[0]
        diceIndex[0] = diceIndex[4]
        diceIndex[4] = diceIndex[5]
        diceIndex[5] = diceIndex[3]
        diceIndex[3] = temp


# 각 주사위 Index에서 동서북남 순
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for command in commands:
    nx = x + dx[command-1]
    ny = y + dy[command-1]
    if 0 <= nx < N and 0 <= ny < M:
        x = nx
        y = ny
    else:
        continue

    moveDice(command)
    diceFront = diceIndex[0]
    diceGround = 7 - diceFront
    if board[x][y] == 0:
        board[x][y] = dice[diceGround]
    else:
        dice[diceGround] = board[x][y]
        board[x][y] = 0
    print(dice[diceFront])
