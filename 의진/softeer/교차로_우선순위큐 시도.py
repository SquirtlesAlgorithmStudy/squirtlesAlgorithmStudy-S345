import sys
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())
carInfos = [list(input().rstrip().split()) for _ in range(n)]
INF = 10 ** 7

queues = [PriorityQueue(), PriorityQueue(), PriorityQueue(), PriorityQueue()]
position = ['A', 'B', 'C', 'D']


# 우선순위 큐에 전체 추가하기
for index, carInfo in enumerate(carInfos):
    carInfo[0] = int(carInfo[0])
    for i in range(4):
        if carInfo[1] == position[i]:
            queues[i].put((carInfo[0], index))
            break
results = [0] * n

# 우선순위 큐에서 하나씩 꺼내면서 처리하기
while (not queues[0].empty()) or (not queues[1].empty()) or (not queues[2].empty()) or (not queues[3].empty()):
    info = [0, 0, 0, 0]
    for i in range(4):
        if not queues[i].empty():
            info[i] = queues[i].get()
        else:
            info[i] = (INF, -1)

    min_value = min(info[0][0], info[1][0], info[2][0], info[3][0])

    infoCode = []
    for i in range(4):
        if info[i][0] == min_value:
            infoCode.append(i)

    # 같은 시간의 값끼리 모아 처리한다, 길이별로 다르게 처리
    if len(infoCode) == 4:
        min_index = min(info[0][1], info[1][1], info[2][1], info[3][1])
        results[min_index:min_index + 4] = [-1, -1, -1, -1]

    elif len(infoCode) == 3:
        emptyValue = 3
        for i, code in enumerate(infoCode):
            if i != code:
                emptyValue = i
                break

        results[info[emptyValue-3][1]] = info[emptyValue-3][0]
        if not queues[emptyValue-3].empty():
            nextInfo = queues[emptyValue-3].get()
            if nextInfo[0] == info[emptyValue-3][0]:
                queues[emptyValue-3].put((nextInfo[0] + 1, nextInfo[1]))
            else:
                queues[[emptyValue-3]].put(nextInfo)

        if info[emptyValue][0] != INF:
            queues[emptyValue].put(info[emptyValue])

        queues[emptyValue-2].put((info[emptyValue-2]
                                 [0] + 1, info[emptyValue-2][1]))
        queues[emptyValue-1].put((info[emptyValue-1]
                                 [0] + 2, info[emptyValue-1][1]))

    elif len(infoCode) == 2:
        min_value = min(infoCode)
        if min_value + 1 in infoCode or infoCode == [0, 3]:  # 두 개가 붙어 있는 경우
            if infoCode == [0, 3]:
                results[info[3][1]] = info[3][0]
                if not queues[3].empty():
                    nextInfo = queues[3].get()
                    if nextInfo[0] == info[3][0]:
                        queues[3].put((nextInfo[0] + 1, nextInfo[1]))
                    else:
                        queues[3].put(nextInfo)
                queues[0].put((info[0][0] + 1, info[0][1]))
                if info[1][0] != INF:
                    queues[1].put(info[1])
                if info[2][0] != INF:
                    queues[2].put(info[2])
            else:
                for i in range(3):
                    if min_value == i:
                        results[info[i][1]] = info[i][0]
                        if not queues[i].empty():
                            nextInfo = queues[i].get()
                            if nextInfo[0] == info[i][0]:
                                queues[i].put(
                                    (nextInfo[0] + 1, nextInfo[1]))
                            else:
                                queues[i].put(nextInfo)
                        queues[i+1].put((info[i+1][0] + 1, info[i+1][1]))
                        if info[i-1][0] != INF:
                            queues[i-1].put(info[i-1])
                        if info[i-2][0] != INF:
                            queues[i-2].put(info[i-2])
                        break
        else:
            for i in range(4):
                if i in infoCode:
                    results[info[i][1]] = info[i][0]
                    if not queues[i].empty():
                        nextInfo = queues[i].get()
                        if nextInfo[0] == info[i][0]:
                            queues[i].put(
                                (nextInfo[0] + 1, nextInfo[1]))
                        else:
                            queues[i].put(nextInfo)
                else:
                    if info[i][0] != INF:
                        queues[i].put(info[i])

    elif len(infoCode) == 1:
        results[info[infoCode[0]][1]] = info[infoCode[0]][0]
        if not queues[infoCode[0]].empty():
            nextInfo = queues[infoCode[0]].get()
            if nextInfo[0] == info[infoCode[0]][0]:
                queues[infoCode[0]].put((nextInfo[0] + 1, nextInfo[1]))
            else:
                queues[infoCode[0]].put(nextInfo)
        for i in range(1, 4):
            if info[infoCode[0] - i][0] != INF:
                queues[infoCode[0] - i].put(info[infoCode[0]-i])

for result in results:
    print(result)
