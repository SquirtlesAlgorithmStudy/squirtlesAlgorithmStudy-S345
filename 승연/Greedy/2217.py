import sys

data = []
new_data = {}
value_list = []
key_list = []

num = int(input())
for _ in range(num):
    data.append(int(sys.stdin.readline()))
after = 0

data.sort(reverse = True)

for i in range(len(data)):
    new_data[i] = data[i] * (i + 1)

for value in new_data.values():
    value_list.append(value)

print(max(value_list))