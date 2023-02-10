import sys
from collections import deque
input = sys.stdin.readline

computer_num = int(input())
connection_num = int(input())
computer_info = [[False]
                 for _ in range(computer_num + 1)]  # [is_infected, 연결된 컴퓨터들 ...]
for _ in range(connection_num):
    com1, com2 = map(int, input().split())
    computer_info[com1].append(com2)
    computer_info[com2].append(com1)


def bfs(start):
    result = 0
    queue = deque()
    computer_info[start][0] = True
    queue.append(start)

    while queue:
        current_computer = queue.popleft()
        for neighbor_computer in computer_info[current_computer][1:]:
            if computer_info[neighbor_computer][0] == False:
                computer_info[neighbor_computer][0] = True
                queue.append(neighbor_computer)
                result += 1
    return result


print(bfs(1))
