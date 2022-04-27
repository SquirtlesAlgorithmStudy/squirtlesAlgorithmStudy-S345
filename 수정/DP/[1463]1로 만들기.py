import sys
fastin = sys.stdin.readline

N = int(fastin().rstrip())

d = [0] * (N+1)
for i in range(1, N+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[N] - 1)