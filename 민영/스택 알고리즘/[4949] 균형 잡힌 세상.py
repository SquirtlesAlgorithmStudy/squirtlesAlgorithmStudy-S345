'''
여는 괄호((, [)는 stack에 넣는다.
stack 有 & 닫힌 괄호가 나올 때 :
    stack[-1]과 짝이 맞으면 pop을 시키고 그렇지 않으면 print ("no") break
stack 無 & 닫힌괄호가 나오면 :
    정상적으로 짝이 맞지 않으므로 print ("no") break
flag == True이면서(정상적인 괄호) not stack이면 올바른 괄호열이고 반대의 경우는 올바르지 않은 괄호 열이다.
'''

import sys
fastin = sys.stdin.readline


def output(temp):
    stack = []
    key = True
    for i in temp:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ']':
            if (len(stack) != 0) and (stack[-1] == '['):
                stack.pop()         
            else:
                key = False
                break
        elif i == ')':
            if (len(stack) != 0) and (stack[-1] == '('):
                stack.pop()       
            else:
                key = False
                break
    if (key == True) and (len(stack) == 0) :
        print ("yes")
    else:
        print ("no")
    return 0

list1 = []
temp2 = []
temp2.append(fastin().rstrip())
'''
재귀함수를 만들어서 입력을 받으면 반복 연산량이 너무 많아짐 -> while 문 이용
'''
while (len(temp2[0]) != 1) and (temp2[0] != '.'):
    list1.extend(temp2)
    temp2 = []
    temp2.append(fastin().rstrip())
    
#print(temp2)

#print(list1)

num = len(list1)
#print(num)

for i in range(num):
    output(list1[i])
