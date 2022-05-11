import sys
input = sys.stdin.readline

stair = int(input().rstrip())
score = [0] * stair
for i in range(stair):
    score[i] = int(input().rstrip())

dp = [0] * stair
dp[0] = score[0]

if stair <= 2:
    print(sum(score))
else:
    dp[1] = dp[0] + score[1]
    for i in range(2, stair):
        dp[i] = max(score[i] + score[i-1] + dp[i-3], score[i] + dp[i-2])
    print(dp[stair-1])