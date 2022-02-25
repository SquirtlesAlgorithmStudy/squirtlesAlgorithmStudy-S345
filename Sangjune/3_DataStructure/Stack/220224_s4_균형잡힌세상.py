import sys

fin = sys.stdin.readline

s = []
stack = []

while True:
    s.append(fin().rstrip().rstrip())
    if s[-1] == ".":
        s.pop()
        break

for line in s:
    result = True
    for i in range(len(line) - 1): # 마지막 점은 무시
        # print(line[i])
        if line[i] == "(":
            stack.append(0)
        elif line[i] == "[":
            stack.append(1)
        elif line[i] == ")" and stack:
            if stack[-1] == 0: stack.pop()
            else: result = False
        elif line[i] == "]" and stack:
            if stack[-1] == 1: stack.pop()
            else: result = False
    if not stack and result: # 차있으면 true, empty list는 false
        print('yes')
    else:
        print('no')
    stack.clear()