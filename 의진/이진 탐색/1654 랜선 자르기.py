import sys
fastin = sys.stdin.readline

k, n = map(int, fastin().split())
lancables = [int(fastin()) for _ in range(k)]

start = 1
end = max(lancables)

while (start <= end):
    mid = (start + end) // 2
    if sum([lancable // mid for lancable in lancables]) >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
