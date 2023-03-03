import sys
import heapq
input = sys.stdin.readline


# 0.3초 -> 성능 좋아야 한다

# input 1. 편집기에 입력되어있는 문자열 
#길이 n 
left_cursor= list(str(input().rstrip()))
right_cursor =list()
m = int(input())


cmd = [list(input().split())
        for _ in range(m)]

# L : move cursor to left (ignored if cursor idx = -1 )
# D : ''' to right (... idx = 0)
# B : rm str left to cursor
# P @ : plus character @  

def imp_cmd(cmd_str):
    if cmd_str[0] == 'P':
        left_cursor.append(cmd_str[1]) 
    elif cmd_str[0] == 'L':
        if len(left_cursor)!=0:
            tmp = left_cursor.pop()
            right_cursor.insert(-1,tmp)
        else: pass    
    elif cmd_str[0] == 'D':
        if len(right_cursor)!=0:
            tmp = right_cursor.pop()
            left_cursor.insert(-1,tmp)
        else: pass
    elif cmd_str[0] == 'B':
        if len(left_cursor)!=0:
            del left_cursor[-1]
        else: pass 

for i in range(m):
    imp_cmd(cmd[i])    

ans = left_cursor+right_cursor

print(''.join(ans))
