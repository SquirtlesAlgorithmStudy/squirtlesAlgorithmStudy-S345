from collections import deque
N = int(input())

card_queue = deque()

# 카드 쌓기
for num in range(1, N+1):
    card_queue.append(num)

# 시행
while len(card_queue) != 1:
    card_queue.popleft()
    card_queue.append(card_queue[0])
    card_queue.popleft()

print(card_queue[0])
