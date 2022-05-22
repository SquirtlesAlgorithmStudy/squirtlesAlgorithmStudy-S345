import copy
n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
b_index = [len(b)] * 0
for i in range(b - 1):
    if b[i] > b[i + 1]:
        b_index[i] += 1
    else:
        b_index[i + 1] += 1
print(b_index)

