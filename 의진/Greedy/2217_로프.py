import sys
fastin = sys.stdin.readline
n = int(fastin())
lopes = [int(fastin()) for _ in range(n)]

lopes.sort()

result = 0
for i in range(len(lopes)):
    result = max(result, lopes[i] * (len(lopes) - i))
print(result)
