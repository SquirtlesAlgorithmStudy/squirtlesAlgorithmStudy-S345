# [Silver I] 피보나치 - 9009 

[문제 링크](https://www.acmicpc.net/problem/9009) 

### 성능 요약

메모리: 30840 KB, 시간: 84 ms

### 분류

그리디 알고리즘(greedy), 수학(math)

### 문제 설명

<p>피보나치 수 ƒ<sub>K</sub>는 ƒ<sub>K</sub> = ƒ<sub>K-1</sub> + ƒ<sub>K-2</sub>로 정의되며 초기값은 ƒ<sub>0</sub> = 0과 ƒ<sub>1</sub> = 1 이다. 양의 정수는 하나 혹은 그 이상의 서로 다른 피보나치 수들의 합으로 나타낼 수 있다는 사실은 잘 알려져 있다. </p>

<p>하나의 양의 정수에 대한 피보나치 수들의 합은 여러 가지 형태가 있다. 예를 들어 정수 100은 ƒ<sub>4</sub> + ƒ<sub>6</sub> + ƒ<sub>11</sub> = 3 + 8 + 89 또는 ƒ<sub>1</sub> + ƒ<sub>3</sub> + ƒ<sub>6</sub> + ƒ<sub>11</sub> = 1 + 2 + 8 + 89, 또는 ƒ<sub>4</sub> + ƒ<sub>6</sub> + ƒ<sub>9</sub> + ƒ<sub>10</sub> = 3 + 8 + 34 + 55 등으로 나타낼 수 있다. 이 문제는 하나의 양의 정수를 최소 개수의 서로 다른 피보나치 수들의 합으로 나타내는 것이다. </p>

<p>하나의 양의 정수가 주어질 때, 피보나치 수들의 합이 주어진 정수와 같게 되는 최소 개수의 서로 다른 피보나치 수들을 구하라. </p>

### 입력 

 <p>입력 데이터는 표준입력을 사용한다. 입력은 T 개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 테스트 데이터의 수를 나타내는 정수 T 가 주어진다. 각 테스트 데이터에는 하나의 정수 n이 주어진다. 단, 1 ≤ n ≤ 1,000,000,000. </p>

### 출력 

 <p>출력은 표준출력을 사용한다. 하나의 테스트 데이터에 대한 해를 하나의 줄에 출력한다. 각 테스트 데이터에 대해, 피보나치 수들의 합이 주어진 정수에 대해 같게 되는 최소수의 피보나치 수들을 증가하는 순서로 출력한다. </p>


# 1차시도(성공)
```python
import sys; input = sys.stdin.readline

N = int(input())
prob = []
for _ in range(N):
    prob.append(int(input()))

itter_val = max(prob)

li = [1, 1]
for i in range(itter_val):
    li.insert(i+2, li[i]+li[i+1])
    if li[i+2] > itter_val: break

i = 1
ans = []

for i in prob:
    ans = []
    for j in li[::-1]:
        if i - j >= 0:
            ans.append(j)
            i = i - j
        if i == 0: 
            for k in range(len(ans)-1, -1, -1):
                print(ans[k], end =' ')
            print()
            break

```
