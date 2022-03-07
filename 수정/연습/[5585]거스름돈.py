pay = 1000 - int(input())
count = 0
coin = [500, 100, 50, 10, 5, 1]

for c in coin:
    count += pay // c
    pay %= c

print(count)