from sys import stdin

n = int(stdin.readline().rstrip())
input_list = list(map(int, stdin.readline().rstrip().split()))


count = 0
circle = 0

for i in range(n):
    circle = 0
    for j in range(i+1, n):
        if input_list[i] < input_list[j]:
            circle += 1
        elif input_list[i] > input_list[j]:
            count += circle

print(count)