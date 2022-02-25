#코딩테스트 시 구글링 해서 나온 다른 사람의 코드를 참고할 수 있는가?
#x를 int로 받아오면 integer overflow로 인한 시간초과가 발생함.

import sys
fastin = sys.stdin.readline

x = str(fastin().rstrip())

count = 0
y = 0

def sum_digit(number):
    return sum(map(int,number))

def func_recursive(x):
    global count
    if int(x) >= 10:
        x = str(sum_digit(x))
        count += 1
    else:
        if (int(x) % 3) == 0:
            print(count)
            print("YES")
            sys.exit()
        else:
            print(count)
            print("NO")
            sys.exit()
    func_recursive(x)

func_recursive(x)
