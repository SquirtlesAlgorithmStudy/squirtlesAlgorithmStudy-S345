import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
holes = list(map(int, input().rstrip().split()))

holes.sort()
tapeRange = []
count = 0

for hole in holes:
    if hole not in tapeRange:
        tapeRange = [i for i in range(hole, hole + k)]
        count += 1

print(count)
