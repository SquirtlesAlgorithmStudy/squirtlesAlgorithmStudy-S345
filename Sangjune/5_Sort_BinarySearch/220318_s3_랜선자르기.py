import sys

fin = sys.stdin.readline

K, N = map(int, fin().split())
array = []

for _ in range(K):
    array.append(int(fin()))

start = 0
end = max(array)

result = 1
while(start <= end):
    cnt = 0
    mid = (start + end) // 2
    if mid == 0:
        break
    for x in array:
        cnt += x // mid
    if cnt < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)