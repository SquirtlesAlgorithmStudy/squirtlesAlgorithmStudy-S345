import sys
input = sys.stdin.readline

n = int(input())
wine =[0]   ##첫 번째 wine을 index 1로 해주기 위해
for i in range(n):
    wine.append(int(input()))
dp = [0]
dp.append(wine[1])
if n >1:
    dp.append(wine[1]+wine[2])
    
print("초기 wine",wine)
print("초기 dp", dp)
    
for i in range(3, n+1):
    print('max안의 값 ',dp[i-1], dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i])
    ##    dp의 마지막 값(아직 i번째는 추가되기 전이니까) 
    ## vs dp[1]=wine[1]이니까 + 두번째 건너뛰고 wine의 3, 4번째 합
    ## vs dp[2] (wine1+wine2) + 세번째 건너뛰고 wine의 4번째 
    dp.append(max(dp[i-1], dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i]))
    print('for문의 dp', dp)


print("최종 답 : ", dp[n])


