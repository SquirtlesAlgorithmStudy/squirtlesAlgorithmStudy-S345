import sys
input = sys.stdin.readline

N, M = map(int, input().split())

data = [0] * M


def dfs(depth):
    global data
    if depth == M:
        for i in range(1, N+1):
            data[depth-1] = i
            for item in data:
                print(item, end=" ")
            print("")
    else:
        for i in range(1, N+1):
            data[depth-1] = i
            dfs(depth + 1)


dfs(1)
