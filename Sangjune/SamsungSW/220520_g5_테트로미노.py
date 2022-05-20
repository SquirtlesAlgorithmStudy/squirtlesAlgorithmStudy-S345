# import sys

# fin = sys.stdin.readline

# n, m = map(int, fin().split())
# paper = []

# for i in range(n):
#     paper.append(list(map(int, fin().split())))

# # print(paper)

# # def find_2d(mat, num):
# #     res = []
# #     for i in range(len(mat)):
# #         for j in range(len(mat[0])):
# #             if mat[i][j] == num:
# #                 res.append([i, j])
# #     return res

# # def find_max_nums(mat, st_r, st_c):
# #     filter = [[0] * 4 for _ in range(4)]
# #     flatten = []

# #     for i in range(4):
# #         for j in range(4):
# #             filter[i][j] = mat[st_r + i][st_c + j]

# #     for i in range(4):
# #         for j in range(4):
# #             flatten.append(filter[i][j])
# #     flatten.sort(reverse=True)

# #     for i in range(len(flatten)):
# #         indices = find_2d(filter, flatten[i])

# #         for j in range(len(indices)):
# #             num_idx = find_2d(filter, flatten[i])
# #     print(find_2d(filter, 4))

# #     print(filter)
# #     print(flatten)

# # find_max_nums(paper, 1, 1)

# # def isConnected(mat, num1, num2):
# #     idx = mat.find(num1)
# #     if mat.find(num2) == [idx[0]]

# import heapq
# from collections import deque

# flatten = []

# def heapsort(iterable):
#     h = []
#     queue = deque()

#     for value in iterable:
#         heapq.heappush(h, -value)

#     for _ in range(len(h)):
#         queue.append(-heapq.heappop(h))
#     return queue

# for i in range(len(paper)):
#     for j in range(len(paper[0])):
#         flatten.append(paper[i][j])

# print(flatten)

# flatten = heapsort(flatten)

# print(flatten)
# print(flatten[3])

# def find_tet(mat, queue):
#     nums = []
#     nums.append(queue.popleft())

#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if mat[i][j] == nums[0]:
#                 row_idx, col_idx = i, j

#     for i in range(1, 4):
#         if col_idx < len(mat[0]) - 1 and mat[row_idx][col_idx + 1] == queue[0]: # right
#             nums[i].append(queue.popleft())
#             row_idx, col_idx = row_idx, col_idx + 1
#         elif col_idx > 0 and mat[row_idx][col_idx - 1] == queue[0]: # left
#             nums[i].append(queue.popleft())
#             row_idx, col_idx = row_idx, col_idx - 1
#         elif row_idx > 0 and mat[row_idx - 1][col_idx] == queue[0]: # up
#             nums[i].append(queue.popleft())
#             row_idx, col_idx = row_idx - 1, col_idx
#         elif row_idx < len(mat) - 1 and mat[row_idx + 1][col_idx] == queue[0]: # down
#             nums[i].append(queue.popleft())
#             row_idx, col_idx = row_idx + 1, col_idx

#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if mat[i][j] == queue[0]:
#                 queu.popleft()
#         queue[i]

# res = 0

import sys

fin = sys.stdin.readline

def dfs(row, col, idx, total):
    global res

    if res >= total + max_val * (3 - idx):
        return
    if idx == 3:
        res = max(res, total)
        return
    else:
        for i in range(4):
            next_row = row + direction_row[i]
            next_col = col + direction_col[i]
            if 0 <= next_row < N and 0 <= next_col < M and visit[next_row][next_col] == 0:
                if idx == 1:
                    visit[next_row][next_col] = 1
                    dfs(row, col, idx + 1, total + paper[next_row][next_col])
                    visit[next_row][next_col] = 0
                
                visit[next_row][next_col] = 1
                dfs(next_row, next_col, idx + 1, total + paper[next_row][next_col])
                visit[next_row][next_col] = 0

N, M = map(int, fin().split())

paper = [list(map(int, fin().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]

direction_row = [-1, 0, 1, 0]
direction_col = [0, 1, 0, -1]
res = 0

max_val = max(map(max, paper))

for row in range(N):
    for col in range(M):
        visit[row][col] = 1
        dfs(row, col, 0, paper[row][col])
        visit[row][col] = 0

print(res)