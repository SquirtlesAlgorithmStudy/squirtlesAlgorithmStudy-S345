import sys
import heapq
import copy
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]

for i in range(1, N+1):
    result = 0
    mid_number = i//2 + i % 2
    temp = numbers[:i].copy()
    heapq.heapify(temp)
    for j in range(mid_number):
        result = heapq.heappop(temp)
    print(result)
