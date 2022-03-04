num = list(map(int, input()))


def multiple(a, cnt):
   
  if len(a)>1:
    sum = 0
    while len(a)!=0:
      sum += a.pop()
    a = list(map(int, str(sum)))
   
    return multiple(a, cnt+1)

  elif len(a)==1:
    
    if a[0]%3==0:
      print(cnt, "YES", sep='\n')
    else:
      print(cnt, "NO", sep ='\n')


multiple(num, 0)