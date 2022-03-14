# DFS로 풀어보기
import sys
fastin = sys.stdin.readline

# 가로 N, 세로 M
N, M = map(int, fastin().rstrip().split())

color = []
for i in range(M):
    color.append(list(map(str, fastin().rstrip())))
# print(color)

sumW = 0
sumB = 0
countW = 0
countB = 0

def dfsW(m, n):
    global countW
    if n <= -1 or n >= N or m <= -1 or m >= M:
        return 0
    if color[m][n] == 'W':
        color[m][n] = '0'
        countW += 1
        dfsW(m - 1, n)
        dfsW(m, n - 1)
        dfsW(m + 1, n)
        dfsW(m, n + 1)
        return countW

def dfsB(m, n):
    global countB
    if n <= -1 or n >= N or m <= -1 or m >= M:
        return 0
    if color[m][n] == 'B':
        color[m][n] = '0'
        countB += 1
        dfsB(m - 1, n)
        dfsB(m, n - 1)
        dfsB(m + 1, n)
        dfsB(m, n + 1)
        return countB

for m in range(M):
    for n in range(N):
        if color[m][n] == 'W':
            countW = dfsW(m, n)
            sumW += (countW * countW)
            countW = 0
        elif color[m][n] == 'B':
            countB = dfsB(m, n)
            sumB += (countB * countB)
            countB = 0

print(sumW, sumB)