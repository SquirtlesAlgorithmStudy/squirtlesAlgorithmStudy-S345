# 복습 필요
def solution(n, computers):
    visited = [False for _ in range(n)]
    count = 0

    # 모든 노드를 탐색하기 위한 부분
    for i in range(n):
        if visited[i] != True:
            dfs(n, computers, i, visited)
            count += 1

    return count

# dfs호출 시 연결된 모든 노드 탐색
def dfs(n, computers, start, visited):
        visited[start] = True
        
        for i in range(n):
            # *헷갈렸던 부분* 여기서 computers[start][1] -> 연결되어있는 노드 다음에 연결된 노드 찾기 위한 것
            if i != start and visited[i] != True and computers[start][i] == 1:
                dfs(n, computers, i, visited)
                
