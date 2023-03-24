N=int(input())

dp=[[0 for _ in range(3)] for _ in range(N+1)]
cost=[]
for _ in range(N):
    cost.append(list(map(int,input().split())))
    
for i in range(1,N+1):
    for j in range(3):
        dp[i][j]=min(dp[i-1][(j+1)%3]+cost[i][j],dp[i-1][(j+2)%3]+cost[i][j])
        
print(min(dp[N]))