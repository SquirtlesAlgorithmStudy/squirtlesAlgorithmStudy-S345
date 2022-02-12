Total = int(input())
Payback = 1000 - Total
CashType = [500, 100, 50, 10, 5, 1]
CoinNum = 0

for i in range(6):
    if Payback >= CashType[i]:
        CoinNum += (Payback // CashType[i])
        Payback %= CashType[i]

print(CoinNum)