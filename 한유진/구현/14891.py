# https://www.acmicpc.net/problem/14891
from collections import deque
s = []
for _ in range(4):
    s.append(deque(list(input())))


K = int(input())
R = [list(map(int, input().split())) for _ in range(K)]

#왼쪽 톱니바퀴 확인
def left(num, direction): 
    if num < 0:
        return 
    if s[num][2] != s[num+1][6]:
        left(num-1, -direction)
        s[num].rotate(direction)

#오른쪽 톱니바퀴 확인
def right(num, direction): 
    if num > 3:
        return
    if s[num][6] != s[num-1][2]:
        right(num+1, -direction)
        s[num].rotate(direction)

for i in range(K):
    num = R[i][0] - 1
    direction = R[i][1]
    
    left(num-1, -direction)
    right(num+1, -direction)
    s[num].rotate(direction)

res = 0

if s[0][0] == '1':
    res += 1
if s[1][0] == '1':
    res += 2
if s[2][0] == '1':
    res += 4
if s[3][0] == '1':
    res += 8
    
print(res)
        

