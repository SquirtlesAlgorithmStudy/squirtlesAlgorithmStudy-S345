# 5585

money = int(input())
pay = 1000
coin = [500, 100, 50, 10, 5, 1]
count = 0
change = pay - money 

for c in coin:
  count = count + change//c
  change = change % c
    
    
print(count)
    