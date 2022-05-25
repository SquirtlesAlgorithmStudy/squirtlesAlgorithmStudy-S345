#15685 드래곤 커브
import sys
input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split()))for _ in range(n)]
b = [[[0]*100]*100]
#한 세대 당 움직임 저장
move=[]
#전체 = 초기 + reverse(move)
drr = []
cnt = 0
#0 오/1 위/2 좌/3 아래
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

#x,y,d,g

#세대 수 만큼 돌려야함
for i in range(n):
  x, y, d, g = array[i]
  #시작방향을 drr에 저장
  drr.append(d)
  
  print ("array :",x,y,d,g)
  print ("drr: ",drr)
  
  for j in range(g):
      move[j].append(list(reversed(drr)))
      print(move)
      for k in move:
        if (move[k]+1) == 4:
            drr.append(0)
        else:
            drr.append(move[k+1])

for i in range(n):
    x, y, d, g = array[i]
    b[y][x] = 1
    for _ in range(drr):
        nx = x + dx[d]
        ny = y + dy[d]
        b[ny][nx] = 1
  

for i in range(100):
  for j in range(100):
    if b[i][j] == 1 & b[i+1][j] == 1 & b[i+1][j+1] == 1 & b[i][j+1] == 1:
      cnt += 1

print (cnt)
