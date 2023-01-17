from collections import deque
import sys; input = sys.stdin.readline


N = int(input())
card = deque()

for i in range(1, N+1):
    card.append(i)

while(len(card) != 1):
    card.popleft()
    card.append(card.popleft())

print(card.pop())