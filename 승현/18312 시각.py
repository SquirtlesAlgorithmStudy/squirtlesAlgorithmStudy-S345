n = int(input())
k = str(input())

cnt = 0
for i in range(n+1):
  for j in range(60):
      for p in range(60):
        i = str(i)
        j = str(j)
        p = str(p)
        if k in i.zfill(2)+j.zfill(2)+p.zfill(2):
          cnt += 1
print(cnt)



n,k = map(int, input().split())

count = 0
for i in range(n+1):
  if i < 10:
    pi = '0' +str(i)
  else:
    pi = str(i)
  for j in range(60):
    if j <10:
      pj = '0'+str(j)
    else :
      pj = str(j)
    for t in range(60):
      if t < 10:
        pt = '0'+str(t)
      else:
        pt = str(t)
      if str(k) in pi + pj + pt:
        count += 1

print(count)