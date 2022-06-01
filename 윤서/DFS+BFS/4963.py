# 섬의 개수

# 왜 틀렸는지 모르겠다~~

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)                          # RecursionError 방지

dx = [-1, 0, 1, 0, 1, 1, -1, -1]                        # 상하좌우, 대각선까지 이동 가능하므로 이동 x, y 배열에 저장
dy = [0, 1, 0, -1, -1, 1, -1, 1]

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:              # 인덱스 범위를 벗어나는 경우 False, x가 m(세로)를 기준으로 하는 이유는 [x][y]인덱스로 배열 접근할 때 x가 세로 의미
        return False
    if graph[x][y] == 1:                                # 땅이면
        graph[x][y] = 0                                 # 확인했다는 의미로 0으로 바꾸고
        for i in range(8):                              # 상하좌우, 대각선 확인
            dfs(x + dx[i], y + dy[i])
        return True                                     # True반환
    return False                                        # 땅이 아니었다면 False반환

while True:
    n, m = map(int, input().rstrip().split())           # n = 가로, m = 세로

    if n == 0 and m == 0:                               # 0 0 종료조건
        break

    graph = []
    count = 0

    for i in range(m):
        graph.append(list(map(int, input().rstrip().split())))
    
    for i in range(m):
        for j in range(n):
            if dfs(j, i) == True:                       # True라면 섬 하나 존재
                count += 1
    
    print(count)