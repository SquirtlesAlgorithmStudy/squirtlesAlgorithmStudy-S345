import sys
fastin = sys.stdin.readline
#입력
N = int(fastin().rstrip())
A = list(map(int, fastin().rstrip().split()))
B = list(map(int, fastin().rstrip().split()))

#print (A, B)

Aset = sorted(A) #오름차순
Bset = sorted(B, reverse = True) #내림차순

Bw = [-1 for i in range(N)]
count = 0
add = -1
for i , j in enumerate(Bset):
    for k in range(N):
        if (j == B[k]) & (Bw[k]== -1):
            Bw[k] = i
            break
Atemp = []
for i in Bw:
    Atemp.append(Aset[i])

#print (A, Aset, Atemp)
#print (B, Bset, Bw)
    
Sum = 0
for i in range (N):
    Sum += Atemp[i]*B[i]

print(Sum)    