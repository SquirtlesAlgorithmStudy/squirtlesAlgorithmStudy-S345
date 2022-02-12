a = 1000
price = int(input())
mine = a - price
less = 0

k = [500, 100, 50, 10, 5, 1]

for coin in k:
    less = less + mine // coin
    mine = mine % coin

print(less)