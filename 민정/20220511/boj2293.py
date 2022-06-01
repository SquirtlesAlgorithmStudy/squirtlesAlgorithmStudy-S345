import sys
fastin = sys.stdin.readline

n, k = map(int, fastin().split())
c = []
noc = [0 for i in range(k+1)]
noc[0] = 1

for i in range(n):
    c.append(int(fastin()))
    
for i in c:
    for j in range(1, k+1):
        if j - i >= 0:  noc[j] += noc[j-i]
        
print(noc[k])