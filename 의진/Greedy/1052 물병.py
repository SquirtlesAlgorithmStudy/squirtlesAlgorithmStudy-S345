import sys
input = sys.stdin.readline

n, k = map(int, input().split())


def find_one(n):
    one_count = 0
    while n != 0:
        one_count += (n % 2)
        n //= 2
    return one_count


result = 0
while True:
    one_count = find_one(n)
    if one_count <= k:
        print(result)
        break
    n += 1
    result += 1
