from sys import stdin

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

com_num = int(stdin.readline().rstrip())
net_num = int(stdin.readline().rstrip())

graph = [[] for i in range(com_num+1)] # 0번 인덱스 안씀
visited = [False] * (com_num +1)
for i in range(1,net_num+1):
    a, b = map(int,stdin.readline().rstrip().split())
    graph[a].append(b)

dfs(graph,1,visited)
print(graph)
print(visited)
print(sum(visited)-1) #1번 컴퓨터 제외
