import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
oper_list = list(map(int, input().split()))

# 무한의 값 1e9 설정
maximum = -1e9
minimum = 1e9

def rec(depth, total, plus, minus, multiple, divide):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # plus의 갯수가 0이 될 때까지 먼저 진행
    if plus:
        rec(depth + 1, total + num_list[depth], plus - 1, minus, multiple, divide)
    if minus:
        rec(depth + 1, total - num_list[depth], plus, minus - 1, multiple, divide)
    if multiple:
        rec(depth + 1, total * num_list[depth], plus, minus, multiple - 1, divide)
    if divide:
        rec(depth + 1, int(total / num_list[depth]), plus, minus, multiple, divide - 1)

# 첫 번째 값을 수열의 첫 번째로 넘겨줌 num_list[0]
rec(1, num_list[0], oper_list[0], oper_list[1], oper_list[2], oper_list[3])
print(maximum)
print(minimum)