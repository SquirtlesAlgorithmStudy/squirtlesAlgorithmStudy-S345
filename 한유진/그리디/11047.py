n , k = map(int,input().split())
coin = list()
for _ in range(n):
    coin.append(int(input()))
count = 0
i = -1
while k > 0 :
    c =  k // coin[i]
    k = k % coin[i]
    if c > 0:
        count += c
    i -= 1
print(count)