# 답 참고

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


n = int(input())
# 띄어쓰기 없이 숫자가 연속으로 입력되는 경우 입력처리 주의 !!
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# dfs구조 다시 한 번 정확히 익히자.
def dfs(x, y):
    global count
    # 여기엔 '종료조건'이 와줘야 한다.
    if x < 0 or x >= n or y < 0 or y >= n:
        # '종료'
        return count

    # 그리고 문제에서 0, 1 둘 중 하나만 있을 때 따로 방문처리 해주는 자료구조 없어도 1을 0으로 바꿔주면 됨
    if graph[x][y] == 1:
        # 단순하게 생각하자. 집이면 하나 세주고, 방문처리
        count += 1
        graph[x][y] = 0
        # 근처 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            dfs(nx, ny)
        # for문 다 돌고나서 count 리턴 (한덩이 다 세주고 나서)
        return count
    # graph[x][y] 가 1이 아니면 (즉, 종료해야함)
    return count

result = []
count = 0
for i in range(n):
    for j in range(n):
        # 집이면(1이면) 한 덩이 탐색 시작
        if graph[i][j] == 1:
            tmp = dfs(i, j)
            # 집이 하나라도 있으면, 한 덩이 추가됨
            if tmp >= 1:
                result.append(tmp)
                count = 0

result.sort()
print(len(result))
for i in result:
    print(i)