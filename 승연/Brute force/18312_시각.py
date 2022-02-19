import sys
input = sys.stdin.readline

N, K = map(int,input().split())
count = 0
K = str(K)
for i in range(N+1):
    if i < 10:
        i = '0' + str(i)
    for j in range(60):
        if j < 10:
            j = '0' + str(j)
        for t in range(60):
            if t < 10:
                t = '0' + str(t)
            if K in str(i) + str(j) + str(t):
                count += 1
print(count)