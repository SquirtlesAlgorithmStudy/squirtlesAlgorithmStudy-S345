import math
A,B,V=map(int,input().split())

count=math.ceil((V-A)/(A-B)+1)

print(count)