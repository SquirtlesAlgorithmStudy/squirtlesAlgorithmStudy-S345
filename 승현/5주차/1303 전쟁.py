from collections import deque
import sys
fastin = sys.stdin.readline

def bfs(y,x,color):
  q = deque()
  q.append((y,x))
  field [y][x] = 1
  cnt = 1
 
  while q:
    y, x = q.popleft()

    for i in range(4):
      nx = x + dx[i] #좌우상하
      ny = y + dy[i]
   
      if 0 <= nx < column and 0 <= ny < row :
        #방문하지 않았고, 같은 색 일경우
        if field [ny][nx] != color:
          continue
        if field[ny][nx] != 1 and field [ny][nx] == color:
          field [ny][nx] = 1
          cnt += 1
          q.append((ny,nx))
 
  return cnt
                    
    
    
    
###메인 함수
field = []
cnt, W_result, B_result = 0, 0, 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#가로, 세로 입력
column, row = map(int,fastin().split())

# field 값 입력
for _ in range(row):
  field.append(list(fastin()))

#dfs 함수 호출
for i in range(row):
  for j in range(column):
    #방문하지 않은 field만 방문
    if field[i][j] != 1:
      if field[i][j] == 'W':
        W_result += (bfs(i,j,'W') ** 2)
      elif field [i][j] == 'B':
        B_result += (bfs(i,j,'B') ** 2)

print (W_result, B_result)