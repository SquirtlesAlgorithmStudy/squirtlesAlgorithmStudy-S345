import sys

finput = sys.stdin.readline
N = int(finput())
ropes = []

for i in range(N):
    ropes.append(int(finput()))

ropes.sort(reverse=True)

print(max(ropes[i] * (i + 1) for i in range(N)))