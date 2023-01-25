N = int(input("임의의 정수를 하나 입력하세요 : "))
li = list(input("임의의 리스트를 입력하세요 : ").split())
li = tuple(li)
# print(N)

if (N % 2 == 1):
    for i in range(0, N):
        print("(", i, ",", li[i], ")")
else:
    for i in range(N, 0):
        print("(", i, ",", li[i], ")")
