N,K=map(int,input().split())
coin=[]
for i in range(N):
    coin.append(int(input()))
coin.sort(reverse=True)

num_coin=0
for i in coin:
    if K>=i:
        num_coin+=K//i
        K%=i

print(num_coin)
