import sys
fastin = sys.stdin.readline

T = int(fastin().rstrip())

N = [0] * T
for i in range(T):
    N[i] = int(fastin().rstrip())

<<<<<<< HEAD
d = [0] * (2 ^ 40)

=======
d = [0] * (2**40)
>>>>>>> 5f00f29b9044fb0d22befe560d50beaaa7fac2e1

def fibo(x):
    x = int(x)
    if x == 0:
        return [1, 0]
    if x == 1:
        return [0, 1]
    if x == 2:
        return [1, 1]
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]


for i in range(T):
    a = fibo(N[i])
    count0 = 0
    count1 = 0
    for k in range(len(a)):
        if k % 2 == 0:
            count0 += a[k]
        else:
            count1 += a[k]
    print(count0, count1)
