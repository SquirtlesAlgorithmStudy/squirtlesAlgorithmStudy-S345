import sys

input= sys.stdin.readline

N=int(input().rstrip())

houses=list(map(int,input().rstrip().split()))
houses=sorted(houses)

distance1=0
distance2=0

if N%2!=0:
    print(houses[int((N-1)/2)])
else:
    for i in range(N):
        distance1+=abs(houses[i]-houses[int((N-2)/2)])
    for i in range(N):
        distance2+=abs(houses[i]-houses[int(N/2)])

    if distance1<=distance2:
        print(houses[int((N-2)/2)])
   
    else: print(houses[int(N/2)])


