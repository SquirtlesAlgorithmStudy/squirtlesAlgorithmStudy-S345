num = int(input())
want_set = [list(map(int, input().split())) for _ in range(num)]
count=1
result=0
last_time=0
count_set=[]

want_set.sort()
print(want_set)

for i in range(num):
  last_time=want_set[i][1]
  for j in range(1,num) :
      break
    if want_set[j][0]>=last_time:
      last_time=want_set[j][1]
      count+=1
  if count>result:
    result=count
  count=1  

print(result)