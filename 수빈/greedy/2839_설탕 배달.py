
n = 11
x = n
print("x는 ", x)

c = 0  #count를 담을 변수
d = 0
type=[5,3]

for t in type:
  c += n//t
  n %=t
  print("n은" ,n)

if n==0:
  print("봉지 개수1:", c)
elif n!=0 and x%3==0:
  d= x//3
  x %= 3
  print("봉지 개수2: ", d)
elif n!=0 and x%3 !=0:
  print(-1)  

## input 이 11일 때, output은 -1이여야 하는거 아닌가? 3과 5로는 11을 정확하게 껄어지게 만들 수 없으니까.