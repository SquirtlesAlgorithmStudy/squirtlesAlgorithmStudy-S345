import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한 설정

#좌표설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra():
    q = []
    #시작노드 좌표 큐에 삽입
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q: #큐가 비어있지 않으면 

        #적은 루피 정보 꺼내기 
        cost, x, y = heapq.heappop(q)

        # 맨끝까지 갔으면 
        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break

        
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            # 노드 확인 
            if 0 <= next_x < n and 0 <= next_y < n:
                next_cost = cost + graph[next_x][next_y]

                #현재 노드를 거쳐서 , 다른 노드로 이동하는 거리가 짧은 경우  ==> 루피 값이 작은경우 
                if next_cost < distance[next_x][next_y]:
                    distance[next_x][next_y] = next_cost
                    heapq.heappush(q, (next_cost, next_x, next_y))

count = 1

while 1:
  #동굴크기
    n = int(input())
  # (2 ≤ N ≤ 125) N = 0인 입력이 주어지면 전체 입력이 종료된다
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    dijkstra()
    count += 1
