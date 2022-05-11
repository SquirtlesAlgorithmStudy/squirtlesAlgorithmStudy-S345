# 답지를 참지 못하고 봤어요 .. 
n = int(input())
count = 0
while n > 0:
    if n % 5 == 0:
        count += n // 5
        break
    n -= 3
    count += 1
if n < 0:
    print(-1)
else:
    print(count)