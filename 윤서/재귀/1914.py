# 하노이 탑

import sys
input = sys.stdin.readline

n = int(input())        # 원판 개수

def hanoi(num, start, other, end):          # start, other, end는 기둥을 의미, start->end로 원판을 옮기는 함수
    if num == 1:
        print(start, end)
    elif num == 0:
        return
    else:
        hanoi(num-1, start, end, other)     # 목적지가 아닌 곳으로 이동
        hanoi(1, start, other, end)         # 가장 무거운 원판(아래 원판) 목적지로 이동
        hanoi(num-1, other, start, end)     # 나머지 원판 다시 목적지로 이동

print(2**n - 1)                             # 이동 횟수 점화식 먼저 출력
if n <= 20:                                 # 문제 조건에 N <= 20 이라는 조건 존재
    hanoi(n, 1, 2, 3)