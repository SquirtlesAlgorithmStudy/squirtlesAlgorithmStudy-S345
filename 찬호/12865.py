import sys 

input = sys.stdin.readline

n,k = map(int,input().split())

w =[]
v =[]
for _ in range(n+1):
    ww,vv = map(int,input().split())
    w.append(ww)
    v.append(vv)

dp =[[0]*(k+1) for _ in range(n+1)]
# dp[i][j] -> when size of bag is i, maximum value when j-th stock was stored 
# Memoization 

for i in range(n+1):
    for j in range(k+1):
        if j<w[i]:
            dp[i][j] =dp[i-1][j]
        else:
            dp[i][j] =max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])

print(dp[n][k])
