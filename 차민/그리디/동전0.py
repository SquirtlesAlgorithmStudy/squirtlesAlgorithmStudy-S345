n,k = map(int, input().split())
result = 0
coin = list()

for i in range(n):
  coin.append(int(input()))

coin.sort(reverse = True)


for x in coin:
  result += k // x
  k %=x

print(result)