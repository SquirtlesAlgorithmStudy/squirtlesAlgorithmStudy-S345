n,k = map(int, input().split())
result = 0
coin = list()

for i in range(n):
  if i == 0:
    coin.append(1)
  elif i!=0 and i%2 ==0:
    coin.append(coin[i-1]*2)
  else:
    coin.append(5*(10**(i//2)))

for j in range(n):
  print(coin[j])

coin.sort(reverse = True)


for x in coin:
  result += k // x
  k %=x

print(result)