# #https://www.acmicpc.net/problem/4963
# #런타임 오류 - dfs로 풀면 런타임 오류가 나는 것 같다!
import sys
input = sys.stdin.readline
#파이썬은 재귀 깊이가 정해져있음
sys.setrecursionlimit(10000000)
def dfs(y, x):
    
    if x < 0 or x >= w or y < 0 or y >= h:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 2
        # 상하좌우 탐색
        dfs(y,x-1)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y+1,x)
        # 대각선 탐색
        dfs(y-1,x-1)
        dfs(y-1,x+1)
        dfs(y+1,x-1)
        dfs(y+1,x+1)
        return True   
    return False

while True:
    w,h = map(int, input().split())
    if w == 0 or h == 0:
        break
    result = 0
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if dfs(i , j) == True:
                result += 1
    print(result)

# from collections import deque
# import sys
# read = sys.stdin.readline
# def bfs(x, y):
#     dx = [-1,-1,-1,0,0,1,1,1]
#     dy = [0,-1,1,-1,1,0,-1,1]
#     graph[x][y] = 0
#     q = deque()
#     q.append([x,y])
#     while q :
#         px,py = q.popleft()
#         for i in range(8):
#             nx = px + dx[i]
#             ny = py + dy[i]
#             #x, y 부분 범위를 잘 생각하지 못했다! - 계속 런타임이 났음
#             if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
#                 graph[nx][ny] = 0 #방문처리
#                 q.append([nx,ny]) # 큐에 집어넣기

# while True:
#     w, h = map(int, read().split())
#     if w == 0 and h == 0:
#         break
#     graph = []
#     result = 0
#     for _ in range(h):
#         graph.append(list(map(int, read().split())))
#     for i in range(h):
#         for j in range(w):
#             if graph[i][j] == 1:
#                 bfs(i,j)
#                 result += 1
#     print(result)