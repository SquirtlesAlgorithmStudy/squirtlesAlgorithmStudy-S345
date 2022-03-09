from collections import deque

a = list[map(int,input)]
'''b = list(int(input().split(,8)))
c = list(int(input().split(,8)))
d = list(int(input().split(,8)))
a = '''
print(a[0])

k = input(int())
for i in k:
  th, way = map(int,input().split())
  if way == 1:
        plag = -1
  elif way == -1:
        plag = 1
  if th == 1: #주어진 값 만큼 바퀴돌리기
    a.rotate(way)
    while a[2] != b[6]: # a 와 b가 다른 동안
      b.rotate(plag)
      if b[6] != c[2]:
        c.rotate(way)
      elif c[2] != d[6]:
        d.rotate(plag)
          
  elif th == 2:
    b.rotate(way)
    while (a[2] != b[6]) or (b[6] != c[2]):# a,b  b,c가 다른 동안
      if a[2] != b[6]:
        a.rotate(plag)
      elif b[6] != c[2]:
        c.rotate(plag)
        if c[2] != d[6]:
          d.rotate(way)
      
  elif th == 3:
    c.rotate(way)
    while (b[6] != c[2]) and (c[2]!=d[6]):
      if b[6] != c[2]:
        b.rotate(plag)
        if a[2] != b[6]:
          a.rotate(way)
      elif c[2] != d[6]:
        d.rotate(plag)
      
  elif th == 4:
    d.rotate(way)
    while d[6] != c[2]:
      c.rotate(plag)
      if c[2] != b[6]:
        b.rotate(way)
      elif a[2] != b[6]:
        a.rotate(plag)

A, B, C, D = 0
if a[0] == 1:
  A = 1
elif b[0] == 1:
  B = 2
elif c[0] == 1:
  C = 4
elif d[0] == 1:
  D = 8
sum = A+B+C+D
print(sum)