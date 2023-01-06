import sys
input = sys.stdin.readline

n, m = map(int, input().split())

if n == 1:
    print(1)

elif n == 2:
    print(min(4, (m // 2 + m % 2)))

else:
    if m > 5:
        print(m - 2)
    else:
        print(min(4, m))
