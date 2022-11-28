import sys

input=sys.stdin.readline

n = int(input().rstrip())

numbers = []

for _ in range(n):
  numbers.append(int( input().rstrip()))

fibo=[]
fibo.append(0)
fibo.append(1)

for number in numbers:
  while fibo[-1]<=number-fibo[-2] :
    fibo.append(fibo[-1]+fibo[-2])
  print(fibo)
    
# 제일 큰 수까지 찾았는데 number에서 fibo[-1]값을 뺀 큰 수 출력은 못했습니다...
  
 

           