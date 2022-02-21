n,k = map(int, input().split())


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