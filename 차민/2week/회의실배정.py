num = int(input())
want_set = [list(map(int, input().split())) for _ in range(num)]

want_set.sort(key=lambda x:(x[1],x[0]))

end_time, count = want_set[0][1], 1

for i in range(1,num):
  if want_set[i][0]>=end_time:
    count+=1
    end_time=want_set[i][1]

print(count)