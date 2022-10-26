### BFS set
# dfs로 풀면 시간초과 나는 문제
# 참고한 bfs 풀이
import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1
def BFS(x, y):
    global answer
    # 시간초과가 난다면 deque() 대신 set()자료형을 써주는 것도 방법.
    # 자료 탐색시 set의 경우 시간복잡도가 O(1)이고, deque는 O(N)이다.
    q = set([(x, y, board[x][y])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)

BFS(0, 0)
print(answer)
