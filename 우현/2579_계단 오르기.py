stair_num = int(input())

stairs = [0 for i in range(301)]
dp = [0 for i in range(301)]

for i in range(stair_num):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[1]+stairs[2], stairs[0]+stairs[2])

for i in range(3, stair_num):
    dp[i] =  max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])
print(dp[stair_num-1])
