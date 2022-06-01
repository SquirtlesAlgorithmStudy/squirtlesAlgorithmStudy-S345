# 4949 - 균형잡힌 문자열


import sys
input = sys.stdin.readline

sList = []

while True :                    # .이 입력될 때까지 실행
    string = input().rstrip()   # rstrip()이 없으면 .을 입력했을 때 반복문 종료되지 않음

    if string == '.' :          # 종료조건인 .이 입력되는 경우 while문 빠져나옴
        break
    stack = []

    for i in string:
        if i =='.':
            break
        elif i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")
