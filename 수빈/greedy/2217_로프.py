##시도1

import sys
fastin = sys.stdin.readline

n = int(fastin())
rope = [] #로프의 리스트
rope_w = [] #로프가 들 수 있는 중량의 리스트

for _ in range(n):
  rope.append(int(sys.stdin.readline()))
  rope.sort(reverse=True)
print(rope)


for i in range(n):
  rope_w.append(rope[i]*(i+1))
print("답은",max(rope_w))
                
print(rope_w)
# print(min(rope)*n)


##시도2
import sys
fastin = sys.stdin.readline

N = int(fastin())
rope = [int(fastin()) for i in range(N)]
rope.sort()
result = 0

for i in range(len(rope)):
    if result <N *rope[i]:
        result = N*rope[i]
        N -=1
    else:
        N -=1
print(result)