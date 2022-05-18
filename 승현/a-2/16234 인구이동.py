#16234 인구이동
from collections import deque
import sys
input = sys.stdin.readline

def BFS(x, y):
  temp = []
  queue = deque()
  queue.append((0,0))
  temp.append([x,y])

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < line and 0 <= ny < line and visit[nx][ny] == 0:
        if under <= abs(s[nx][ny] - s[x][y]) <= over:
          visit[nx][ny] = 1
          queue.append([nx,ny])
          temp.append([nx,ny])
  return temp
  
##Main##
#칸 수, 최소값, 최댓값
line, under, over = map(int, input().split())
s = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
s = [list(map(int, input()))for _ in range(line)]
cnt = 0
while True:
  visit = [[0] * line for i in range(line)]
  isTrue = False
  for i in range(line):
    for j in range(line):
      if visit[i][j] == 0:
        visit[i][j] = 1
        temp = BFS(i,j)
        if len(temp) > 1:
          isTrue = True
          num = sum([s[x][y]for x,y in temp]) //len(temp)
          for x, y in temp:
            s[x][y] = num
  if not isTrue:
    break
  cnt += 1
print(cnt)

#https://pacific-ocean.tistory.com/375