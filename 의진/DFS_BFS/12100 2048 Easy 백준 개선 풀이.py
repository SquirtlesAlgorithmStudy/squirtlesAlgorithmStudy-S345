import sys
from collections import deque
import copy
input = sys.stdin.readline

N = int(input())
initial_state = [list(map(int, input().split())) for _ in range(N)]
result = 0
direction_list = ["left", "right", "up", "down"]
id_generator = 0


class Node:
    def __init__(self, previous_node_id, id, state, local_max_val):
        self.previous_node_id = previous_node_id
        self.id = id
        self.state = state
        self.local_max_val = local_max_val


def get_initial_result_value(state):
    global result
    for row in range(N):
        for col in range(N):
            result = max(result, state[row][col])
    return result


def action(direction, previous_node):
    global result
    global id_generator
    local_max_val = previous_node.local_max_val
    next_state = copy.deepcopy(previous_node.state)
    deque_data = deque()
    if direction == "left":
        for row in range(N):
            trigger = False
            deque_data.clear()
            for col in range(N):
                if deque_data and next_state[row][col] != 0:
                    if deque_data[len(deque_data)-1] == next_state[row][col] and not trigger:
                        deque_data[len(deque_data)-1] *= 2
                        result = max(result, deque_data[len(deque_data)-1])
                        local_max_val = max(
                            local_max_val, deque_data[len(deque_data)-1])
                        trigger = True
                    else:
                        deque_data.append(next_state[row][col])
                        trigger = False
                elif next_state[row][col] != 0:
                    deque_data.append(next_state[row][col])
                    trigger = False
            while len(deque_data) != N:
                deque_data.append(0)
            next_state[row][:] = list(deque_data)

    elif direction == "right":
        for row in range(N):
            deque_data.clear()
            for col in range(N-1, -1, -1):
                if deque_data and next_state[row][col] != 0:
                    if deque_data[0] == next_state[row][col] and not trigger:
                        deque_data[0] *= 2
                        result = max(result, deque_data[0])
                        local_max_val = max(local_max_val, deque_data[0])
                        trigger = True
                    else:
                        deque_data.appendleft(next_state[row][col])
                        trigger = False
                elif next_state[row][col] != 0:
                    deque_data.appendleft(next_state[row][col])
                    trigger = False
            while len(deque_data) != N:
                deque_data.appendleft(0)
            next_state[row][:] = list(deque_data)

    elif direction == "up":
        for col in range(N):
            deque_data.clear()
            for row in range(N):
                if deque_data and next_state[row][col] != 0:
                    if deque_data[len(deque_data)-1] == next_state[row][col] and not trigger:
                        deque_data[len(deque_data)-1] *= 2
                        result = max(result, deque_data[len(deque_data)-1])
                        local_max_val = max(
                            local_max_val, deque_data[len(deque_data)-1])
                        trigger = True
                    else:
                        deque_data.append(next_state[row][col])
                        trigger = False
                elif next_state[row][col] != 0:
                    deque_data.append(next_state[row][col])
                    trigger = False
            while len(deque_data) != N:
                deque_data.append(0)
            for row in range(N):
                next_state[row][col] = deque_data.popleft()

    elif direction == "down":
        for col in range(N):
            deque_data.clear()
            for row in range(N-1, -1, -1):
                if deque_data and next_state[row][col] != 0:
                    if deque_data[0] == next_state[row][col] and not trigger:
                        deque_data[0] *= 2
                        result = max(result, deque_data[0])
                        local_max_val = max(local_max_val, deque_data[0])
                        trigger = True
                    else:
                        deque_data.appendleft(next_state[row][col])
                        trigger = False
                elif next_state[row][col] != 0:
                    deque_data.appendleft(next_state[row][col])
                    trigger = False
            while len(deque_data) != N:
                deque_data.appendleft(0)
            for row in range(N):
                next_state[row][col] = deque_data.popleft()

    else:
        print("Input Error!")
        return -1
    id_generator += 1
    return Node(previous_node_id=previous_node.id, id=id_generator, state=next_state, local_max_val=local_max_val)


def dfs(depth, root_node):
    if depth > 5:
        return
    else:
        for direction in direction_list:
            if root_node.local_max_val >= (result ** (1 / (7 - depth))):
                dfs(depth + 1, action(direction, root_node))


initial_node = Node(previous_node_id=-1, id=0, state=initial_state,
                    local_max_val=get_initial_result_value(initial_state))
dfs(1, initial_node)
print(result)