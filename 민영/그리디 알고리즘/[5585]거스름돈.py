price = int(input())
count = 0

a = [500, 100, 50, 10, 5, 1]

change = 1000 - price

for i in range (6) :
    if change == 0: break
    elif change >= a[i] :
        count += change // a[i]
        change = change % a[i]
    else:
        continue

print(count)
