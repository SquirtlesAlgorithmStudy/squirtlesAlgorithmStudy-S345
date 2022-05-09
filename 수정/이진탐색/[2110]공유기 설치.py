import sys
fastin = sys.stdin.readline

N, C= map(int, fastin().rstrip().split())

x = [0] * N
for i in range(N):
    x[i] = int(fastin().rstrip())

x.sort()
start = 1
end = max(x)
maxvalue = 0

while (start <= end):
    mid = (start + end) // 2
    d = x[0]
    c = 1
    for j in range(N):
        if x[j] >= d + mid:
            d = x[j]
            c += 1
    if c >= C:
        start = mid + 1
        maxvalue = mid
    else:
        end = mid - 1

print(maxvalue)