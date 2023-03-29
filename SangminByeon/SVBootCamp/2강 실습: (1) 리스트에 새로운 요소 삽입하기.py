def solution(L, x):
    
    if L[-1] <= x:
        L.append(x)
        return L
    
    for i in range(len(L)):
        if L[i] > x: break
    L.insert(i,x)
    
    return L