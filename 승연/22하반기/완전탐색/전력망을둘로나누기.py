# 하나씩 끊어본다
# 끊고 한 덩이의 송전탑 수만 세면 됨
from collections import deque

def solution(n, wires):
    minimum = 1e9
    linked_info = [[0] for _ in range(n + 1)]
    
    # 연결된 정보 저장하는 그래프
    for x, y in wires:
        linked_info[x].append(y)
        linked_info[y].append(x)

    for i in range(n + 1):
        linked_info[i].pop(0)
    
    # [x, y]형태로 연결되어 있을 때 y에 연결된 송전탑 갯수 세어줌
    def bfs(x, y):
        dq = deque()
        dq.append(y)
        y_linked_list = []
        visited = [0] * (n + 1)
        visited[y] = True
        
        while dq:
            tmp = dq.pop()
            for i in linked_info[tmp]:
                if not visited[i] and i != x:
                    y_linked_list.append(i)
                    visited[i] = True
                    dq.append(i)
        if len(y_linked_list) == 0:
            return 1 # y에 아무것도 연결되어있지 않은 경우
        return (len(y_linked_list) + 1) # y까지 포함시켜야하기에 +1
    
    for x, y in wires:
        num_y = bfs(x, y)
        num_x = n - num_y
        
        minimum = min(minimum, abs(num_y - num_x))
    
    answer = minimum
    return answer