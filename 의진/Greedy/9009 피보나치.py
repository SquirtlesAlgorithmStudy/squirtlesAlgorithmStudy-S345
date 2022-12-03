import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    # 입력 
    n = int(input())

    # 초기화
    result = []
    fibo = [0, 1]
    while fibo[-1] <= n:
        fibo.append(fibo[-2] + fibo[-1])


    # 초항
    result.append(fibo[-2])
    n -= fibo[-2]

    # 두번째 항부터 찾는 로직
    while n > 0:
        for index, element in enumerate(fibo):
            if element > n:
                n -= fibo[index - 1]
                result.append(fibo[index - 1])
                break

    for element in reversed(result):
        print(element, end = " ")
    print() 
