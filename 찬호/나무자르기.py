import sys 

input = sys.stdin.readline

n,m = map(int,input().split())

trees = list(map(int,input().split()))
lb,ub = 1, sum(trees)

while lb<=ub:
    mid = (lb+ub)//2 
    sum = 0 
    for tree in trees: 
        if tree >mid :
            sum = sum + tree-mid  # 따로 리스트에다 저장하니 시간 초과되는듯 
    if sum >=m:
        lb = mid +1 
    else:
        ub = mid -1 

print(ub)