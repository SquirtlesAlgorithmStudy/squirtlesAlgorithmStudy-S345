# 1769 - 3의 배수

import sys
input = sys.stdin.readline

number = input().rstrip()
count = 0

def checkThree(number):                     # type(number) == str
    global count
    if len(number) != 1:                    # 숫자가 한 자리 수가 아닐 때
        count+=1                            # 계산 수행
    checkNum = 0                

    for i in str(number):
        checkNum += int(i)                  # 각 자리의 숫자의 합

    if len(str(checkNum)) != 1:             # 문자열의 길이가 1(정수 자릿수가 1)이 아니라면: int형은 len함수 사용할 수 없음
        checkThree(str(checkNum))           # checkThree함수가 number를 str로 받기 때문에 형 변환 필수!
    elif len(str(checkNum)) == 1:           # 정수 자릿수가 1이라면
        if checkNum % 3 != 0:               # 3의 배수인지 아닌지 확인
            print(count)
            print("NO")
            return
        elif checkNum % 3 == 0:
            print(count)
            print("YES")
            return

checkThree(number)