def fibonacci(x):
    if x == 0: return 0
    elif x == 1: return 1
    else:
        return fibonacci(x-2) + fibonacci(x-1)

def solution(x):
    fibonacci = [0,1]
    
    for i in range(2,x+1):
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    
    return fibonacci[-1] if x > 0 else 0