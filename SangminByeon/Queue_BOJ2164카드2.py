from sys import stdin
from collections import deque

cards = deque()

n = int(stdin.readline().rstrip())
for i in range(1,n+1):
    cards.append(i)
print(cards)
while(len(cards)>1):
    cards.popleft()
    cards.append(cards.popleft())
print(*cards)