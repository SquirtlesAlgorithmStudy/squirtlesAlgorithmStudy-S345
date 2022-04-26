import sys
fastin = sys.stdin.readline

T = int(fastin().rstrip())

N = [0] * T
for i in range(T):
    N[i] = fastin().rstrip()

d = [0] * (2^40)
d[0] = 0
d[1] = 1
d[2] = 1
count0 = 0
count1 = 0

for i in range(T):
    for i in range(N):
        d[i] = d[i-1] + d[i-2]
        if i == 0:
            count0 += 1
        if i == 1:
            count1 += 1
    print(count0, count1)
    d = [0] * (2^40)
    count0 = 0
    count1 = 0
