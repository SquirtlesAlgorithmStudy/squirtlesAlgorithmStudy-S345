# 탐험 가능한 곳 중 소모 피로도 작은 것부터 선택
# 실수한 부분 -> 다음 던전 선택시 소모체력 말고도 최소 체력도 고려해줘야 함
# 재시도 : 최소 필요도 - 소모 필요도 계산해서 큰 것보터 탐험하기 !
# 실패한 코드 
def solution(k, dungeons):
    count = 0
    
    dungeons_order = {}
    for start, energy in dungeons:
        if dungeons_order.get(start-energy) == None:
            dungeons_order[start-energy] = [start, energy]
    dungeons_order = dict(sorted(dungeons_order.items(), key = lambda x: x[0], reverse = True))
    order_list = list(dungeons_order.values())
    
    while order_list:
        start, energy = order_list.pop(0)
        if k < start:
            continue
        k -= energy
        count += 1
        
    answer = count
    return answer

# 다른 사람 풀이 (dfs 활용)
def solution(k, dungeons):
    N = len(dungeons)
    visited = [0] * N
    answer = 0

    # dfs활용해서 모든 던전 탐색
    def dfs(k, cnt, dungeons):
        nonlocal answer
        if answer < cnt: # 우선 한 번 다 탐색했으면 던전을 모두 탐색하는 경우는 존재하기 때문에
            answer = cnt

        for i in range(N):
            if k >= dungeons[i][0] and not visited[i]:
                visited[i] = 1
                dfs(k - dungeons[i][1], cnt + 1, dungeons)
                visited[i] = 0
    dfs(k, 0, dungeons)
    return answer