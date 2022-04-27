import sys
input = sys.stdin.readline

score = []
people = int(input())

for i in range(people):
    score.append(tuple(input().split()))

score_sorted = sorted(score, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(people):
    print(score_sorted[i][0])