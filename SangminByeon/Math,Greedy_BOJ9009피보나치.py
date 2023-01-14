from sys import stdin

pibonacciSeq = [0,1]

for i in range(0, 1000000000):
    pibonacciSeq.append(pibonacciSeq[i] + pibonacciSeq[i+1])
    if pibonacciSeq[-1] > 1000000000: break

t = int(stdin.readline().rstrip())

for _ in range(t):
    n = int(stdin.readline().rstrip())
    answer = []

    for i in range(len(pibonacciSeq)-1,0,-1): #0제외
        if n >= pibonacciSeq[i]:
            n -= pibonacciSeq[i]
            answer.append(pibonacciSeq[i])
    
    print(*sorted(answer))
    
    # for i in range(len(answer)-1,-1,-1):
    #     print(answer[i], end=' ')
    