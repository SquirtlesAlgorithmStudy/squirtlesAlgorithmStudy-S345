import sys

fin = sys.stdin.readline

M, N = map(int, fin().split())
array = list(map(int, fin().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    cnt = 0
    mid = (start + end) // 2
    if mid == 0:
        break
    for length in array:
        cnt += length // mid
    if cnt < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)