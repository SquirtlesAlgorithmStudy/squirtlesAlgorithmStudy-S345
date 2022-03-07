#예제는 맞는데 "틀렸습니다" 왜 틀릴까?
import sys
fastin = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, K = map(int, fastin().split(' '))

if N > K:
    print(N - K)

if N == K:
    print(0)

else:
    count = 0
    while(N * 2 < K):
        N *= 2
        count += 1

    a = abs((N * 2) - K)
    b = abs(N - K)
    if a > b:
        if (abs(N - K) % 2) == 0:
            print(count + (abs(N - K) // 2))
        else:
            print(count + (abs(N - K) // 2) + 1)
    else:
        N *= 2
        count += 1
        if (abs(N - K) % 2) == 0:
            print(count + (abs(N - K) // 2))
        else:
            print(count + (abs(N - K) // 2) + 1)