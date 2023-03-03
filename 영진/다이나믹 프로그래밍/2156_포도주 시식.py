# 조건에 맞을 경우, 특정 번째까지 마신 와인의 양을 저장해놓고 이용하므로 dp

n=int(input())
wine=[0]*n
for i in range(n):
    wine[i]=int(input())
dp=[0]*n

dp[0]=wine[0]
dp[1]=wine[0]+wine[1]
for i in range(2,n):
    dp[i]=max(dp[i-3]+wine[i]+wine[i-1],dp[i-2]+wine[i],wine[i-1])

print(max(dp))