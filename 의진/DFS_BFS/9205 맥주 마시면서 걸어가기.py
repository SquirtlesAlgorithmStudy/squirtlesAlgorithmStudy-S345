from collections import deque
import sys
fastin = sys.stdin.readline
t = int(fastin())

def testcasein(t):
  n = int(fastin())
  home = tuple(map(int, fastin().strip().split()))
  cu = []
  for _ in range(n):
     cu.append(tuple(map(int, fastin().strip().split())))
  festival = tuple(map(int, fastin().strip().split()))

  return (n, home, cu, festival)

def dis(p, q):
  return abs(p[0] - q[0]) + abs(p[1] - q[1])

def distancetoCU(home, cu, festival):
  pos = []
  pos.append(home)
  pos += [i for i in cu]
  pos.append(festival)
  graph = [[] for _ in range(len(cu) + 2)]
  for i in range(len(cu) + 2):
    for j in range(len(cu)+ 2):
      graph[i].append(dis(pos[i], pos[j]))

  return graph

def bfs(node, graph):
  queue = deque()
  queue.append(node)
  visited = [0] * (n + 2)
  visited[node] = 1

  while queue:
  
    node = queue.popleft()
    for index, distance in enumerate(graph[node]):
      if 0 < distance <= 1000 and index == n+1:
        return 'happy'

      if 0 < distance <= 1000 and (visited[index] == 0):
        visited[index] = 1
        queue.append(index)
    
  return 'sad' 

data = []      
for i in range(t):
  data.append(tuple(testcasein(t)))
for i in range(t):
  n, home, cu, festival = data[i]
  graph = distancetoCU(home, cu, festival)
  print(bfs(0, graph))


