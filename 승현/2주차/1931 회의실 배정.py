n = int(input())
bod=[0][0]

bod = [[int(x)for x in input().split()]for y in range(n)]
bod.sort()
cnt = 0

start = bod[0][0]
end = bod[0][1]

for i in range(n):
  if start > bod[i][1]:
    start = bod[i][0]
    end = bod[i][1]
    emp = end
    end =start
    start = emp
  elif start <= bod[i][0]:
    start = bod[i][0]
    end = bod[i][1]
    emp = end
    end =start
    start = emp
    cnt += 1

print(cnt)