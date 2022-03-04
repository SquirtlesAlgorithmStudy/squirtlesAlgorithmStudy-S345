import sys
fastin = sys.stdin.readline

x = fastin().rstrip()
count = 0


def find_digit_sum(x):
    result = 0
    for digit in x:
        result += int(digit)
    return str(result)


def isMulOf3(x):
    if len(x) == 1:
        if int(x) % 3 == 0:
            return True
        else:
            return False
    else:
        global count
        count += 1
        return isMulOf3(find_digit_sum(x))


if isMulOf3(x):
    print(count)
    print("YES")

else:
    print(count)
    print("NO")
