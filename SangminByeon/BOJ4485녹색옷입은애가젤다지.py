from sys import stdin
import heapq

INF = int(1e9)

def dijkstra(n, cave, start = (0,0)):
    q = []
    route = [[INF for j in range(N)] for i in range(N)]

    heapq.heappush(q,(0,0,0))
    while q:
        y,x, dist = heapq.heappop(q)
        for i,j in zip([0,0,1,-1],[1,-1,0,0]):
            ny = y + i
            nx = x + j
            # print(y,x,'->',ny,nx)

            if ny < 0 or ny >= n or nx < 0 or nx >= n: continue
            if route[ny][nx] < dist: continue
            ndist = dist + cave[ny][nx]
            if ndist < route[ny][nx]:
                route[ny][nx] = ndist
                print(route)
                heapq.heappush(q,(ny,nx,ndist))
    return route[-1][-1]

while(True):
    N = int(stdin.readline().strip())
    if not N: break
    # print(N)

    cave = []
    
    for _ in range(N):
        cave.append(list(map(int,stdin.readline().strip().split())))
    
    # print(cave)

    print(dijkstra(N, cave))


    

        