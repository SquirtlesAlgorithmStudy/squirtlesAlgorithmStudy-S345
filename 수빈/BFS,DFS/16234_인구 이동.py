
import sys
input = sys.stdin.readline
from collections import deque

# x, y direction setting
dx = [1,-1,0,0]  ## 우, 좌
dy = [0,0,-1,1]  ## 하, 상
N, L, R = map(int, input().rstrip().split())
s = []
for i in range(N):
    s.append(list(map(int, input().rstrip().split())))
    

def BFS(i,j):
    q = deque()
    q.append([i,j])
    temp = []
    temp.append([i,j])
    # 연합된 국가 담기
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 여기서 x, y가 ...
            if 0<= nx <N and 0<= ny <N and visit[nx][ny]==0:
                # 인접 국가를 탐색하면서 인구차이가 L명 이상 R명 이하인 경우 연합 국가에 담기
                if L <= abs(s[nx][ny]- s[x][y]) <=R:
                    visit[nx][ny] = 1
                    q.append([nx,ny])
                    temp.append([nx,ny])
    return temp

#인구이동이 발생하는 일 수       
cnt = 0
while True:  #인구 이동이 없을 때까지 반복
    visit = [[0]*N for i in range(N)]
    isTrue = False  #인구 이동 존재 유무 플래그
    # 모든 곳을 BFS로 방문하여 연합 진행
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                temp = BFS(i,j)
                if len(temp) > 1:
                    isTrue = True
                    num = sum([s[x][y] for x,y in temp]) //len(temp)
                    for x,y in temp:
                        s[x][y] = num
    if not isTrue: 
        # 지금까지 인구 이동이 없는 경우 break
        break
    cnt +=1
    
print(cnt)



##ex try
for q in range(N):
    for w in range(N):
        if 10 <= abs(board[q][w]-board[q+1][w]) <=80:
            BFS(q,w)
            board[q][w]=1 # 방문처리
            cnt +=1
        elif 10 <= abs(board[q][w+1]-board[q][w]) <=80:
            BFS(q,w)
            board[q][w]=1 # 방문처리
            cnt +=1
        else: