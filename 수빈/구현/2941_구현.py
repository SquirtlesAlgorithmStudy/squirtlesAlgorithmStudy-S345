import sys
fastin = sys.stdin.readline

alpa = ['c=','c-','dz=','d-','lj','nj','s=','z=']

examp = fastin().rstrip()

for i in range(len(alpa)):
    if alpa[i] in examp:
        # print('alpa[i]', alpa[i])
        examp = examp.replace(alpa[i], '*')
        # print('examp: ',examp)
print(len(examp))
    