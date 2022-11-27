from sys import stdin

n, a, d = map(int, stdin.readline().rstrip().split())
notes = list(map(int, stdin.readline().rstrip().split()))

x = 0

for note in notes:
    if note == a+(x*d):
        x+=1

print(x)