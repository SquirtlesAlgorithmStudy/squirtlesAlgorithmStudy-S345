from sys import stdin

n = int(stdin.readline().strip())
cards = list(map(int,stdin.readline().strip().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    for j in  range(i):
        dp[i] = max(dp[i], dp[i-j]+cards[j])


print(dp[n-3])