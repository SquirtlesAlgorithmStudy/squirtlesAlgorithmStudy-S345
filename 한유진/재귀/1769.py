# https://www.acmicpc.net/problem/1769
n = input()
count = 0
while len(n) > 1:
    sum_int = 0
    for s in n:
        sum_int += int(s)
    # print(sum_int)
    count += 1
    n = str(sum_int)
print(count)
print("YES") if int(n) % 3 == 0 else print("NO") 
