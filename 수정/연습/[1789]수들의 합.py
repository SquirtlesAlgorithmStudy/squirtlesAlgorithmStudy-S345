S = int(input())
count = 0
for i in range(1,S):
    S -= i
    if S < 0:
        break
    elif S == 0:
        count += 1
        break
    count += 1
print(count)