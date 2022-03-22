import sys
input = sys.stdin.readline

m, n = map(int, input().split())
cookies = list(map(int, input().split()))


start = 1
end = max(cookies)
result = 0

while (start <= end):
    mid = (start + end) // 2
    if sum([cookie // mid for cookie in cookies]) >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
