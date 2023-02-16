N,M=map(int,input().split())

trees=list(map(int,input().split()))

start=0
end=max(trees)

result=0
while start<=end:
    mid=(start+end)//2
    total=0
    
    for tree in trees:
        if tree>mid:
            total+=tree-mid
    #더 자른 경우(오른쪽 부분 탐색)
    if total>=M:
        start=mid+1
        result=mid
    #덜 자른 경우(왼쪽 부분 탐색)
    else:
        end=mid-1
        
print(result)