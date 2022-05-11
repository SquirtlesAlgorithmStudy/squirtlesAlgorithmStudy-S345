import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

node, line = map(int, input().rstrip().split())
start = int(input().rstrip())
distance = [INF] * (node + 1)

graph = [[] for i in range(node + 1)]
for _ in range(line):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))


q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: # 이미 방문한 노드 무시
        continue
    for i in graph[now]: # now 정점에서 갈 수 있는 정점 모두 확인
        cost = dist + i[1] # now 최단거리 + 사이의 거리
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))


for i in range(1, node + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])