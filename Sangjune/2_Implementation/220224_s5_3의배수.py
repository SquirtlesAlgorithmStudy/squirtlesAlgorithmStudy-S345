import sys

fin = sys.stdin.readline

count = 0

def isMultiple_3(n, cnt):
    if len(n) > 1:
        S = 0
        cnt += 1
        for num in n:
            S += int(num)
        return isMultiple_3(str(S), cnt)
    else:
        if int(n) % 3 == 0:
            return cnt, 'YES'
        else:
            return cnt, 'NO'

num = fin().rstrip()

result = isMultiple_3(num, count)
print(result[0])
print(result[1])



#============================================================
# 메모리초과, 시간초과 뜬 함수
#============================================================

# python의 기본 재귀 깊이 제한은 1000으로
# 매우 얕으므로, 재귀 함수 사용 시 거의 필수!
# sys.setrecursionlimit(10**6)

# def isMultiple(n, cnt):
#     if n == ('3' or '6' or '9'):
#         return 'YES', cnt
#     elif n == ('1' or '2' or '4' or '5' or '7' or '8'):
#         return 'NO', cnt
#     intArr = list(map(int, n))
#     S = sum(intArr)
#     S = str(S)
#     cnt += 1
#     return isMultiple(S, cnt)

# result = isMultiple(num, count)
# print(result[1])
# print(result[0])



#============================================================
# 재귀함수 사용 X → 시간초과
#============================================================

# import sys

# fin = sys.stdin.readline

# count = 0
# num = fin().rstrip()

# while True:
#     if num == ('3' or '6' or '9'):
#         print(count)
#         print('YES')
#         break
#     elif num == ('1' or '2' or '4' or '5' or '7' or '8'):
#         print(count)
#         print('NO')
#         break
#     intArr = list(map(int, num))
#     S = sum(intArr)
#     count += 1
#     num = str(S)