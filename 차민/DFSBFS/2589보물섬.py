# from collections import deque

#입력받기
n,m=map(int,input().split())
graph = []

for i in range(n):
  graph.append(list(input()))

# 숫자로 바꾸기 
for i in range(n):
  for j in range(m):
    if graph[i][j] == "W":
      graph[i][j] = 0
    else:
      graph[i][j] = 1

# 공간 쪼개기
col = []
row = []
dia = []
#1. 행으로 공간 쪼개기 
def divide_row():
  for i in range(n):
    sum=0
    if graph[i][0] == 0:
      for j in range(m):
        sum += graph[i][j]
      if sum == 0:
        row.append(i)


#2.열로 공간 쪼개기
def divide_col():
  for j in range(m):
    sum = 0
    if graph[0][j] == 0:
      for i in range(n):
        sum += graph[i][j]
      if sum == 0:
          col.append(j)

#3.대각선으로 공간 쪼개기
def divide_dia():
  #왼쪽
  for j in range(1,m):
    sum = 0
    if graph[0][j]==0:
      for i in range(j+1):
        sum+=graph[i][j-i]
      if sum == 0:
        dia.append((0,j))
    
  #오른쪽
  for a in range(1,n-1):
    sum = 0
    if graph[a][m-1] == 0:
      for b in range(m-1,0,-1):
        sum+=graph[a][b]
      if sum ==0:
        dia.append((a,m-1))

divide_row()
divide_col()
divide_dia()

#L 위치를 리스트로 받기
location = []
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      location.append((i,j))

# nC2만큼 좌표를 옮겨가며 개수 세기 + 슬라이싱 이용 

        