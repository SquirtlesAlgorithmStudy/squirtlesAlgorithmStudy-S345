import sys
sys.setrecursionlimit(10**6)
fastin = sys.stdin.readline

def dfs (y,x):
  if y <= -1 or y >= row or x <= -1 or x >= column:
    return False

  if field[y][x] == 1:
    field[y][x] = 3
    dfs(y,x-1)
    dfs(y,x+1)
    dfs(y-1,x)
    dfs(y+1,x)
    return True
  return False

test = int(fastin())

for i in range(test):
  
  column, row, cnt = map(int,fastin().split())
  
  # 모든 값이 0인 리스트 생성
  # 리스트 컴프리핸션
  field = [[0]*column for _ in range(row)]

  for _ in range(cnt):
    # 입력된 좌표값 1로 변경
    x, y = map(int,fastin().split())
    field[y][x] = 1 
  
  x = 0
  y = 0
  result = 0
    
  for y in range(row):
    for x in range(column):
      if dfs(y,x) == True:
        result += 1
  print(result)