import sys
import re

input=sys.stdin.readline

prob = input().split('-')

sum = 0

for i in prob[1:]:
    for j in i.split('+'):
        sum -=int(j)
        
for k in prob[0].split('+'):
    sum += int(k)

print(sum)