import sys
n = int(sys.stdin.readline())
rope = []

for i in range(n):
  rope.append(int(input()))
rope.sort(reverse = True)

k = []
for j in range(1, n + 1):
  a = j * min(rope[0:j])
  k.append(a)
print(max(k))