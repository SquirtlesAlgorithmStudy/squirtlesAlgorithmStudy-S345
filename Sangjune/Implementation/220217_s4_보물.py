import sys

finput = sys.stdin.readline
n = int(finput())
A = list(map(int, finput().split()))
B = list(map(int, finput().split()))
result = 0

A.sort()
TempArr = sorted(B, reverse=True)

for i in range(n):
    result += A[i] * TempArr[i]

print(result)