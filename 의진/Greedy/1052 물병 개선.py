import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = 0

while bin(n).count('1') > k:
    first_one_index = bin(n)[::-1].index('1')
    result += 2 ** first_one_index
    n += 2 ** first_one_index

print(result)
