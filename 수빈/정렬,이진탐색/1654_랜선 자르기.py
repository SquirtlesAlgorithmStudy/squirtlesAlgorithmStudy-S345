import sys
fastin = sys.stdin. readline

k, n = map(int, fastin().split())
leng = [ int(fastin()) for _ in range(k) ]
start , end = 1, max(leng)

while start <= end:
    mid = (start+end)//2
    cnt = 0 #랜선(leng)의 수
    for i in leng:
        cnt += i//mid   # 분할된 랜선의 수
        
    if cnt >=n:  #랜선 개수의 분기점
        start = mid +1
    else:
        end = mid -1
    


print(end)