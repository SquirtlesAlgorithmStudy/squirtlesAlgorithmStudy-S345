h, k = map(int, input().split())
k=str(k)
count =0

hour=""
minute =""
second = ""

for i in range(h+1):
  if i<10:
    hour = '0'+str(i)
  else: 
    hour = str(i)
  for j in range(60):
    if j<10:
      minute ='0'+str(j)
    else: 
      minute = str(j)
    for s in range(60):
      if s<10:
        second='0'+str(s)
      else:
        second=str(s)
      if k in hour+minute+second:
        count+=1


print(count)