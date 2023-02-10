import sys 
from collections import deque
input =sys.stdin.readline
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def sum_all_element(data:list):
    sum = 0 
    for x in data:
        for i in x:
            sum +=i
    return sum 


side = [] # 가장자리를 저장하는 리스트 

def bfs(where):
    q = deque([])

    visited[x][y] = 1 
    q.append((x,y))

    # 1시간 전에 대한 구현: 가장자리 픽셀의 개수와 남은 치즈의 개수가 
    # 같다고 보면 마무리하기 한시간 전이다
    if len(side) == sum_all_element(place):
        leftover = sum_all_element(place)

    if sum_all_element(place) ==0:
        return hours,leftover
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<nx<n and 0<ny<m and not visited[nx][ny]:
                visited[nx][ny] = 1 #방문 처리 
                if place[nx][ny] == 0: # 가장자리 라면
                    #Store x,y
                    q.append((x,y))
                    #가장자리 따로 뺴서 store
                    side.append((x,y))

                    bfs((x,y))

hours = 0 
leftover = 0 
n ,m = map(int,input().split()) # n 세로길이 m 가로길이 # 최대 길이 100
place = [input().rsplit() for _ in range(n)]
visited = [[0]*m for _ in n]
 # 치즈가 모두 없어질때 까지  
hours, leftover = bfs((0,0))