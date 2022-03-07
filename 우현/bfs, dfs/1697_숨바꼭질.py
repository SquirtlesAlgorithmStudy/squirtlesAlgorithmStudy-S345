from collections import deque

def bfs(n):
  queue = deque()
  queue.append(n)
  
  while queue:
    x = queue.popleft()
    dx = [x-1, x+1, x*2] #계속 변화하는 x라 bfs함수에 넣었다.

    if x == k:
      print(load[x])
      break

    for i in range(3):
      nx = dx[i] #nx : 다음  x 계산
      if 0 <= nx < max_val and not load[nx]:
        load[nx] = load[x]+1 # nx일때 몇번 카운트 했는지, 한번 카운트 된건 다시 방문하지 않기 때문에 항상 최소
        queue.append(nx) # 다음 nx를 계산하기 위해 queue에 넣는다
    
n, k = map(int, input().split())
max_val = 10**6 ############입력 최대가 100,000이라 10**5 가능할텐데 10**5라고 하면 틀렸다고 하는 이유??
load = [0]*(max_val+1) #어디가 끝일지 모르는 배열 생성, k값 넘어간다음 빼는 방법 고려
bfs(n)