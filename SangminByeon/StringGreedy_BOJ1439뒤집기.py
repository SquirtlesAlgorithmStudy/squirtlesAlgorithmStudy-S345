import sys
import math

cnt=0
s = list(map(int,sys.stdin.readline().rstrip()))

for i in range(len(s)-1):
  if s[i] != s[i+1]: cnt+=1

print(math.ceil(cnt/2))