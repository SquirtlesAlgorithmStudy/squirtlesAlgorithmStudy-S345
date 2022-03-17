import sys
fastin = sys.stdin.readline

m, n = map(int, fastin().split())
snack = fastin().split()
snack_int = list(map(int, snack))

start, end = 1, max(snack_int)

while start<=end:
    mid = (start+end)//2
    cnt = 0  #막대 과자의 수
    for i in snack_int:
        cnt += i//mid
    if cnt >= m:
        start = mid+1
    else:
        end = mid-1


print(end)