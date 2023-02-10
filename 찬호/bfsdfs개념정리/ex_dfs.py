from collections import deque

def dfs(graph,v,visited):
    '''
    params:
    graph : 노드가 연결된 정보를 표현한 2차원 리스트 -> graph의 첫번째 인덱스는 현재 노드 
    이고 두번째 리스트는 현재 노드와 인접한 리스트 
    
    v : vertex ; 재귀적으로 구현하기 위해 필요한 변수 

    visited : 방문 boolean 변수가 저장되어 있는 리스트 
    '''
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:  # 방문한적 없을때
            dfs(graph,i,visited)


def bfs(graph,start,visited):
     queue = deque([start])

     visited[start] = True

     while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True