def solution(L, x):
    answer = []
    length = len(L)
    i = 0
    
    while(i<length):
        if x in L[i:]:
            answer.append(L[i:].index(x)+i)
            i += L[i:].index(x)+1
        else: break
    
    return answer if len(answer) else [-1]