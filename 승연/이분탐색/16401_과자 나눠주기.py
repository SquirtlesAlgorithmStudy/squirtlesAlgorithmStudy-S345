import sys
input = sys.stdin.readline

nephew, snack = map(int, input().split())

snacks = list(map(int, input().split()))

start = 1
end = max(snacks)

result = 0
while (start <= end):
    mid = (start+end)//2
    if sum([i//mid for i in snacks]) >= nephew:
        result = mid
        start = mid+1
    else:
        end = mid - 1

print(result)