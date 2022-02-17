n = int(input())
con = []

for i in range(n):
  con.append(list(map(int, input().split())))

con.sort(key=lambda x: (x[1],x[0]))
count = 1 

end = con[0][1]

for i in range(1,n):
  if end <= con[i][0]:
    count += 1
    end = con[i][1]

print(count)