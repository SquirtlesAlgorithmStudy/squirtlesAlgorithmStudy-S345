import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

count = 0
for index, first_element in enumerate(sequence):
    value = 0
    for second_element in sequence[index + 1:]:
        if first_element < second_element:
            value += 1
        elif first_element > second_element:
            count += value
print(count)
