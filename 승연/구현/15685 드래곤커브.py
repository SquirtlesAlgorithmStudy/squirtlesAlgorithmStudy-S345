#BaekJoon 15685 드래곤커브
import sys
input = sys.stdin.readline

graph = [[0]*101 for _ in range(101)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

DragonNum = int(input())

for _ in range(DragonNum):
    x, y, D, G = map(int, input().split())

    #시작점 방문처리
    graph[x][y] = 1
    move = [D]

    #규칙 : 이전 세대의 정보를 뒤집어 1 더하기. 4가 되면 다시 처음인 0으로.
    for _ in range(G):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4)
        move.extend(tmp)

    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        graph[nx][ny] = 1
        x, y = nx, ny



# 정사각형 개수 구하기
result = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            result += 1

print(result)