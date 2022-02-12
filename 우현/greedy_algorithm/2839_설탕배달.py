# 2839

kg = int(input())
count = 0
x=1

while(kg >=0):
    if kg%5 == 0:
        count = count + kg//5
        print(count)
        break
    kg = kg - 3
    count = count + 1
else:
    print(-1)
        