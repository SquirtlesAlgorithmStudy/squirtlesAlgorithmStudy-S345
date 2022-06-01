# https://www.acmicpc.net/problem/4949

while True :
    S = input()
    # print(S)
    stack = []

    if S == '.':
        break
    
    for s in S:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif s == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break

    print('yes') if len(stack) == 0 else print('no')