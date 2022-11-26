# [Silver II] 잃어버린 괄호 - 1541 

[문제 링크](https://www.acmicpc.net/problem/1541) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

그리디 알고리즘(greedy), 수학(math), 파싱(parsing), 문자열(string)

### 문제 설명

<p>세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.</p>

<p>그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.</p>

<p>괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.</p>

### 출력 

 <p>첫째 줄에 정답을 출력한다.</p>

 # 1차 시도(실패)

 ```python
prob = input().split('-')

sum = 0

for i in prob[1:]:
    for j in i.split('+'):
        sum -=int(j)

# 이부분에서 runtime error   
sum += int(prob[0].split('-'))

print(sum)
 ```

 # 2차 시도(성공)

 ```python
prob = input().split('-')

sum = 0

for i in prob[1:]:
    for j in i.split('+'):
        sum -=int(j)
        
for k in prob[0].split('+'):
    sum += int(k)
print(sum)
 ```

보완점 : 아래 코드를 추가하여 '25+35'처럼 두번째에 '+'가 붙는 경우 int() 함수 안에 list가 들어가 error를 유발할 것으로 예상 됨


for을 사용해서 list 안의 값을 빼내는 작업을 함 
