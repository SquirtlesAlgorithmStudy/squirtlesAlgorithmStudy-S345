import sys

fastin = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0
k = str(k)
for i in range(n+1):
    if i<10:
        i = '0' + str(i)
    for j in range(60):
        if j < 10:
            j = '0' + str(j)
        for t in range(60):
            if t < 10:
                t = '0'+str(t)
            if k in str(i) + str(j)+str(t):
                cnt += 1

print(cnt)