from sys import stdin
N=int(input())
T_P=[list(map(int,stdin.readline().rstrip().split())) for _ in range(N)]

dp=[0]*(N+1)

for i in range(N):
    for j in range(i+T_P[i][0],N+1):
        if dp[j]<dp[i]+T_P[i][1]:
            dp[j]=dp[i]+T_P[i][1]
            
print(max(dp))