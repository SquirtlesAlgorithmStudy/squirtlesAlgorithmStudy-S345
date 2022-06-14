import sys
fastin = sys.stdin.readline

sentences = []
inputString = ""
while(True):
    inputString = fastin().rstrip()
    if (inputString != '.'):
        sentences.append(inputString)
    else:
        break


for sentence in sentences:
    stack = []
    isOkay = True
    for character in sentence:
        if character == '(':
            stack.append('(')
        elif character == '[':
            stack.append('[')
        elif character == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                isOkay = False
                break
        elif character == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                isOkay = False
                break
    if len(stack) != 0:
        isOkay = False
    if isOkay:
        print('yes')
    else:
        print('no')
