from collections import deque
import sys
input = sys.stdin.readline

height, width = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(height)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited = [[0] * width for _ in range(height)]
    visited[x][y] = 1
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < height and 0 <= ny < width:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return cnt


if __name__ == "__main__":
    result = 0
    saved = 0
    while True:
        cnt = bfs(0, 0)
        if not cnt:
            print(result)
            print(saved)
            break
        result += 1
        saved = cnt
