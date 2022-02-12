coin = [500, 100, 50, 10, 5, 1]
pay = 1000

change = 1000 - int(input())

cnt = 0

for i in coin:
  cnt += change // i
  change %= i
  

print(cnt)