# 시간초과_원인 미해결
import sys
input = sys.stdin.readline

N = int(input())
power_graph = [list(map(int, input().split())) for _ in range(N)]
minimum = int(1e9)
visited = [False for _ in range(N)]

def rec(depth, idx):
    global minimum, N
    # 한 팀의 인원 선정되면 나머지는 자동 선정
    if depth == N/2:
        ateam, bteam = 0, 0
        for row in range(N):
            for col in range(N):
                if visited[row] and visited[col]: # 둘다 1인 경우
                    ateam += power_graph[row][col]
                elif not visited[row] and not visited[col]:
                    bteam += power_graph[row][col]
        minimum = min(abs(ateam-bteam), minimum)
        return

    for i in range(idx, N):
        if not visited[i]:
            #ateam -> 1 bteam -> 0
            visited[i] = True
            rec(depth + 1, i + 1)
            visited[i] = False

rec(0, 0)
print(minimum)