#카드팩 가짓수 
N = int(input())
p = list(map(int,input().split()))
P = [0] + p

#dp 생성
dp = []
for i in range(N+1):
  dp.append(i)

#최댓값 구하기 
for i in range(1,N+1):
  for j in range(1,i+1):
    dp[i] = max(dp[i], dp[i-j]+P[j])

print(dp[i])
