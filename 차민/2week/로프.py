n = int(input())
w = []
max_m=[]

for i in range(n):
  w.append(int(input()))

w.sort(reverse=True)
for i in range(len(w)):
  max_m.append((i+1)*w[i])

max_m.sort(reverse=True)
print(max_m[0])