# 배추 있는 곳 : 1 없는 곳 : 0
import sys
fastin = sys.stdin.readline
sys.setrecursionlimit(10**6)
# Q재귀깊이 설정. 구글링 결과 파이썬 최대 재귀 깊이는 1000이라고 함. 근데 1000을 넣었을 때는 런타임 에러 / 10**6을 넣었을 때는 정답. 왜?

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
TestCase = int(fastin().rstrip())
for i in range(TestCase):
    m, n, cabbage = map(int, fastin().split(' '))

    cabbages = []
    for i in range(cabbage):
        cabbages.append(list(map(int, fastin().split(' '))))
    graph = []

    # (이런 방법도 존재)
    # graph = list()
    # for i in range(n):
    #     tmp = []
    #     for j in range(m):
    #         tmp.append(0)
    #     graph.append(tmp)

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