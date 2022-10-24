# 문제 잘 읽기! 오른쪽과 아래쪽으로만 움직일 수 있다면 모든 가능한 경로가 최단경로
# 행, 열 뒤바뀌지 않았는지 확인
# m 열 n 행 , 더미변수 만들어주기
# 각 칸으로 올 수 있는 경로 더하기, 각 칸으로 올 수 있는 경로는 (좌, 상의 각 경로 수의 합)
from collections import deque

def solution(m, n, puddles):
    graph = [[0]*(m+1) for _ in range(n+1)]
    
    for x, y in puddles:
        graph[y][x] = -1
    
    # 좌, 상
    dx = [0, -1]
    dy = [-1, 0]
    graph[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 and j == 1) or graph[i][j] == -1:
                continue
            else:
                if graph[i + dx[0]][j + dy[0]] == -1:
                    left = 0
                else:
                    left = graph[i + dx[0]][j + dy[0]]
                if graph[i + dx[1]][j + dy[1]] == -1:
                    top = 0
                else:
                    top = graph[i + dx[1]][j + dy[1]]
                graph[i][j] += (left + top)
                                                       
    answer = graph[n][m] % 1000000007
    return answer