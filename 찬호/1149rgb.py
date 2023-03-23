import sys

input = sys.stdin.readline 

n = int(input())

#House 
h = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]


for i in range(n):
    dp[i][0] = min(h[i-1][1],h[i-1][2])
    dp[i][1] = min(h[i-1][0],h[i-1][2])
    dp[i][2] = min(h[i-1][0],h[i-1][1])


print(min(dp[n]))