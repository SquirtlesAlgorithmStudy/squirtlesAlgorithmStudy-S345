from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
list1 = []

data = [list(input().strip()) for _ in range(m)] #한 글자씩 저장
# print (data)

def dfs_W(x, y):
    if x < 0 or x >= m:
        return False
    if visited[y][x] == 0 and data[y][x] == 'W':
        visited[y][x] = 1
        dfs_W(x-1, y)
        dfs_W(x+1, y)
        dfs_W(x, y-1)
        dfs_W(x, y+1)
        return True
    return False

def dfs_B(x, y):
    if y < 0 or y >= n:
        return False
    if visited[y][x] == 0 and data[y][x] == 'B':
        visited[y][x] = 1
        dfs_B(x-1, y)
        dfs_B(x+1, y)
        dfs_B(x, y-1)
        dfs_B(x, y+1)
        return True    
    return False

countW = 0
countB = 0
visited = [[0] * m for _ in range(n)]
for i in range(m):
    for j in range(n):
        if dfs_W(i , j) == True:
            countW += 1    
            
visited = [[0] * m for _ in range(n)]
for i in range(m):
    for j in range(n):
        if dfs_B(i , j) == True:
            countB += 1

print(countW*countW, countB*countB)
