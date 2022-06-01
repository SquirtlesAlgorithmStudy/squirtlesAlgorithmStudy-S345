import sys
from collections import deque
fastin = sys.stdin.readline
# (0) Parameter
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
mapp = [[0] * 101 for _ in range(101)]
curves = deque()

# (1) Input
n = int(input())
for _ in range(n):
    curves.append(list(map(int, fastin().split())))


# (2) curves 그리기
def draw_curve():
    while curves:
        [x, y, d, g] = curves.popleft()
        mapp[x][y] = 1
        temp = [d]
        move = [d]
        for _ in range(g+1):
            for dir in move:
                x += dx[dir]
                y += dy[dir]
                mapp[x][y] = 1
            move = [(i+1) % 4 for i in temp]
            move.reverse()
            temp = temp + move


def solution():
    draw_curve()
    answer = 0
    for i in range(100):
        for j in range(100):
            if mapp[i][j] and mapp[i+1][j] and mapp[i+1][j+1] and mapp[i][j+1]:
                answer += 1
    return answer

result = solution()
print(result)
