#시도1 - 런타임 에러

import sys
input = sys.stdin.readline

l = int(input())
arr = [int(input()) for _ in range(l)]
dp = []

dp.append(arr[0])
dp.append(max(arr[0]+arr[1], arr[1]))
dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))

for i in range(3, l):
    dp.append(max(dp[i-2]+arr[i], dp[i-3]+arr[i]+arr[i-1]))
    
print(dp.pop())


#시도2 - 정답
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])