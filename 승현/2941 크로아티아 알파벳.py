a = input()
cnt = len(a)


for i in range(cnt):
  if a[i] == '=':
    if a[i-1] == 'c' or a[i-1] =='s':
      cnt -= 1
      
    elif a[i-1] == 'z':
      if a[i-2] == 'd':
        cnt-= 2
      else:
        cnt -= 1
        continue
  elif a[i] == '-':
    if a[i-1] == 'c' or a[i-1] =='d':
      cnt -= 1
      
  elif a[i] == 'j':
      if a[i-1] == 'l' or a[i-1] == 'n':
        cnt -= 1
        

print(cnt)