import sys

fin = sys.stdin.readline

num_stair = int(fin())

dp = [0] * 301
score = [0] * 301

for i in range(num_stair):
    # score.append(int(fin()))
    score[i + 1] = int(fin())

dp[1] = score[1]
dp[2] = score[1] + score[2]
dp[3] = max(score[1], score[2]) + score[3]

for i in range(4, num_stair + 1):
    dp[i] = max(dp[i - 2], dp[i - 3] + score[i - 1]) + score[i]

print(dp[num_stair])

# 왜 (num_stair + 1)만큼 리스트 생성하면 안되지?