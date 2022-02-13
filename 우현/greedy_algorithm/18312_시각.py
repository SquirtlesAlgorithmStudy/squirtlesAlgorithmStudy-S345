n, k = map(int, input().split())

count = 0

for h in range(n+1):
  if h < 10:
    h = '0'+str(h)
  
  for min in range(60):
    if min < 10:
      min = '0'+str(min)
    
    for sec in range(60):
      if sec < 10:
        sec = '0'+str(sec)

      if str(k) in str(h)+str(min)+str(sec):
        count += 1

print(count)