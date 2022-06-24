import sys
from collections import deque

input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(12)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def trace_bfs(y, x, color):
    count = 1
    queue = deque()
    queue.append((y, x))
    visited = [[0] * 6 for _ in range(12)]
    trace_stack = []
    visited[y][x] = 1
    trace_stack.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 6 or ny >= 12:
                continue
            if visited[ny][nx] == 1:
                continue
            if board[ny][nx] != color:
                continue

            visited[ny][nx] = 1
            count += 1
            queue.append((ny, nx))
            trace_stack.append((ny, nx))
    if count >= 4:
        for y, x in trace_stack:
            board[y][x] = '.'
        return True
    return False


def explode_puyo():
    is_exploded = False
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                if not is_exploded:
                    is_exploded = trace_bfs(i, j, board[i][j])
                else:
                    trace_bfs(i, j, board[i][j])
    return is_exploded


def drop_puyo():
    for line in range(6):
        count = 0
        drop_queue = deque()
        for floor in range(11, -1, -1):
            if board[floor][line] != '.':
                drop_queue.append(board[floor][line])
        for floor in range(11, -1, -1):
            if drop_queue:
                board[floor][line] = drop_queue.popleft()
            else:
                board[floor][line] = '.'


answer = 0
while explode_puyo():
    drop_puyo()
    answer += 1
print(answer)
