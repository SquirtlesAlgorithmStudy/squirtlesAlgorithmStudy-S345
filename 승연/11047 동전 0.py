N, K = map(int, input().split())
CoinType = []
NumCoin = 0

for i in range(N):
    CoinType.append(int(input()))

#동전 종류 내림차순으로 정렬
CoinType.sort(reverse=True)

for i in range(N):
    if K >= CoinType[i]:
        NumCoin += (K // CoinType[i])
        K %= CoinType[i]
        
print(NumCoin)