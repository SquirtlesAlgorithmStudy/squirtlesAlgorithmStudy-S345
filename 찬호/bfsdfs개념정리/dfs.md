DFS 동작 예시 

Step 0 . 그래프를 준비(번호가 낮은 인접 노드 부터)

Step 1 . 인접 노드 중 가작 작은 노드를 스택에 넣고 방문 처리 


# 1. 각 노드가 연결된 정보는 2차원 리스트로 표현 된다.

# 각 노드가 방문된 정보를 표현하기 위해
 visited = [false]* 9 

# 정의된 dfs 함수 호출 
dfs(graph,1,visited)

def dfs(g,v,visited):
    visited[i] =True 

    for n in g[v]:
        if not visited[n]:
            dfs(g,n,visited)
