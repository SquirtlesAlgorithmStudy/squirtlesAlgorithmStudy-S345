#계단 수 
n = int(input())
#점수  
score =[0]
for i in range(n):
  score.append(int(input()))

d = [0]*(n+2) 

d[1] = score[1]

if n==1 :
  print(d[n])

else :
  d[2] = score[1]+score[2]
  if n==2:
    print(d[n])
  else:  
    for i in range(3,n+1):
      d[i] = max(d[i-3]+score[i]+score[i-1], d[i-2]+score[i])

    print(d[n])