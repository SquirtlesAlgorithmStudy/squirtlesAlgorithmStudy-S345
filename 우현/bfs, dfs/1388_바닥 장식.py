n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(input()))

def dfs_1(x,y):
  if x<= -1 or x>=n or y <= -1 or y >= m:
    return False
  if graph[x][y] == '-':
    graph[x][y] = 'check_x'
    dfs_1(x,y-1)
    dfs_1(x,y+1)
    return True
  return False

def dfs_2(x,y):
  if x<= -1 or x>=n or y <= -1 or y >= m:
    return False
  if graph[x][y] == '|':
    graph[x][y] = 'check_y'
    dfs_2(x-1,y)
    dfs_2(x+1,y)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    # DFS는 한번 수행되면 해당 노드와 연결된 모든 노드들 방문 처리
    # 시작점 노드가 방문처리가 되었다면(처음 방문하는 것이라면) 그때만  RESULT 값 증가
    if dfs_1(i,j) == True:
      result += 1
    elif dfs_2(i,j) == True:
      result += 1

print(result)