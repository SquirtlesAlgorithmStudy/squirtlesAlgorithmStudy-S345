import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
zeroString = ''
result = 0
zero = [0, 0, 0]
for i in range(n + 1):
    if i < 10:
        zero[0] = 1
    for j in range(60):
        if j < 10:
            zero[1] = 1
        for t in range(60):
            if t < 10:
                zero[2] = 1
            if 1 in zero:
                zeroString = '0'
            if str(k) in str(i) + str(j) + str(t) + zeroString:
                result += 1
            zerostring = ''
            zero[2] = 0
        zero[1] = 0
    zero[0] = 0

print(result)
