#맨 마지막에 들어온 ] or ) 를 찾고 앞에서부터 [ or ( 찾기
#output = 0으로 저장 후 멈추는 실행 만들기
#list out of range?
import sys
fastin = sys.stdin.readline().rstrip()
string = []
output = [2] #yes는 1, no는 0으로 저장
cntstring = int(0)

while True:
    string = fastin
    if string == '.':
        break
    else:
        for i in range(len(string)-1):
            if string[-i] == ']':
                for k in range(len(string)):
                    if string[k] == '[':
                        string[k] = ' '
                        string [-i] = ' '
                        break
                    elif string[k] == '(':
                        output[cntstring] = 0
                        break
            elif string[-i] == ')':
                for k in range(len(string)):
                    if string[k] == '[':
                        string[k] = 'a'
                        string [-i] = 'a'
                        break
                    elif string[k] == '(':
                        output[cntstring] = 0
                        break
            elif i == len(string)-1:
                output[cntstring] = 1
                break
    cntstring += 1

for j in range(len(output)):
    if output(j) == 1:
        print("yes")
    elif output(j) == 0:
        print("no")