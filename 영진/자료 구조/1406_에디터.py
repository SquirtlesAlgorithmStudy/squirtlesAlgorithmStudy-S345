import sys
Left_list=list(input())
Right_list=[]

M=int(input())
for _ in range(M):
    command=list(input().split())
    
    if command[0]=='L' and len(Left_list)!=0:
        Right_list.append(Left_list.pop())
    elif command[0]=='D' and len(Right_list)!=0:
        Left_list.append(Right_list.pop())
    elif command[0]=='B' and len(Left_list)!=0:
        Left_list.pop()
    elif command[0]=='P':
        Left_list.append(command[1])

print("".join(Left_list+list(reversed(Right_list))))


"""
1. reversed() :리스트의 값을 좌우반전 시켜준다.
2. 다중 if문보다 elif를 사용하는 것이 시간이 절약된다.

<시간 초과>
text=list(input())
cursor=len(text)
M=int(input())

for _ in range(M):
    command=input().split()
    if command[0]=='L':
        if cursor!=0:
            cursor-=1
    elif command[0]=='D':
        if cursor!=len(text):
            cursor+=1
    elif command[0]=='B':
        if cursor!=0:
            del(text[cursor-1])
            cursor-=1
    elif command[0]=='P':
        text.insert(cursor,command[1])
        cursor+=1

print(''.join(text))
"""