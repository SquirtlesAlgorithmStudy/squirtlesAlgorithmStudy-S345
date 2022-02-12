# 1789

s = int(input())
real_s = 0
n = 0

while(True):
    n = n+1
    real_s = real_s + n
    if real_s > s:
        break
        
print(n-1)