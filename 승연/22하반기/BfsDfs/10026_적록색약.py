# 같은 색끼리 모여있으면 한 구역

import sys
# 이부분을 안써줘서 계속 런타임에러가 났었다
# dfs사용하는 경우 습관적으로 써주기
sys.setrecursionlimit(10000)
input = sys.stdin.readline
import copy

row = int(input())
# 문자열 공백없이 입력받는 경우 input().strip() 잊지말기!
drawing = [list(input().strip()) for _ in range(row)]
col = len(drawing[0])
visited = [[0]*col for _ in range(row)]


tmp_drawing = copy.deepcopy(drawing)
def dfs(x, y, tmp_drawing, alphabet):
    if 0 <= x < row and 0 <= y < col:
        if tmp_drawing[x][y] in alphabet:
            tmp_drawing[x][y] = 0
            dfs(x - 1, y,tmp_drawing, alphabet)
            dfs(x + 1, y,tmp_drawing, alphabet)
            dfs(x, y - 1,tmp_drawing, alphabet)
            dfs(x, y + 1,tmp_drawing, alphabet)
            return True
    return False

normal_count, special_count = 0, 0
# 정상인의 경우
for i in range(row):
    for j in range(col):
        if tmp_drawing[i][j] != 0:
            if dfs(i, j, tmp_drawing, ["R"]) == True:
                normal_count += 1
            elif dfs(i, j, tmp_drawing, ["G"]) == True:
                normal_count += 1
            elif dfs(i, j, tmp_drawing, ["B"]) == True:
                normal_count += 1
# 적록색맹의 경우
for i in range(row):
    for j in range(col):
        if drawing[i][j] != 0:
            if dfs(i, j, drawing, ["R", "G"]) == True:
                special_count += 1
            elif dfs(i, j, drawing, ["B"]) == True:
                special_count += 1

print(normal_count, special_count)

