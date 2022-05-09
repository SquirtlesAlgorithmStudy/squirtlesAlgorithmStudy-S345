#계단 수 
n = int(input())
#점수  
arr = []
for i in range(n):
  arr.append(list(map(int,input().split())))


#dp 생성
dp = []
index = 0
for i in range(n):
  dp[index:index+3]=arr[index:index+3]
  index +=3

  
#dp 진행
for j in range(1,n):
  for i in range(3):
      if i ==0: 
        dp[j][i] = min(arr[j][i]+dp[j-1][i+1], arr[j][i]+dp[j-1][i+2])
      elif i==1:
        dp[j][i] = min(arr[j][i]+dp[j-1][i-1], arr[j][i]+dp[j-1][i+1])
      else : 
        dp[j][i] = min(arr[j][i]+dp[j-1][i-1], arr[j][i]+dp[j-1][i-2])

  
  

result = min(dp[n-1][0], dp[n-1][1], dp[n-1][2])
print(result)
      