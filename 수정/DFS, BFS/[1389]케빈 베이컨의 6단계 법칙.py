from collections import deque
import sys
fastin = sys.stdin.readline

User, Relation = map(int, fastin().rstrip().split())
R = deque([[0] * 1 for _ in range(User + 1)])
for i in range(Relation):
    A, B = map(int, fastin().rstrip().split())
    R[A].append(B)
    R[B].append(A)
for j in range(1, User + 1):
    R[j].pop(0)
# print(R)

def bfs(R, num):
    queue = deque([num])
    visit = [0] * (User + 1)
    visit[num] = 1
    while queue:
        num = queue.popleft()
        for i in R[num]:
            if visit[i] == 0:
                visit[i] = visit[num] + 1
                queue.append(i)
    return sum(visit) - User
# print(bfs(R, 1))

Sum = bfs(R, 1)
mini = 1
for Users in range(2, User + 1):
    s = bfs(R, Users)
    if Sum > s:
        Sum = s
        mini = Users

print(mini)