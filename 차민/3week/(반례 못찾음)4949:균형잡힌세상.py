document =[]

while 1:
  a=list(input())
  if a == ['.']:
    break
  document.append(a)

for i in document:
  result = "yes"
  check=[]
  i.reverse()
  while len(i)!=0:
    b=i.pop()
    if b == '(' or b=='[':
      check.append(b)
    elif b==']':
      if len(check)==0:
        result ="no"
      elif check[-1] == '[':
        result = "yes"
        check.pop()
      else:
        result ="no"
        break
    elif b ==')':
      if len(check)==0:
        result = "no"
      elif check[-1] =='(':
        result ="yes"
        check.pop()
      else:
        result ="no"
        break

  print(result)
