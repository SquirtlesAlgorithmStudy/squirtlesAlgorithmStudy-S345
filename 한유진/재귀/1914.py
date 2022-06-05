# 하노이탑 이동 규칙
# n개의 원판이 있을때,
# 1. n - 1개의 원판을 1번째 장대에서 2번째 장대로 옮긴다.
# 2. n번 원판(맨 밑에 있는 원판)을 1번째 장대에서 3번째 장대로 옮긴다.
# 3. 나머지 n-1개의 원판들을 다시 2번째 장대에서 3번째 장대로 옮긴다.

import sys
read = sys.stdin.readline

def hanoi(n, rod1, rod2, rod3):
    if n == 1:
        #원판이 하나일 경우는 rod1->rod3으로 옮긴다.
        print(rod1, rod3)
    else:
        hanoi(n-1, rod1, rod3, rod2)
        #1. 원판 n - 1개를 rod1에서 rod2로 옮긴다. rod3은 보조 기둥으로 사용

        print(rod1, rod3)
        #2. n번째 원반 - 제일 밑에 있는 원판을 목적지(rod3)으로 이동

        hanoi(n-1, rod2, rod1, rod3)
        #3. rod2(가운데 장대)에 있는 원판 n-1개를 목적지(rod3)로 이동(rod1)를 보조 기둥으로

n = int(read())
print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 2, 3)
