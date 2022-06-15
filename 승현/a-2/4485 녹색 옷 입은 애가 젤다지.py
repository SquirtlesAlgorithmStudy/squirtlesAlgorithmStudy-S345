from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS (x,y,graph,costs):
  queue = deque()
  queue.append((x,))
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        #무한으로 설정되어있는 costs 값보다 현위치costs+주변board값 이 더 작을 경우
        # costs 좌표에는 '거기까지의 최소값'저장
        if costs[nx][ny] > costs[x][y] + graph[nx][ny]:
          #그 길로 갔을 경우의 최소 값을 저장
          costs[nx][ny] = costs[x][y] + graph [nx][ny]
          queue.append((nx,ny))

count = 1    
while True:
  #배열 크기 입력
  n = int(input())
  if n == 0:
    break
  #배열 입력
  board = [list(map(int, input().split())) for _ in range (n)]
  #매우 큰 값으로 초기화
  costs = [[int(1e9)]*n for _ in range(n)]
  
  costs [0][0] = board[0][0]
  #시작 값의 좌표값 board, costs전달
  BFS(0,0,board,costs)
  print(f'Problem {count} : {costs[n-1][n-1]}')
  count += 1

#1. 상하좌우의 최소값-> 중간에 큰 값이 있거나 돌아가게 됨
#2. costs(1e9)를 하지 않