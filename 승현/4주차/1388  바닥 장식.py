import sys
fastin = sys.stdin.readline

#dfs 함수
def recursive_row (y,x):
  #범위 밖일 경우 False 값 리턴
  if x <= -1 or x >= column or y <= -1 or y >= row:
    return False
  # 만약 - 라면 방문 처리 
  if board[y][x] == '-':
    board[y][x] = 0
    recursive_row (y,x+1)
    return True
  return False
  
def recursive_column (y,x):
  if x <= -1 or x >= column or y <= -1 or y >= row:
    return False
  #만약 | 라면 방문 처리
  elif board[y][x] == '|':
    board[y][x] = 1
    recursive_column (y+1,x)
    return True
  return False
  
#메인 함수
board = []
result = 0
row, column = map(int,fastin().split())

#바닥 장식 입력
for _ in range(row):
  board.append(list(input()))

for i in range(row):
  for j in range(column):
    if recursive_row(i,j) == True:
      result += 1
    if recursive_column(i,j) == True:
      result += 1

print(result)

'''의진님!! 궁금한게 있습니다!!
  제가 원래 한 함수 안에서 - 과 |를 구분하여 만들고 싶었는데 if문을 써서 구별을 하면 오류가 발생했습니다. 

혹시 if문이 아닌 다른 방법으로 한 함수 내에서 - 과 | 의 상태를 구분하는 방법이 있을까요?'''