#입력받기
n,k = map(int,input().split())
num=[]
for i in range(n):
  num.append(int(input()))

#dp 생성
dp=[]
for i in range(k+1):
  dp.append(i)
print(dp)

dp[0] = 1
print(dp)

for i in num:
  for j in range(1, k+1):
    if j-i >=0:
      dp[j] +=dp[j-i]

print(dp[k])
