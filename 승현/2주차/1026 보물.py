n = int(input())

a = list(map(int,input().split()))
b = list(map(int, input().split()))
sum = 0

a.sort()

for i in range(n):
  sum += a[i] * max(b)
  b.remove(max(b))

print(sum)  