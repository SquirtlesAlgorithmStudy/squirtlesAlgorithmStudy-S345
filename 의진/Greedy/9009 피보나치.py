import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    result = []
    fibo = [0, 1]
    while fibo[-1] <= n:
        fibo.append(fibo[-2] + fibo[-1])
    
    result.append(fibo[-2])
    n -= fibo[-2]

    while n > 0:
        for index, element in enumerate(fibo):
            if element > n:
                n -= fibo[index - 1]
                result.append(fibo[index - 1])
                break

    for element in reversed(result):
        print(element, end = " ")
    print() 
