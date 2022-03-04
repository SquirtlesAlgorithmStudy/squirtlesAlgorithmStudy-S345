n, m = map(int, input().split(' '))
graph = []
for i in range(n):
    graph.append(list(input()))

count = 0
# '-'모양 타일의 개수를 세는 부분
for i in range(n):
    isTrue = False
    for j in range(m):
        if graph[i][j] == '-':
            isTrue = True
        if graph[i][j] == '|':
            if isTrue == True:
                count += 1
                isTrue = False
    if isTrue == True:
        count += 1


# '|'모양 타일ㄹ의 개수를 세는 부분
for j in range(m):
    isTrue = False
    for i in range(n):
        if graph[i][j] == '|':
            isTrue = True
        if graph[i][j] == '-':
            if isTrue == True:
                count += 1
                isTrue = False
    if isTrue == True:
        count += 1

print(count)