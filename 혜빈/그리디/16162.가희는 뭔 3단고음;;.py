import sys

input=sys.stdin.readline

count=0

n,A,D=map(int,input().rstrip().split())

test=A

notes=list(map(int,input().rstrip().split()))

for note in notes:
    if note==test:
        count=count+1
        test=test+D

print(count)        




