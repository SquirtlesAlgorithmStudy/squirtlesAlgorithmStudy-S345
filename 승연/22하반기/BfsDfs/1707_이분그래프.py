# 이분 그래프
# 잘못 풀었던 이유 : 다른 편의 모든 노드에 연결되어있다고 착각
# 참고한 아이디어 : 한 그룹을 색으로 칠하고, 같은 색끼리 연결되면 NO리턴하기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(20000)

# 이 dfs함수는 '그룹을 할당'해주는 기능. 재귀 함수 짤 때 해당 함수의 기능 인지하고 코드 짜기
def dfs(i, group):
    global error
    # 사이클이 있으면 재귀 탈출
    if error:
        return
    # 이 부분이 그룹 설정하는 부분. 재귀 호출시 그룹을 활당 해주는 것.
    # 따라서 if not visied[j]: 이 부분 아래에 재귀를 호출(그룹 할당)해줘야 함
    visited[i] = group # 0:미방문 1:1그룹 -1:-1그룹
    for j in graph[i]:
        if not visited[j]:
            # 반대 그룹으로 할당
            dfs(j, -group)
        elif visited[i] == visited[j]:
            error = True
            return

n = int(input())
for _ in range(n):
    error = False
    nodes, lines = map(int, input().split())
    visited = [False]*(nodes+1) # 연결 정보 담는 그래프
    graph = [[] for _ in range(nodes+1)] # 방문한 정점 체크

    for _ in range(lines):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    # 이 부분은 정점들의 방문 처리(그룹할당)을 해주는 부분
    # 따라서 i가 노드의 숫자를 가리킴 -> 1~v 필요
    for i in range(1, nodes + 1):
        if not visited[i]:
            dfs(i, 1)
            if error: # 사이클이 있으면 탈출
                break
    if error:
        print("NO")
    else:
        print("YES")
