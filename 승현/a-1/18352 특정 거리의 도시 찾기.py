import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

#N: 도시의 수 M: 도로 수 K: 최단 거리 X: 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for i in range (n +1)]
distance =  [ INF ] * (n + 1)
plag = 0

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append((b,1)) #a: 출발 b: 도착 ,1 가중치

def dijkstra (x):
  q = []
  heapq.heappush(q, (0,x))
  distance[x] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist +i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(x)

for i in range(1, n+1):
  if k == distance[i]:
    print(i)
    plag = 1
    
if plag == 0:
  print ("-1")