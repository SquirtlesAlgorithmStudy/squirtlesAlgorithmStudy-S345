import sys
input = sys.stdin.readline

n = int(input())
colored_papers = [tuple(map(int, input().split())) for _ in range(n)]
board = [[0] * 100 for _ in range(100)]

for colored_paper in colored_papers:
    for row in range(colored_paper[1], colored_paper[1] + 10):
        for offset in range(10):
            board[row][colored_paper[0] + offset] = 1

count = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            count += 1

print(count)
