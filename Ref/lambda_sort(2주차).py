# 백준 회의실 배정 (1931) 문항에 대한 코드
# sort 함수의 key parameter에 관하여

import sys
fastin = sys.stdin.readline

n = int(fastin())
confers = [tuple(map(int, fastin().rstrip().split())) for _ in range(n)]

# Sort 의  key parameter에는 이렇게 함수가 들어가는 것이다.


def sortingrule(x):
    return (x[1], x[0])


confers.sort(key=sortingrule)
print(confers)

result = 1
last_time = confers[0][1]

for confer in confers[1:]:
    if confer[0] >= last_time:
        result += 1
        last_time = confer[1]

print(result)
