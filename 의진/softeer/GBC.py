import sys
from itertools import accumulate
input = sys.stdin.readline

# Input
N, M = map(int, input().split())
spec_data = [tuple(map(int, input().split())) for _ in range(N)]
test_data = [tuple(map(int, input().split())) for _ in range(M)]

# (interval_length, speed_limit)

# Get spec_boundary and test_boundary
spec_boundary = list(accumulate([i[0] for i in spec_data]))
test_boundary = list(accumulate([i[0] for i in test_data]))

# Get Result_dict
result_dict = {}
pointer = 0
for data in zip(test_boundary, [i[1] for i in test_data]):
    buffer_list = []
    buffer_list.append(pointer)
    while data[0] > spec_boundary[pointer]:
        pointer += 1
        buffer_list.append(pointer)
    if data[0] == spec_boundary[pointer]:
        pointer += 1

    result_dict[data] = buffer_list

# Calculate Result
result = 0

for test_data, intervals in result_dict.items():
    for interval_idx in intervals:
        result = max(result, max(test_data[1] - spec_data[interval_idx][1], 0))

print(result)
