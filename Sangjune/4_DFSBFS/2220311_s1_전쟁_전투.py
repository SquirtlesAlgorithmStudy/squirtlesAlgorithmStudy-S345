import sys
import copy

fin = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(graph, x_coord, y_coord, m, n, visited, not_visited, count):
    if x_coord < 0 or x_coord >= m or y_coord < 0 or y_coord >= n:
        return False, count
    if graph[x_coord][y_coord] == not_visited:
        graph[x_coord][y_coord] = visited
        count += 1
        count = dfs(graph, x_coord - 1, y_coord, m, n, visited, not_visited, count)[1]
        count = dfs(graph, x_coord, y_coord - 1, m, n, visited, not_visited, count)[1]
        count = dfs(graph, x_coord + 1, y_coord, m, n, visited, not_visited, count)[1]
        count = dfs(graph, x_coord, y_coord + 1, m, n, visited, not_visited, count)[1]
        return True, count
    return False, count

N, M = map(int, fin().rstrip().split())
g = []

for _ in range(M):
    g.append(list(fin().rstrip()))

ally_cnt = 0
enemy_cnt = 0

ally_res = 0
enemy_res = 0

ally_g = copy.deepcopy(g)
enemy_g = copy.deepcopy(g)

# ally (W)
for i in range(M):
    for j in range(N):
        result = dfs(ally_g, i, j, M, N, 'B', 'W', ally_cnt)
        if result[0]:
            ally_res += result[1] * result[1]

# enemy (B)
for i in range(M):
    for j in range(N):
        result = dfs(enemy_g, i, j, M, N, 'W', 'B', enemy_cnt)
        if result[0]:
            enemy_res += result[1] * result[1]

print(ally_res, enemy_res)

# note
# copy and deep copy