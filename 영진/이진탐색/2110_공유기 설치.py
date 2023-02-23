N,C=map(int,input().split())
houses=[]
for _ in range(N):
    houses.append(int(input()))
houses.sort()

min=1
max=houses[-1]-houses[0]

result=0
while min<=max:
    mid=(min+max)//2
    installed=houses[0]
    count=1
    
    for i in range(1,len(houses)):
        if houses[i]-installed>=mid:
            count+=1
            installed=houses[i]
    
    if count>=C:
        min=mid+1
        result=mid
    else:
        max=mid-1
  
print(result)