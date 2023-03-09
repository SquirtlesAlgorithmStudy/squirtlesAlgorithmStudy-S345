import sys
input = sys.stdin.readline

N = int(input())
counsels = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (N+1)
data = [[] for _ in range(N+1)]

for day, counsel in enumerate(counsels):
    if (day + counsel[0]) < N+1:
        data[day + counsel[0]].append((day, counsel[0], counsel[1]))

for i in range(N+1):
    dp[i] = dp[i-1]
    for item in data[i]:
        dp[i] = max(dp[i], dp[item[0]] + item[2])

print(dp[N])
