while 1:
  line = input()
  if line == '.': # 입력받은 문장이 . 이면 종료
    break
  a = []
  for i in line:
    if i == '(': # (일 때 스택 추가
      a.append('(')
    elif i == ')': # )일 때 스택이 비어있거나 (가 없으면 종료, 있다면 (제거
      if not a or a[-1] != '(':
        a.append(')')
        break
      else:
        a.pop()
       
          
    elif i == '[':
      a.append('[')
    elif i == ']':
      if not a or a[-1] != '[':
        a.append(']')
        break
      else:
        a.pop()

  if not a: #스택이 비어있을 경우 yes 출력 
    print ('yes')
  else:
    print('no')
