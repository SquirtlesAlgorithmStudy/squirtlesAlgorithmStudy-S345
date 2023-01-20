from collections import deque

N =int(input())
cards = deque([n for n in range(1,N+1)])
while(len(cards)>1):
    cards.popleft()
    sec=cards.popleft()
    cards.append(sec)

print(cards[0])

#2번째 -> print(cards) 가 틀린것 같다 print(cards[0])

#3번째 채점 -> 정답