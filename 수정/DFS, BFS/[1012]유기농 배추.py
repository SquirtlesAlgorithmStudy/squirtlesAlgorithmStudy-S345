#list index out of range 해결 하면
#list assignment index out of range
import sys
fastin = sys.stdin.readline

case = int(fastin().rstrip())
for k in range(case):
    M, N, K = map(int, fastin().rstrip().split())
    cabbage = [[1]*N for _ in range(M)]

    def dfs(x, y):
        if x <= -1 or x >= M or y <= -1 or y >= N:
            return False
        if cabbage[x][y] == 0:
            cabbage[x][y] = 1
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False

    for i in range(K): #인덱스 입력
        X, Y = map(int, fastin().rstrip().split())
        cabbage[X][Y] = 0

    result = [[0]*case]
    for i in range(M):
        for j in range(N):
            if dfs(i, j) == True:
                result[k] += 1 #해결 안됨

for l in range(case):
    print(result[l])