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
# 상 하 좌 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]
import sys 
input = sys.stdin.readline
n,m = map(int,input().split())

battleground = [[]*m for _ in range(n) ]
visited = [[[0]*m for _ in range(n) ]]

for b in battleground:
    st = map(str,input().rstrip())
    for c in st:
        b.append(c)

def back(x,y):
    for i in range(4):
        nx ,ny = x+ dx[i], y+ dy[i]
        battleground[nx][ny]
    