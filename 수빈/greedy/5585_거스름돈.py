a = 380
n = 1000-a

c = 0  #count를 담을 변수
money_type=[500,100,50,10,5,1]

for money in money_type:
  c += n//money
  n %= money
  if n ==0:
    break
print(c)