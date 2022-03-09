n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0

for i in range(n):
  result += a.pop(a.index(max(a))) * b.pop(b.index(min(b)))

print(result)