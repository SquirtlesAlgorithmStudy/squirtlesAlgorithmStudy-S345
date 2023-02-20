import sys
import heapq
input = sys.stdin.readline


# 0.3초 -> 성능 좋아야 한다

# input 1. 편집기에 입력되어있는 문자열 
#길이 n 
str_x = list(str(input().rstrip()))

m = int(input())


cmd = [list(input().split())
        for _ in range(m)]
print(cmd)
# L : move cursor to left (ignored if cursor idx = -1 )
# D : ''' to right (... idx = 0)
# B : rm str left to cursor
# P @ : plus character @  

heapq.heapify(str_x)
print(str_x)



#def imp_cmd(cmd_str):
#    if cmd_str[0]