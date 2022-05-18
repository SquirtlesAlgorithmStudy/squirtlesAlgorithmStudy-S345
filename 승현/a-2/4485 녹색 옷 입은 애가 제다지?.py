import sys, heapq
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while (1):
  n = int(input())
  if n == 0:
    break
  board = [list(map(int, input().split())) for _ in range (n)]
  #방문처리
  visited = [[False]*n for _ in range(n)]
  #시작 값의 가중치, 좌표값 추가
  queue = [[arr[0][0],0,0]]

  while queue:
    w,x,y = heapq.heappop(queue)
    for  
      if 0 <=  < n and 0 <= ny < n and not visited[nx][ny]:
        if min > board