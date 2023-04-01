from sys import stdin
import heapq

def dijkstra(n, start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start[0]][start[1]] = 0

    while q: #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now[0]][now[1]] < dist: continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in range(4):
            next = (now[0] + dy[i], now[1] + dx[i])
            if next[0] < 0 or next[0] >=n or next[1] < 0 or next[1] >=n: continue
            cost = dist + cave[next[0]][next[1]]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next[0]][next[1]]:
                distance[next[0]][next[1]] = cost
                heapq.heappush(q, (cost, next))


n = int(stdin.readline().strip())
start = (0,0)
dy = [1,-1,0,0]
dx = [0,0,1,-1]
INF = int(1e9)
while(n):
    cave = []
    distance = [[INF for _ in range(n)] for _ in range(n)]
    # print(distance)

    for i in range(n):
        cave.append(list(map(int, stdin.readline().strip().split())))

    dijkstra(n,start)

    print(distance[n-1][n-1])





    ###
    n = int(stdin.readline().strip())

    # print(cave)
# 입력 완료



