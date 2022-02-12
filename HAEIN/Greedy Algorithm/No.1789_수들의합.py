N = 0
S = int(input())
result = 0

while S >= 0:
  N += 1
  S -= N

print(N-1)