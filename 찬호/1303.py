'''
당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었다. 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.

N명이 뭉쳐있을 때는 N^2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가?
단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

입력
첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 
그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 
모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 
당신의 병사와 적국의 병사는 한 명 이상 존재한다.

출력
첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.

'''
#DFS 로 짜니까 메모리 초과 

#BFS 로 짜자
# 상 하 좌 우
d = [(-1,0),(1,0),(0,-1),(0,1)]
import sys 
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())

battleground = [[]*n for _ in range(m) ]
B_score = 0
W_score = 0

# get battleground data 
for b in battleground:
    st = map(str,input().rstrip())
    for c in st:
        b.append(c)

#Do BFS 
def BFS(x,y,c):
    queue =deque()
    queue.append((x,y))
    cnt =0
    while queue:
        x,y=queue.popleft()
        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if 0<=nx <m and 0 <=ny <n:
                if battleground[nx][ny]==c and battleground!=0:
                    queue.append((nx,ny))
                    cnt+=1
                    battleground[nx][ny]=0
    return 1 if cnt ==0 else cnt
        
for i in range(m):
    for j in range(n):
        if battleground[i][j] =="W":
            W_score +=BFS(i,j,battleground[i][j])**2
        elif battleground[i][j] =="B":
            B_score += BFS(i,j,battleground[i][j])**2
            
            
print(W_score,B_score)

#54767696	grvty0717	 1303	맞았습니다!!	34296	68	Python 3 / 수정	2053	
