import sys
fastin = sys.stdin.readline

n = int(fastin())
n = 1000 - n
result = 0
coinList = [500, 100, 50, 10, 5, 1]

for coin in coinList:
  result += (n // coin)
  n %= coin

print(result)