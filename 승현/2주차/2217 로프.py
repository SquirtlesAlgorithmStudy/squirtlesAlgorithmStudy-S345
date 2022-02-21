n = int(input())
line = []
max, new = 0, 0

for i in range(n):
  line.append(int(input()))
  
line.sort(reverse=True)
i=0
max = int(line[i]) * int(i+1)

for i in range(n):
  new = int(line[i]) * int(i+1)
  if max < new:
    max = new
    
print(max)