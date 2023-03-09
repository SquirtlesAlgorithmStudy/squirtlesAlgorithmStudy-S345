#특정 날까지의 수익을 계산할 때 이전에 저장했던 값을 이용해서 계산하므로 dp

from sys import stdin
N=int(input())
T_P=[list(map(int,stdin.readline().rstrip().split())) for _ in range(N)]

dp=[0]*(N+1)  

for i in range(N):
    for j in range(i+T_P[i][0],N+1): #특정 일의 상담을 받았을 경우, 다음 상담을 할 수 있을 때부터 퇴사 전까지
        if dp[j]<dp[i]+T_P[i][1]: #상담을 받을 수 있는 일정인 경우, 최대 수익을 창출하도록
            dp[j]=dp[i]+T_P[i][1]
            
print(dp[-1]) #가장 마지막으로 업데이트한 dp값이 최대일 것이므로 index=-1