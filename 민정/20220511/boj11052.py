import sys
fastin = sys.stdin.readline

n = int(fastin())
p = list(map(int, fastin().split()))
p.insert(0, 0)
price = [0 for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        price[i] = max(price[i], p[j] + price[i-j])
        
print(price[n])