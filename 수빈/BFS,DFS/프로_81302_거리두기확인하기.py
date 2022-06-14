import sys
input = sys.stdin.readline
from collections import deque

def solution(places):
    dx, dy = [0,0,-1,1],[-1,1,0,0]
    def BFS(i, j, m, visited):
        q.append((i,j))
        visited[i][j] = True
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and n[nx][ny]!='X' and not visited[nx][ny]:
                    m[nx][ny] = m[x][y]+1
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    
        return m
    
    answer = []
    for n in places: # 5x5 대기실에 n개가 한 번에 입력되므로, n번째 대기실마다 bfs를 돌려준다
        p = []
        tf = False
        for i in range(5):
            for j in range(5):
                if n[i][j] =='P':  # 반복문을 돌며, n[i][j]가 'P'이면 p에 (i,j)좌표를 넣어준다(응시자가 앉아있는 자리)
                    p.append([i,j])
        
        for i, j in p:              # 반복문을 돌며, P에 있는 모든 응시자들 사이의 거리를 BFS함수를 통해 구해준다
            m = [[0]*5 for _ in range(5)]
            q = deque()
            visited = [[False]*5 for _ in range(5)]
            dist = BFS(i, j, m, visited)  # n번째 대기실에 있는 응시자들 한명 한명을 대상으로 각각 BFS 함수 실행
            # dist에 응시자들 사이의 거리가 저장됨. 
            for cx, cy in p:
                if (cx,cy) != (i,j) and 1<=dist[cx][cy] <=2:
                    #자기 자신을 제외하고 다른 응시자들 사이의 거리가 1~2이면
                    answer.append(0)   # 거리두기가 지켜지지 않은 것이므로 answer에 0을 넣고
                    tf = True          # tf는 True 로 바꾸고
                    break              # 한 명이라도 안 지키면 0을 출력할 것이므로 바로 break
            if tf:         # 다음 대기실 확인
                break
        if not tf:         # 모든 응시자를 확인했는데 tf가 False이면, 모두 거리두기를 잘 지키고 있으므로
            answer.append(1) # answer에 1을 append
    return answer            # 최종적으로 모든 대기실을 확인한 뒤 answer를 return


## dfs보단 BFS 라더라~~...
back tracking은 dfs 
탐색 순서의 차이
최단거리 문제의 간선거리가 다 같을 경우엔 BFS