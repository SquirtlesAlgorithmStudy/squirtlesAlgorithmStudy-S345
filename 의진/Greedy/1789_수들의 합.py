import sys
fastin = sys.stdin.readline

s = int(fastin())
result = 0
add = 1

while(s >= add):
  s -= add
  result += 1
  add += 1

print(result)