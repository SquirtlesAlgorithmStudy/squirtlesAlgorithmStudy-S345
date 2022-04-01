import sys

fin = sys.stdin.readline
sys.setrecursionlimit(10**6)

dp = [0] * 41

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    if dp[n] != 0:
        return dp[n]

    dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]

t = int(fin())
for i in range(t):
    n = int(fin())
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(fibonacci(n - 1), fibonacci(n))