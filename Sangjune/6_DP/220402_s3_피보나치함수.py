import sys

fin = sys.stdin.readline
sys.setrecursionlimit(10**6)

nums = []
cnt_0 = []
cnt_1 = []

def fibonacci(idx, n):
    if n == 0:
        cnt_0[idx] += 1
        return 0
    elif n == 1:
        cnt_1[idx] += 1
        return 1
    else:
        return fibonacci(idx, n-1) + fibonacci(idx, n-2)

t = int(fin())

for i in range(t):
    nums.append(int(fin()))
    cnt_0.append(0)
    cnt_1.append(0)

for i in range(t):
    fibonacci(i, nums[i])
    print(cnt_0[i], cnt_1[i])