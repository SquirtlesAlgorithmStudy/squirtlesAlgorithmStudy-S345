import sys
input = sys.stdin.readline

N, A, D = map(int, input().rstrip().split())
melody_list = list(map(int, input().rstrip().split()))

current_melody = A
result = 0

for melody in melody_list:
    if melody == current_melody:
        result += 1
        current_melody += D

print(result)


