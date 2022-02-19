import sys

data = []

num = int(input())
for _ in range(num):
    data.append(int(sys.stdin.readline()))
after = 0

data.sort(reverse = True)

for i in range(len(data)):
    data[i] = data[i] * (i + 1)

print(max(data))