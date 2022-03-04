# 배추 있는 곳 : 1 없는 곳 : 0
# 예제 오류없이 정답 나옴. 런타임에러 해결 못함. 왜안되지???
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

result = []
TestCase = int(input())
for i in range(TestCase):
    m, n, cabbage = map(int, input().split(' '))

    cabbages = []
    for i in range(cabbage):
        cabbages.append(list(map(int, input().split(' '))))
    graph = []
    for i in range(n):
        graph.append([0] * m)

    for i in range(cabbage):
        y = cabbages[i][0]
        x = cabbages[i][1]
        graph[x][y] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                count += 1
    result.append(count)

for i in range(TestCase):
    print(result[i])