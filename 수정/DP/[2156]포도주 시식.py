import sys
input = sys.stdin.readline

n = int(input().rstrip())
wine = [0] * n
for i in range(n):
    wine[i] = int(input().rstrip())

dp = [0] * n
dp[0] = wine[0]

if n <= 2:
    print(sum(wine))
elif n == 3:
    print(max(wine[2] + max(wine[0], wine[1]), wine[1] + wine[0]))
else:
    dp[1] = wine[1] + wine[0]
    dp[2] = max(wine[2] + max(wine[0], wine[1]), wine[1] + wine[0])
    for i in range(3, n):
        dp[i] = max(wine[i] + wine[i-1] + dp[i-3], wine[i] + wine[i-1] + dp[i-4], wine[i] + dp[i-2])
    print(max(dp))