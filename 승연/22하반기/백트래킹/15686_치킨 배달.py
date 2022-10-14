import sys
from itertools import combinations
input = sys.stdin.readline

len_map, rest_chic = map(int, input().split())
town_map = [list(map(int, input().split())) for _ in range(len_map)]

house_loc = [] # 집의 좌표
chick_loc = [] # 치킨집의 좌표

for i in range(len_map):
    for j in range(len_map):
        if town_map[i][j] == 1:
            house_loc.append([i, j])
        elif town_map[i][j] == 2:
            chick_loc.append([i, j])

result = 1e9
for chicks in combinations(chick_loc, rest_chic):
    total_dist = 0
    for house in house_loc:
        tmp = 1e9
        for i in range(rest_chic):
            # 집 별 최소거리의 치킨집 찾기
            tmp = min(tmp, (abs(house[0] - chicks[i][0]) + abs(house[1] - chicks[i][1])))
        total_dist += tmp
    result = min(result, total_dist)

print(result)

# combination을 못 떠올려 빙빙 돌아갔던 문제