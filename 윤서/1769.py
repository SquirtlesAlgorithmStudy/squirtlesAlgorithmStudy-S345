# 뇌피셜 코드,,
# 1769 - 3의 배수

import sys
input = sys.stdin.readline

x = input()
count = 0

def checkNum(num):
    y = 0
    global count
    count += 1
    for i in num:
        y += i                      # 오류 수정 전
    if num != y:
        checkNum(y)
    else:
        if y % 3 == 0:
            print("yes")
            return count

checkNum(x)
