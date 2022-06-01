import sys
input = sys.stdin.readline

n = int(input())
dragonCurves = [list(map(int, input().split())) for _ in range(n)]
board = [[0] * 101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def generateDragonCurve(dragonCurve):
    x = dragonCurve[0]
    y = dragonCurve[1]
    board[y][x] = 1

    nowDirection = dragonCurve[2]
    directionsAccumulate = [nowDirection]
    direction = [dx[nowDirection], dy[nowDirection]]
    x = x + direction[0]
    y = y + direction[1]

    board[y][x] = 1

    if dragonCurve[3] > 0:
        for i in range(dragonCurve[3]):
            directions = []
            length = len(directionsAccumulate)
            for j in range(length):
                element = (directionsAccumulate[length - 1 - j] + 1) % 4
                directions.append(element)
                directionsAccumulate.append(element)
            for j in range(2 ** i):
                direction = [dx[directions[j]], dy[directions[j]]]
                x = x + direction[0]
                y = y + direction[1]
                board[y][x] = 1


def findSquare():
    count = 0
    for x in range(100):
        for y in range(100):
            if board[y][x] == 1:
                if board[y+1][x] >= 1 and board[y][x+1] >= 1 and board[y+1][x+1] >= 1:
                    count += 1
    return count


for dragonCurve in dragonCurves:
    generateDragonCurve(dragonCurve)
print(findSquare())
