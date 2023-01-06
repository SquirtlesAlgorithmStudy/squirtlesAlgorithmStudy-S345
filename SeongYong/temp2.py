import sys; 
input = sys.stdin.readline


drawing = [[0] * 100 for _ in range(100) ]

n_draw = int(input())



for _ in range(n_draw):
    left_side, down_side = map(int, input().split())

    for i in range(left_side, left_side+10):
        for j in range(down_side, down_side+10):
            drawing[i][j] = 1

area = 0
for i in range(100):
    for j in range(100):
        if drawing[i][j] == 1:
            area +=1

print(area)
