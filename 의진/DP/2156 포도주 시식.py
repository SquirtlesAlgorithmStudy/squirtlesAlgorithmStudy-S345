import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]

if n == 1:
    print(wines[0])
    sys.exit()
elif n == 2:
    print(wines[0] + wines[1])
    sys.exit()

elif n == 3:
    print(max(max(wines[0], wines[1]) + wines[2], wines[0] + wines[1]))
    sys.exit()

dp = []

dp.append(wines[0])
dp.append(dp[0] + wines[1])
dp.append(max(wines[0], wines[1]) + wines[2])
dp.append(max(dp[0] + wines[2], dp[1]) + wines[3])

if n >= 4:
    for i in range(4, n):
        dp.append(max(dp[i-4] + wines[i-1], dp[i-3] +
                  wines[i-1], dp[i-2]) + wines[i])

print(max(dp[n-1], dp[n-2]))
