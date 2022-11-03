# 답 참고
# '최단경로', '최단길이'를 구해야 한다면 ? bfs !!!!!

import sys
input = sys.stdin.readline
from collections import deque

suvin, dong = map(int, input().split())
# bfs 사용시 방문처리 필요.
# bfs 사용시 반드시 문제에서 주어진 입력값의 '범위' 활용해서 문제 풀기
# 최단거리, 최단경로 찾을 땐 한 번 간 곳은 더이상 갈 필요가 없다!
# -1로 초기화해서 미방문 -1, -1보다 크면 방문 + 각 위치에 가기까지의 소요량 한 번에 나타낼 수 있음
visited = [-1]*(100001)

def bfs(x):
    dq = deque()
    dq.append(suvin)
    visited[x] = 0

    while dq:
        x = dq.popleft()
        if x == dong:
            print(visited[x])
            break
        for i in (2*x, x+1, x-1):
            if i == 2*x:
                # 주의 ! 곱해서 0이 될 경우는 이동 전, 후 위치 똑같기 때문에 여기선 0 포함하면 안됨
                # 한줄한줄 의미 생각하면서 쓰기 ! 더하기, 곱셈이 있다면 각각의 특성 생각해야함
                if 0 < i < 100001 and visited[i] == -1:
                    visited[i] = visited[x]
                    # 가능하다면 곱하기를 많이 쓸 때 최단시간 사용할 수 있기에 popleft
                    dq.appendleft(i)
            else:
                if 0 <= i < 100001 and visited[i] == -1:
                    visited[i] = visited[x] + 1
                    dq.append(i)

bfs(suvin)






