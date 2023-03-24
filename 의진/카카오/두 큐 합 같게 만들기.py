from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    count = 0
    difference = sum(queue1) - sum(queue2)
    if difference == 0:
        return 0
    while True:
        if difference == 0:
            return count

        if count > 2 * (len(queue1) + len(queue2)):
            count = -1
            break
        count += 1

        if difference < 0:
            difference += (2 * queue2[0])
            move(1, queue1, queue2)

        else:
            difference -= (2 * queue1[0])
            move(2, queue1, queue2)
    return count


def move(state, queue1, queue2):

    if state == 1:
        queue1.append(queue2.popleft())
    elif state == 2:
        queue2.append(queue1.popleft())


# print(solution([1, 1], [1, 5]))
