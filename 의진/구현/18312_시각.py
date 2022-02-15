import sys
fastin = sys.stdin.readline

n, k = map(int, fastin().rstrip().split())
zerostring = ''
result = 0
isZero = [0, 0, 0]
for i in range(n + 1):
    if i < 10:
        isZero[0] = 1
    for j in range(60):
        if j < 10:
            isZero[1] = 1
        for t in range(60):
            if t < 10:
                isZero[2] = 1
            if 1 in isZero:
                zerostring = '0'
            if str(k) in str(i) + str(j) + str(t) + zerostring:
                result += 1
            zerostring = ''
            isZero[2] = 0
        isZero[1] = 0
    isZero[0] = 0

print(result)
