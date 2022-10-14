from itertools import permutations

def calc(op, seq, exp):
    # exp가 숫자로만 이루어진 경우(즉, 더이상 연산할 것이 없는 경우)
    if exp.isdigit():
        return str(exp)
    else:
        if op[seq] == "*":
            split_data = exp.split("*")
            temp = []
            # 쪼개진 각 부분 재귀로 연산
            for s in split_data:
                temp.append(calc(op, seq + 1, s))
            #배열에 담긴 숫자(str형) eval()함수로 계산
            return str(eval("*".join(temp)))

        if op[seq] == "+":
            split_data = exp.split("+")
            temp = []
            for s in split_data:
                temp.append(calc(op, seq + 1, s))
            return str(eval("+".join(temp)))

        if op[seq] == "-":
            split_data = exp.split("-")
            temp = []
            for s in split_data:
                temp.append(calc(op, seq + 1, s))
            return str(eval("-".join(temp)))

def solution(expression):
    answer = 0
    # 3가지 operation의 조합
    operations = list(permutations(['*', '+', '-'], 3))

    for op in operations:
        #결과값은 절댓값으로 크기비교
        result = abs(int(calc(op, 0, expression)))
        
        #기존의 결과보다 크면 갱신
        if result > answer:
            answer = result

    return answer