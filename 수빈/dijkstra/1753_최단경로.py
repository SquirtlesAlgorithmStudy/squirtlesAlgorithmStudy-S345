import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

V, E = map(int, input().rstrip().split())
K = int(input())

# 가중치 테이블 dp
dp = [INF]*(V+1)
heap = []
graph =[[] for _ in range(V+1)]
print('dp 가중치',dp)
print('graph 초기 그래프', graph)

def Dijkstra(start):
    #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    dp[start] = 0
    heapq.heappush(heap, (0,start))
    print('heap1', heap)
    
    #힙에 원소가 없을 때까지 반복
    while heap:
        wei, now = heapq.heappop(heap)
        print('heap2', heap)
        
        #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시
        if dp[now]<wei:
            print('dp1',dp)
            continue
        for w, next_node in graph[now]:
            #현재 정점까지의 가중치 wei + 현재 정점에서 다음정점(next_node)까지의 가중치 W
            # = 다음 노드까지의 가중치(next_wei)
            next_wei = w + wei
            print('가중치 업데이트',w, wei, next_wei)
            #다음 노트까지의 가중치(next_wei)가 현재 기록된 값보다 작으면 조건 성립
            if next_wei < dp[next_node]:
                #계산했던 next_wei를 가중치 테이블에 업데이트
                dp[next_node] = next_wei
                print('dp2', dp)
                #다음 점 까지의 가중치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입
                heapq.heappush(heap, (next_wei, next_node))
                print('heap3', heap)

# 초기화
for i in range(E):
    u, v, w = map(int, input().rstrip().split())
    # print('반복문' ,u,v,w)
    graph[u].append((w,v))
    
# print(V, E, K)

Dijkstra(K)
for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])



# a->b가 c비용
  #  graph[a].append((b, c))