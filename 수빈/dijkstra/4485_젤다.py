
import sys
from turtle import distance
input = sys.stdin.readline
import heapq

INF = int(1e9)
cnt = 0
#좌우하상
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# graph에 2차원 리스트로 동굴 정보를 입력받고o
# 최단 경로는 : 2차원 리스트 INF(int(1e9))로 초기화o
# 상하좌우 탐색하면서 각 distance에 최단 경로를 갱신o
# distance[3][3]은 0,0부터 3,3으로 가는 최단경로가 저장됨?


while True:
    cnt +=1
    # 동굴의 크기를 입력받음(n)
    n = int(input().rstrip())
    
    # n==0이면 반복문 탈출
    if n==0: break
    
    # 최단 경로를 초기화
    distance = [[INF]*n for _ in range(n)]
    # 동굴 정보를 입력받음
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    
    # 0,0 은 무조건 거쳐야 함
    # 0에서 시작하기 때문에 distance[0][0]값을 graph[0][0]로 초기화o
    distance[0][0] = graph[0][0]

    # q에 (x,y좌표로 이동하는 최소 경로, 탐색을 시작하는 지점의 x좌표, 탐색을 시작하는 지점의 y좌표를 저장)o
    q = [(graph[0][0], 0, 0)]

    # 우선순위 q를 사용해서 q가 빌(empty) 때까지, 
    # 다익스트라 알고리즘으로 최단경로 갱신해서 distance에 저장

    while q:
        # dis에는 graph[x][y] 까지의 최단 경로가 저장됨
        # x,y는 각각 탐색을 시작하는 좌표의 x,y가 저장됨
        dis, x, y = heapq.heappop(q)
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인(상,하,좌,우)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나면 탐색 종료
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            
            # 최단 경로를 갱신
            cost = dis + graph[nx][ny]
            
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print("Problem "+str(cnt)+": "+ str(distance[n-1][n-1]))



# 런타임 에러?