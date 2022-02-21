import sys
fastin = sys.stdin.readline

N = int(fastin().rstrip())
K = [int(fastin().rstrip()) for i in range(N)]

K.sort(reverse=True)
Max = K[0]
for i in range(1, N+1):
    if i * K[i-1] > Max:
        Max = i * K[i-1]
print (Max)
