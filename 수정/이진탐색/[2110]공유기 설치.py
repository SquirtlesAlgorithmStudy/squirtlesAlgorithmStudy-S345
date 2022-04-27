import sys
fastin = sys.stdin.readline

N, C= map(int, fastin().rstrip().split())

x = [0] * N
for i in range(N):
    x[i] = int(fastin().rstrip())

x.sort()
distance = []
for k in range(N-1):
    distance.append(x[k+1] - x[k])
start = 1
end = sum(distance)
maxvalue = start

while (start <= end):
    mid = (start + end) // 2
    d = 0
    c = 1
    for j in range(N-1):
        d += distance[j]
        if d > mid:
            d = distance[j]
            c += 1
    if c >= C:
        start = mid + 1
        maxvalue = mid
    else:
        end = mid - 1

print(maxvalue-1)