import sys
fastin = sys.stdin.readline

n, k = map(int, fastin().rstrip().split())
cnt = 0

for i in range(n+1):
  if i<10:
    pi = '0'+str(i)
  else:
    pi = str(i)
  for j in range(60):
    if j<10:
      pj = '0'+str(j)
    else:
      pj = str(j)
    for t in range(60):
      if t<10:
        pt = '0'+str(t)
      else:
        pt = str(t)
      if str(k) in pi + pj + pt:
        cnt +=1

print(cnt)
    