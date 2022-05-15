import sys
input = sys.stdin.readline

def func (max, p,q):
  if q == -1: 
    return max
  if max < (d[p] + cards[q]):
    max = d[p] + cards[q]
  return func(max, p + 1, q - 1)


n = int(input())
cards = [0] + list(map(int,input().split()))
d = [0] * (n+1)
d[0] = cards[0]
d[1] = cards[1]  #카드 1개
for i in range (2, n+1):
  d[i] = func(0,0,i)

print (d[i])