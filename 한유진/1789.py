n = int(input())
i = 1
while i <= n: 
    # while n > 0: 이런식으로 하면 오류인데 왜인지 모르겠어요!
    n -= i
    i += 1

print(i - 1)
