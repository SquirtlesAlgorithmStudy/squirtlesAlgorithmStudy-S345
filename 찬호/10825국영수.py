import sys 

input = sys.stdin.readline

n = int(input())
student =  [list(map(str,input().split())) for _ in range(n)]

student.sort(key =lambda x : (-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for st in student:
    print(st[0]) 