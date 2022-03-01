import sys
fastin = sys.stdin.readline
S=int(fastin().rstrip())

number = [0, 1]

for i in number:
  S-=number[i+1]
  if S in number:
    break
  else : 
    number.append(i+2)

number.pop()
print(len(number))