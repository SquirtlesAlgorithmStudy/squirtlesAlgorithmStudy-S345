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

## __2. time__
00 시 00분 00초부터 N시 59분 59초까지 3이 들어간 경우 세기

```python
h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
```

## __3. Location of Knight__
count the method of Knight movements
```python
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_column = column + step[1]

  if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <= 8:
    result += 1
print(result)
```

## __4.Sort string__
```python
data = input()
result = []
value = 0

for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)

result.sort()

if value != 0:
  result.append(str(value))

print(''.join(result))
```
