# https://www.acmicpc.net/problem/2667
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))
# strip : \n 문자열 제거

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    count = 0
    q.append((x, y))
    while q:
        px, py = q.popleft()
        if graph[px][py] == 1:
            graph[px][py] = 0  # 탐색중인 위치를 0으로 바꾸어서 다시 방문하지 않도록 한다
            count += 1
            for i in range(4):
                nx = px + dx[i]
                ny = py + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    q.append((nx, ny))
    return count


result = 0
house = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            house.append(bfs(i, j))
            result += 1
house.sort()
print(len(house))
for i in range(len(house)):
    print(house[i])
