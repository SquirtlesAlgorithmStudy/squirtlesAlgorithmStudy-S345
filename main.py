def dfs_row(x,y):
  if y>=m:
    return False

  if graph[x][y]== '-':
    graph[x][y] = 'c'
    dfs_row(x,y+1)
    return True
  return False


def dfs_col(x,y):
  if x>=n:
    return False
  if graph[x][y] =='|':
    graph[x][y] = 'c'
    dfs_col(x+1,y)
    return True
  return False


n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(input()))


result = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == '-':
      if dfs_row(i,j) == True:
        result+=1

    elif graph[i][j] =='|':
      if dfs_col(i,j) ==True:
        result +=1



print(result)

               