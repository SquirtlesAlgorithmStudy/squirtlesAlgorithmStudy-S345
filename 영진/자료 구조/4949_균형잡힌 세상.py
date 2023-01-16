import sys
input = sys.stdin.readline
while True:
    stack = []

    script = input()
    if script == '.':
        break

    for ch in script:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)
        elif ch == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(ch)

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
