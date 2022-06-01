from operator import le


leftMoney = 1000 - int(input())
count = 0
money = [500,100,50,10,5,1]
i = 0
while leftMoney >= 0:
    if i == len(money):
        break
    if leftMoney >= money[i] :
        leftMoney -= money[i]
        count += 1
    else:
        i += 1
print(count)
