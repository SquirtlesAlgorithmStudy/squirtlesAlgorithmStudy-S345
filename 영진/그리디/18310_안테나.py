
##시간초과##
"""

from sys import stdin
N=int(input()) # N입력
house=list(map(int,stdin.readline().rstrip().split())) #집들의 위치 입력

sum=0
sum_of_distance=[]

for i in range(N):
    standard_house=house[i]
    for j in range(N):
        sum+=abs(standard_house-house[j])
    sum_of_distance.append(sum)
    sum=0   

standard_sum=int(sum_of_distance[0])
antenna_location=0

for i in range(N):
    if standard_sum>int(sum_of_distance[i]):
        standard_sum=int(sum_of_distance[i])
        antenna_location=i

print(house[antenna_location])
"""

##

from sys import stdin
N=int(input()) # N입력
house=list(map(int,stdin.readline().rstrip().split())) #집들의 위치 입력
house.sort()

ans=0

if N%2==1:
    ans=int((N+1)/2)-1
elif N%2==0:
    ans=int(N/2)-1

print(house[ans])
    
           