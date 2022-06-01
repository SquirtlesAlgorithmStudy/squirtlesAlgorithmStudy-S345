# A -> B

import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())

count = 1                       # a == b일 때 기본 출력

while b != a:
    if b < a:                   # b가 a보다 작아지는 경우에 break를 걸지 않으면 무한루프에 빠질 수 있음
        count = -1
        break
    count += 1
    if b % 10 == 1:             # 끝자리가 1인 경우
        b = b // 10             # 10으로 나눈 몫을 b로 설정
    elif b % 2 == 0:            # 2로 나누어 떨어지면
        b /= 2                  # 2로 나눈 몫을 b로 설정
    else:                       # 모든 경우에 해당하지 않는다면 수를 바꿀 수 없음, count = -1 & 반복문 종료
        count = -1
        break

print(count)