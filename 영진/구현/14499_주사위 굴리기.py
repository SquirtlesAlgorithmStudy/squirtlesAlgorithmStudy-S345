from sys import stdin
N,M,x,y,K=map(int,stdin.readline().rstrip().split())

num_of_map=[]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
dice=[0,0,0,0,0,0,0]

#주사위를 굴린 결과를 반영하는 함수
def roll(c):
    if c == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif c == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif c == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif c == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]



for _ in range(N):
    num_of_map.append(list(map(int,stdin.readline().rstrip().split())))

command=list(map(int,stdin.readline().rstrip().split()))

nx=x
ny=y
for comm in command:
    nx+=dx[comm-1]
    ny+=dy[comm-1]
    
    if nx<=-1 or nx>=N or ny<=-1 or ny>=M:
        nx-=dx[comm-1]
        ny-=dy[comm-1]
        continue
    roll(comm)
    
    if num_of_map[nx][ny]!=0:
        dice[6]=num_of_map[nx][ny]
        num_of_map[nx][ny]=0
    elif num_of_map[nx][ny]==0:
        num_of_map[nx][ny]=dice[6]
    
    print(dice[1])
    
"""
1.a,b,c=1,2,3 등의 방식으로도 값을 할당할 수 있다
"""       
     
