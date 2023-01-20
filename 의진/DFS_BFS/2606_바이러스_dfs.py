import sys
input = sys.stdin.readline

computer_num = int(input())
connection_num = int(input())

computer_info = [[False]
                 for _ in range(computer_num + 1)]  # [is_infected, 연결된 컴퓨터들 ...]
for _ in range(connection_num):
    com1, com2 = map(int, input().split())
    computer_info[com1].append(com2)
    computer_info[com2].append(com1)

result = 0


def dfs(current_computer):
    global result
    computer_info[current_computer][0] = True
    result += 1
    for neighbor_computer in computer_info[current_computer][1:]:
        if computer_info[neighbor_computer][0] == False:
            dfs(neighbor_computer)


dfs(1)
print(result - 1)
