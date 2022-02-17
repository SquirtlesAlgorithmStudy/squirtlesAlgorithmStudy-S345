import sys
fastin = sys.stdin.readline
n = int(fastin())
a = list(map(int, fastin().rstrip().split()))
b = list(map(int, fastin().rstrip().split()))

a.sort()
b.sort(reverse=True)

result = 0

for i in range(n):
    result += (a[i] * b[i])

print(result)
