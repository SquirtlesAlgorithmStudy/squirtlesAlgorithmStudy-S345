import sys
input = sys.stdin.readline

def func (max, p,q):
  if q == -1: 
    return max
  if max < (d[p] + cards[q]):
    max = d[p] + cards[q]
  return func(max, p + 1, q -1)


n = int(input())
cards = list(map(int,input().split()))
d = [0] * n
d[0] = 0
d[1] = cards[0]
for i in range (2, n+1):
  d[i] = func(0,0,n)

print (d[i])