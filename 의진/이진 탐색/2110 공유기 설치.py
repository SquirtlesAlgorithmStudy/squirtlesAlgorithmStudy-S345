import sys
fastin = sys.stdin.readline

n, c = map(int, fastin().strip().split())
home = [int(fastin().strip()) for _ in range(n)]
home.sort()
start = 0
end = home[-1]-home[0]
result = 0
while(start <= end):
    mid = (start + end) // 2
    present = home[0]
    cnt = c-1
    ccnt = 0
    for i in range(1, n):
        if(home[i] - present >= mid):
            present = home[i]
            cnt -= 1
            if (cnt == 0):
                result = mid
                start = mid + 1
                break
        ccnt += 1
    if (ccnt == n-1):
        end = mid-1

print(result)
