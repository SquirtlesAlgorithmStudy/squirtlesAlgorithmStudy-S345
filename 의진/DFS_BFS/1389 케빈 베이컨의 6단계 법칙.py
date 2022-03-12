import sys
fastin = sys.stdin.readline

n, m = map(int, fastin().split())
relations = [tuple(map(int, fastin().split())) for _ in range(m)]
board = [[] for _ in range(n+1)]


for relation in relations:
    board[relation[0]].append(relation[1])
    board[relation[1]].append(relation[0])

print(board)
