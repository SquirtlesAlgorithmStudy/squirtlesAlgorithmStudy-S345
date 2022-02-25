# 11047

n, k = map(int, input().split())
coin = list()
count = 0

for i in range(n):
    coin.append(int(input()))
    
coin.sort(reverse=True)

for x in range(n):
    count = count + k//coin[x]
    k = k % coin[x]

print(count)