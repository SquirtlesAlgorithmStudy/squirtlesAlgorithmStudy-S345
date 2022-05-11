import sys
input = sys.stdin.readline

N = int(input().rstrip())
P = list(map(int,input().rstrip().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    for k in range(1, i + 1):
        dp[i] = max(dp[i-k] + P[k - 1], dp[i])

print(dp[N])