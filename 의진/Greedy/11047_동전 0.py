import sys
fastin = sys.stdin.readline

n, k = map(int, fastin().split())
coinList = [int(fastin()) for _ in range(n)]
coinList.sort(reverse=True)


result = 0
for coin in coinList:
    result += (k // coin)
    k %= coin

print(result)
