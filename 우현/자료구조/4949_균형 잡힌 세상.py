#a = 'So when I die (the [first] I will see in (heaven) is a score list).'

while True:
  stack = []
  bool_flag = 0
  a = input()
  if a == '.':
    break

  for i in a:
    if i == '(' or i == '[':
      stack.append(i) 
  
    if i == ')':
      if len(stack) == 0 or stack[-1] == '[':
        print("no")
        bool_flag = 1
        break
      else:
        stack.pop()

    if i == ']':
      if len(stack) == 0 or stack[-1] == '(':
        print("no")
        bool_flag = 1
        break
      else:
        stack.pop()

  if bool_flag == 0:
    if len(stack) == 0:
      print("yes")
    else:
      print("no")
