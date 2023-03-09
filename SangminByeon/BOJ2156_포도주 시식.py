from sys import stdin

n = int(stdin.readline().strip())

glasses = []
dp = [0 for _ in range(n)]

for _ in range(n):
    glasses.append(int(stdin.readline().strip()))

if n == 1:
    print(glasses[0])
elif n == 2:
    print(glasses[0] + glasses[1])
elif n == 3:
    print(max(glasses[0] + glasses[1], glasses[0] + glasses[2], glasses[1] + glasses[2]))

for i in range(n):
    dp[i] = max(dp[n+3] + dp[n+1] + glasses[i], dp[n+3] + dp[n+2] + glasses[i], dp[n+2] + dp[n+1])

print(dp[0])