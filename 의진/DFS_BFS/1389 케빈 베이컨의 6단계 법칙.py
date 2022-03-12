from collections import deque
import sys
fastin = sys.stdin.readline

n, m = map(int, fastin().split())
relations = [tuple(map(int, fastin().split())) for _ in range(m)]
board = [[] for _ in range(n+1)]


for relation in relations:
    if relation[1] not in board[relation[0]]:
        board[relation[0]].append(relation[1])
    if relation[0] not in board[relation[1]]:
        board[relation[1]].append(relation[0])
# print(board)


def bfs(start, end):
    if start == end:
        return 0
    queue = deque()
    visited = [-1] * (n+1)
    visited[start] = 0
    queue.append(start)

    while queue:
        x = queue.popleft()
        for friend in board[x]:
            if friend == end:
                return visited[x] + 1
            if visited[friend] == -1:
                visited[friend] = visited[x] + 1
            queue.append(friend)
    return -1


result = []
for i in range(1, n+1):
    kevinNum = 0
    for j in range(1, n+1):
        kevinNum += bfs(i, j)
    result.append(kevinNum)
print(result.index(min(result))+1)
