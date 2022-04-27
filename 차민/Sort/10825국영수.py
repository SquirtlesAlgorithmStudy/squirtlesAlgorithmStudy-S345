n = int(input())

a = []
for _ in range(n):
    name, korean, english, math = input().split()
    a.append((name, int(korean), int(english), int(math)))



for i in sorted(a, key = lambda x : (-x[1], x[2], -x[3], x[0])):