# 11047 - 동전 0

n, k = map(int,input().split())
coin = []
count = 0

for i in range(n) :
    c = int(input())
    coin.append(c)
coin.reverse()              #최소 개수 구하기 위해 내림차순 정렬

for i in coin[0:] :
    count += k // i
    k = k % i               #나머지
print(count)