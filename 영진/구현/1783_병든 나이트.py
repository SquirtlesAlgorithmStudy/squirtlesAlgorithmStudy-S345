"""min(): 괄호 안의 값 중 가장 작은 값 출력"""

from sys import stdin
N,M=map(int,stdin.readline().rstrip().split())

if N==1:
    print(N)
elif N==2:
    print(min(4,(M+1)//2))
else:
    if M<=6:
        print(min(4,M))
    else:
        print(M-2)          