import sys
input=sys.stdin.readline

n,k=map(int,input().rstrip().split())

# 처음 생각 >마지막 답 틀림

# for i in range(n):
#     if n%2!=0:
#         n+=1
#         need+=2**i
#         n=n/2
#         if n/2==1:
#             break
#     else:
#         n=n/2
#         if n/2==1:
#             break
# print(need,i) 


# 두번째 생각 >마지막만 답 맞음..^^ 젠장

# water=0
# number=0

# for i in range(n):
#     if n<=2**i:
#         break
#     number=i  

# while n-2**number>2**(number-1):   
#     n=n-2**number
#     number-=1

# water=2**(number-1)-n+2**number

# print(water)