import sys
fastin = sys.stdin.readline

n = int(fastin())
num_5 = 0
num_3 = 0
if (n < 5) : 
  if n == 3 : print(1)
  else : print(-1)
  sys.exit()
for i in range((n // 5) ,-1, -1):
  if (n - 5 * i) % 3 == 0 :
    num_5 = i
    num_3 = (n - 5 * i) // 3
    break

if num_5 == 0 and num_3 == 0 : print(-1)
else: print(num_5 + num_3)


