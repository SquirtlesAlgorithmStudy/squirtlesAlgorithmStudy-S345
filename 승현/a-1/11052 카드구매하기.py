# 가져야 하는 카드 n만큼의 '1회 구입 카드 수'의 경우가 있다. 그리고 그 경우 마다 가격이 다르다
# 1개 - 1, 2개 - 5, 3개 - 6, 4개 - 7
import sys
input = sys.stdin.readline

def func (max, p,q):
  # 배열이 끝나면 max 값 전달
  if q == -1: 
    return max
  # 최대값 변경
  if max < (d[p] + cards[q]):
    max = d[p] + cards[q]
  #재귀함수
  return func(max, p + 1, q - 1)


n = int(input())  # 카드 수 입력
cards = [0] + list(map(int,input().split()))
d = [0] * (n+1)
d[0] = cards[0] # 0
d[1] = cards[1]  #카드 1개
for i in range (2, n+1):
  d[i] = func(0,0,i) #max, d ,cards

print (d[i])