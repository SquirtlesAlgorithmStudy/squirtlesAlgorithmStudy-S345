# stack 구현
# 한쪽으로 입, 출력 모두 구현
stack = []

stack.append(5)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 부터 출력


# deque 구현
# 한쪽으로는 입력, 다른 한쪽으로는 출력 """

from collections import deque

queue = deque()

queue.append(5)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력