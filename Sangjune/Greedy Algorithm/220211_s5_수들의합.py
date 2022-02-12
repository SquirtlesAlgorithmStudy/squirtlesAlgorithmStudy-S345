import sys

s = int(sys.stdin.readline())
num = 1
S = 0

for i in range(s):
    S += num
    num += 1
    if s < S:
        print(i)
        break