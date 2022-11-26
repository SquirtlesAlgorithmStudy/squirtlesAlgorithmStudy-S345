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
    
    
  
 

           