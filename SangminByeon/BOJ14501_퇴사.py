from sys import stdin



n = int(stdin.readline().strip())
times = []
prices = []
dp = [0 for _ in range(n+1)]

for i in range(n):
    t,p = map(int,stdin.readline().strip().split())
    times.append(t)
    prices.append(p)

print(times, prices)

for i in range(n-1, -1, -1):
    if times[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[times[i] + i] + prices[i])

print(dp[0])

# pre_t = 0
# for i in range(n):
#     if times[i]-1 + pre_t <= i and i+times[i] <= n: #1일차 = index 0
#         pre_t = times[i]
#         if i>0:
#             benefits[i]=prices[i]+benefits[i-1]
#         else: benefits[i] = prices[i]

# print(benefits)
# print(max(benefits))





# def best_benefit(int i):
#     if i == 0:
#         return 0
#     if t[i] 
#         return best_benefit(i-1)