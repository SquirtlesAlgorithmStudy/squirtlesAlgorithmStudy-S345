# python3 시간초과 pypy3 통과.....
# 두 문자열 중 공통된 부분 찾는 문제 -> DP !!
# 문제를 풀 때 무조건 구현하기보단 효율적으로 구현해야 한다. 메모리, 시간 복잡도 생각하고 풀기.

import sys
input = sys.stdin.readline

# 문자열 입력받을 때 rstrip() 습관
str1, str2 = input().rstrip(), input().rstrip()
row = len(str1)
col = len(str2)

# 값 비교할 때 +1을 할땐 인덱스 초과로 조건 걸어줘야하니 그래프 생성할 때 +1로 만들고 -1로 비교하기 !
# 이것도 습관들이자.
graph = [[0] * (col + 1) for _ in range(row + 1)]

# 그럼 0부터가 아닌 1부터 탐색하면 됨
for i in range(1, row + 1):
    for j in range(1, col + 1):
        # 1부터 탐색하면 여기서 인덱스 오류 안남 !
        if str1[i - 1] == str2[j - 1]:
            graph[i][j] = graph[i - 1][j - 1] + 1

print(max(map(max, graph)))