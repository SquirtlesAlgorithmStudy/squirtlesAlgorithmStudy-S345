import sys

fin = sys.stdin.readline

N, M = map(int, fin().rstrip().split())

graph = []
for i in range(N):
    graph.append(list(fin().rstrip()))

count = 0

# row
cpied_g = graph.copy()
for i in range(N):
    temp = ""
    for j in range(M):
        if graph[i][j] == '-' and graph[i][j] != temp:
            count += 1
        temp = graph[i][j]

# column
transposed_graph = list(map(list, zip(*graph)))
# print(transposed_graph)
for i in range(M):
    temp = ""
    for j in range(N):
        if transposed_graph[i][j] == '|' and transposed_graph[i][j] != temp:
            count += 1
        temp = transposed_graph[i][j]

print(count)


# note
# string을 문자 하나씩 char의 list로 변환 : 그냥 list(str) 해주면 됨
# 2차원 리스트 뒤집기 : new_list = list(map(list, zip(*origin_list)))
# 리스트 복사