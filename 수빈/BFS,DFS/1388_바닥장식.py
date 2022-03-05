## 시도1 -- 시간초과

import sys
fastin = sys.stdin.readline

h, w = map(int, fastin().rstrip().split())

jangsik = [fastin() for _ in range(w)]
cnt = 0

# '-' 확인
for i in range(h):
    j = 0
    while j<h:
        if jangsik[i][j] =='|':
            j +=1
        else:
            cnt +=1
            while j<h and jangsik[i][j]=='-':
                j +=1
                
# '|' 확인         
for j in range(w):
    i = 0
    while i<w:
        if jangsik[i][j] =='-':
            i +=1
        else:
            cnt +=1
            while i<w and jangsik[i][j]=='|':
                i +=1
                
print(cnt)


##시도2 - DFS
import sys
fastin = sys.stdin.readline

N, M = map(int, fastin().rstrip().split())

graph = []
for _ in range(N):
    graph.append(list(fastin()[:-1]))
answer = 0

def DFS(x,y):
    if graph[x][y] =='|':
        graph[x][y] = 'o'
        
        for _x in [1,-1]:
            X = x + _x
            if (X>0 and X<N) and graph[X][y]=='|':
                DFS(X,y)
                
    if graph[x][y] =='-':
        graph[x][y] = 'o'
        
        for _y in [1, -1]:
            Y = y + _y
            if (Y>0 and Y<M) and graph[x][Y]=='-':
                DFS(x,Y)
                
for i in range(N):
    for j in range(M):
        if graph[i][j] == '|' or graph[i][j] =='-':
            DFS(i,j)
            answer +=1 
    
    
print(answer)

