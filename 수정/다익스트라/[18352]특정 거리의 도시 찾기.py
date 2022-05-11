import heapq
import sys
input = sys.stdin.readline
INF = int(1e7)

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
    if min_distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + 1
        if cost < min_distance[i]:
            min_distance[i] = cost
            heapq.heappush(q, (cost, i))

cnt = 0
for i in range(1, city+1):
    if min_distance[i] == distance:
        print(i)
    elif i == city and distance not in min_distance[1:city]:
        print(-1)