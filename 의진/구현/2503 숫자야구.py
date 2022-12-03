from itertools import permutations
import sys

input = sys.stdin.readline
n = int(input())
input_datas = [tuple(input().rstrip().split()) for _ in range(n)]

# input_data = (number, strike_num, ball_num)


def filter(input_data, all_numbers):
    survived_numbers = []
    for number in all_numbers:
        strike = 0
        ball = 0

        for index, tuple_item in enumerate([(1, 2), (0, 2), (0, 1)]):
            if input_data[0][index] == number[index]:
                strike += 1
            if input_data[0][index] == number[tuple_item[0]] or input_data[0][index] == number[tuple_item[1]]:
                ball += 1
        if strike == int(input_data[1]) and ball == int(input_data[2]):
            survived_numbers.append(number)
    return survived_numbers


def tuple_to_number(tuple_item):
    buffer = ""
    for element in tuple_item:
        buffer += str(element)
    return buffer


number_list = list(range(1, 10))
all_numbers_tuple = list(permutations(number_list, 3))
all_numbers = list(map(tuple_to_number, all_numbers_tuple))

result = all_numbers
for input_data in input_datas:
    result = filter(input_data, result)
print(len(result))
