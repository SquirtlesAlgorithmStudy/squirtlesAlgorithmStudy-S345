#런타임 에러
import sys
fastin = sys.stdin.readline
num = list(fastin().rstrip())
cnt = 0

def sum(number):
    s = 0
    if len(number) == 1 and int(number) % 3 == 0:
        return 'YES'
    elif len(number) == 1 and int(number) % 3 != 0:
        return 'NO'
    else:
        for i in range(len(number)):
            s += int(number[i])
        number = str(s)
        global cnt
        cnt += 1
        return sum(number)

f = sum(num)
print(cnt)
print(f)