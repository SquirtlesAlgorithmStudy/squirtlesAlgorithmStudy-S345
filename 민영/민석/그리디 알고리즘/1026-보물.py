n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=False)
b.sort(reverse=True)

k = 0

for i in range(n):
  k = k + int(a[i]) * int(b[i])

print(k)