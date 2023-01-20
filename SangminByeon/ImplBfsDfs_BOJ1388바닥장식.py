from sys import stdin

def dfs_horizon(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if floor[x][y] == '-':
        floor[x][y] = 'x'
        dfs_horizon(x, y-1)
        dfs_horizon(x, y+1)
        return True
    return False

def dfs_vertical(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if floor[x][y] == '|':
        floor[x][y] = 'x'
        dfs_vertical(x-1, y)
        dfs_vertical(x+1, y)
        return True
    return False

n,m = map(int, stdin.readline().rstrip().split())

floor = [[0 for col in range(m)] for row in range(n)]
for i in range(n):
    temp = stdin.readline().rstrip()
    for j in range(m):
        floor[i][j] = temp[j]

print(floor)

count = 0

for i in range(n):
    for j in range(m):
        if dfs_horizon(i,j) == True: count += 1
        if dfs_vertical(i,j) == True: count+=1

print(count)

