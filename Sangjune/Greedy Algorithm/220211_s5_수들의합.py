import sys

s = int(sys.stdin.readline())
num = 1
sum = 0

for i in range(s):
    sum += num
    num += 1
    if s < sum:
        print(i)
        break