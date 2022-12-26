from sys import stdin
N,A,D=notes = map(int, stdin.readline().rstrip().split()) ## N,A,D 입력
notes = list(map(int, stdin.readline().rstrip().split())) ## N 개의 정수 입력

X=0

for i in range(N):
    if notes[i]==A+(X*D):
        X+=1
print(X)