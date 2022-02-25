import sys

n = int(sys.stdin.readline())
weight = [5, 3]
numbers = [n]
count = 0

if n % weight[0] == 0:
    count = int(n / weight[0])
    print(count)
else:
    while weight[0] <= numbers[-1]:
        n -= weight[0]
        numbers.append(n)
        
    for i in range(len(numbers) - 1, -1, -1): # i는 weight[0]를 뺀 횟수와 같음
        if numbers[i] % weight[1] == 0:
            count = int(i + numbers[i] / weight[1])
            print(count)
            break
        if i == 0:
            print(-1)