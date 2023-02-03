# 1/15 17:51~19:20
# 한방에 맞춤
# 다음에는 최적화 할 것
# 1/16 17:39 수정 > pop(0) 대신 idx로 접근
# 1/16 18:03 수정 > reverse, transpose 함수 분리. trapose unpacking으로 대체
# 1/16 18:09 수정 > deepcopy 배제
# deepcopy를 너무 의식했네..
# fuction을 반환형이 있도록 하고 원본 graph를 수정하지 않는 형태로 구현한다면 deepcopy가 필요없겠지!!

# import copy
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 함수 자체는 왼쪽으로 미는 경우인 direction == 0만 구현함.
# 최적화 더 할 수 있겠지만 귀찮아서...
# 오른쪽으로 미는 경우(1)은 그래프를 좌우반전 [::-1]시키고 left를 수행한 다음 다시 반전 [::-1] 하는 거랑 동일함
# 위로 미는 경우는(2) 그래프를 transpose하고 left를 수행한 뒤 다시 transpose한 것과 동일함
# 아래로 미는 경우는(3) 그래프를 transpose하고 right를 수행하고 다시 transpose한 것과 동일함


def reverse(graph):
    result = []
    for g in graph:
        result.append(g[::-1])
    return result


def transpose(board):
    # board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # for : (*board) = [1, 2, 3], [4, 5, 6], [7, 8, 9]
    # for : (zip(*board)) = (1, 4, 7), (2, 4, 8), (3, 6, 9) <= 튜플로 묶음
    # for : map(list, zip(*board)) = [1, 4, 7], [2, 4, 8], [3, 6, 9]
    # list(map(list, zip(*board)) = [[1, 4, 7], [2, 4, 8], [3, 6, 9]] <= Transpose
    return list(map(list, zip(*board)))


def function(graph, direction):
    if direction == 0:  # left
        new_graph = []
        for y in range(n):
            line_answer = []
            can_put = True

            for x in range(n):
                v = graph[y][x]
                if v == 0:
                    continue
                else:
                    if not line_answer:
                        line_answer.append(v)
                    else:
                        if line_answer[-1] == v and can_put:
                            line_answer[-1] *= 2
                            can_put = False
                        else:
                            line_answer.append(v)
                            can_put = True

            for _ in range(n-len(line_answer)):
                line_answer.append(0)
            new_graph.append(line_answer)
        return new_graph

    elif direction == 1:  # right
        return reverse(function(reverse(graph), 0))

    elif direction == 2:  # up
        return transpose(function(transpose(graph), 0))

    elif direction == 3:  # down
        return transpose(function(transpose(graph), 1))


ans = 0


def dfs(graph, orders=[]):
    if len(orders) == 5:
        global ans
        for y in range(n):
            ans = max(ans, max(graph[y]))
        return
    for i in range(4):
        dfs(function(graph, i), orders + [i])
        # dfs(function(copy.deepcopy(graph), i), orders + [i])


dfs(graph)
print(ans)
