def solution(numbers):
    answer = []
    return answer


def make_binary_string(decimal_number):
    return str(bin(decimal_number)[2:])


def add_zero(binary_string):
    zero_added_length = len(binary_string)
    while True:
        zero_added_length += 1
        if (zero_added_length & (zero_added_length - 1)) == 0:  # 2의 제곱수 이면
            zero_added_length = zero_added_length - 1
            break
    return binary_string.zfill(zero_added_length)


def is_possible(zerofilled_binary_string):
    for i in range(0, len(zerofilled_binary_string), 2):
        if zerofilled_binary_string[i] == "0":
            return 0
    return 1


def end_to_end(number):
    return is_possible(add_zero(make_binary_string(number)))


print(end_to_end(7))
