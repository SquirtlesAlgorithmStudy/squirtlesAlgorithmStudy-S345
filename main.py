n = int(input())

data = []
for _ in range(n):
    name, korean, english, math = input().split()
    data.append((name, int(korean), int(english), int(math)))



for i in sorted(data, key = lambda x : (-x[1], x[2], -x[3], x[0])):
    print(i[0])
