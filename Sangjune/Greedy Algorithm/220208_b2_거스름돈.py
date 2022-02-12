import sys

pay = int(sys.stdin.readline())

n = 1000 - pay

money = [500, 100, 50, 10, 5, 1]
count = 0

for i in money:
    while n >= i:
        n -= i
        count += 1
        if n == 0: break

print(count)