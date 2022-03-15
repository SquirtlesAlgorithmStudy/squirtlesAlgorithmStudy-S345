n,m = map(int,input().split())
graph = []
color = []

for i in range(n):
  graph.append(list(input()))

def bfs_white(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return 0
  if graph[x][y] == 'W':
    graph[x][y]=1
    color.append(graph[x][y])

    bfs_white(x-1,y)
    bfs_white(x,y-1)
    bfs_white(x+1,y)
    bfs_white(x,y+1)

  return 0


def bfs_blue(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return 0
  if graph[x][y] == 'B':
    graph[x][y]=-1
    color.append(graph[x][y])

    bfs_blue(x-1,y)
    bfs_blue(x,y-1)
    bfs_blue(x+1,y)
    bfs_blue(x,y+1)

  return 0


for i in range(n):
  for j in range(m):
    if graph[i][j] == "W":
      bfs_white(i,j)
      color.append(0)
      
    elif graph[i][j] == "B":
      bfs_blue(i,j)
      color.append(0)


length = len(color)
sum = 0
sum_white = 0
sum_blue = 0




#최대값(모든 성분이 1, -1로 교차될 때)을 range로
for k in range(length-1,-1,-1):

  if k ==0:
    sum+=color[0]

    if sum>0:
      sum_white += sum**2
    else :
      sum_blue += sum**2

    break
    
  
  if color[k] == color [k-1]:
    sum += color.pop()
  else:
    sum+=color.pop()
    if sum>0:
      sum_white += sum**2
    else :
      sum_blue += sum**2
    sum = 0    


print(sum_white, sum_blue) 