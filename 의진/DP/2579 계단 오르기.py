import sys
input = sys.stdin.readline

n = int(input())
a = [0]
stairs = [int(input()) for _ in range(n)]
stairs = a + stairs

dp = [(0, 0)] * (n+1)
dp[1] = (stairs[1], 0)

for i in range(2, n+1):
    if dp[i-2][0] >= dp[i-1][0] or dp[i-1][1] == 1:
        dp[i] = (dp[i-2][0] + stairs[i], 0)
    else:
        dp[i] = (dp[i-1][0] + stairs[i], dp[i-1][1] + 1)
print(dp[n][0])
