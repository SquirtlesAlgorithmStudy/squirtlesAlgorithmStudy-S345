# solution1) dfs
def solution(numbers, target):
    count = 0
    def dfs(total, target, depth):
        nonlocal count
        if depth == (len(numbers)) and total == target:
            count += 1
            return
        elif depth == (len(numbers)):
            return

        dfs(total + numbers[depth], target, depth + 1)
        dfs(total - numbers[depth], target, depth + 1)

    dfs(0, target, 0)

    answer = count
    return answer

# solution2) bfs (큐)
from collections import deque

def solution(numbers, target):
    count = 0
    q = deque()
    n = len(numbers)
    q.append((numbers[0], 1))
    q.append((-1*numbers[0], 1))
    
    while q:
        total, depth = q.popleft()
        
        if depth < n:
            # 먼저 큐에 depth가 n인 것 모두 저장
            q.append((total + numbers[depth], depth + 1))
            q.append((total - numbers[depth], depth + 1))
        else:
            # depth가 n인것 큐에 저장 완료되면, 앞에서부터 하나씩 꺼내면서 total값이랑 target값 동일한지 count
            if total == target:
                count += 1
    
    answer = count
    return answer

# solution3) bfs(스택)
def solution(numbers, target):
  stack = [[numbers[0], 1], [-1*numbers[0], 1]]
  n = len(numbers)
  count = 0
  
  while stack:
      total, depth = stack.pop()
      
      if depth < n:
          stack.append([total + numbers[depth], depth + 1])
          stack.append([total - numbers[depth], depth + 1])
      else:
          if total == target:
              count += 1
              
  answer = count
  return answer
