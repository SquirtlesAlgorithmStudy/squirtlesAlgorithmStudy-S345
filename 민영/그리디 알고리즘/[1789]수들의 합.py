Sum = int(input())
count = 0
rest = Sum
for i in range (1, Sum + 1):
    if (Sum - i) > i :
        Sum -= i
        count += 1
    elif(Sum - i) ==0:
        count += 1
        break
    else:
        continue

print(count)
