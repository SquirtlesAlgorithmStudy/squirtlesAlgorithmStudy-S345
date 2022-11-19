from sys import stdin

n, l = map(int, stdin.readline().rstrip().split())
pipe = list(map(int, stdin.readline().rstrip().split()))
pipe.sort()

cover = pipe[0] + l - 0.5
cnt = 1

for hole in pipe:
  if hole <= cover: continue
  cover = hole + l - 0.5
  cnt+=1

print(cnt)