change = 1000 - int(input())
coin= [500, 100, 50, 10, 5, 1]
num_coin = 0
for i in coin:
    num_coin += change// i
    change %= i
print(num_coin)
