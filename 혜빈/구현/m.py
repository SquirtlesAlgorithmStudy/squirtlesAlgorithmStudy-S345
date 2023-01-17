import sys

input=sys.stdin.readline

row,col,inventory=map(int,input().rstrip().split())

floors = [list(map(int, input().split())) for _ in range(row)]

min_floor=min(map(min,floors))
max_floor=max(map(max,floors))

count_2s=0
count_1s=0

for i in range(row):
    for j in range(col):
        count_2s+=floors[i,j]-min_floor
        count_1s+=max_floor-floors[i,j]

print(count_2s,count_1s)