def solution(N, number):
    if number == N:
        return 1
    answer = -1
    # 중복 제거 set자료형 사용, set은 append 아닌 add
    _li = [set() for _ in range(8)]
    # 1 2  3   4    5     6 7 8
    # 5 55 555 5555 55555 ...
    for i in range(len(_li)):
        _li[i].add(int(str(N)*(i + 1)))
    
    # 구조 기억
    for i in range(1, 8):
        for j in range(i):
            for op1 in _li[j]:
                # i 4일 때 op1 op2 각각 0 3 / 1 2 / 2 1 / 3 0 
                for op2 in _li[i-j-1]:
                    _li[i].add(op1 + op2)
                    _li[i].add(op1 - op2)
                    _li[i].add(op1 * op2)
                    if op2 != 0:
                        _li[i].add(op1 // op2)
    
        if number in _li[i]:
            answer = i + 1
            break
        
    return answer