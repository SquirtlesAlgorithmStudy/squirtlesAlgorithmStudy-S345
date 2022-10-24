# 풀이1 python 시간초과 / pypy3 통과
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
import copy

row, col = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(row)]

# 초기 lab에서 0의 인덱스 저장
zero_idx = []
for i in range(row):
    for j in range(col):
        if lab[i][j] == 0:
            zero_idx.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽 세운 후 바이러스 전파(bfs), 0의 갯수 세기
def bfs(tmp_lab, x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and tmp_lab[nx][ny] == 0:
                tmp_lab[nx][ny] = 2
                queue.append((nx, ny))

    # 0의 갯수 세기
    num_zero = 0
    for i in range(row):
        for j in range(col):
            if tmp_lab[i][j] == 0:
                num_zero += 1
    return num_zero

# 벽을 세우는 모든 경우의 수 탐색
maximum = -1e9
for walls in combinations(zero_idx, 3):
    tmp_lab = []
    # 얕은 복사 ex) tmp_lab = lab을 하게 되면 둘 다 같은 주소를 바라봐서 하나를 수정하면 다른 하나의 값도 변함
    tmp_lab = copy.deepcopy(lab)
    for r, c in walls:
        tmp_lab[r][c] = 1
    result = 0
    for i in range(row):
        for j in range(col):
            if tmp_lab[i][j] == 2:
                result = bfs(tmp_lab, i, j)
    maximum = max(maximum, result)

print(maximum)

# 풀이2 python3 시간초과 PYPY 통과
import sys
input = sys.stdin.readline
from collections import deque
import copy

row, col = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
maximum = -1e9
def bfs():
    queue = deque()
    # tmp_lab = []
    tmp_lab = copy.deepcopy(lab)
    for i in range(row):
        for j in range(col):
            if tmp_lab[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and tmp_lab[nx][ny] == 0:
                tmp_lab[nx][ny] = 2
                queue.append((nx, ny))

    global result, maximum
    for i in range(row):
        result += tmp_lab[i].count(0)
    maximum = max(maximum, result)
    result = 0

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(row):
        for j in range(col):
            if lab[i][j] == 0:
                lab[i][j] = 1
                makeWall(cnt + 1)
                lab[i][j] = 0

makeWall(0)
print(maximum)

# 드디어 python3 정답 !
import sys
input = sys.stdin.readline
from collections import deque
import copy

row, col = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

zeros = []
viruses = []
maximum = -1e9


def bfs(tmp_lab, viruses):
    # 0의 총 갯수 중에서 벽 만든 갯수 빼기(3)
    result = num_zeros - 3
    # 여기서 바로 바이러스인 큐 만들어줌 (bfs 다시 호출 할 필요 없이)
    for i, j in viruses:
        queue = deque([(i, j)])
        # 바이러스 전파
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < row and 0 <= ny < col and tmp_lab[nx][ny] == 0:
                    tmp_lab[nx][ny] = 2
                    queue.append((nx, ny))
                    # 이렇게 해주면 따로 0의 갯수를 세주는 부분이 필요 없음 (시간 절약)
                    result -= 1

    return result


for i in range(row):
    for j in range(col):
        if lab[i][j] == 0:
            zeros.append((i, j))
        elif lab[i][j] == 2:
            viruses.append((i, j))

num_zeros = len(zeros)
# 여기서 벽을 세우는 모든 조합 탐색
for i in range(0, num_zeros - 2):
    for j in range(i + 1, num_zeros - 1):
        for k in range(j + 1, num_zeros):
            w1_r, w1_c = zeros[i]
            w2_r, w2_c = zeros[j]
            w3_r, w3_c = zeros[k]

            tmp_lab = copy.deepcopy(lab)
            tmp_lab[w1_r][w1_c] = 1
            tmp_lab[w2_r][w2_c] = 1
            tmp_lab[w3_r][w3_c] = 1

            result = bfs(tmp_lab, viruses)
            maximum = max(maximum, result)

print(maximum)