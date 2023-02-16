N,C=map(int,input().split())
houses=[]
for _ in range(N):
    houses.append(int(input()))
houses.sort()

print(houses[-1]-houses[0])