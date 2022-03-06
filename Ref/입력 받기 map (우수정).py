import sys
fastin = sys.stdin.readline
# s = fastin().rstrip()

# print(s)
# print(len(s))

# a, b = map(int, fastin().rstrip().split())

# print(a, b)


# input vs sys.stdin.realine

# 1. input은 입력받을 때 맨 뒤에 있는 /n를 삭제한다.
# 그러나 sys.stdin.readline -> /n를 삭제하지 않는다.

# -> fastin().rstrip()

# 2. input은 입력 시 프롬프트를 띄울 수 있다.
# sys.stdin.readline은 프롬프트를 띄울 수 없다.

a = input("입력해주세용")  # 프롬프트에 입력해주세용이 뜸
a = fastin("입력해주세용")  # 이거 오류남
