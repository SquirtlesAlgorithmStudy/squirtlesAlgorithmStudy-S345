# 크로아티아 알파벳

import sys
input = sys.stdin.readline

word = input().rstrip()

alphas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for alpha in alphas:
    if alpha in word:
        word = word.replace(alpha, '*')     # .replace는 원본을 바꾸지 않음

print(len(word))