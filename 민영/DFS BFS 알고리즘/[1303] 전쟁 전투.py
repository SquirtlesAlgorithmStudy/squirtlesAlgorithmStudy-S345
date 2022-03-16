from collections import deque
from itertools import count
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
list1 = []

data = [list(input().strip()) for _ in range(m)] #한 글자씩 저장
# print (data)

def dfs_W(x, y, cnt):
    if(y < 0 or y >= n) & (x < 0 or x >= m):
        return 0
    if visited[y][x] == 0 and data[y][x] == 'W':
        visited[y][x] = 1
        cnt += 1
        dfs_W(x-1, y, cnt)
        dfs_W(x+1, y, cnt)
        dfs_W(x, y-1, cnt)
        dfs_W(x, y+1, cnt)
        return cnt
    return 0

def dfs_B(x, y, cnt):
    if (y < 0 or y >= n) & (x < 0 or x >= m):
        return 0
    if visited[y][x] == 0 and data[y][x] == 'B':
        visited[y][x] = 1
        cnt += 1
        dfs_B(x-1, y, cnt)
        dfs_B(x+1, y, cnt)
        dfs_B(x, y-1, cnt)
        dfs_B(x, y+1, cnt)
        return cnt  
    return 0

countW = []
countB = []
visited = [[0] * m for _ in range(n)]
for i in range(m):
    for j in range(n):
        if dfs_W(i , j, 0) != 0:
            countW.append(dfs_W(i , j, 0))    

visited = [[0] * m for _ in range(n)]
for i in range(m):
    for j in range(n):
        if dfs_B(i , j, 0) != 0:
            countB.append(dfs_B(i , j, 0))
cntW = 0
cntB = 0
for i in countW:
    cntW += i**2
for i in countB:
    cntB += i**2
print(cntW, cntB)
