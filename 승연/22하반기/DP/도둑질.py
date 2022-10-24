# dp문제는 꼭 점화식을 세우자
# dp : 도둑이 훔칠 수 있는 돈의 최댓값
# dp[i]는 1번부터 i번째 집까지 털었을 때 훔칠 수 있는 돈의 최댓값
# dp[i]는 (바로 전 집까지 훔칠 수 있는 최댓값)와 (전전집까지의 훔칠 수 있는 최댓값 + 현재 집의 money) 두 가지 경우
# 점화식 : dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])

def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money)-1): # 첫 집을 무조건 터는 경우
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2])

    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)): # 마지막 집을 무조건 터는 경우
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대