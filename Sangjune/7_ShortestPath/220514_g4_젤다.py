import sys
import heapq

fin = sys.stdin.readline

INF = int(1e9)
prob_count = 0
N = int(fin())
probs = []
ans = []

while(N != 0):
    prob_count += 1
    v = N * N
    e = 2 * N * (N - 1) # (1부터 N-1까지의 합) * 4

    graph = [[] for _ in range(v + 1)]
    distance = [INF] * (v + 1)

    weights = [[-1 for _ in range(N + 2)]] # 가장자리에 -1 weight 두기
    for _ in range(N):
        temp_list = list(map(int, fin().split()))
        weights.append([-1] + temp_list + [-1])
    weights.append([-1 for _ in range(N + 2)])

    # print(weights)

    for i in range(1, N * N + 1):
        if i % N == 0:
            row = i // N
        else:
            row = i // N + 1
        if i % N == 0:
            col = N
        else:
            col = i % N
        if weights[row - 1][col] >= 0: # 위
            graph[i].append((i - N, weights[row - 1][col]))
        if weights[row][col - 1] >= 0: # 왼쪽
            graph[i].append((i - 1, weights[row][col - 1]))
        if weights[row][col + 1] >= 0: # 오른쪽
            graph[i].append((i + 1, weights[row][col + 1]))
        if weights[row + 1][col] >= 0: # 아래
            graph[i].append((i + N, weights[row + 1][col]))

    # print(graph)

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    dijkstra(1)
    probs.append(prob_count)
    ans.append(weights[1][1] + distance[v]) # 시작 지점 고려!

    N = int(fin())

for i in range(len(probs)):
        print(f'Problem {probs[i]}: {ans[i]}')