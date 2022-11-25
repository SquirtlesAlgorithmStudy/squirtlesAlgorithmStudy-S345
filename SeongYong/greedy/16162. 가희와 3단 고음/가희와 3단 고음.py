import sys; input = sys.stdin.readline

N,A,D = map(int, input().split())
notes = list(map(int, input().split()))
n=0


for i in range(N):
    val = A + D*n
    if notes[i] == val:
        n+=1

print(n)