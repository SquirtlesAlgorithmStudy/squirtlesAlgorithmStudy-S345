from collections import deque
length,width=map(int,input().split())
cheese=[]
for _ in range(length):
    cheese.append(list(map(int,input().split())))

dx=[0,0,-1,1]
dy=[-1,1,0,0]

num_of_melting_cheese=[]

def bfs():
    queue=deque()
    queue.append((0,0))
    cnt=0
    visited[0][0]=1
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<width and 0<=ny<length and visited[ny][nx]==0:
                if cheese[ny][nx]==0: #치즈가 없는 부분의 사방 탐색(치즈가 있는 부분의 사방을 탐색할 경우, 치즈의 내부를 탐색할 수도 있기 때문)
                    visited[ny][nx]=1
                    queue.append((nx,ny))
                elif cheese[ny][nx]==1: #치즈가 있으면 바로 녹이면서 녹은 치즈의 수를 셈
                    cheese[ny][nx]=0
                    visited[ny][nx]=1
                    cnt+=1
    num_of_melting_cheese.append(cnt)
    return cnt   
              
time=0
while True:
    time+=1
    visited=[[0]*width for _ in range(length)]
    count=bfs()
    if count==0:
        break

print(time-1)
print(num_of_melting_cheese[-2])  