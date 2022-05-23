# 2941 - 크로아티아 알파벳

import sys
input = sys.stdin.readline

word = input()
alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for alpha in alphabets:
  if alpha in word:
    count += word.count(alpha)
    
result = len(word) - count*2 + count

print(result)
