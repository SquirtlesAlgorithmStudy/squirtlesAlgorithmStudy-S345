n = int(input())

dx = [1,0,-1,0]
dy = [0,-1,0,1]


cordinate = [[0]*101 for _ in range(101)]

#정사각형 꼭짓점을 1해주기 
for _ in range(n):
  x,y,d,g = map(int,input().split())
  cordinate[x][y] = 1

  move = [d]

  for _ in range(g):
    update = []
    for i in range(len(move)):
      update.append((move[-i-1]+1)%4)

      
    move.extend(update)

  for i in move:
    nx = x+dx[i]
    ny = y+dy[i]
    cordinate[nx][ny] = 1
    x = nx
    y= ny


# 커브 일부 정사각형 구하기
  result = 0
  for i in range(100):
    for j in range(100):
      if cordinate[i][j] and cordinate[i + 1][j] and cordinate[i][j + 1] and cordinate[i + 1][j + 1]:
              result += 1

print(result)