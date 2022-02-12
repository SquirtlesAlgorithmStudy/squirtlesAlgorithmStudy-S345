S = int(input())
sum = 0
add = 1
N = 0

while(True):
    sum += add
    N += 1
    add += 1
    if sum == S:
        print(N)
        break
    if sum > S:
        N -= 1
        print(N)
        break
    else:
        continue
        
