import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, start = map(int, input().split())
graph = [[]for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b= map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    #q가 비어있으면 False, 값이 들어있으면 True
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드인 경우
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
for i in range(1, n + 1):
    if distance[i] == k:
        count += 1
        print(i)
if count == 0:
    print(-1)