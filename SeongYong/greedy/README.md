# _Greedy algorithm_
An algorithm is designed to achieve optimum solution for a given problem   



># __problems__
## __1. Until 1__


```python
n, k = map(int, input().split())
result = 0

while n >= k:

    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1
    
print(result)

```

---
```python
n, k = map(int, input().split())
result = 0

while True:

    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)

```

> ## Comment
위의 두 코드를 비교해 보았을 때 첫번째 코드보다 두번째 코드가 N이 늘어났을 때 연산에서 더 우월하다. 

'n' 을 'k' 로 나누기 위해 1을 빼는 과정을 두번째 코드는 result에 직접 빼는 횟수를 적용시킴으로써 연산을 간단히 했기 때문이다 
