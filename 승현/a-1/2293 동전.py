import sys
input = sys.stdin.readline

n, won = map(int, input().split())
wons =[0] * (n+1)
r = [0] * (n+1)
for i in range(1,n+1):
  wons[i] = int(input())

dp = [0] * (n+1)
dp[0] = 0
dp[1] = wons[1]