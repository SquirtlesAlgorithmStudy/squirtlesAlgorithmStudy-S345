from collections import deque
queue =deque()
document =[]
while True:
  a=list(input())
  if a == ['.']:
    break
  document.append(a)

for i in document:
  result = "yes"
  queue=[]
  i.reverse()
  while len(i)!=0:
    b=i.pop()
    if (b=='(') or (b=='['):
      queue.append(b)
    elif b==']':
      if len(queue)==0:
        result = "no"
      elif queue[-1] != '[':
        result = "no"
      else:
        queue.pop()
        result ="yes"
    elif b==')':
      if len(queue)==0:
        result = "no"

      elif queue[-1] != '(':
        result = "no"
      else:
        queue.pop()
        result = "yes"

  if len(queue)>0:
    result ="no"

  print(result)