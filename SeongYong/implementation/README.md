# _ Implementation_
The process of converting an algorithm in your head into source code  



## 개념정리
---
* 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬로 정의 됨 
    * 맨 왼쪽 위는 (0 ,0)임을 고려
  ```python
  for i in range(5):
    for j in range(5):
        print('(', i ,',', j, ')', end=' ')
    print()
  ```

* 시뮬레이션 및 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용됩니다
  * dx, dy 는 행렬의 좌푝값에서 빼준다는 생각을 해야 함 
  ```python
  # west, north, east, south
  dx = [0, -1, 0, 1]
  dy = [1, 0, -1, 0]

  # current location
  x, y = 2, 2

  for i in range(4):
    # next location
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
  ```

># __problems__
## __1. U,D,R,L__

```python
n = int(input())
#set start pint
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    if plan == move_types[i]
        nx = x + dx[i]
        ny = y + dy[i]
    
    # moving outer space
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)
```

