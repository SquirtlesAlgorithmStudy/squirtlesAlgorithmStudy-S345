# 1012_유기농 배추 문제풀이 (수빈 발표)

import sys
fastin = sys.stdin.readline
from collections import deque 


# x direction/ y direction setting
#####우,좌,하,상
dx = [1,-1,0,0]
dy = [0,0,-1,1]

test = int(fastin())

def BFS(x,y):   # BFS 함수 이용
    queue = [[x,y]]   # '큐'사용
    while queue:
        a, b = queue[0][0], queue[0][1]
        print('a, b 출력' , a,b)
        del queue[0]
        for i in range(4): #상하좌우 탐색
            q = a + dx[i]
            w = b + dy[i]
            if 0<=q<sero and 0<=w<garo and board[q][w]==1:
                board[q][w]=0   # 탐색한 배추는 0으로 갱신
                queue.append([q,w])
                print('마지막 큐', queue)

for i in range(test):
    cnt = 0   # 지렁이 수 count
    garo, sero, k = map(int, fastin().rstrip().split()) # 가로, 세로, 1의 개수
    board = [ [0]*garo for _ in range(sero)]  # 너비10, 높이8인 보드 생성
    # print('초기 board','\n', board)
    
    for j in range(k):  # 배추 수만큼 반복
        a, b = map(int, fastin().rstrip().split())
        board[b][a] = 1  # board에 배추의 위치 표현(b,a 순서주의)
    for q in range(sero):
        for w in range(garo):
            if board[q][w] ==1:  # 구역 중 1인 곳을 찾으면
                BFS(q,w)         # BFS를 수행하고
                board[q][w] = 0  # 그 구역을 모두 0으로 바꾼 뒤
                cnt +=1          # count +=1
    print(cnt)

# print('후기 board','\n', board)



