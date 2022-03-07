import sys
sys.setrecursionlimit(10**8) # 재귀 깊이 재설정

def dfs(x,y):
  if x<= -1 or x>= m or y <= -1 or y >= n:
    return False
  if bat[x][y] == 1:
    bat[x][y] = 3 # 방문처리
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

t = int(input())
for _ in range(t):
  m, n, k = map(int, input().split())
  bat = [[0]*n for i in range(m)]
  cnt = 0
  
  for _ in range(k):
    i, j = map(int,input().split())
    bat[i][j] = 1
  for i in range(m):
    for j in range(n):
      if dfs(i,j) == True:
        cnt += 1

  print(cnt)

# 코렙에서는 코드 확인 => 백준에서 돌려보니 런 타임 에러
# 재귀 깊이 재설정