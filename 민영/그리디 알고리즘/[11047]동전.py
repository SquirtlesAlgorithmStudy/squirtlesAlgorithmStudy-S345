n, k= input().split()
n = int(n)
k = int(k)
count = 0

a = []

for i in range(n): # 원소의 개수가 n개일 때 
    a.append(int(input()))
   
for i in range (n-1, -1 , -1) :
    if k == 0: break
    elif k >= a[i] :
        count += k // a[i]
        k = k % a[i]
    else:
        continue

print(count)
