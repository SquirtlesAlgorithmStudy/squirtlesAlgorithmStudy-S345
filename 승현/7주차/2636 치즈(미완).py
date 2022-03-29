#bfs를 사용:
#바깥과 접하는 부분이 하나라도 있으면 범위 처리
# 전체 수에서 테두리 수를 빼서 남은 치즈 수 저장
from collections import deque
import sys
fastin = sys.stdin.readline

def bfs(y,x):
  q = deque()
  q.append((y,x))
  
###print('bfs 내 들어간 값 확인: ', y, x)
  #ask = 주변 판단, cnt = 회차세기, 다음 주변 판단, total = 주변 테두리 수 세기
  ask, cnt= 0, 2
  
  while q:
    y, x = q.popleft()
    total = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      # 범위 밖일 경우 무시 
      if 0 > nx or nx > column or ny < 0 or ny > row or board[y][x] == 0:
        continue

      #상하좌우 중 값이 1일 경우 q에 추가 
      if  board[y][x] == 1 and board[ny][nx] == 1:
        print('append 좌표', ny, nx)
        print(*board,sep = '\n') #pprint함수를 사용할 수도 있다
        q.append((ny, nx))
      #주변이 ask일 경우 cnt으로 변경
      if  board[y][x] == 1 and board[ny][nx] == ask:
        print('값변경 좌표:', ny, nx)
        board[y][x] = cnt
        total += 1 
    cnt += 1
  #print(board)
  return cnt, total
      
          
          
          
# 판의 세로, 가로 입력
row, column = map(int,fastin().split())
print('row, column: ',row, column )
# 판내의 치즈 입력
board = [[int(x) for x in fastin().split()]for y in range(row)]
print(*board,sep = '\n') #pprint함수를 사용할 수도 있다

dy = [0,0,-1,1]
dx = [-1,1,0,0]

#bfs를 사용
for i in range(row):
  for j in range(column):
    result, total = bfs(i,j)

print(result)
print(total)