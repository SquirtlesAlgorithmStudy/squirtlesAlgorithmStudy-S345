import sys
finput = sys.stdin.readline
N, K = map(int, finput().split())

K = str(K)
count = 0

for i in range(N + 1):
    i = str(i)
    if len(i) == 1:
        i = '0' + i
    for j in range(60):
        j = str(j)
        if len(j) == 1:
            j = '0' + j
        for k in range(60):
            k = str(k)
            if len(k) == 1:
                k = '0' + k
            time = i + j + k
            if K in time:
                count += 1

print(count)