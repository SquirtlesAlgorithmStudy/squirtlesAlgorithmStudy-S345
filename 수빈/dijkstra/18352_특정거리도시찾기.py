import heapq
import sys
from turtle import distance
input = sys.stdin.readline
INF = int(1e9)  # 초기 거리를 무한으로 초기화

n, m, k, x = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
# 여기서 m이 아닌 n+1을 해주는 이유는?
distance = [INF]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
# graph를 print출력하면 [[], [2, 3], [3, 4], [], []] 이렇게 이상하게 나오는데, 
# graph를 이렇게 만들어주는 이유는?
## 출발점으로부터 연결된 도착점들을 연결해주기 위해??
## 그럼 [2,3]은 말이 되도 [3,4]는 말이 안되는데...
print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    # heapq를 이용해 거리가 짧을수록 앞에 오는 큐(우선순위 큐)를 만듬
    print(q)
    distance[start] = 0
    # 처음 자기자신과의 거리는 0으로 설정
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + 1
            # 현재 나의 지점과 연결된 점들과의 거리를 누적거리+1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost,i))
                
dijkstra(x)  # 출발지점
flag = 0
for i in range(1, n+1):  
    # 왜 자꾸 노드 기준으로 하는거지? 도로 기준으로 해야하는거 아닌가
    if distance[i] ==k:
        print(i)
        flag =1 
        
if flag==0:
    print(-1)


# 런타임에러