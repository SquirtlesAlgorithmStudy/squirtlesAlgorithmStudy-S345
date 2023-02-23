
import sys
input=sys.stdin.readline

                


# 인풋 
n, c =map(int,input().split())
homes = []
for i in range(n):
    homes.append(int(input()))

    
homes.sort()


ub = homes[-1] - homes[0] 
lb = 1 
res = 0


while lb<=ub:
    mid =(lb+ub)//2 # mid는 공유기 설치한 거리를 뜻한다.
    cnt =1 
    now = homes[0] #시작점
    for i in range(1,n): # 인풋으로 받은 집을 모두 방문
        if now+mid <=homes[i]:
            cnt+=1
            now = homes[i]
    if cnt <c: # c 개보다 더 적게 라우터를 놓았다면 더 좁게 설치 해야함 
        ub =mid-1
    elif cnt>=c: # c개 보다 더 많게 놓거나 같은 경우라면 
        lb =mid+1
        res = mid # if-else condition 을 세개로 두니 시간 초과 생김 

        
print(res)

#55987055	grvty0717	 2110	맞았습니다!!	38984	568	Python 3 / 수정	716	1분 전