# 거스름돈 - 5585

# 물건의 금액
money = int(input())

taro = 0        # 타로가 받을 동전의 개수
result = 1000 - money
coin = [500, 100, 50, 10, 5, 1]

for c in coin :
    taro += result // c   # 거스름돈을 코인으로 나눈 몫
    result %= c          # 해당 화폐로 거슬러주고 남은 돈

print(taro)
