import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

dp = [0] * (k+1)

for i in coin:
    for j in range():
        dp[i]