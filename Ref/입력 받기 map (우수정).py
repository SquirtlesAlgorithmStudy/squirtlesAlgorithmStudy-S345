import sys
fastin = sys.stdin.readline
# s = fastin().rstrip()

# print(s)
# print(len(s))

a, b = map(int, fastin().rstrip().split())

print(a, b)


# input vs sys.stdin.realine

# 1. input은 입력받을 때 맨 뒤에 있는 /n를 삭제한다.
# 그러나 sys.stdin.readline -> /n를 삭제하지 않는다.

# -> fastin().rstrip()
