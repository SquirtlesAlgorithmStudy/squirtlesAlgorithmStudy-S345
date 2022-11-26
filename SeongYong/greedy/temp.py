import sys; input = sys.stdin.readline

N = int(input())
prob = []
for _ in range(N):
    prob.append(int(input()))

itter_val = max(prob)

li = [1, 1]
for i in range(itter_val):
    li.insert(i+2, li[i]+li[i+1])
    if li[i+2] > itter_val: break

i = 1
ans = []

for i in prob:
    ans = []
    for j in li[::-1]:
        if i - j >= 0:
            ans.append(j)
            i = i - j
        if i == 0: 
            for k in range(len(ans)-1, -1, -1):
                print(ans[k], end =' ')
            print()
            break

        
        
    
    









