#try1:bfs 함수 안에서 전부처리하고 출력하려 하였으나 실패
#try2:bfs 함수 안에서는 연합한 국가의 좌표 값만 받아오고
#     계산과 할당은 메인문에서 동작시켜서 성공

from collections import deque
from sys import stdin
N,L,R=map(int,input().split())

world=[]
for _ in range(N):
    world.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y): #연합한 국가의 좌표를 저장하기 위한 함수
    queue=deque()
    union=[] 
    queue.append((x,y))
    union.append((x,y))
    while queue:
        x,y=queue.popleft()        
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if L<=abs(world[nx][ny]-world[x][y])<=R: #이웃한 국가의 인구수가 조건 범위 내일 때
                        visited[nx][ny]=1
                        queue.append((nx,ny))
                        union.append((nx,ny))
    return union

num_of_days=0
while True:
    visited=[[0]*(N) for _ in range(N)]
    united=False
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0:
                visited[i][j]=1
                country=bfs(i,j) #연합한 국가의 좌표값 저장
                if len(country)>1:
                    united=True
                    #연합한 국가에 이동한 후의 인구수 계산
                    number=sum([world[x][y] for x,y in country])//len(country)
                    for x,y in country:
                        world[x][y]=number
                        #인구 이동
    if united==False:
        break
    num_of_days+=1
print(num_of_days)

"""
1.abs():괄호 안의 값을 절대값으로 바꿔주는 내장 함수
2.world[x][y] for x,y in country
:for 문을 통해 list 안의 원소들을 가져와 배열에 대입할 수 있다. 
"""