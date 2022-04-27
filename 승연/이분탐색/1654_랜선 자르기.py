import sys
input = sys.stdin.readline

rans = []
ran_before, ran_after = map(int, input().split())
for i in range(ran_before):
    rans.append(int(input()))

start = 1
end = max(rans)

#result = 0
while (start <= end):
    mid = (start+end)//2
    if sum([i//mid for i in rans]) >= ran_after:
        result = mid
        start = mid+1
    else:
        end = mid - 1

print(result)