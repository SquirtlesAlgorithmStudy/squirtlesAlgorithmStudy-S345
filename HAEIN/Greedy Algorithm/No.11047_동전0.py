coin, val_sum = map(int, input().split())

val = [0]*coin # 리스트 초기화

for i in range(coin):
  val[(coin-i-1)] = int(input()) # N종류만큼 입력

cnt = 0

for coin_val in val:
  cnt += val_sum // coin_val
  val_sum %= coin_val

print(cnt)