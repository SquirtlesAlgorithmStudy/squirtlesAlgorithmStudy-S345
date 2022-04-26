d = [0]*100


def fibo(x):
  if x==0 :
    cnt[0] = cnt[0]+1

    return 0
  if x==1 :
    cnt[1] = cnt[1]+1

    return 1

  d[x] = fibo(x-1)+fibo(x-2)
  
  return d[x]

tc = int(input())
x = []

for i in range(tc):
  x.append(int(input()))

a=0
b=0
for j in x:
  cnt = [0]*2
  fibo(j)

  print(cnt[0], cnt[1])

  