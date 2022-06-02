from collections import deque


def bfs(y, x, place):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    visited = [[-1] * 5 for _ in range(5)]
    queue.append((y, x))
    visited[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue
            if visited[ny][nx] != -1 or place[ny][nx] == 'X':
                continue
            visited[ny][nx] = visited[y][x] + 1
            if visited[ny][nx] == 3:
                continue
            if place[ny][nx] == 'P':
                return False
            queue.append((ny, nx))
    return True


def solution(places):
    answer = []
    for place in places:
        flag = True
        place = [list(element) for element in place]
        for x in range(5):
            for y in range(5):
                if place[y][x] == 'P':
                    if not bfs(y, x, place):
                        answer.append(0)
                        flag = False
                        break
                if not flag:
                    break
            if not flag:
                break
        if flag:
            answer.append(1)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                         "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
