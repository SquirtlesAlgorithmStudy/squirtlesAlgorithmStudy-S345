# ABCDE

# 실수1 처음에 문제를 잘못 이해했다. 문제를 제대로 이해하고 풀어야 시간낭비를 안할 수 있음

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

num_people, num_relations = map(int, input().split())
relations_info = [list(map(int, input().split())) for _ in range(num_relations)]

graph = [[] for _ in range(num_people)]
visited = [False]*num_people

# 실수2 a, b 둘다 인덱스로 해주고 append를 해줘야 모든 경우를 탐색할 수 있음
for a, b in relations_info:
    graph[a].append(b)
    graph[b].append(a)

# count 4 이상이면 1
answer = 0
def dfs(v, count):
    global answer
    visited[v] = True

    if count >= 4:
        answer = 1
        return

    for i in graph[v]:
        if not visited[i]:
            dfs(i, count + 1)
            visited[i] = False

for i in range(num_people):
    if not visited[i]:
        if answer == 0:
            # 실수3 초기값을 1이 아닌 0으로 줘야한다. 디버깅으로 count 변화 체크 꼭 하자. 
            dfs(i, 0)
            # *** 실수4 dfs를 재귀로 호출해주고, 방문처리를 사용하는 경우 꼭 재귀호출 구문 바로 아래에 방문을 철회해주는 부분이 필요하다.
            visited[i] = False

print(answer)