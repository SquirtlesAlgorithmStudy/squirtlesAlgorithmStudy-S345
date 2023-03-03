n=int(input())
wine=[0]*(n)
for i in range(n):
    wine[i]=int(input())
dp=[0]*(n)

dp[0]=wine[0]
dp[1]=wine[0]+wine[1]

for i in range(2,n):
    dp[i]=max(wine[i]+wine[i-1]+dp[i-3],wine[i]+dp[i-2],wine[i-1])

print(max(dp))