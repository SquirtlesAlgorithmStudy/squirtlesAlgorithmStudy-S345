#포도잔 수 
n = int(input())
#포도주 양 
drink =[0]
for i in range(n):
  drink.append(int(input()))

d = [0]*100

d[1] = drink[1]

if n>1:
  d[2] = drink[1] + drink[2]

for i in range(3,n+1):
  d[i] = max(d[i-1], d[i-3]+drink[i-1]+drink[i], d[i-2]+drink[i])

print(d[n])  

# n = int(input())
# w = [0]
# for i in range(n):
#     w.append(int(input()))
# dp = [0]
# dp.append(w[1])
# if n > 1:
#     dp.append(w[1] + w[2])
# for i in range(3, n + 1):
#     dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
# print(dp[n])