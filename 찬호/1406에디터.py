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

# L : move cursor to left (ignored if cursor idx = -1 )
# D : ''' to right (... idx = 0)
# B : rm str left to cursor
# P @ : plus character @  

#make str_x to min_heap 
heapq.heapify(str_x)
# Heap 으로 풀지 말고 stack 2개를 이용해서 풀려고 노력해보자 
cursor = len(str_x)

def imp_cmd(cmd_str):
    global cursor
    if cmd_str[0] == 'P':
        str_x.insert(cursor,cmd_str[1])
        cursor = cursor + 1 
    elif cmd_str[0] == 'L':
        if cursor > 0:
            cursor = cursor - 1
        else: pass 
    elif cmd_str[0] == 'D':
        if cursor <len(str_x) - 1: 
            cursor = cursor + 1 # 커서 아이콘은 항상 마지막 문자에 위치한다고 개념 잡아보자 
        else: pass 
    elif cmd_str[0] == 'B':
        heapq.heappop(str_x)

for i in range(m):
    imp_cmd(cmd[i])    

print(str_x)