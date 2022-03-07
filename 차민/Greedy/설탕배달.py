num = int(input())
count = 0

while True:
  if num%5 ==0:
    print(count+num//5)
    break
  else :
    num-=3
    count+=1
    if num==0:
      print(count)
      break
    elif num<0:
      print(-1)
      break
