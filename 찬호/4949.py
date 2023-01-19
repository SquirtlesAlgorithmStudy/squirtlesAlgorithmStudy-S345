while True:
    string = input()
    if string == '.':
        break
    stack = []
    temp = True
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] == '[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif char == ']':
            if not stack or stack[-1] == '(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == True and not stack:
        print('yes')
    else:
        print('no')