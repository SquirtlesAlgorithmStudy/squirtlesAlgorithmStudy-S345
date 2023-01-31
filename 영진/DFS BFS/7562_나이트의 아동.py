from collections import deque  
num_of_test_case=int(input())

dx=[-1,1,2,2,1,-1,-2,-2]
dy=[-2,-2,-1,1,2,2,1,-1]

def knight(initial_x,initial_y,finish_x,finish_y):
    queue=deque()
    queue.append((initial_x,initial_y))
    visited[initial_y][initial_x]=1
    
    while queue:
        x,y=queue.popleft()
        if x==finish_x and y==finish_y:
            print(visited[finish_y][finish_x]-1) #10번째 줄에서 초기값을 1로 설정하였기 때문에 출력할 때 1을 빼주고 출력
            return
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<l and 0<=ny<l and visited[ny][nx]==0:
                visited[ny][nx]=visited[y][x]+1
                queue.append((nx,ny))

for _ in range(num_of_test_case):
    l=int(input())
    start_x,start_y=map(int,input().split())
    goal_x,goal_y=map(int,input().split())
    visited=[[0]*l for _ in range(l)]
    knight(start_x,start_y,goal_x,goal_y)