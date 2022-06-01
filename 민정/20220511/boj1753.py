import sys
import heapq

fastin = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, fastin().split())
k = int(fastin())

w = [INF] * (v+1)
heap = []
graph = [[] for _ in range(v+1)]


def dij(start):
    w[start] = 0
    heapq.heappush(heap, (0, start))
    
    while heap:
        weight, now = heapq.heappop(heap)
        if w[now] < weight: continue
        
        for wei, next in graph[now]:
            next_wei = wei + weight
            if next_wei < w[next]:
                w[next] = next_wei
                
                heapq.heappush(heap, (next_wei, next))
                
       
for _ in range(e):
    U, V, W = map(int, fastin().split())
    graph[U].append((W, V))
    
dij(k)
for i in range(1, v+1):
    print("INF" if w[i] == INF else w[i])