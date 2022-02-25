from inspect import stack
import sys
fastin = sys.stdin.readline

while 1:
    reading = fastin().rstrip()
    stack = []
    true_flag = 1
    for cha in reading:
        if cha =='(' or cha =='[':
            stack.append(cha)
        elif cha == ')':
            if stack and stack[-1] =='(':
                stack.pop()
            else:
                true_flag =0
                break
        elif cha ==']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                true_flag = 0
                break
    if reading=='.':
        break
    print("yes" if true_flag and not(stack) else "no")