import sys
fastin = sys.stdin.readline

x = str('aaaaaaa')
y = str('aa')

c = 0 #반복횟수를 세는 변수 
idx = 0 #index를 세는 변수

print(len(x)-len(y))
print(x[4:4+len(y)])

while idx<=(len(x)-len(y)):
  if x[idx:idx+len(y)]==y:
    c +=1
    idx += len(y)
    print(c, idx)
  else:
    idx +=1

print("정답은",c)

    