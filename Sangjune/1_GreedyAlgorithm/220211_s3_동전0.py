import sys

n, k = map(int, sys.stdin.readline().split())
value = []
count = 0

for i in range(n):
    temp = int(sys.stdin.readline())
    if temp <= k:
        value.append(temp)

for m in reversed(value):
    if k >= m:
        count += k // m
        k = k % m
    if k == 0:
        break

print(count)