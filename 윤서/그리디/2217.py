import sys
input = sys.stdin.readline
n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort()

result = 0
for i in range(len(ropes)):
    result = max(result, ropes[i] * (len(ropes) - i))
print(result)