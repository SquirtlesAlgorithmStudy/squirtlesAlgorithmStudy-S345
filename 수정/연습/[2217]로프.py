#4012, 4068ms 나오는데 맞았습니다?

N = int(input())
rope = [] #[]말고 list를 적으면?

for i in range(N):
    rope.append(int(input())) #map이 정확히 무엇?

rope.sort()
rope.reverse()
weight = 0
for k in range(N):
    max = int(rope[k]*(k+1))
    if max > weight:
        weight = max

print(weight)