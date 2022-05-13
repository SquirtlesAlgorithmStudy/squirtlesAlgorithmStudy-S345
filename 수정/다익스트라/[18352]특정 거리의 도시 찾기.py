import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

city, road, distance, start = map(int, input().rstrip().split())
min_distance = [INF] * (city + 1)

graph = [[] for i in range(city + 1)]
for _ in range(road):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)

q = []

heapq.heappush(q, (0, start))
min_distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if min_distance[now] < dist: # 이미 방문한 도시 무시
        continue
    for i in graph[now]:
        cost = dist + 1 # now까지의 최단거리 + 1
        if cost < min_distance[i]:
            min_distance[i] = cost
            heapq.heappush(q, (cost, i))

for i in range(1, city+1):
    if min_distance[i] == distance:
        print(i)
    elif i == city and distance not in min_distance[1:city]:
        print(-1)