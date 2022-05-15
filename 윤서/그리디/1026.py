# 1026 - 보물

import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().rsplit()))
b = list(map(int, input().rsplit()))

result = 0

for _ in range(N) :
    result += min(a) * max(b)
    a.remove(min(a))
    b.remove(max(b))
    
print(result)