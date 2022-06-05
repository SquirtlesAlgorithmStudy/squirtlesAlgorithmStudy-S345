#14500 테트로미노
import heapq
import sys
input = sys.stdin.readline

#세로 n, 가로 m
n, m = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


#dijkstra 함수
def dijkstra(b[i][j],i,j):
  # 거리 -1으로 초기화 (최대값이 나오면 갱신)
  d = [[[-1]*n]*m]
  d[i][j] = 0
  #최대힙을 사용
  q = []
  #q에 가중치,좌표값 추가
  heapq.heappush(-q,(b[i][j],i,j))
  cnt = 1

  #cnt가 5일동안
  while cnt < 5:
    w, y, x = heapq.heappop(-q)
    print ("w,x,y",w,x,y)
    for t in range (4):
      nx = x + dx[t]
      ny = y + dy[t]

      # 범위 내에 있으면서 최대값이 커지면 갱신
      if 0 <= nx < m and 0 <= ny <= n:
        if d[ny][nx] < b[y][x]+b[ny][nx]:
          d[ny][nx] = b[y][x]+b[ny][nx]
        heapq.heappush(-q,(b[nx][ny],nx,ny))
        
  

# 시작 좌표값 전달
for i in range(n):
  for j in range(m):
    dijkstra(b[i][j],i,j)
