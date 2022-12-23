import re
import sys
input = sys.stdin.readline

n = int(input())
input_datas = [tuple(map(int, input().rstrip().split())) for _ in range(n)]


def check_strike(input_data, case_list):
    strike_case_list = []
    if input_data[1] == 0:
        return case_list
    elif input_data[1] == 1:
        for case in case_list:
            for index, letter in enumerate(case):
                if letter == '?':
                    new_case = list(case)
                    new_case[index] = input_data[0][index]
                    strike_case_list.append(str(new_case))
    elif input_data[1] == 2:
        for case in case_list:
            format_1 = re.compile("??[1-9]")
            format_2 = re.compile("?[1-9]?")
            format_3 = re.compile("[1-9]??")
            format_4 = re.compile("???")
            if format_1.match(case):
                new_case = list(case)
                new_case[0] = input_data[0][0]
                new_case[1] = input_data[0][1]
                strike_case_list.append(str(new_case))
            elif format_2.match(case):
                new_case = list(case)
                new_case[0] = input_data[0][0]
                new_case[2] = input_data[0][2]
                strike_case_list.append(str(new_case))
            elif format_3.match(case):
                new_case = list(case)
                new_case[1] = input_data[0][1]
                new_case[2] = input_data[0][2]
                strike_case_list.append(str(new_case))
            elif format_4.match(case):
                strike_case_list.append(
                    str(input_data[0][0]) + str(input_data[0][1]) + '?')
                strike_case_list.append(
                    str(input_data[0][0]) + '?' + str(input_data[0][2]))
                strike_case_list.append(
                    '?' + str(input_data[0][1]) + str(input_data[0][2]))
    elif input_data[1] == 3:
        print(1)
        sys.exit()

    return strike_case_list


def check_ball(input_data, case_list):
    ball_case_list = []
    if input_data[2] == 0:
        return case_list
    elif input_data[2] == 1:
        for case in case_list:
            for index, index_tuple in enumerate([(1, 2), (0, 2), (0, 1)]):
                for index_value in index_tuple:
                    if case[index_value] == '?':
                        new_case = list(case)
                        new_case[index_value] = input_data[0][index]
                        ball_case_list.append(str(new_case))
    elif input_data[2] == 2:
        pass


def make_new_case(input_data, case_list):

    return new_case_list


def case_to_result(case_list):

    return result


case_list = ["???"]
for input_data in input_datas:
    case_list = make_new_case(input_data, case_list)

print(case_to_result(case_list))
